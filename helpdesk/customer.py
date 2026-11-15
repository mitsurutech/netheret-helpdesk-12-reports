"""The customer's side: their company's requests, and replying to them.

Every query here is limited to the signed-in customer's company. That is
the rule that stops one business seeing another business's requests.
"""
from flask import Blueprint, abort, flash, g, redirect, render_template, request, url_for

from .auth import role_required
from .extensions import db
from .models import Ticket, TicketUpdate
from .tickets import add_update, change_status

bp = Blueprint("customer", __name__)


def company_ticket_or_404(ticket_id):
    """Load a request, but only if it belongs to the customer's company.

    Another company's request gets 404, the same as one that does not exist,
    so a customer cannot find out which references are in use.
    """
    ticket = db.get_or_404(Ticket, ticket_id)
    if ticket.company_id != g.user.company_id:
        abort(404)
    return ticket


@bp.route("/my/requests")
@role_required("customer")
def my_requests():
    show = request.args.get("show", "open")
    query = db.select(Ticket).where(Ticket.company_id == g.user.company_id)
    if show == "open":
        query = query.where(Ticket.status.in_(["new", "open", "waiting"]))
    elif show == "finished":
        query = query.where(Ticket.status.in_(["resolved", "closed"]))
    tickets = db.session.scalars(query.order_by(Ticket.created_at.desc())).all()
    return render_template("customer/list.html", tickets=tickets, show=show)


@bp.route("/my/requests/<int:ticket_id>")
@role_required("customer")
def my_request(ticket_id):
    ticket = company_ticket_or_404(ticket_id)
    # Only the updates meant for the customer. Internal notes stay hidden.
    updates = db.session.scalars(
        db.select(TicketUpdate)
        .where(TicketUpdate.ticket_id == ticket.id, TicketUpdate.visible_to_customer.is_(True))
        .order_by(TicketUpdate.created_at)
    ).all()
    return render_template("customer/detail.html", ticket=ticket, updates=updates)


@bp.route("/my/requests/<int:ticket_id>/comments", methods=["POST"])
@role_required("customer")
def add_comment(ticket_id):
    ticket = company_ticket_or_404(ticket_id)
    body = request.form.get("body", "").strip()
    if ticket.status == "closed":
        flash("This request is closed. Please raise a new request.")
    elif not body:
        flash("Write your comment before sending it.")
    else:
        status_change = None
        # A reply means the help desk has something to act on again.
        if ticket.status in ["waiting", "resolved"]:
            change_status(ticket, "open")
            status_change = "open"
        add_update(ticket, body, True, status_change)
        db.session.commit()
        flash("Comment sent. The help desk will see it on your request.")
    return redirect(url_for("customer.my_request", ticket_id=ticket.id))

"""General pages that do not belong to one feature."""
from flask import Blueprint, g, redirect, render_template, url_for

from .auth import login_required
from .extensions import db
from .models import Ticket

bp = Blueprint("main", __name__)

# How each role is shown to people.
ROLE_NAMES = {
    "customer": "a customer",
    "tier1": "a Tier 1 agent",
    "tier2": "a Tier 2 engineer",
    "tier3": "a Tier 3 engineer",
    "manager": "a manager",
}


@bp.route("/")
def home():
    if g.user:
        return redirect(url_for("main.dashboard"))
    return render_template("home.html")


@bp.route("/dashboard")
@login_required
def dashboard():
    open_tickets = []
    if g.user.role == "customer":
        open_tickets = db.session.scalars(
            db.select(Ticket)
            .where(Ticket.company_id == g.user.company_id,
                   Ticket.status.in_(["new", "open", "waiting"]))
            .order_by(Ticket.created_at.desc())
        ).all()
    return render_template("dashboard.html", role_names=ROLE_NAMES, open_tickets=open_tickets)

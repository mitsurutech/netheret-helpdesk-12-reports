"""Reports for managers: KPIs worked out with SQL queries.

Each function below answers one question with one query, so you can read
them one at a time. The page shows every number in a table, and the
JavaScript in static/js/charts.js draws a bar chart from each table.
"""
from datetime import date, datetime, timedelta

from flask import Blueprint, render_template
from sqlalchemy import func

from .auth import role_required
from .extensions import db
from .models import PRIORITIES, STAFF_ROLES, Article, Job, Ticket, User

bp = Blueprint("reports", __name__)

OPEN_STATUSES = ["new", "open", "waiting"]
FINISHED_STATUSES = ["resolved", "closed"]


def open_by_priority():
    """How many requests are still open at each priority."""
    rows = db.session.execute(
        db.select(Ticket.priority, func.count(Ticket.id))
        .where(Ticket.status.in_(OPEN_STATUSES))
        .group_by(Ticket.priority)
    ).all()
    counts = dict(rows)
    # Every priority in the usual order, with 0 for any that have none.
    return [(priority, counts.get(priority, 0)) for priority in PRIORITIES]


def hours_to_resolve_by_priority():
    """The average time from raised to resolved, in hours, per priority."""
    # julianday() is SQLite's way to turn a date into a number of days, so
    # subtracting two of them and multiplying by 24 gives hours.
    hours = (func.julianday(Ticket.resolved_at) - func.julianday(Ticket.created_at)) * 24
    rows = db.session.execute(
        db.select(Ticket.priority, func.avg(hours))
        .where(Ticket.resolved_at.is_not(None))
        .group_by(Ticket.priority)
    ).all()
    averages = dict(rows)
    return [(priority, round(averages.get(priority) or 0, 1)) for priority in PRIORITIES]


def requests_per_person():
    """How many requests each member of staff has: open and in total."""
    open_count = func.sum(Ticket.status.in_(OPEN_STATUSES).cast(db.Integer))
    rows = db.session.execute(
        db.select(User.name, func.count(Ticket.id), open_count)
        .join(Ticket, Ticket.assigned_to_id == User.id)
        .where(User.role.in_(STAFF_ROLES))
        .group_by(User.id)
        .order_by(func.count(Ticket.id).desc())
    ).all()
    return [(name, total, opened or 0) for name, total, opened in rows]


def first_contact_resolution():
    """The percentage of finished requests that Tier 1 fixed without escalating."""
    finished = db.session.scalar(
        db.select(func.count(Ticket.id)).where(Ticket.status.in_(FINISHED_STATUSES))
    )
    at_tier_one = db.session.scalar(
        db.select(func.count(Ticket.id))
        .where(Ticket.status.in_(FINISHED_STATUSES), Ticket.tier == 1)
    )
    if not finished:
        return 0
    return round(100 * at_tier_one / finished)


def working_days_before(day, count):
    """Go back count working days (Monday to Friday) from day."""
    while count > 0:
        day -= timedelta(days=1)
        if day.weekday() < 5:  # 5 and 6 are Saturday and Sunday
            count -= 1
    return day


def open_older_than_two_working_days():
    cutoff = working_days_before(datetime.now(), 2)
    return db.session.scalar(
        db.select(func.count(Ticket.id))
        .where(Ticket.status.in_(OPEN_STATUSES), Ticket.created_at < cutoff)
    )


def jobs_this_week():
    """Jobs this week (Monday to Sunday) that are done, out of all not cancelled."""
    monday = date.today() - timedelta(days=date.today().weekday())
    start = datetime.combine(monday, datetime.min.time())
    end = start + timedelta(days=7)
    this_week = (Job.scheduled_start >= start, Job.scheduled_start < end, Job.status != "cancelled")
    total = db.session.scalar(db.select(func.count(Job.id)).where(*this_week))
    done = db.session.scalar(db.select(func.count(Job.id)).where(*this_week, Job.status == "done"))
    return done, total


def past_jobs_done():
    """Of the jobs that should have finished by now, the percentage marked done."""
    jobs = db.session.scalars(
        db.select(Job).where(Job.status != "cancelled", Job.scheduled_start < datetime.now())
    ).all()
    # The end time is worked out in Python, so this one is a loop, not SQL.
    due = [job for job in jobs if job.scheduled_end <= datetime.now()]
    if not due:
        return 100
    return round(100 * sum(1 for job in due if job.status == "done") / len(due))


def most_helpful_articles():
    return db.session.execute(
        db.select(Article.title, Article.helpful_count)
        .order_by(Article.helpful_count.desc()).limit(5)
    ).all()


@bp.route("/reports")
@role_required("manager")
def index():
    done, total = jobs_this_week()
    return render_template(
        "reports.html",
        open_by_priority=open_by_priority(),
        hours_to_resolve=hours_to_resolve_by_priority(),
        per_person=requests_per_person(),
        fcr=first_contact_resolution(),
        older=open_older_than_two_working_days(),
        jobs_done=done, jobs_total=total,
        past_done=past_jobs_done(),
        articles=most_helpful_articles(),
    )

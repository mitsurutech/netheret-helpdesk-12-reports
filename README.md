# Netheret help desk, step 12: reports

A teaching example. Over sixteen steps we build a help desk web app for
Netheret, a made-up company that supports the IT of small businesses. This
step gives managers a reports page: KPIs worked out with SQL queries, and
bar charts drawn with plain JavaScript.

## What this step adds

- `helpdesk/reports.py`: one small function per KPI:
  - open requests by priority;
  - average hours to resolve, by priority;
  - requests per member of staff, in total and still open;
  - first-contact resolution: the share of finished requests Tier 1 fixed
    without escalating;
  - open requests older than 2 working days;
  - on-site jobs done this week, and the share of past jobs marked done;
  - the most helpful knowledge base articles.
- `helpdesk/templates/reports.html`: the key numbers, then a table for each
  KPI.
- `helpdesk/static/js/charts.js`: finds each `table.chart` and draws a bar
  chart on a `<canvas>` above it, reading the numbers from the table.

## Run it

```
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
python seed.py
flask --app helpdesk run --debug
```

Sign in as `manager@netheret.example` (demo password `password123`) and
open Reports. Resolve a request or mark a job done, then reload: the numbers
change, because nothing is stored, everything is counted when the page opens.

## What to look at

- `func.count`, `func.avg` and `group_by`: the database does the counting,
  rather than Python looping over every row.
- `julianday()` is SQLite's own function: another database would need a
  different way to subtract dates.
- The chart is drawn from the table, so the two can never disagree. The
  canvas has `aria-hidden="true"` because the table already says everything
  for screen readers.
- `devicePixelRatio`: the canvas is drawn at the screen's real resolution so
  the text is not blurry.

<!-- links -->

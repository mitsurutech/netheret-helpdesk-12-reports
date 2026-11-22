# Netheret help desk, step 12: reports

[English](README.md) | [Français](README.fr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [Deutsch](README.de.md)

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

## Learn this step

This is step 12 of 16 of **Task 2. Developing the solution**, a free series of T Level Digital Software Development
lessons that builds the Netheret help desk in agile sprints with Python and Flask. Read the lesson for this step:
[KPI reports and charts](https://mitsurutech.co.uk/resources/t-level/dsd-t2-12-reports).

- Previous step: [step 11, the customer's view of their requests](https://github.com/mitsurutech/netheret-helpdesk-11-customer-view)
- Next step: [step 13, accessibility settings](https://github.com/mitsurutech/netheret-helpdesk-13-accessibility)
- [Every free T Level Digital lesson](https://mitsurutech.co.uk/resources/t-level)
- [Teach these lessons to your class on MitsuruTech](https://mitsurutech.co.uk/learning), [see the pricing](https://mitsurutech.co.uk/pricing) or
  [start a free year for your college](https://mitsurutech.co.uk/signup)

## About

Written by [Mitsuru Technologies](https://mitsurutech.co.uk) (MitsuruTech) as a teaching example for T Level Digital
Software Development. The Netheret IT Support Solutions brief is from Pearson's sample assessment material; this code
and its notes are our own, and are not published, endorsed or approved by Pearson or the Department for Education.
'T Level' is a registered trade mark of the Department for Education.


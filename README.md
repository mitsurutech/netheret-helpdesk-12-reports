# Netheret help desk, step 11: customer view

A teaching example. Over sixteen steps we build a help desk web app for
Netheret, a made-up company that supports the IT of small businesses. This
step finishes the customer's side: they can track their company's requests,
follow the progress on a timeline and add comments.

## What this step adds

- `helpdesk/customer.py`, a new blueprint for customers only:
  - `/my/requests`: the company's requests, still open, finished or all;
  - `/my/requests/<id>`: one request with its timeline, showing only the
    updates staff marked "the customer can see this";
  - `/my/requests/<id>/comments`: the customer's reply. A reply to a
    request that was waiting or resolved opens it again.
- The customer dashboard lists the company's open requests.
- After raising a request, a link to follow its progress.

## Run it

```
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
python seed.py
flask --app helpdesk run --debug
```

Sign in as `customer@brightwell.example` (demo password `password123`),
open My requests and add a comment. Then sign in as `tier1@netheret.example`
and open the same request: the comment is on the staff timeline too, along
with internal notes the customer never saw.

## What to look at

- `company_ticket_or_404()`: one function that every customer page uses to
  load a request, so the "own company only" rule cannot be forgotten.
- Try `/my/requests/2` as the Brightwell customer: request 2 belongs to
  another company, so the answer is 404, not the request.
- The timeline query filters on `visible_to_customer`, so internal notes are
  never even sent to the template.

<!-- links -->

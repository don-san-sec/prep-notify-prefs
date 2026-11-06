# Notification preferences

Brightwatt Energy's comms service: sending customer notifications and
respecting their communication preferences.

## Context

Brightwatt Energy is an app-first UK domestic energy supplier. About 180,000
customers get notifications through the app and by email — their bill is ready,
a payment failed, occasional energy-saving tips and the odd plan promotion.

The ticket for this work is COMMS-88:

> "Respect customer notification preferences: don't send marketing to customers
> who opted out; don't send marketing during quiet hours; transactional
> notifications are unaffected."

## The comms team's rules

These come from the comms team's sending policy. The service must follow them
exactly, or we risk regulator trouble and customer complaints.

1. There are two kinds of notification:
   - **transactional**: `bill_ready`, `payment_failed`
   - **marketing**: `energy_tips`, `referral_offer`, `plan_promo`
2. Marketing must **not** be sent to a customer whose preferences have
   `marketing_opt_out = True`. A customer with **no stored preferences**
   counts as opted **in**.
3. Quiet hours are **21:00–07:00 UK local time**. Marketing must not be sent
   during quiet hours. Transactional notifications may be sent at any time, and
   are **never** blocked by marketing opt-outs.

Worked examples from the policy:

- An opted-out customer with `payment_failed` → **still sent** (transactional
  is never blocked by opt-outs).
- A customer with no stored preferences and `energy_tips` → **sent** (no
  preferences counts as opted in).
- 22:30 and `referral_offer` → **not sent** (quiet hours).

## How it works

```
src/notify/
  models.py           NotificationKind; is_marketing(); CustomerPreferences
  prefs.py            PreferenceStore: save/get customer preferences
  notifications.py    Notifier protocol (email + push senders live elsewhere)
tests/
  fakes.py            FakeNotifier for tests
```

Preferences aren't applied yet: the send path currently sends everything
unconditionally, opted in or not, day or night. The Notifier protocol is in
place, but nothing consults the PreferenceStore before sending.

## Running locally

```
uv sync
uv run pytest -q
```

## Your task

A colleague has opened a PR: https://github.com/don-san-sec/prep-notify-prefs/pull/1. You are the owner of this feature. Review the PR and decide whether to accept or reject it, and explain why.

from datetime import datetime

from fakes import FakeNotifier
from notify.gate import send_with_preferences
from notify.models import CustomerPreferences, NotificationKind

MIDDAY = datetime(2026, 11, 5, 12, 30)


def test_opted_out_marketing_is_blocked() -> None:
    notifier = FakeNotifier()
    prefs = CustomerPreferences(marketing_opt_out=True)

    sent = send_with_preferences(
        "cus_0001", NotificationKind.ENERGY_TIPS, prefs, MIDDAY, notifier
    )

    assert sent is False
    assert notifier.sent == []


def test_opted_in_marketing_is_sent_during_the_day() -> None:
    notifier = FakeNotifier()
    prefs = CustomerPreferences(marketing_opt_out=False)

    sent = send_with_preferences(
        "cus_0001", NotificationKind.PLAN_PROMO, prefs, MIDDAY, notifier
    )

    assert sent is True
    assert notifier.sent == [("cus_0001", "plan_promo")]


def test_transactional_is_sent_during_the_day() -> None:
    notifier = FakeNotifier()
    prefs = CustomerPreferences(marketing_opt_out=True)

    sent = send_with_preferences(
        "cus_0001", NotificationKind.BILL_READY, prefs, MIDDAY, notifier
    )

    assert sent is True
    assert notifier.sent == [("cus_0001", "bill_ready")]
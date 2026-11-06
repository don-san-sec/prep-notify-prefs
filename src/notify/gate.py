"""Sending gate for COMMS-88: notification preferences and quiet hours."""

import logging
from datetime import datetime

from notify.models import CustomerPreferences, NotificationKind, is_marketing
from notify.notifications import Notifier

logger = logging.getLogger(__name__)

QUIET_HOURS_START = 21  # inclusive, UK local time
QUIET_HOURS_END = 7  # exclusive, UK local time


def _in_quiet_hours(now: datetime) -> bool:
    """21:00 (inclusive) to 07:00 (exclusive), UK local time."""
    return now.hour >= QUIET_HOURS_START or now.hour < QUIET_HOURS_END


def should_send(
    kind: NotificationKind,
    prefs: CustomerPreferences | None,
    now: datetime,
) -> bool:
    """Decide whether a notification may go out at this moment."""
    if _in_quiet_hours(now):
        return False

    # Marketing is suppressed for opted-out customers; transactional
    # notifications are never blocked by preferences.
    if is_marketing(kind) and (prefs is None or prefs.marketing_opt_out):
        return False

    return True


def send_with_preferences(
    customer_id: str,
    kind: NotificationKind,
    prefs: CustomerPreferences | None,
    now: datetime,
    notifier: Notifier,
) -> bool:
    """Send via the notifier if the gate allows it; returns whether it sent."""
    if not should_send(kind, prefs, now):
        logger.info("Suppressed %s notification for %s", kind, customer_id)
        return False

    notifier.send(customer_id, kind.value)
    return True
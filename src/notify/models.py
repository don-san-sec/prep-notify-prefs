"""Notification kinds and customer preferences."""

from dataclasses import dataclass
from enum import StrEnum


class NotificationKind(StrEnum):
    """The kinds of notification the comms service sends."""

    BILL_READY = "bill_ready"
    PAYMENT_FAILED = "payment_failed"
    ENERGY_TIPS = "energy_tips"
    REFERRAL_OFFER = "referral_offer"
    PLAN_PROMO = "plan_promo"


_MARKETING_KINDS = frozenset(
    {
        NotificationKind.ENERGY_TIPS,
        NotificationKind.REFERRAL_OFFER,
        NotificationKind.PLAN_PROMO,
    }
)


def is_marketing(kind: NotificationKind) -> bool:
    """True for marketing notifications, False for transactional ones."""
    return kind in _MARKETING_KINDS


@dataclass(frozen=True)
class CustomerPreferences:
    """A customer's stored communication preferences."""

    marketing_opt_out: bool
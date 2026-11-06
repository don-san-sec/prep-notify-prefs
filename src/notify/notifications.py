"""The sending interface for notifications."""

from typing import Protocol


class Notifier(Protocol):
    """Sends a notification to a customer.

    Implementations live in the email and push services. Here we only care
    about the shape: given a customer and a template, it sends.
    """

    def send(self, customer_id: str, template: str) -> None: ...
"""Fakes for tests. No network, no real sends."""

from notify.notifications import Notifier


class FakeNotifier:
    """Records sends so tests can assert on them."""

    def __init__(self) -> None:
        self.sent: list[tuple[str, str]] = []

    def send(self, customer_id: str, template: str) -> None:
        self.sent.append((customer_id, template))


def assert_sent(notifier: FakeNotifier, customer_id: str, template: str) -> None:
    assert (customer_id, template) in notifier.sent


def assert_not_sent(notifier: FakeNotifier, customer_id: str) -> None:
    assert all(cid != customer_id for cid, _ in notifier.sent)
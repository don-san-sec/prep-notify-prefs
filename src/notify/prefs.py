"""Storage for customer communication preferences."""

from notify.models import CustomerPreferences


class PreferenceStore:
    """In-memory store of customer preferences.

    The production service persists these in the customer table; the shape of
    the API is what matters here.
    """

    def __init__(self) -> None:
        self._preferences: dict[str, CustomerPreferences] = {}

    def save(self, customer_id: str, preferences: CustomerPreferences) -> None:
        self._preferences[customer_id] = preferences

    def get(self, customer_id: str) -> CustomerPreferences | None:
        """Return the customer's preferences, or None if none are stored."""
        return self._preferences.get(customer_id)
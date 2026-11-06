from notify.models import CustomerPreferences
from notify.prefs import PreferenceStore


def test_get_returns_saved_preferences() -> None:
    store = PreferenceStore()
    store.save("cus_0001", CustomerPreferences(marketing_opt_out=True))

    assert store.get("cus_0001") == CustomerPreferences(marketing_opt_out=True)


def test_get_returns_none_when_no_preferences_stored() -> None:
    store = PreferenceStore()

    assert store.get("cus_0002") is None

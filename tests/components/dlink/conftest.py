"""Configure pytest for D-Link tests."""

from copy import deepcopy
from unittest.mock import MagicMock, patch

import pytest

from homeassistant.components.dlink.const import CONF_USE_LEGACY_PROTOCOL, DOMAIN
from homeassistant.const import CONF_HOST, CONF_NAME, CONF_PASSWORD, CONF_USERNAME
from homeassistant.core import HomeAssistant

from tests.common import MockConfigEntry

HOST = "1.2.3.4"
PASSWORD = "123456"
USERNAME = "admin"

CONF_DATA = {
    CONF_HOST: HOST,
    CONF_USERNAME: USERNAME,
    CONF_PASSWORD: PASSWORD,
    CONF_USE_LEGACY_PROTOCOL: True,
}

CONF_IMPORT_DATA = CONF_DATA | {CONF_NAME: "Smart Plug"}


def create_entry(hass: HomeAssistant) -> MockConfigEntry:
    """Create fixture for adding config entry in Home Assistant."""
    entry = MockConfigEntry(domain=DOMAIN, data=CONF_DATA)
    entry.add_to_hass(hass)
    return entry


@pytest.fixture()
def config_entry(hass: HomeAssistant) -> MockConfigEntry:
    """Add config entry in Home Assistant."""
    return create_entry(hass)


@pytest.fixture()
def mocked_plug() -> MagicMock:
    """Create mocked plug device."""
    mocked_plug = MagicMock()
    mocked_plug.state = "OFF"
    mocked_plug.temperature = 0
    mocked_plug.current_consumption = "N/A"
    mocked_plug.total_consumption = "N/A"
    mocked_plug.authenticated = ("0123456789ABCDEF0123456789ABCDEF", "ABCDefGHiJ")
    return mocked_plug


@pytest.fixture()
def mocked_plug_no_auth(mocked_plug: MagicMock) -> MagicMock:
    """Create mocked unauthenticated plug device."""
    mocked_plug = deepcopy(mocked_plug)
    mocked_plug.authenticated = None
    return mocked_plug


def patch_config_flow(mocked_plug: MagicMock):
    """Patch D-Link Smart Plug config flow."""
    return patch(
        "homeassistant.components.dlink.config_flow.SmartPlug",
        return_value=mocked_plug,
    )

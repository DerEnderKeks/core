"""This component provides support for Reolink IP cameras."""
from __future__ import annotations

import logging

from homeassistant.components.camera import Camera, CameraEntityFeature
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import ReolinkData
from .const import DOMAIN
from .entity import ReolinkCoordinatorEntity

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up a Reolink IP Camera."""
    reolink_data: ReolinkData = hass.data[DOMAIN][config_entry.entry_id]
    host = reolink_data.host

    cameras = []
    for channel in host.api.channels:
        streams = ["sub", "main", "snapshots"]
        if host.api.protocol in ["rtmp", "flv"]:
            streams.append("ext")

        for stream in streams:
            cameras.append(ReolinkCamera(reolink_data, config_entry, channel, stream))

    async_add_entities(cameras, update_before_add=True)


class ReolinkCamera(ReolinkCoordinatorEntity, Camera):
    """An implementation of a Reolink IP camera."""

    _attr_supported_features: CameraEntityFeature = CameraEntityFeature.STREAM
    _attr_has_entity_name = True

    def __init__(
        self,
        reolink_data: ReolinkData,
        config_entry: ConfigEntry,
        channel: int,
        stream: str,
    ) -> None:
        """Initialize Reolink camera stream."""
        ReolinkCoordinatorEntity.__init__(self, reolink_data, config_entry, channel)
        Camera.__init__(self)

        self._stream = stream

        self._attr_name = self._stream
        self._attr_unique_id = f"{self._host.unique_id}_{self._channel}_{self._stream}"
        self._attr_entity_registry_enabled_default = stream == "sub"

    async def stream_source(self) -> str | None:
        """Return the source of the stream."""
        return await self._host.api.get_stream_source(self._channel, self._stream)

    async def async_camera_image(
        self, width: int | None = None, height: int | None = None
    ) -> bytes | None:
        """Return a still image response from the camera."""
        return await self._host.api.get_snapshot(self._channel)

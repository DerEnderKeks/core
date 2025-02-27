"""Constants for the MusicCast integration."""

from aiomusiccast.capabilities import EntityType

from homeassistant.components.media_player import MediaClass, RepeatMode
from homeassistant.helpers.entity import EntityCategory

DOMAIN = "yamaha_musiccast"

BRAND = "Yamaha Corporation"

# Attributes
ATTR_PLAYLIST = "playlist"
ATTR_PRESET = "preset"
ATTR_MC_LINK = "mc_link"
ATTR_MAIN_SYNC = "main_sync"
ATTR_MC_LINK_SOURCES = [ATTR_MC_LINK, ATTR_MAIN_SYNC]

CONF_UPNP_DESC = "upnp_description"
CONF_SERIAL = "serial"

DEFAULT_ZONE = "main"
HA_REPEAT_MODE_TO_MC_MAPPING = {
    RepeatMode.OFF: "off",
    RepeatMode.ONE: "one",
    RepeatMode.ALL: "all",
}

NULL_GROUP = "00000000000000000000000000000000"


MC_REPEAT_MODE_TO_HA_MAPPING = {
    val: key for key, val in HA_REPEAT_MODE_TO_MC_MAPPING.items()
}

MEDIA_CLASS_MAPPING = {
    "track": MediaClass.TRACK,
    "directory": MediaClass.DIRECTORY,
    "categories": MediaClass.DIRECTORY,
}

ENTITY_CATEGORY_MAPPING = {
    EntityType.CONFIG: EntityCategory.CONFIG,
    EntityType.REGULAR: None,
    EntityType.DIAGNOSTIC: EntityCategory.DIAGNOSTIC,
}

TRANSLATION_KEY_MAPPING = {
    "DIMMER": "dimmer",
    "zone_SLEEP": "zone_sleep",
    "zone_TONE_CONTROL_mode": "zone_tone_control_mode",
    "zone_SURR_DECODER_TYPE": "zone_surr_decoder_type",
    "zone_EQUALIZER_mode": "zone_equalizer_mode",
    "zone_LINK_AUDIO_QUALITY": "zone_link_audio_quality",
    "zone_LINK_CONTROL": "zone_link_control",
    "zone_LINK_AUDIO_DELAY": "zone_link_audio_delay",
}

ZONE_SLEEP_STATE_MAPPING = {
    "off": "off",
    "30 min": "30_min",
    "60 min": "60_min",
    "90 min": "90_min",
    "120 min": "120_min",
}
STATE_ZONE_SLEEP_MAPPING = {val: key for key, val in ZONE_SLEEP_STATE_MAPPING.items()}

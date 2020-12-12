from __future__ import annotations

import abc
import logging
import typing as tp
import struct
from io import BufferedReader, BytesIO

from soulstruct.core import InvalidFieldValueError, SoulstructError
from soulstruct.game_types import *
from soulstruct.maps.base.msb_entry import MSBEntryList, MSBEntryEntityCoordinates
from soulstruct.maps.enums import CollisionHitFilter, MSBPartSubtype
from soulstruct.utilities import BinaryStruct, read_chars_from_buffer, unpack_from_buffer
from soulstruct.utilities.conversion import int_group_to_bit_set, bit_set_to_int_group
from soulstruct.utilities.maths import Vector3

if tp.TYPE_CHECKING:
    from soulstruct.maps.base.regions import BaseMSBRegion


_LOGGER = logging.getLogger(__name__)


class MSBPart(MSBEntryEntityCoordinates, abc.ABC):
    PART_HEADER_STRUCT = None  # type: BinaryStruct
    PART_BASE_DATA_STRUCT = None  # type: BinaryStruct

    PART_TYPE_DATA_STRUCT = ()

    ENTRY_SUBTYPE: MSBPartSubtype

    def __init__(self, msb_part_source=None):
        super().__init__()
        self.sib_path = ""
        self._part_type_index = None
        self.model_name = None
        self._model_index = None
        self.scale = Vector3(1, 1, 1)  # only relevant for MapPiece and Object

        if isinstance(msb_part_source, bytes):
            msb_part_source = BytesIO(msb_part_source)
        if isinstance(msb_part_source, BufferedReader):
            self.unpack(msb_part_source)
        elif msb_part_source is not None:
            raise TypeError("`msb_part_source` must be a buffer, `bytes`, or `None` (default).")

    @abc.abstractmethod
    def unpack(self, msb_buffer):
        """Unpack MSBPart from buffer. Fully defined by each game's MSBPart subclass."""

    @abc.abstractmethod
    def pack(self) -> bytes:
        """Pack MSBPart into bytes, presumably as part of a full MSB pack. Fully defined by each game's subclass."""

    def unpack_type_data(self, msb_buffer):
        """This unpacks simple attributes by default, but some Parts need to process these values more."""
        self.set(**BinaryStruct(*self.PART_TYPE_DATA_STRUCT).unpack(msb_buffer, include_asserted=False))

    def pack_type_data(self):
        try:
            return BinaryStruct(*self.PART_TYPE_DATA_STRUCT).pack_from_object(self)
        except struct.error:
            raise SoulstructError(f"Could not pack type data of MSB part '{self.name}'. See traceback.")

    def set_indices(
        self,
        part_type_index,
        model_indices,
        local_environment_indices,
        region_indices,
        part_indices,
        local_collision_indices,
    ):
        self._part_type_index = part_type_index
        try:
            self._model_index = model_indices[self.model_name] if self.model_name else -1
        except KeyError:
            raise KeyError(
                f"Invalid model name for {self.ENTRY_SUBTYPE.name} {self.name} (entity ID {self.entity_id}): "
                f"{self.model_name}"
            )

    def set_names(
        self, model_names, region_names, environment_names, part_names, collision_names,
    ):
        try:
            self.model_name = model_names[self._model_index]
        except KeyError:
            raise KeyError(
                f"Invalid model index for {self.ENTRY_SUBTYPE.name} {self.name} (entity ID {self.entity_id}): "
                f"{self._model_index}"
            )

    @property
    def draw_groups(self):
        return self._draw_groups

    @draw_groups.setter
    def draw_groups(self, value):
        """Converts value to a `set()` (possibly empty) and validates index range."""
        if value is None or isinstance(value, str) and value in {"None", ""}:
            self._draw_groups = set()
            return
        try:
            draw_groups = set(value)
        except (TypeError, ValueError):
            raise TypeError(
                "Draw groups must be a set, sequence, `None`, 'None', or ''. " "Or use `.draw_groups.add()`, etc.)."
            )
        for i in draw_groups:
            if not 0 <= i <= 127:
                raise InvalidFieldValueError(f"Invalid draw group: {i}. Must range from 0 to 127, inclusive.")
        self._draw_groups = draw_groups

    @property
    def display_groups(self):
        return self._display_groups

    @display_groups.setter
    def display_groups(self, value):
        """Converts value to a `set()` (possibly empty) and validates index range."""
        if value is None or isinstance(value, str) and value in {"None", ""}:
            self._display_groups = set()
            return
        try:
            display_groups = set(value)
        except (TypeError, ValueError):
            raise TypeError(
                "Display groups must be a set, sequence, `None`, 'None', or ''. "
                "Or use `.display_groups.add()`, etc.)."
            )
        for i in display_groups:
            if not 0 <= i <= 127:
                raise ValueError(f"Invalid display group: {i}. Must range from 0 to 127, inclusive.")
        self._display_groups = display_groups


class MSBMapPiece(MSBPart, abc.ABC):
    """Just a textured, visible mesh asset. Does not include any collision."""

    PART_TYPE_DATA_STRUCT = (
        "8x",
    )

    ENTRY_SUBTYPE = MSBPartSubtype.MapPiece

    def __init__(self, msb_part_source=None, **kwargs):
        super().__init__(msb_part_source)
        # Existing defaults are fine (all bools are False).
        self.set(**kwargs)


class MSBObject(MSBPart, abc.ABC):
    """Instance of a physical object."""

    PART_TYPE_DATA_STRUCT = ()  # Differs per game.

    ENTRY_SUBTYPE = MSBPartSubtype.Object

    def __init__(self, msb_part_source=None):
        self.draw_parent_name = None
        self._draw_parent_index = None
        super().__init__(msb_part_source)

    def set_indices(
        self,
        part_type_index,
        model_indices,
        local_environment_indices,
        region_indices,
        part_indices,
        local_collision_indices,
    ):
        super().set_indices(
            part_type_index,
            model_indices,
            local_environment_indices,
            region_indices,
            part_indices,
            local_collision_indices,
        )
        self._draw_parent_index = part_indices[self.draw_parent_name] if self.draw_parent_name else -1

    def set_names(
        self, model_names, region_names, environment_names, part_names, collision_names,
    ):
        super().set_names(
            model_names, environment_names, region_names, part_names, collision_names,
        )
        self.draw_parent_name = part_names[self._draw_parent_index] if self._draw_parent_index != -1 else None


class MSBCharacter(MSBPart, abc.ABC):
    """Physical character instance."""

    PART_TYPE_DATA_STRUCT = ()  # Differs for each game (slightly).

    ENTRY_SUBTYPE = MSBPartSubtype.Character

    def __init__(self, msb_part_source=None):
        self.think_id = -1
        self.npc_id = -1
        self.talk_id = 0
        self.chara_init_id = -1
        self.draw_parent_name = None
        self._draw_parent_index = None
        self._patrol_point_names = [None] * 8
        self._patrol_point_indices = [-1] * 8
        self.default_animation = -1
        self.damage_animation = -1
        super().__init__(msb_part_source)

    @property
    def patrol_point_names(self):
        return self._patrol_point_names

    @patrol_point_names.setter
    def patrol_point_names(self, value):
        """Pads out to eight names with `None`. Also replaces empty strings with `None`."""
        names = []
        for v in value:
            if v is not None and not isinstance(v, str):
                raise TypeError("Patrol point names must be strings or `None`.")
            names.append(v if v else None)
        self._patrol_point_names = value
        while len(self._patrol_point_names) < 8:
            self._patrol_point_names.append(None)

    def set_indices(
        self,
        part_type_index,
        model_indices,
        local_environment_indices,
        region_indices,
        part_indices,
        local_collision_indices,
    ):
        super().set_indices(
            part_type_index,
            model_indices,
            local_environment_indices,
            region_indices,
            part_indices,
            local_collision_indices,
        )
        self._draw_parent_index = part_indices[self.draw_parent_name] if self.draw_parent_name else -1
        self._patrol_point_indices = [region_indices[n] if n else -1 for n in self._patrol_point_names]
        while len(self._patrol_point_indices) < 8:
            self._patrol_point_indices.append(-1)

    def set_names(
        self, model_names, region_names, environment_names, part_names, collision_names,
    ):
        super().set_names(
            model_names, environment_names, region_names, part_names, collision_names,
        )
        self.draw_parent_name = part_names[self._draw_parent_index] if self._draw_parent_index != -1 else None
        self._patrol_point_names = [region_names[i] if i != -1 else None for i in self._patrol_point_indices]


class MSBPlayerStart(MSBPart):
    """Starting point for a player character (e.g. a warp point). No additional data."""

    PART_TYPE_DATA_STRUCT = ("16x",)

    FIELD_INFO = {
        "model_name": (
            "Model Name",
            CharacterModel,
            "Name of character model to use for this PlayerStart. This should always be c0000.",
        ),
        **MSBPart.FIELD_INFO,
    }

    FIELD_NAMES = (
        "model_name",
        "entity_id",
        "translate",
        "rotate",
        "scale",
        "draw_groups",
        "display_groups",
        "ambient_light_id",
        "fog_id",
        "scattered_light_id",
        "lens_flare_id",
        "shadow_id",
        "dof_id",
        "tone_map_id",
        "point_light_id",
        "tone_correct_id",
        "lod_id",
        "is_shadow_source",
        "is_shadow_destination",
        "is_shadow_only",
        "draw_by_reflect_cam",
        "draw_only_reflect_cam",
        "use_depth_bias_float",
        "disable_point_light_effect",
    )

    HIDDEN_FIELDS = (
        "scale",
        "draw_groups",
        "display_groups",
        "ambient_light_id",
        "fog_id",
        "scattered_light_id",
        "lens_flare_id",
        "shadow_id",
        "dof_id",
        "tone_map_id",
        "point_light_id",
        "tone_correct_id",
        "lod_id",
        "is_shadow_source",
        "is_shadow_destination",
        "is_shadow_only",
        "draw_by_reflect_cam",
        "draw_only_reflect_cam",
        "use_depth_bias_float",
        "disable_point_light_effect",
    )

    ENTRY_SUBTYPE = MSBPartSubtype.PlayerStart

    def __init__(self, msb_part_source=None, **kwargs):
        super().__init__(msb_part_source)
        if self.model_name is None:
            self.model_name = "c0000"
        if msb_part_source is None:
            # Set some defaults.
            kwargs.setdefault("is_shadow_source", True)
            kwargs.setdefault("is_shadow_destination", True)
            kwargs.setdefault("draw_by_reflect_cam", True)
        self.set(**kwargs)


class MSBCollision(MSBPart):
    """Physical Collision geometry. Usually these are floor pieces."""

    PART_TYPE_DATA_STRUCT = (
        ("hit_filter_id", "b"),
        ("sound_space_type", "b"),
        ("_environment_event_index", "h"),
        ("reflect_plane_height", "f"),
        ("__navmesh_groups", "4I"),
        ("vagrant_entity_ids", "3i"),
        ("__area_name_id", "h"),
        ("starts_disabled", "?"),
        ("unk_x27_x28", "B"),
        ("attached_bonfire", "i"),
        ("minus_ones", "3i", [-1, -1, -1]),  # Never used. Possibly more bonfires?
        ("__play_region_id", "i"),
        ("lock_cam_param_id_1", "h"),
        ("lock_cam_param_id_2", "h"),
        "16x",
    )

    FIELD_INFO = {
        "model_name": (
            "Model Name",
            CollisionModel,
            "Name of collision model to use for this collision.",
        ),
        **MSBPart.FIELD_INFO,
        "display_groups": (
            "Display Groups",
            list,
            "Display groups of collision. These display groups will be active when the player is standing on this "
            "Collision, which will draw any parts with an overlapping draw group.",
        ),
        "hit_filter_id": (
            "Hit Filter ID",
            CollisionHitFilter,
            "Determines what happens when the player activates this collision.",
        ),
        "sound_space_type": (
            "Sound Space Type",
            int,
            "Unknown.",
        ),
        "environment_event_name": (
            "Environment Event",
            EnvironmentEvent,
            "Environment event in map that determines ambience when standing on this collision.",
        ),
        "reflect_plane_height": (
            "Reflect Plane Height",
            float,
            "Vertical height of the reflect plane for this collision.",
        ),
        "navmesh_groups": (
            "Navmesh Groups",
            list,
            "Controls collision backread.",
        ),
        "vagrant_entity_ids": (
            "Vagrant Entity IDs",
            list,
            "Unknown.",
        ),
        "area_name_id": (
            "Area Name",
            PlaceName,
            "Name of area that this collision is in, which determines the area banner that is shown when you step on "
            "this collision (a linked texture ID lookup) and the area name that appears in the load screen (text ID). "
            "Set it to -1 to use the default area name for this map (i.e. text ID XXYY for map 'mXX_YY').",
        ),
        "force_area_banner": (
            "Show Area Banner",
            bool,
            "By default, the game will only show an area name banner when you enter a map (e.g. after warping). If "
            "this option is enabled, the area name banner will be shown when you step on this collision if the area ID "
            "changes to a new value. Typical usage is to have this disabled for collisions that are very close to a "
            "different area (a 'silent area transition') and have it enabled for collisions that are further away, "
            "which produces a 'delayed area banner' effect.\n\n"
            ""
            "Do NOT enable this for two adjacent collisions with different area names, or moving back and forth "
            "between those collisions will build up a huge queue of area banners to display, which can only be cleared "
            "by restarting the game entirely.",
        ),
        "starts_disabled": (
            "Starts Disabled",
            bool,
            "If True, this collision is disabled on map load and must be manually enabled with an event script.",
        ),
        "unk_x27_x28": (
            "Unknown [27-28]",
            int,
            "Unknown. Almost always zero, but see e.g. Anor Londo gondola collision.",
        ),
        "attached_bonfire": (
            "Attached Bonfire",
            int,
            "If this is set to a bonfire entity ID, that bonfire will be disabled if any living enemy characters are "
            "on this collision. Note that this also checks for enemies that are disabled by events.",
        ),
        "play_region_id": (
            "Play Region ID",
            int,
            "Determines the multiplayer (e.g. invasion) sub-area this collision is part of.\n\n"
            ""
            "NOTE: This field shares space with the stable footing flag, so only one of them can be set to a non-zero "
            "value per collision.",
        ),
        "stable_footing_flag": (
            "Stable Footing Flag",
            int,
            "This flag must be enabled for the player's stable footing (i.e. last saved position) to be updated while "
            "standing on this collision. This is used to prevent players loading inside boss arenas before the boss is "
            "defeated. If set to -1, the player's position will never be saved on this collision.\n\n"
            ""
            "NOTE: This field shares space with the play region ID, so only one of them can be set to a non-zero value "
            "per collision.",
        ),
        "lock_cam_param_id_1": (
            "Camera Param ID 1",
            CameraParam,
            "First camera ID to use on this collision. Unsure how the two slots differ.",
        ),
        "lock_cam_param_id_2": (
            "Camera Param ID 2",
            CameraParam,
            "Second camera ID to use on this collision. Unsure how the two slots differ.",
        ),
    }

    FIELD_NAMES = (
        "model_name",
        "entity_id",
        "translate",
        "rotate",
        "scale",
        "draw_groups",
        "display_groups",
        "navmesh_groups",
        "hit_filter_id",
        "sound_space_type",
        "environment_event_name",
        "reflect_plane_height",
        "vagrant_entity_ids",
        "area_name_id",
        "force_area_banner",
        "starts_disabled",
        "unk_x27_x28",
        "attached_bonfire",
        "play_region_id",
        "stable_footing_flag",
        "lock_cam_param_id_1",
        "lock_cam_param_id_2",
        "ambient_light_id",
        "fog_id",
        "scattered_light_id",
        "lens_flare_id",
        "shadow_id",
        "dof_id",
        "tone_map_id",
        "point_light_id",
        "tone_correct_id",
        "lod_id",
        "is_shadow_source",
        "is_shadow_destination",
        "is_shadow_only",
        "draw_by_reflect_cam",
        "draw_only_reflect_cam",
        "use_depth_bias_float",
        "disable_point_light_effect",
    )

    HIDDEN_FIELDS = (
        "scale",
        "lod_id",
        "unk_x27_x28",
        "use_depth_bias_float",
    )

    ENTRY_SUBTYPE = MSBPartSubtype.Collision

    def __init__(self, msb_part_source=None, **kwargs):
        self.hit_filter_id = CollisionHitFilter.Normal
        self.sound_space_type = 0
        self._environment_event_index = None
        self.environment_event_name = None
        self.reflect_plane_height = 0.0
        self._navmesh_groups = set(range(128))
        self.vagrant_entity_ids = [-1, -1, -1]
        self.area_name_id = -1
        self._force_area_banner = False  # Custom field (see property).
        self.starts_disabled = False
        self.unk_x27_x28 = 0
        self.attached_bonfire = -1
        self._play_region_id = 0
        self._stable_footing_flag = 0
        self.lock_cam_param_id_1 = -1
        self.lock_cam_param_id_2 = -1
        super().__init__(msb_part_source)
        if msb_part_source is None:
            # Set some defaults.
            kwargs.setdefault("is_shadow_source", True)
            kwargs.setdefault("is_shadow_destination", True)
            kwargs.setdefault("draw_by_reflect_cam", True)
        self.set(**kwargs)

    def unpack_type_data(self, msb_buffer):
        data = BinaryStruct(*self.PART_TYPE_DATA_STRUCT).unpack(msb_buffer, include_asserted=False)
        self.set(**data)
        self._navmesh_groups = int_group_to_bit_set(data["__navmesh_groups"])
        self.area_name_id = abs(data["__area_name_id"]) if data["__area_name_id"] != -1 else -1
        self._force_area_banner = data["__area_name_id"] < 0  # Custom field.
        if data["__play_region_id"] > -10:
            self._play_region_id = data["__play_region_id"]
            self._stable_footing_flag = 0
        else:
            self._play_region_id = 0
            self._stable_footing_flag = -data["__play_region_id"] - 10

    def pack_type_data(self):
        """Pack to bytes, presumably as part of a full `MSB` pack."""

        # Validate navmesh groups before doing any real work.
        navmesh_groups = bit_set_to_int_group(self._navmesh_groups)

        if self.area_name_id == -1 and not self._force_area_banner:
            raise InvalidFieldValueError("`force_area_banner` must be enabled if `area_name_id == -1` (default).")
        signed_area_name_id = self.area_name_id * (-1 if self.area_name_id >= 0 and self._force_area_banner else 1)
        if self._stable_footing_flag != 0:
            play_region_id = -self._stable_footing_flag - 10
        else:
            play_region_id = self._play_region_id
        return BinaryStruct(*self.PART_TYPE_DATA_STRUCT).pack(
            hit_filter_id=self.hit_filter_id,
            sound_space_type=self.sound_space_type,
            _environment_event_index=self._environment_event_index,
            reflect_plane_height=self.reflect_plane_height,
            __navmesh_groups=navmesh_groups,
            vagrant_entity_ids=self.vagrant_entity_ids,
            __area_name_id=signed_area_name_id,
            starts_disabled=self.starts_disabled,
            unk_x27_x28=self.unk_x27_x28,
            attached_bonfire=self.attached_bonfire,
            __play_region_id=play_region_id,
            lock_cam_param_id_1=self.lock_cam_param_id_1,
            lock_cam_param_id_2=self.lock_cam_param_id_2,
        )

    @property
    def force_area_banner(self):
        return self._force_area_banner

    @force_area_banner.setter
    def force_area_banner(self, value: bool):
        if not value and self.area_name_id == -1:
            raise InvalidFieldValueError(
                "Banner must appear when area name is set to default (-1). You must specify the area name manually to "
                "set this to False."
            )
        self._force_area_banner = bool(value)

    @property
    def play_region_id(self):
        return self._play_region_id

    @play_region_id.setter
    def play_region_id(self, value):
        if self._stable_footing_flag != 0:
            raise InvalidFieldValueError(
                "Cannot set 'play_region_id' to a non-zero value while 'stable_footing_flag' " "is non-zero."
            )
        if not isinstance(value, int) or value <= -10:
            raise InvalidFieldValueError("'play_region_id' must be an integer greater than or equal to -9.")
        self._play_region_id = value

    @property
    def stable_footing_flag(self):
        return self._stable_footing_flag

    @stable_footing_flag.setter
    def stable_footing_flag(self, value):
        if self._play_region_id != 0:
            raise InvalidFieldValueError(
                "Cannot set 'stable_footing_flag' to a non-zero value while 'play_region_id' " "is non-zero."
            )
        if not isinstance(value, int) or value < 0:
            raise InvalidFieldValueError("'stable_footing_flag' must be an integer greater than or equal to 0.")
        self._stable_footing_flag = value

    @property
    def navmesh_groups(self):
        return self._navmesh_groups

    @navmesh_groups.setter
    def navmesh_groups(self, value):
        """Converts value to a `set()` (possibly empty) and validates index range."""
        if value is None or isinstance(value, str) and value in {"None", ""}:
            self._navmesh_groups = set()
            return
        try:
            navmesh_groups = set(value)
        except (TypeError, ValueError):
            raise TypeError(
                "Navmesh groups must be a set, sequence, `None`, 'None', or ''. "
                "Or use `.navmesh_groups.add()`, etc.)."
            )
        for i in navmesh_groups:
            if not 0 <= i <= 127:
                raise ValueError(f"Invalid navmesh group: {i}. Must range from 0 to 127, inclusive.")
        self._navmesh_groups = navmesh_groups

    def set_indices(
        self,
        part_type_index,
        model_indices,
        local_environment_indices,
        region_indices,
        part_indices,
        local_collision_indices,
    ):
        super().set_indices(
            part_type_index,
            model_indices,
            local_environment_indices,
            region_indices,
            part_indices,
            local_collision_indices,
        )
        if self.environment_event_name:
            self._environment_event_index = local_environment_indices[self.environment_event_name]
        else:
            self._environment_event_index = -1

    def set_names(
        self, model_names, region_names, environment_names, part_names, collision_names,
    ):
        super().set_names(
            model_names, environment_names, region_names, part_names, collision_names,
        )
        if self._environment_event_index != -1:
            try:
                self.environment_event_name = environment_names[self._environment_event_index]
            except IndexError:
                for i, env in enumerate(environment_names):
                    print(i, env)
                print(self._environment_event_index)
                self.environment_event_name = f"BROKEN ({self._environment_event_index})"
        else:
            self.environment_event_name = None


class MSBNavmesh(MSBPart):
    """AI navigation mesh ('navmesh'). Often called 'navimesh' in the game files."""

    PART_NAVMESH_STRUCT = (
        ("navmesh_groups", "4I"),
        "16x",
    )

    FIELD_INFO = {
        "model_name": (
            "Model Name",
            NavmeshModel,
            "Name of navmesh model to use for this navmesh.",
        ),
        **MSBPart.FIELD_INFO,
        "navmesh_groups": (
            "Navmesh Groups",
            list,
            "Enables backread of collisions with overlapping navmesh groups, if the nodes are also close enough in "
            "the MCG/MCP network.",
        ),
    }

    FIELD_NAMES = (
        "model_name",
        "entity_id",
        "translate",
        "rotate",
        "scale",
        "draw_groups",
        "display_groups",
        "navmesh_groups",
        "ambient_light_id",
        "fog_id",
        "scattered_light_id",
        "lens_flare_id",
        "shadow_id",
        "dof_id",
        "tone_map_id",
        "point_light_id",
        "tone_correct_id",
        "lod_id",
        "is_shadow_source",
        "is_shadow_destination",
        "is_shadow_only",
        "draw_by_reflect_cam",
        "draw_only_reflect_cam",
        "use_depth_bias_float",
        "disable_point_light_effect",
    )

    HIDDEN_FIELDS = (
        "scale",
        "lod_id",
        "use_depth_bias_float",
        "draw_groups",
        "display_groups",
        "ambient_light_id",
        "fog_id",
        "scattered_light_id",
        "lens_flare_id",
        "shadow_id",
        "dof_id",
        "tone_map_id",
        "point_light_id",
        "tone_correct_id",
        "lod_id",
        "is_shadow_source",
        "is_shadow_destination",
        "is_shadow_only",
        "draw_by_reflect_cam",
        "draw_only_reflect_cam",
        "use_depth_bias_float",
        "disable_point_light_effect",
    )

    ENTRY_SUBTYPE = MSBPartSubtype.Navmesh

    def __init__(self, msb_part_source=None, **kwargs):
        self._navmesh_groups = set(range(128))
        super().__init__(msb_part_source)
        if msb_part_source is None:
            # Set some defaults.
            kwargs.setdefault("is_shadow_source", True)
        self.set(**kwargs)

    def unpack_type_data(self, msb_buffer):
        data = BinaryStruct(*self.PART_NAVMESH_STRUCT).unpack(msb_buffer, include_asserted=False)
        self._navmesh_groups = int_group_to_bit_set(data["navmesh_groups"])

    def pack_type_data(self):
        return BinaryStruct(*self.PART_NAVMESH_STRUCT).pack(
            navmesh_groups=bit_set_to_int_group(self._navmesh_groups),
        )

    @property
    def navmesh_groups(self):
        return self._navmesh_groups

    @navmesh_groups.setter
    def navmesh_groups(self, value):
        """Converts value to a `set()` (possibly empty) and validates index range."""
        if value is None or isinstance(value, str) and value in {"None", ""}:
            self._navmesh_groups = set()
            return
        try:
            navmesh_groups = set(value)
        except (TypeError, ValueError):
            raise TypeError(
                "Navmesh groups must be a set, sequence, `None`, 'None', or ''. "
                "Or use `.navmesh_groups.add()`, etc.)."
            )
        for i in navmesh_groups:
            if not 0 <= i <= 127:
                raise ValueError(f"Invalid navmesh group: {i}. Must range from 0 to 127, inclusive.")
        self._navmesh_groups = navmesh_groups


class MSBUnusedObject(MSBObject):
    """Unused object. May be used in cutscenes; disabled otherwise. Identical structure to `MSBObject`."""
    ENTRY_SUBTYPE = MSBPartSubtype.UnusedObject


class MSBUnusedCharacter(MSBCharacter):
    """Unused character. May be used in cutscenes; disabled otherwise. Identical structure to `MSBCharacter`."""
    ENTRY_SUBTYPE = MSBPartSubtype.UnusedCharacter


class MSBMapConnection(MSBPart):
    """Links to an `MSBCollision` entry and causes another specified map to load into backread when the linked collision
    is itself in backread in the current map.

    Note that sensible draw, display, and navmesh groups are still needed to advance the backread state of the
    connected map's collisions to an interactive state (while map pieces don't care about navmesh groups).

    Uses collision models, and almost always has the same model as the linked `MSBCollision`.
    """

    PART_MAP_LOAD_TRIGGER_STRUCT = (
        ("collision_index", "i"),
        ("map_id", "4b"),
        "8x",
    )

    FIELD_INFO = {
        "model_name": (
            "Collision Model Name",
            CollisionModel,
            "Name of collision model to use for this map load trigger.",
        ),
        **MSBPart.FIELD_INFO,
        "collision_name": (
            "Collision Part Name",
            Collision,
            "Collision part that triggers this map load.",
        ),
        "connected_map": (
            "Map ID",
            Map,
            "Vanilla name or 'mAA_BB_CC_DD'-style name or (AA, BB, CC, DD) sequence of the map to be loaded.",
        ),
    }

    FIELD_NAMES = (
        "model_name",
        "entity_id",
        "translate",
        "rotate",
        "scale",
        "draw_groups",
        "display_groups",
        "collision_name",
        "connected_map",
        "ambient_light_id",
        "fog_id",
        "scattered_light_id",
        "lens_flare_id",
        "shadow_id",
        "dof_id",
        "tone_map_id",
        "point_light_id",
        "tone_correct_id",
        "lod_id",
        "is_shadow_source",
        "is_shadow_destination",
        "is_shadow_only",
        "draw_by_reflect_cam",
        "draw_only_reflect_cam",
        "use_depth_bias_float",
        "disable_point_light_effect",
    )

    HIDDEN_FIELDS = (
        "scale",
        "lod_id",
        "is_shadow_destination",
        "is_shadow_only",
        "draw_by_reflect_cam",
        "draw_only_reflect_cam",
        "use_depth_bias_float",
        "disable_point_light_effect",
    )

    ENTRY_SUBTYPE = MSBPartSubtype.MapConnection

    def __init__(self, msb_part_source=None, **kwargs):
        self.collision_name = None
        self._collision_index = None
        self._connected_map = get_map(10, 0)  # defaults to m10_00_00_00 (Depths)
        super().__init__(msb_part_source)
        if msb_part_source is None:
            # Set some defaults.
            kwargs.setdefault("is_shadow_source", True)
            kwargs.setdefault("is_shadow_destination", True)
            kwargs.setdefault("draw_by_reflect_cam", True)
        self.set(**kwargs)

    def unpack_type_data(self, msb_buffer):
        data = BinaryStruct(*self.PART_MAP_LOAD_TRIGGER_STRUCT).unpack(msb_buffer)
        self.collision_name = None
        self._collision_index = data["collision_index"]
        area_id, block_id, _, _ = data["map_id"]
        self._connected_map = get_map(area_id, block_id)

    def pack_type_data(self):
        return BinaryStruct(*self.PART_MAP_LOAD_TRIGGER_STRUCT).pack(
            collision_index=self._collision_index,
            map_id=self._connected_map.map_load_tuple,  # note use of EMEVD file stem
        )

    @property
    def connected_map(self) -> Map:
        return self._connected_map

    @connected_map.setter
    def connected_map(self, value):
        self._connected_map = get_map(value)

    def set_indices(
        self,
        part_type_index,
        model_indices,
        local_environment_indices,
        region_indices,
        part_indices,
        local_collision_indices,
    ):
        super().set_indices(
            part_type_index,
            model_indices,
            local_environment_indices,
            region_indices,
            part_indices,
            local_collision_indices,
        )
        self._collision_index = local_collision_indices[self.collision_name] if self.collision_name else -1

    def set_names(
        self, model_names, region_names, environment_names, part_names, collision_names,
    ):
        super().set_names(
            model_names, environment_names, region_names, part_names, collision_names,
        )
        self.collision_name = collision_names[self._collision_index] if self._collision_index != -1 else None


class MSBPartList(MSBEntryList[MSBPart]):
    ENTRY_LIST_NAME = "Parts"
    ENTRY_CLASS = staticmethod(MSBPart)
    ENTRY_SUBTYPE_ENUM = MSBPartSubtype

    PART_SUBTYPE_CLASSES = {}  # type: dict[MSBPartSubtype, type]
    PART_SUBTYPE_OFFSET = None  # type: int

    _entries: tp.List[MSBPart]

    MapPieces: tp.Sequence[MSBMapPiece]
    Objects: tp.Sequence[MSBObject]
    Characters: tp.Sequence[MSBCharacter]
    PlayerStarts: tp.Sequence[MSBPlayerStart]
    Collisions: tp.Sequence[MSBCollision]
    Navmeshes: tp.Sequence[MSBNavmesh]
    UnusedObjects: tp.Sequence[MSBUnusedObject]
    UnusedCharacters: tp.Sequence[MSBUnusedCharacter]
    MapConnections: tp.Sequence[MSBMapConnection]

    def set_indices(
        self, model_indices, local_environment_indices, region_indices, part_indices, local_collision_indices,
    ):
        """Local type-specific index only.

        Events and other Parts may point to Parts by global entry index, but it seems the local index still matters, as
        ObjAct Events seem to break when the local object index is changed. It's possible this was just an idiosyncrasy
        of Wulf's MSB Editor. Either way, this method should ensure the global and local indices are consistent.

        Remember that Navmesh indices are hard-coded into MCP and MCG files. Also note that cutscene files (remo) access
        MSB parts by index as well, which is why map mods tend to break them so often.

        `local_environment_indices` are needed for Collisions and `local_collision_indices` are needed for Map Load
        Triggers. No other MSB entry type requires local subtype indices.
        """
        type_indices = {}
        for entry in self._entries:
            try:
                entry.set_indices(
                    part_type_index=type_indices.setdefault(entry.ENTRY_SUBTYPE, 0),
                    model_indices=model_indices,
                    local_environment_indices=local_environment_indices,
                    region_indices=region_indices,
                    part_indices=part_indices,
                    local_collision_indices=local_collision_indices,
                )
            except KeyError as e:
                raise SoulstructError(str(e))
            else:
                type_indices[entry.ENTRY_SUBTYPE] += 1

    def set_names(
        self, model_names, environment_names, region_names, part_names, collision_names,
    ):
        for entry in self._entries:
            entry.set_names(
                model_names, region_names, environment_names, part_names, collision_names,
            )

    def get_instance_counts(self):
        """Returns a dictionary mapping model names to part instance counts."""
        instance_counts = {}
        for entry in self._entries:
            instance_counts.setdefault(entry.model_name, 0)
            instance_counts[entry.model_name] += 1
        return instance_counts

    def duplicate_map_piece(
        self, map_piece_name_or_index, insert_below_original=True, **kwargs,
    ) -> MSBMapPiece:
        return self.duplicate_entry(MSBPartSubtype.MapPiece, map_piece_name_or_index, insert_below_original, **kwargs)

    def add_map_piece(self, **kwargs):
        map_piece = MSBMapPiece(msb_part_source=None, **kwargs)
        return self.add_entry(map_piece, append_to_entry_subtype=MSBPartSubtype.MapPiece)

    def duplicate_object(
        self, object_name_or_index, insert_below_original=True, **kwargs,
    ) -> MSBObject:
        return self.duplicate_entry(MSBPartSubtype.Object, object_name_or_index, insert_below_original, **kwargs)

    def add_object(self, **kwargs):
        obj = MSBObject(msb_part_source=None, **kwargs)
        return self.add_entry(obj, append_to_entry_subtype=MSBPartSubtype.Object)

    def duplicate_character(
        self, character_name_or_index, insert_below_original=True, **kwargs,
    ) -> MSBObject:
        return self.duplicate_entry(MSBPartSubtype.Character, character_name_or_index, insert_below_original, **kwargs)

    def add_character(self, **kwargs):
        character = MSBCharacter(msb_part_source=None, **kwargs)
        return self.add_entry(character, append_to_entry_subtype=MSBPartSubtype.Character)

    def duplicate_player_start(
        self, player_start_name_or_index, insert_below_original=True, **kwargs,
    ) -> MSBPlayerStart:
        return self.duplicate_entry(
            MSBPartSubtype.PlayerStart, player_start_name_or_index, insert_below_original, **kwargs,
        )

    def add_player_start(self, **kwargs):
        player_start = MSBPlayerStart(msb_part_source=None, **kwargs)
        return self.add_entry(player_start, append_to_entry_subtype=MSBPartSubtype.PlayerStart)

    def duplicate_collision(
        self, collision_name_or_index, duplicate_env_event_from_msb: MSB = None, insert_below_original=True, **kwargs,
    ) -> MSBCollision:
        """Duplicate a Collision and optionally (if able) duplicate the attached `MSBEnvironment` instance and its
        region."""
        new_collision = self.duplicate_entry(
            MSBPartSubtype.Collision, collision_name_or_index, insert_below_original=insert_below_original, **kwargs,
        )  # type: MSBCollision
        if duplicate_env_event_from_msb and new_collision.environment_event_name:
            if "name" not in kwargs:
                raise ValueError(f"Must pass `name` to duplication call to duplicate attached environment event.")
            msb = duplicate_env_event_from_msb
            try:
                environment_event = msb.events.get_entry_by_name(
                    new_collision.environment_event_name, "Environment",
                )  # type: MSBEnvironment
            except KeyError:
                raise KeyError(f"Could not find environment event '{new_collision.environment_event_name}' in MSB.")
            if not environment_event.base_region_name:
                raise AttributeError(f"Environment event '{environment_event.name}' has no anchor Region.")
            try:
                environment_region = msb.regions.get_entry_by_name(
                    environment_event.base_region_name,
                )  # type: BaseMSBRegion
            except KeyError:
                raise KeyError(f"Could not find environment region '{environment_event.base_region_name}' in MSB.")
            new_region = msb.regions.duplicate_entry(environment_region, name=f"GI Region ({kwargs['name']})")
            new_event = msb.events.duplicate_entry(environment_event, name=f"GI Event ({kwargs['name']})")
            new_event.base_region_name = new_region.name
            new_collision.environment_event_name = new_event.name
        return new_collision

    def add_collision(self, **kwargs):
        collision = MSBCollision(msb_part_source=None, **kwargs)
        return self.add_entry(collision, append_to_entry_subtype=MSBPartSubtype.Collision)

    def duplicate_navmesh(
        self, navmesh_name_or_index, insert_below_original=True, **kwargs,
    ) -> MSBNavmesh:
        return self.duplicate_entry(MSBPartSubtype.Navmesh, navmesh_name_or_index, insert_below_original, **kwargs)

    def add_navmesh(self, **kwargs):
        navmesh = MSBNavmesh(msb_part_source=None, **kwargs)
        return self.add_entry(navmesh, append_to_entry_subtype=MSBPartSubtype.Navmesh)

    def duplicate_unused_object(
            self, object_name_or_index, insert_below_original=True, **kwargs,
    ) -> MSBUnusedObject:
        return self.duplicate_entry(
            MSBPartSubtype.UnusedObject, object_name_or_index, insert_below_original, **kwargs,
        )

    def duplicate_unused_character(
        self, character_name_or_index, insert_below_original=True, **kwargs,
    ) -> MSBUnusedCharacter:
        return self.duplicate_entry(
            MSBPartSubtype.UnusedCharacter, character_name_or_index, insert_below_original, **kwargs,
        )

    def duplicate_map_connection(
            self, trigger_name_or_index, insert_below_original=True, **kwargs,
    ) -> MSBMapConnection:
        return self.duplicate_entry(
            MSBPartSubtype.MapConnection, trigger_name_or_index, insert_below_original, **kwargs,
        )

    def create_map_connection(self, collision, connected_map, name=None, draw_groups=None, display_groups=None):
        """Creates a new `MapConnection` that references and copies the transform of the given `collision`.

        The `name` and `map_id` of the new `MapConnection` must be given. You can also specify its `draw_groups` and
        `display_groups`. Otherwise, it will leave them as the extensive default values: [0, ..., 127].
        """
        if not isinstance(collision, MSBCollision):
            collision = self.get_entry_by_name(collision, "Collision")
        if name is None:
            game_map = get_map(connected_map)
            name = collision.name + f"_[{game_map.area_id:02d}_{game_map.block_id:02d}]"
        if name in self.get_entry_names("MapConnection"):
            raise ValueError(f"{repr(name)} is already the name of an existing MapConnection.")
        map_connection = MSBMapConnection(
            name=name,
            connected_map=connected_map,
            collision_name=collision.name,
            translate=collision.translate.copy(),
            rotate=collision.rotate.copy(),
            scale=collision.scale.copy(),  # for completion's sake
            model_name=collision.model_name,
        )
        if draw_groups is not None:
            map_connection.draw_groups = draw_groups
        if display_groups is not None:
            map_connection.display_groups = display_groups
        self.add_entry(map_connection, append_to_entry_subtype="MapConnection")
        return map_connection

    def add_c1000(self, name, **kwargs) -> MSBCharacter:
        """Useful to create basic c1000 instances as debug warp points."""
        return self.add_character(
            name=name,
            model_name="c1000",
            **kwargs,
        )

    def get_subtype_instance(self, entry_subtype, **kwargs):
        entry_subtype = self.resolve_entry_subtype(entry_subtype)
        entry_class = self.PART_SUBTYPE_CLASSES[entry_subtype]
        return entry_class(msb_part_source=None, **kwargs)

    @classmethod
    def MSBPart(cls, msb_buffer):
        """Detects the appropriate subclass of `MSBPart` to instantiate, and does so."""
        event_type_int = unpack_from_buffer(msb_buffer, "i", offset=cls.PART_SUBTYPE_OFFSET, relative_offset=True)
        event_type = MSBPartSubtype(event_type_int)
        return cls.PART_SUBTYPE_CLASSES[event_type](msb_buffer)


for _entry_subtype in MSBPartList.ENTRY_SUBTYPE_ENUM:
    setattr(
        MSBPartList,
        _entry_subtype.pluralized_name,
        property(lambda self, _e=_entry_subtype: [e for e in self._entries if e.ENTRY_SUBTYPE == _e]),
    )
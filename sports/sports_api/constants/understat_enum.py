from enum import Enum


class UnderstatTeamSituationEnum(Enum):
    OPEN_PLAY = "OpenPlay"
    FROM_CORNER = "FromCorner"
    SET_PIECE = "SetPiece"
    DIRECT_FREEKICK = "DirectFreekick"
    PENALTY = "Penalty"
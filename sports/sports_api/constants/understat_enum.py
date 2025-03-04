from enum import Enum


class UnderstatTeamSituationEnum(Enum):
    OPEN_PLAY = "OpenPlay"
    FROM_CORNER = "FromCorner"
    SET_PIECE = "SetPiece"
    DIRECT_FREEKICK = "DirectFreekick"
    PENALTY = "Penalty"
    
class UnderstatFormationEnum(Enum):
    FOUR_TWO_THREE_ONE = "4-2-3-1"
    FOUR_ONE_FOUR_ONE = "4-1-4-1"
    THREE_TWO_FOUR_ONE = "3-2-4-1"
    FOUR_THREE_THREE = "4-3-3"
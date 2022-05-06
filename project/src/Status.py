from enum import Enum

class Status(Enum):
    REJECT_ACTIVATION = -1,
    REPORT_AVAILABILITY = 1,
    REQUEST_SMS = 3,
    COMPLETE_ACTIVATION = 6,
    NUMBER_USED_OR_BANNED = 8
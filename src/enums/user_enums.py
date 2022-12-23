from enum import Enum


class Genders(Enum):
    female = "female"
    male = "male"


class Status(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class UserErrors(Enum):
    WRONG_EMAIL = "Email doesn't have @"
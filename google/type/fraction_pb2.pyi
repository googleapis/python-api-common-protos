from typing import ClassVar as _ClassVar
from typing import Optional as _Optional

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class Fraction(_message.Message):
    __slots__ = ("numerator", "denominator")
    NUMERATOR_FIELD_NUMBER: _ClassVar[int]
    DENOMINATOR_FIELD_NUMBER: _ClassVar[int]
    numerator: int
    denominator: int
    def __init__(
        self, numerator: _Optional[int] = ..., denominator: _Optional[int] = ...
    ) -> None: ...

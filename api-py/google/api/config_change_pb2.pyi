from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChangeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHANGE_TYPE_UNSPECIFIED: _ClassVar[ChangeType]
    ADDED: _ClassVar[ChangeType]
    REMOVED: _ClassVar[ChangeType]
    MODIFIED: _ClassVar[ChangeType]
CHANGE_TYPE_UNSPECIFIED: ChangeType
ADDED: ChangeType
REMOVED: ChangeType
MODIFIED: ChangeType

class ConfigChange(_message.Message):
    __slots__ = ("element", "old_value", "new_value", "change_type", "advices")
    ELEMENT_FIELD_NUMBER: _ClassVar[int]
    OLD_VALUE_FIELD_NUMBER: _ClassVar[int]
    NEW_VALUE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ADVICES_FIELD_NUMBER: _ClassVar[int]
    element: str
    old_value: str
    new_value: str
    change_type: ChangeType
    advices: _containers.RepeatedCompositeFieldContainer[Advice]
    def __init__(self, element: _Optional[str] = ..., old_value: _Optional[str] = ..., new_value: _Optional[str] = ..., change_type: _Optional[_Union[ChangeType, str]] = ..., advices: _Optional[_Iterable[_Union[Advice, _Mapping]]] = ...) -> None: ...

class Advice(_message.Message):
    __slots__ = ("description",)
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    description: str
    def __init__(self, description: _Optional[str] = ...) -> None: ...
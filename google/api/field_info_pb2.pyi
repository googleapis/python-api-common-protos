from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
FIELD_INFO_FIELD_NUMBER: _ClassVar[int]
field_info: _descriptor.FieldDescriptor

class FieldInfo(_message.Message):
    __slots__ = ("format",)

    class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FORMAT_UNSPECIFIED: _ClassVar[FieldInfo.Format]
        UUID4: _ClassVar[FieldInfo.Format]
        IPV4: _ClassVar[FieldInfo.Format]
        IPV6: _ClassVar[FieldInfo.Format]
        IPV4_OR_IPV6: _ClassVar[FieldInfo.Format]
    FORMAT_UNSPECIFIED: FieldInfo.Format
    UUID4: FieldInfo.Format
    IPV4: FieldInfo.Format
    IPV6: FieldInfo.Format
    IPV4_OR_IPV6: FieldInfo.Format
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    format: FieldInfo.Format
    def __init__(
        self, format: _Optional[_Union[FieldInfo.Format, str]] = ...
    ) -> None: ...

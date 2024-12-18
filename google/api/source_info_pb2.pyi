from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class SourceInfo(_message.Message):
    __slots__ = ("source_files",)
    SOURCE_FILES_FIELD_NUMBER: _ClassVar[int]
    source_files: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(
        self, source_files: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...
    ) -> None: ...
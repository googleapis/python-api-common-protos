from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

from google.api import label_pb2 as _label_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class LogDescriptor(_message.Message):
    __slots__ = ("name", "labels", "description", "display_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    labels: _containers.RepeatedCompositeFieldContainer[_label_pb2.LabelDescriptor]
    description: str
    display_name: str
    def __init__(
        self,
        name: _Optional[str] = ...,
        labels: _Optional[
            _Iterable[_Union[_label_pb2.LabelDescriptor, _Mapping]]
        ] = ...,
        description: _Optional[str] = ...,
        display_name: _Optional[str] = ...,
    ) -> None: ...

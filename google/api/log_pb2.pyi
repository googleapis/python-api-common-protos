# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.api import label_pb2 as _label_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import (
    ClassVar as _ClassVar,
    Iterable as _Iterable,
    Mapping as _Mapping,
    Optional as _Optional,
    Union as _Union,
)

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

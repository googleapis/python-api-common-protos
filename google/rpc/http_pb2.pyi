from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class HttpRequest(_message.Message):
    __slots__ = ("method", "uri", "headers", "body")
    METHOD_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    method: str
    uri: str
    headers: _containers.RepeatedCompositeFieldContainer[HttpHeader]
    body: bytes
    def __init__(
        self,
        method: _Optional[str] = ...,
        uri: _Optional[str] = ...,
        headers: _Optional[_Iterable[_Union[HttpHeader, _Mapping]]] = ...,
        body: _Optional[bytes] = ...,
    ) -> None: ...

class HttpResponse(_message.Message):
    __slots__ = ("status", "reason", "headers", "body")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    status: int
    reason: str
    headers: _containers.RepeatedCompositeFieldContainer[HttpHeader]
    body: bytes
    def __init__(
        self,
        status: _Optional[int] = ...,
        reason: _Optional[str] = ...,
        headers: _Optional[_Iterable[_Union[HttpHeader, _Mapping]]] = ...,
        body: _Optional[bytes] = ...,
    ) -> None: ...

class HttpHeader(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(
        self, key: _Optional[str] = ..., value: _Optional[str] = ...
    ) -> None: ...

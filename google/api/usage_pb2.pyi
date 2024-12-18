from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class Usage(_message.Message):
    __slots__ = ("requirements", "rules", "producer_notification_channel")
    REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    PRODUCER_NOTIFICATION_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    requirements: _containers.RepeatedScalarFieldContainer[str]
    rules: _containers.RepeatedCompositeFieldContainer[UsageRule]
    producer_notification_channel: str
    def __init__(
        self,
        requirements: _Optional[_Iterable[str]] = ...,
        rules: _Optional[_Iterable[_Union[UsageRule, _Mapping]]] = ...,
        producer_notification_channel: _Optional[str] = ...,
    ) -> None: ...

class UsageRule(_message.Message):
    __slots__ = ("selector", "allow_unregistered_calls", "skip_service_control")
    SELECTOR_FIELD_NUMBER: _ClassVar[int]
    ALLOW_UNREGISTERED_CALLS_FIELD_NUMBER: _ClassVar[int]
    SKIP_SERVICE_CONTROL_FIELD_NUMBER: _ClassVar[int]
    selector: str
    allow_unregistered_calls: bool
    skip_service_control: bool
    def __init__(
        self,
        selector: _Optional[str] = ...,
        allow_unregistered_calls: bool = ...,
        skip_service_control: bool = ...,
    ) -> None: ...

from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class Logging(_message.Message):
    __slots__ = ("producer_destinations", "consumer_destinations")

    class LoggingDestination(_message.Message):
        __slots__ = ("monitored_resource", "logs")
        MONITORED_RESOURCE_FIELD_NUMBER: _ClassVar[int]
        LOGS_FIELD_NUMBER: _ClassVar[int]
        monitored_resource: str
        logs: _containers.RepeatedScalarFieldContainer[str]
        def __init__(
            self,
            monitored_resource: _Optional[str] = ...,
            logs: _Optional[_Iterable[str]] = ...,
        ) -> None: ...
    PRODUCER_DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    producer_destinations: _containers.RepeatedCompositeFieldContainer[
        Logging.LoggingDestination
    ]
    consumer_destinations: _containers.RepeatedCompositeFieldContainer[
        Logging.LoggingDestination
    ]
    def __init__(
        self,
        producer_destinations: _Optional[
            _Iterable[_Union[Logging.LoggingDestination, _Mapping]]
        ] = ...,
        consumer_destinations: _Optional[
            _Iterable[_Union[Logging.LoggingDestination, _Mapping]]
        ] = ...,
    ) -> None: ...
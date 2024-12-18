from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class Monitoring(_message.Message):
    __slots__ = ("producer_destinations", "consumer_destinations")

    class MonitoringDestination(_message.Message):
        __slots__ = ("monitored_resource", "metrics")
        MONITORED_RESOURCE_FIELD_NUMBER: _ClassVar[int]
        METRICS_FIELD_NUMBER: _ClassVar[int]
        monitored_resource: str
        metrics: _containers.RepeatedScalarFieldContainer[str]
        def __init__(
            self,
            monitored_resource: _Optional[str] = ...,
            metrics: _Optional[_Iterable[str]] = ...,
        ) -> None: ...
    PRODUCER_DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    producer_destinations: _containers.RepeatedCompositeFieldContainer[
        Monitoring.MonitoringDestination
    ]
    consumer_destinations: _containers.RepeatedCompositeFieldContainer[
        Monitoring.MonitoringDestination
    ]
    def __init__(
        self,
        producer_destinations: _Optional[
            _Iterable[_Union[Monitoring.MonitoringDestination, _Mapping]]
        ] = ...,
        consumer_destinations: _Optional[
            _Iterable[_Union[Monitoring.MonitoringDestination, _Mapping]]
        ] = ...,
    ) -> None: ...
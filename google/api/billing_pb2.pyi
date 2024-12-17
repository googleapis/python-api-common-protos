from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class Billing(_message.Message):
    __slots__ = ("consumer_destinations",)

    class BillingDestination(_message.Message):
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
    CONSUMER_DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    consumer_destinations: _containers.RepeatedCompositeFieldContainer[
        Billing.BillingDestination
    ]
    def __init__(
        self,
        consumer_destinations: _Optional[
            _Iterable[_Union[Billing.BillingDestination, _Mapping]]
        ] = ...,
    ) -> None: ...

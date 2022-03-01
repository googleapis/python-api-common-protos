# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
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

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/rpc/context/attribute_context.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b"\n*google/rpc/context/attribute_context.proto\x12\x12google.rpc.context\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc6\x0c\n\x10\x41ttributeContext\x12\x39\n\x06origin\x18\x07 \x01(\x0b\x32).google.rpc.context.AttributeContext.Peer\x12\x39\n\x06source\x18\x01 \x01(\x0b\x32).google.rpc.context.AttributeContext.Peer\x12>\n\x0b\x64\x65stination\x18\x02 \x01(\x0b\x32).google.rpc.context.AttributeContext.Peer\x12=\n\x07request\x18\x03 \x01(\x0b\x32,.google.rpc.context.AttributeContext.Request\x12?\n\x08response\x18\x04 \x01(\x0b\x32-.google.rpc.context.AttributeContext.Response\x12?\n\x08resource\x18\x05 \x01(\x0b\x32-.google.rpc.context.AttributeContext.Resource\x12\x35\n\x03\x61pi\x18\x06 \x01(\x0b\x32(.google.rpc.context.AttributeContext.Api\x1a\xbe\x01\n\x04Peer\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x03\x12\x45\n\x06labels\x18\x06 \x03(\x0b\x32\x35.google.rpc.context.AttributeContext.Peer.LabelsEntry\x12\x11\n\tprincipal\x18\x07 \x01(\t\x12\x13\n\x0bregion_code\x18\x08 \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aL\n\x03\x41pi\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x11\n\toperation\x18\x02 \x01(\t\x12\x10\n\x08protocol\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\t\x1a\x7f\n\x04\x41uth\x12\x11\n\tprincipal\x18\x01 \x01(\t\x12\x11\n\taudiences\x18\x02 \x03(\t\x12\x11\n\tpresenter\x18\x03 \x01(\t\x12'\n\x06\x63laims\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x15\n\raccess_levels\x18\x05 \x03(\t\x1a\xef\x02\n\x07Request\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06method\x18\x02 \x01(\t\x12J\n\x07headers\x18\x03 \x03(\x0b\x32\x39.google.rpc.context.AttributeContext.Request.HeadersEntry\x12\x0c\n\x04path\x18\x04 \x01(\t\x12\x0c\n\x04host\x18\x05 \x01(\t\x12\x0e\n\x06scheme\x18\x06 \x01(\t\x12\r\n\x05query\x18\x07 \x01(\t\x12(\n\x04time\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04size\x18\n \x01(\x03\x12\x10\n\x08protocol\x18\x0b \x01(\t\x12\x0e\n\x06reason\x18\x0c \x01(\t\x12\x37\n\x04\x61uth\x18\r \x01(\x0b\x32).google.rpc.context.AttributeContext.Auth\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\xcd\x01\n\x08Response\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x03\x12\x0c\n\x04size\x18\x02 \x01(\x03\x12K\n\x07headers\x18\x03 \x03(\x0b\x32:.google.rpc.context.AttributeContext.Response.HeadersEntry\x12(\n\x04time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\xb1\x01\n\x08Resource\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12I\n\x06labels\x18\x04 \x03(\x0b\x32\x39.google.rpc.context.AttributeContext.Resource.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x8b\x01\n\x16\x63om.google.rpc.contextB\x15\x41ttributeContextProtoP\x01ZUgoogle.golang.org/genproto/googleapis/rpc/context/attribute_context;attribute_context\xf8\x01\x01\x62\x06proto3"
)


_ATTRIBUTECONTEXT = DESCRIPTOR.message_types_by_name["AttributeContext"]
_ATTRIBUTECONTEXT_PEER = _ATTRIBUTECONTEXT.nested_types_by_name["Peer"]
_ATTRIBUTECONTEXT_PEER_LABELSENTRY = _ATTRIBUTECONTEXT_PEER.nested_types_by_name[
    "LabelsEntry"
]
_ATTRIBUTECONTEXT_API = _ATTRIBUTECONTEXT.nested_types_by_name["Api"]
_ATTRIBUTECONTEXT_AUTH = _ATTRIBUTECONTEXT.nested_types_by_name["Auth"]
_ATTRIBUTECONTEXT_REQUEST = _ATTRIBUTECONTEXT.nested_types_by_name["Request"]
_ATTRIBUTECONTEXT_REQUEST_HEADERSENTRY = _ATTRIBUTECONTEXT_REQUEST.nested_types_by_name[
    "HeadersEntry"
]
_ATTRIBUTECONTEXT_RESPONSE = _ATTRIBUTECONTEXT.nested_types_by_name["Response"]
_ATTRIBUTECONTEXT_RESPONSE_HEADERSENTRY = _ATTRIBUTECONTEXT_RESPONSE.nested_types_by_name[
    "HeadersEntry"
]
_ATTRIBUTECONTEXT_RESOURCE = _ATTRIBUTECONTEXT.nested_types_by_name["Resource"]
_ATTRIBUTECONTEXT_RESOURCE_LABELSENTRY = _ATTRIBUTECONTEXT_RESOURCE.nested_types_by_name[
    "LabelsEntry"
]
AttributeContext = _reflection.GeneratedProtocolMessageType(
    "AttributeContext",
    (_message.Message,),
    {
        "Peer": _reflection.GeneratedProtocolMessageType(
            "Peer",
            (_message.Message,),
            {
                "LabelsEntry": _reflection.GeneratedProtocolMessageType(
                    "LabelsEntry",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _ATTRIBUTECONTEXT_PEER_LABELSENTRY,
                        "__module__": "google.rpc.context.attribute_context_pb2"
                        # @@protoc_insertion_point(class_scope:google.rpc.context.AttributeContext.Peer.LabelsEntry)
                    },
                ),
                "DESCRIPTOR": _ATTRIBUTECONTEXT_PEER,
                "__module__": "google.rpc.context.attribute_context_pb2"
                # @@protoc_insertion_point(class_scope:google.rpc.context.AttributeContext.Peer)
            },
        ),
        "Api": _reflection.GeneratedProtocolMessageType(
            "Api",
            (_message.Message,),
            {
                "DESCRIPTOR": _ATTRIBUTECONTEXT_API,
                "__module__": "google.rpc.context.attribute_context_pb2"
                # @@protoc_insertion_point(class_scope:google.rpc.context.AttributeContext.Api)
            },
        ),
        "Auth": _reflection.GeneratedProtocolMessageType(
            "Auth",
            (_message.Message,),
            {
                "DESCRIPTOR": _ATTRIBUTECONTEXT_AUTH,
                "__module__": "google.rpc.context.attribute_context_pb2"
                # @@protoc_insertion_point(class_scope:google.rpc.context.AttributeContext.Auth)
            },
        ),
        "Request": _reflection.GeneratedProtocolMessageType(
            "Request",
            (_message.Message,),
            {
                "HeadersEntry": _reflection.GeneratedProtocolMessageType(
                    "HeadersEntry",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _ATTRIBUTECONTEXT_REQUEST_HEADERSENTRY,
                        "__module__": "google.rpc.context.attribute_context_pb2"
                        # @@protoc_insertion_point(class_scope:google.rpc.context.AttributeContext.Request.HeadersEntry)
                    },
                ),
                "DESCRIPTOR": _ATTRIBUTECONTEXT_REQUEST,
                "__module__": "google.rpc.context.attribute_context_pb2"
                # @@protoc_insertion_point(class_scope:google.rpc.context.AttributeContext.Request)
            },
        ),
        "Response": _reflection.GeneratedProtocolMessageType(
            "Response",
            (_message.Message,),
            {
                "HeadersEntry": _reflection.GeneratedProtocolMessageType(
                    "HeadersEntry",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _ATTRIBUTECONTEXT_RESPONSE_HEADERSENTRY,
                        "__module__": "google.rpc.context.attribute_context_pb2"
                        # @@protoc_insertion_point(class_scope:google.rpc.context.AttributeContext.Response.HeadersEntry)
                    },
                ),
                "DESCRIPTOR": _ATTRIBUTECONTEXT_RESPONSE,
                "__module__": "google.rpc.context.attribute_context_pb2"
                # @@protoc_insertion_point(class_scope:google.rpc.context.AttributeContext.Response)
            },
        ),
        "Resource": _reflection.GeneratedProtocolMessageType(
            "Resource",
            (_message.Message,),
            {
                "LabelsEntry": _reflection.GeneratedProtocolMessageType(
                    "LabelsEntry",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _ATTRIBUTECONTEXT_RESOURCE_LABELSENTRY,
                        "__module__": "google.rpc.context.attribute_context_pb2"
                        # @@protoc_insertion_point(class_scope:google.rpc.context.AttributeContext.Resource.LabelsEntry)
                    },
                ),
                "DESCRIPTOR": _ATTRIBUTECONTEXT_RESOURCE,
                "__module__": "google.rpc.context.attribute_context_pb2"
                # @@protoc_insertion_point(class_scope:google.rpc.context.AttributeContext.Resource)
            },
        ),
        "DESCRIPTOR": _ATTRIBUTECONTEXT,
        "__module__": "google.rpc.context.attribute_context_pb2"
        # @@protoc_insertion_point(class_scope:google.rpc.context.AttributeContext)
    },
)
_sym_db.RegisterMessage(AttributeContext)
_sym_db.RegisterMessage(AttributeContext.Peer)
_sym_db.RegisterMessage(AttributeContext.Peer.LabelsEntry)
_sym_db.RegisterMessage(AttributeContext.Api)
_sym_db.RegisterMessage(AttributeContext.Auth)
_sym_db.RegisterMessage(AttributeContext.Request)
_sym_db.RegisterMessage(AttributeContext.Request.HeadersEntry)
_sym_db.RegisterMessage(AttributeContext.Response)
_sym_db.RegisterMessage(AttributeContext.Response.HeadersEntry)
_sym_db.RegisterMessage(AttributeContext.Resource)
_sym_db.RegisterMessage(AttributeContext.Resource.LabelsEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\026com.google.rpc.contextB\025AttributeContextProtoP\001ZUgoogle.golang.org/genproto/googleapis/rpc/context/attribute_context;attribute_context\370\001\001"
    _ATTRIBUTECONTEXT_PEER_LABELSENTRY._options = None
    _ATTRIBUTECONTEXT_PEER_LABELSENTRY._serialized_options = b"8\001"
    _ATTRIBUTECONTEXT_REQUEST_HEADERSENTRY._options = None
    _ATTRIBUTECONTEXT_REQUEST_HEADERSENTRY._serialized_options = b"8\001"
    _ATTRIBUTECONTEXT_RESPONSE_HEADERSENTRY._options = None
    _ATTRIBUTECONTEXT_RESPONSE_HEADERSENTRY._serialized_options = b"8\001"
    _ATTRIBUTECONTEXT_RESOURCE_LABELSENTRY._options = None
    _ATTRIBUTECONTEXT_RESOURCE_LABELSENTRY._serialized_options = b"8\001"
    _ATTRIBUTECONTEXT._serialized_start = 130
    _ATTRIBUTECONTEXT._serialized_end = 1736
    _ATTRIBUTECONTEXT_PEER._serialized_start = 581
    _ATTRIBUTECONTEXT_PEER._serialized_end = 771
    _ATTRIBUTECONTEXT_PEER_LABELSENTRY._serialized_start = 726
    _ATTRIBUTECONTEXT_PEER_LABELSENTRY._serialized_end = 771
    _ATTRIBUTECONTEXT_API._serialized_start = 773
    _ATTRIBUTECONTEXT_API._serialized_end = 849
    _ATTRIBUTECONTEXT_AUTH._serialized_start = 851
    _ATTRIBUTECONTEXT_AUTH._serialized_end = 978
    _ATTRIBUTECONTEXT_REQUEST._serialized_start = 981
    _ATTRIBUTECONTEXT_REQUEST._serialized_end = 1348
    _ATTRIBUTECONTEXT_REQUEST_HEADERSENTRY._serialized_start = 1302
    _ATTRIBUTECONTEXT_REQUEST_HEADERSENTRY._serialized_end = 1348
    _ATTRIBUTECONTEXT_RESPONSE._serialized_start = 1351
    _ATTRIBUTECONTEXT_RESPONSE._serialized_end = 1556
    _ATTRIBUTECONTEXT_RESPONSE_HEADERSENTRY._serialized_start = 1302
    _ATTRIBUTECONTEXT_RESPONSE_HEADERSENTRY._serialized_end = 1348
    _ATTRIBUTECONTEXT_RESOURCE._serialized_start = 1559
    _ATTRIBUTECONTEXT_RESOURCE._serialized_end = 1736
    _ATTRIBUTECONTEXT_RESOURCE_LABELSENTRY._serialized_start = 726
    _ATTRIBUTECONTEXT_RESOURCE_LABELSENTRY._serialized_end = 771
# @@protoc_insertion_point(module_scope)

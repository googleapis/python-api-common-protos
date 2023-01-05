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
# source: google/rpc/http.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x15google/rpc/http.proto\x12\ngoogle.rpc"a\n\x0bHttpRequest\x12\x0e\n\x06method\x18\x01 \x01(\t\x12\x0b\n\x03uri\x18\x02 \x01(\t\x12\'\n\x07headers\x18\x03 \x03(\x0b\x32\x16.google.rpc.HttpHeader\x12\x0c\n\x04\x62ody\x18\x04 \x01(\x0c"e\n\x0cHttpResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0e\n\x06reason\x18\x02 \x01(\t\x12\'\n\x07headers\x18\x03 \x03(\x0b\x32\x16.google.rpc.HttpHeader\x12\x0c\n\x04\x62ody\x18\x04 \x01(\x0c"(\n\nHttpHeader\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\tBX\n\x0e\x63om.google.rpcB\tHttpProtoP\x01Z3google.golang.org/genproto/googleapis/rpc/http;http\xa2\x02\x03RPCb\x06proto3'
)


_HTTPREQUEST = DESCRIPTOR.message_types_by_name["HttpRequest"]
_HTTPRESPONSE = DESCRIPTOR.message_types_by_name["HttpResponse"]
_HTTPHEADER = DESCRIPTOR.message_types_by_name["HttpHeader"]
HttpRequest = _reflection.GeneratedProtocolMessageType(
    "HttpRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _HTTPREQUEST,
        "__module__": "google.rpc.http_pb2"
        # @@protoc_insertion_point(class_scope:google.rpc.HttpRequest)
    },
)
_sym_db.RegisterMessage(HttpRequest)

HttpResponse = _reflection.GeneratedProtocolMessageType(
    "HttpResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _HTTPRESPONSE,
        "__module__": "google.rpc.http_pb2"
        # @@protoc_insertion_point(class_scope:google.rpc.HttpResponse)
    },
)
_sym_db.RegisterMessage(HttpResponse)

HttpHeader = _reflection.GeneratedProtocolMessageType(
    "HttpHeader",
    (_message.Message,),
    {
        "DESCRIPTOR": _HTTPHEADER,
        "__module__": "google.rpc.http_pb2"
        # @@protoc_insertion_point(class_scope:google.rpc.HttpHeader)
    },
)
_sym_db.RegisterMessage(HttpHeader)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\016com.google.rpcB\tHttpProtoP\001Z3google.golang.org/genproto/googleapis/rpc/http;http\242\002\003RPC"
    _HTTPREQUEST._serialized_start = 37
    _HTTPREQUEST._serialized_end = 134
    _HTTPRESPONSE._serialized_start = 136
    _HTTPRESPONSE._serialized_end = 237
    _HTTPHEADER._serialized_start = 239
    _HTTPHEADER._serialized_end = 279
# @@protoc_insertion_point(module_scope)

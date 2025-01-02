# -*- coding: utf-8 -*-

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

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/httpbody.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x19google/api/httpbody.proto\x12\ngoogle.api\x1a\x19google/protobuf/any.proto"X\n\x08HttpBody\x12\x14\n\x0c\x63ontent_type\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12(\n\nextensions\x18\x03 \x03(\x0b\x32\x14.google.protobuf.AnyBe\n\x0e\x63om.google.apiB\rHttpBodyProtoP\x01Z;google.golang.org/genproto/googleapis/api/httpbody;httpbody\xa2\x02\x04GAPIb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "google.api.httpbody_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\016com.google.apiB\rHttpBodyProtoP\001Z;google.golang.org/genproto/googleapis/api/httpbody;httpbody\242\002\004GAPI"
    _globals["_HTTPBODY"]._serialized_start = 68
    _globals["_HTTPBODY"]._serialized_end = 156
# @@protoc_insertion_point(module_scope)

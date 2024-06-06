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
# source: google/api/control.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import policy_pb2 as google_dot_api_dot_policy__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x18google/api/control.proto\x12\ngoogle.api\x1a\x17google/api/policy.proto"Q\n\x07\x43ontrol\x12\x13\n\x0b\x65nvironment\x18\x01 \x01(\t\x12\x31\n\x0fmethod_policies\x18\x04 \x03(\x0b\x32\x18.google.api.MethodPolicyBn\n\x0e\x63om.google.apiB\x0c\x43ontrolProtoP\x01ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\xa2\x02\x04GAPIb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "google.api.control_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n\016com.google.apiB\014ControlProtoP\001ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\242\002\004GAPI"
    _globals["_CONTROL"]._serialized_start = 65
    _globals["_CONTROL"]._serialized_end = 146
# @@protoc_insertion_point(module_scope)

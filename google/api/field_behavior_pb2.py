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
# source: google/api/field_behavior.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b"\n\x1fgoogle/api/field_behavior.proto\x12\ngoogle.api\x1a google/protobuf/descriptor.proto*\xb6\x01\n\rFieldBehavior\x12\x1e\n\x1a\x46IELD_BEHAVIOR_UNSPECIFIED\x10\x00\x12\x0c\n\x08OPTIONAL\x10\x01\x12\x0c\n\x08REQUIRED\x10\x02\x12\x0f\n\x0bOUTPUT_ONLY\x10\x03\x12\x0e\n\nINPUT_ONLY\x10\x04\x12\r\n\tIMMUTABLE\x10\x05\x12\x12\n\x0eUNORDERED_LIST\x10\x06\x12\x15\n\x11NON_EMPTY_DEFAULT\x10\x07\x12\x0e\n\nIDENTIFIER\x10\x08:U\n\x0e\x66ield_behavior\x12\x1d.google.protobuf.FieldOptions\x18\x9c\x08 \x03(\x0e\x32\x19.google.api.FieldBehaviorB\x02\x10\x00\x42p\n\x0e\x63om.google.apiB\x12\x46ieldBehaviorProtoP\x01ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\xa2\x02\x04GAPIb\x06proto3"
)

_FIELDBEHAVIOR = DESCRIPTOR.enum_types_by_name["FieldBehavior"]
FieldBehavior = enum_type_wrapper.EnumTypeWrapper(_FIELDBEHAVIOR)
FIELD_BEHAVIOR_UNSPECIFIED = 0
OPTIONAL = 1
REQUIRED = 2
OUTPUT_ONLY = 3
INPUT_ONLY = 4
IMMUTABLE = 5
UNORDERED_LIST = 6
NON_EMPTY_DEFAULT = 7
IDENTIFIER = 8

FIELD_BEHAVIOR_FIELD_NUMBER = 1052
field_behavior = DESCRIPTOR.extensions_by_name["field_behavior"]

if _descriptor._USE_C_DESCRIPTORS == False:
    google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(
        field_behavior
    )

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\016com.google.apiB\022FieldBehaviorProtoP\001ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\242\002\004GAPI"
    field_behavior._options = None
    field_behavior._serialized_options = b"\020\000"
    _FIELDBEHAVIOR._serialized_start = 82
    _FIELDBEHAVIOR._serialized_end = 264
# @@protoc_insertion_point(module_scope)

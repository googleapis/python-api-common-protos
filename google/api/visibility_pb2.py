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
# source: google/api/visibility.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1bgoogle/api/visibility.proto\x12\ngoogle.api\x1a google/protobuf/descriptor.proto"7\n\nVisibility\x12)\n\x05rules\x18\x01 \x03(\x0b\x32\x1a.google.api.VisibilityRule"7\n\x0eVisibilityRule\x12\x10\n\x08selector\x18\x01 \x01(\t\x12\x13\n\x0brestriction\x18\x02 \x01(\t:T\n\x0f\x65num_visibility\x12\x1c.google.protobuf.EnumOptions\x18\xaf\xca\xbc" \x01(\x0b\x32\x1a.google.api.VisibilityRule:Z\n\x10value_visibility\x12!.google.protobuf.EnumValueOptions\x18\xaf\xca\xbc" \x01(\x0b\x32\x1a.google.api.VisibilityRule:V\n\x10\x66ield_visibility\x12\x1d.google.protobuf.FieldOptions\x18\xaf\xca\xbc" \x01(\x0b\x32\x1a.google.api.VisibilityRule:Z\n\x12message_visibility\x12\x1f.google.protobuf.MessageOptions\x18\xaf\xca\xbc" \x01(\x0b\x32\x1a.google.api.VisibilityRule:X\n\x11method_visibility\x12\x1e.google.protobuf.MethodOptions\x18\xaf\xca\xbc" \x01(\x0b\x32\x1a.google.api.VisibilityRule:V\n\x0e\x61pi_visibility\x12\x1f.google.protobuf.ServiceOptions\x18\xaf\xca\xbc" \x01(\x0b\x32\x1a.google.api.VisibilityRuleBn\n\x0e\x63om.google.apiB\x0fVisibilityProtoP\x01Z?google.golang.org/genproto/googleapis/api/visibility;visibility\xf8\x01\x01\xa2\x02\x04GAPIb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "google.api.visibility_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\016com.google.apiB\017VisibilityProtoP\001Z?google.golang.org/genproto/googleapis/api/visibility;visibility\370\001\001\242\002\004GAPI"
    _globals["_VISIBILITY"]._serialized_start = 77
    _globals["_VISIBILITY"]._serialized_end = 132
    _globals["_VISIBILITYRULE"]._serialized_start = 134
    _globals["_VISIBILITYRULE"]._serialized_end = 189
# @@protoc_insertion_point(module_scope)

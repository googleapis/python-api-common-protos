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
# source: google/rpc/context/audit_context.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n&google/rpc/context/audit_context.proto\x12\x12google.rpc.context\x1a\x1cgoogle/protobuf/struct.proto"\xc7\x01\n\x0c\x41uditContext\x12\x11\n\taudit_log\x18\x01 \x01(\x0c\x12\x31\n\x10scrubbed_request\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x32\n\x11scrubbed_response\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12$\n\x1cscrubbed_response_item_count\x18\x04 \x01(\x05\x12\x17\n\x0ftarget_resource\x18\x05 \x01(\tBk\n\x16\x63om.google.rpc.contextB\x11\x41uditContextProtoP\x01Z9google.golang.org/genproto/googleapis/rpc/context;context\xf8\x01\x01\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "google.rpc.context.audit_context_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n\026com.google.rpc.contextB\021AuditContextProtoP\001Z9google.golang.org/genproto/googleapis/rpc/context;context\370\001\001"
    _globals["_AUDITCONTEXT"]._serialized_start = 93
    _globals["_AUDITCONTEXT"]._serialized_end = 292
# @@protoc_insertion_point(module_scope)

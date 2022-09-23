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
# source: google/api/monitored_resource.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import label_pb2 as google_dot_api_dot_label__pb2
from google.api import launch_stage_pb2 as google_dot_api_dot_launch__stage__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n#google/api/monitored_resource.proto\x12\ngoogle.api\x1a\x16google/api/label.proto\x1a\x1dgoogle/api/launch_stage.proto\x1a\x1cgoogle/protobuf/struct.proto"\xc0\x01\n\x1bMonitoredResourceDescriptor\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12+\n\x06labels\x18\x04 \x03(\x0b\x32\x1b.google.api.LabelDescriptor\x12-\n\x0claunch_stage\x18\x07 \x01(\x0e\x32\x17.google.api.LaunchStage"\x8b\x01\n\x11MonitoredResource\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x39\n\x06labels\x18\x02 \x03(\x0b\x32).google.api.MonitoredResource.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\xca\x01\n\x19MonitoredResourceMetadata\x12.\n\rsystem_labels\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12J\n\x0buser_labels\x18\x02 \x03(\x0b\x32\x35.google.api.MonitoredResourceMetadata.UserLabelsEntry\x1a\x31\n\x0fUserLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42y\n\x0e\x63om.google.apiB\x16MonitoredResourceProtoP\x01ZCgoogle.golang.org/genproto/googleapis/api/monitoredres;monitoredres\xf8\x01\x01\xa2\x02\x04GAPIb\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "google.api.monitored_resource_pb2", globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\016com.google.apiB\026MonitoredResourceProtoP\001ZCgoogle.golang.org/genproto/googleapis/api/monitoredres;monitoredres\370\001\001\242\002\004GAPI"
    _MONITOREDRESOURCE_LABELSENTRY._options = None
    _MONITOREDRESOURCE_LABELSENTRY._serialized_options = b"8\001"
    _MONITOREDRESOURCEMETADATA_USERLABELSENTRY._options = None
    _MONITOREDRESOURCEMETADATA_USERLABELSENTRY._serialized_options = b"8\001"
    _MONITOREDRESOURCEDESCRIPTOR._serialized_start = 137
    _MONITOREDRESOURCEDESCRIPTOR._serialized_end = 329
    _MONITOREDRESOURCE._serialized_start = 332
    _MONITOREDRESOURCE._serialized_end = 471
    _MONITOREDRESOURCE_LABELSENTRY._serialized_start = 426
    _MONITOREDRESOURCE_LABELSENTRY._serialized_end = 471
    _MONITOREDRESOURCEMETADATA._serialized_start = 474
    _MONITOREDRESOURCEMETADATA._serialized_end = 676
    _MONITOREDRESOURCEMETADATA_USERLABELSENTRY._serialized_start = 627
    _MONITOREDRESOURCEMETADATA_USERLABELSENTRY._serialized_end = 676
# @@protoc_insertion_point(module_scope)

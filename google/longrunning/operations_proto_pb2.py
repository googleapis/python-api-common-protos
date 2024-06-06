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
# source: google/longrunning/operations.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n#google/longrunning/operations.proto\x12\x12google.longrunning\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x17google/rpc/status.proto\x1a google/protobuf/descriptor.proto"\xa8\x01\n\tOperation\x12\x0c\n\x04name\x18\x01 \x01(\t\x12&\n\x08metadata\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0c\n\x04\x64one\x18\x03 \x01(\x08\x12#\n\x05\x65rror\x18\x04 \x01(\x0b\x32\x12.google.rpc.StatusH\x00\x12(\n\x08response\x18\x05 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x42\x08\n\x06result"#\n\x13GetOperationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"\\\n\x15ListOperationsRequest\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"d\n\x16ListOperationsResponse\x12\x31\n\noperations\x18\x01 \x03(\x0b\x32\x1d.google.longrunning.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"&\n\x16\x43\x61ncelOperationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"&\n\x16\x44\x65leteOperationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"P\n\x14WaitOperationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12*\n\x07timeout\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration"=\n\rOperationInfo\x12\x15\n\rresponse_type\x18\x01 \x01(\t\x12\x15\n\rmetadata_type\x18\x02 \x01(\t2\xaa\x05\n\nOperations\x12\x94\x01\n\x0eListOperations\x12).google.longrunning.ListOperationsRequest\x1a*.google.longrunning.ListOperationsResponse"+\xda\x41\x0bname,filter\x82\xd3\xe4\x93\x02\x17\x12\x15/v1/{name=operations}\x12\x7f\n\x0cGetOperation\x12\'.google.longrunning.GetOperationRequest\x1a\x1d.google.longrunning.Operation"\'\xda\x41\x04name\x82\xd3\xe4\x93\x02\x1a\x12\x18/v1/{name=operations/**}\x12~\n\x0f\x44\x65leteOperation\x12*.google.longrunning.DeleteOperationRequest\x1a\x16.google.protobuf.Empty"\'\xda\x41\x04name\x82\xd3\xe4\x93\x02\x1a*\x18/v1/{name=operations/**}\x12\x88\x01\n\x0f\x43\x61ncelOperation\x12*.google.longrunning.CancelOperationRequest\x1a\x16.google.protobuf.Empty"1\xda\x41\x04name\x82\xd3\xe4\x93\x02$"\x1f/v1/{name=operations/**}:cancel:\x01*\x12Z\n\rWaitOperation\x12(.google.longrunning.WaitOperationRequest\x1a\x1d.google.longrunning.Operation"\x00\x1a\x1d\xca\x41\x1alongrunning.googleapis.com:Z\n\x0eoperation_info\x12\x1e.google.protobuf.MethodOptions\x18\x99\x08 \x01(\x0b\x32!.google.longrunning.OperationInfoB\x9d\x01\n\x16\x63om.google.longrunningB\x0fOperationsProtoP\x01ZCcloud.google.com/go/longrunning/autogen/longrunningpb;longrunningpb\xf8\x01\x01\xaa\x02\x12Google.LongRunning\xca\x02\x12Google\\LongRunningb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "google.longrunning.operations_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n\026com.google.longrunningB\017OperationsProtoP\001ZCcloud.google.com/go/longrunning/autogen/longrunningpb;longrunningpb\370\001\001\252\002\022Google.LongRunning\312\002\022Google\\LongRunning"
    _globals["_OPERATIONS"]._options = None
    _globals["_OPERATIONS"]._serialized_options = b"\312A\032longrunning.googleapis.com"
    _globals["_OPERATIONS"].methods_by_name["ListOperations"]._options = None
    _globals["_OPERATIONS"].methods_by_name[
        "ListOperations"
    ]._serialized_options = (
        b"\332A\013name,filter\202\323\344\223\002\027\022\025/v1/{name=operations}"
    )
    _globals["_OPERATIONS"].methods_by_name["GetOperation"]._options = None
    _globals["_OPERATIONS"].methods_by_name[
        "GetOperation"
    ]._serialized_options = (
        b"\332A\004name\202\323\344\223\002\032\022\030/v1/{name=operations/**}"
    )
    _globals["_OPERATIONS"].methods_by_name["DeleteOperation"]._options = None
    _globals["_OPERATIONS"].methods_by_name[
        "DeleteOperation"
    ]._serialized_options = (
        b"\332A\004name\202\323\344\223\002\032*\030/v1/{name=operations/**}"
    )
    _globals["_OPERATIONS"].methods_by_name["CancelOperation"]._options = None
    _globals["_OPERATIONS"].methods_by_name[
        "CancelOperation"
    ]._serialized_options = (
        b'\332A\004name\202\323\344\223\002$"\037/v1/{name=operations/**}:cancel:\001*'
    )
    _globals["_OPERATION"]._serialized_start = 262
    _globals["_OPERATION"]._serialized_end = 430
    _globals["_GETOPERATIONREQUEST"]._serialized_start = 432
    _globals["_GETOPERATIONREQUEST"]._serialized_end = 467
    _globals["_LISTOPERATIONSREQUEST"]._serialized_start = 469
    _globals["_LISTOPERATIONSREQUEST"]._serialized_end = 561
    _globals["_LISTOPERATIONSRESPONSE"]._serialized_start = 563
    _globals["_LISTOPERATIONSRESPONSE"]._serialized_end = 663
    _globals["_CANCELOPERATIONREQUEST"]._serialized_start = 665
    _globals["_CANCELOPERATIONREQUEST"]._serialized_end = 703
    _globals["_DELETEOPERATIONREQUEST"]._serialized_start = 705
    _globals["_DELETEOPERATIONREQUEST"]._serialized_end = 743
    _globals["_WAITOPERATIONREQUEST"]._serialized_start = 745
    _globals["_WAITOPERATIONREQUEST"]._serialized_end = 825
    _globals["_OPERATIONINFO"]._serialized_start = 827
    _globals["_OPERATIONINFO"]._serialized_end = 888
    _globals["_OPERATIONS"]._serialized_start = 891
    _globals["_OPERATIONS"]._serialized_end = 1573
# @@protoc_insertion_point(module_scope)

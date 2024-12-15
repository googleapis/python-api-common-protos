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
# source: google/api/distribution.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1dgoogle/api/distribution.proto\x12\ngoogle.api\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd9\x06\n\x0c\x44istribution\x12\r\n\x05\x63ount\x18\x01 \x01(\x03\x12\x0c\n\x04mean\x18\x02 \x01(\x01\x12 \n\x18sum_of_squared_deviation\x18\x03 \x01(\x01\x12-\n\x05range\x18\x04 \x01(\x0b\x32\x1e.google.api.Distribution.Range\x12>\n\x0e\x62ucket_options\x18\x06 \x01(\x0b\x32&.google.api.Distribution.BucketOptions\x12\x15\n\rbucket_counts\x18\x07 \x03(\x03\x12\x34\n\texemplars\x18\n \x03(\x0b\x32!.google.api.Distribution.Exemplar\x1a!\n\x05Range\x12\x0b\n\x03min\x18\x01 \x01(\x01\x12\x0b\n\x03max\x18\x02 \x01(\x01\x1a\xb5\x03\n\rBucketOptions\x12G\n\x0elinear_buckets\x18\x01 \x01(\x0b\x32-.google.api.Distribution.BucketOptions.LinearH\x00\x12Q\n\x13\x65xponential_buckets\x18\x02 \x01(\x0b\x32\x32.google.api.Distribution.BucketOptions.ExponentialH\x00\x12K\n\x10\x65xplicit_buckets\x18\x03 \x01(\x0b\x32/.google.api.Distribution.BucketOptions.ExplicitH\x00\x1a\x43\n\x06Linear\x12\x1a\n\x12num_finite_buckets\x18\x01 \x01(\x05\x12\r\n\x05width\x18\x02 \x01(\x01\x12\x0e\n\x06offset\x18\x03 \x01(\x01\x1aO\n\x0b\x45xponential\x12\x1a\n\x12num_finite_buckets\x18\x01 \x01(\x05\x12\x15\n\rgrowth_factor\x18\x02 \x01(\x01\x12\r\n\x05scale\x18\x03 \x01(\x01\x1a\x1a\n\x08\x45xplicit\x12\x0e\n\x06\x62ounds\x18\x01 \x03(\x01\x42\t\n\x07options\x1as\n\x08\x45xemplar\x12\r\n\x05value\x18\x01 \x01(\x01\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12)\n\x0b\x61ttachments\x18\x03 \x03(\x0b\x32\x14.google.protobuf.AnyBq\n\x0e\x63om.google.apiB\x11\x44istributionProtoP\x01ZCgoogle.golang.org/genproto/googleapis/api/distribution;distribution\xa2\x02\x04GAPIb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "google.api.distribution_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n\016com.google.apiB\021DistributionProtoP\001ZCgoogle.golang.org/genproto/googleapis/api/distribution;distribution\242\002\004GAPI"
    _globals["_DISTRIBUTION"]._serialized_start = 106
    _globals["_DISTRIBUTION"]._serialized_end = 963
    _globals["_DISTRIBUTION_RANGE"]._serialized_start = 373
    _globals["_DISTRIBUTION_RANGE"]._serialized_end = 406
    _globals["_DISTRIBUTION_BUCKETOPTIONS"]._serialized_start = 409
    _globals["_DISTRIBUTION_BUCKETOPTIONS"]._serialized_end = 846
    _globals["_DISTRIBUTION_BUCKETOPTIONS_LINEAR"]._serialized_start = 659
    _globals["_DISTRIBUTION_BUCKETOPTIONS_LINEAR"]._serialized_end = 726
    _globals["_DISTRIBUTION_BUCKETOPTIONS_EXPONENTIAL"]._serialized_start = 728
    _globals["_DISTRIBUTION_BUCKETOPTIONS_EXPONENTIAL"]._serialized_end = 807
    _globals["_DISTRIBUTION_BUCKETOPTIONS_EXPLICIT"]._serialized_start = 809
    _globals["_DISTRIBUTION_BUCKETOPTIONS_EXPLICIT"]._serialized_end = 835
    _globals["_DISTRIBUTION_EXEMPLAR"]._serialized_start = 848
    _globals["_DISTRIBUTION_EXEMPLAR"]._serialized_end = 963
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/location/locations.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/cloud/location/locations.proto\x12\x15google.cloud.location\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/protobuf/any.proto\x1a\x17google/api/client.proto\"[\n\x14ListLocationsRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\"d\n\x15ListLocationsResponse\x12\x32\n\tlocations\x18\x01 \x03(\x0b\x32\x1f.google.cloud.location.Location\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\"\n\x12GetLocationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\xd7\x01\n\x08Location\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0blocation_id\x18\x04 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x05 \x01(\t\x12;\n\x06labels\x18\x02 \x03(\x0b\x32+.google.cloud.location.Location.LabelsEntry\x12&\n\x08metadata\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32\xa4\x03\n\tLocations\x12\xab\x01\n\rListLocations\x12+.google.cloud.location.ListLocationsRequest\x1a,.google.cloud.location.ListLocationsResponse\"?\x82\xd3\xe4\x93\x02\x39\x12\x14/v1/{name=locations}Z!\x12\x1f/v1/{name=projects/*}/locations\x12\x9e\x01\n\x0bGetLocation\x12).google.cloud.location.GetLocationRequest\x1a\x1f.google.cloud.location.Location\"C\x82\xd3\xe4\x93\x02=\x12\x16/v1/{name=locations/*}Z#\x12!/v1/{name=projects/*/locations/*}\x1aH\xca\x41\x14\x63loud.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformBo\n\x19\x63om.google.cloud.locationB\x0eLocationsProtoP\x01Z=google.golang.org/genproto/googleapis/cloud/location;location\xf8\x01\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.location.locations_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031com.google.cloud.locationB\016LocationsProtoP\001Z=google.golang.org/genproto/googleapis/cloud/location;location\370\001\001'
  _globals['_LOCATION_LABELSENTRY']._options = None
  _globals['_LOCATION_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_LOCATIONS']._options = None
  _globals['_LOCATIONS']._serialized_options = b'\312A\024cloud.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform'
  _globals['_LOCATIONS'].methods_by_name['ListLocations']._options = None
  _globals['_LOCATIONS'].methods_by_name['ListLocations']._serialized_options = b'\202\323\344\223\0029\022\024/v1/{name=locations}Z!\022\037/v1/{name=projects/*}/locations'
  _globals['_LOCATIONS'].methods_by_name['GetLocation']._options = None
  _globals['_LOCATIONS'].methods_by_name['GetLocation']._serialized_options = b'\202\323\344\223\002=\022\026/v1/{name=locations/*}Z#\022!/v1/{name=projects/*/locations/*}'
  _globals['_LISTLOCATIONSREQUEST']._serialized_start=146
  _globals['_LISTLOCATIONSREQUEST']._serialized_end=237
  _globals['_LISTLOCATIONSRESPONSE']._serialized_start=239
  _globals['_LISTLOCATIONSRESPONSE']._serialized_end=339
  _globals['_GETLOCATIONREQUEST']._serialized_start=341
  _globals['_GETLOCATIONREQUEST']._serialized_end=375
  _globals['_LOCATION']._serialized_start=378
  _globals['_LOCATION']._serialized_end=593
  _globals['_LOCATION_LABELSENTRY']._serialized_start=548
  _globals['_LOCATION_LABELSENTRY']._serialized_end=593
  _globals['_LOCATIONS']._serialized_start=596
  _globals['_LOCATIONS']._serialized_end=1016
# @@protoc_insertion_point(module_scope)
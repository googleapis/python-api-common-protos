# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gapic/metadata/gapic_metadata.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#gapic/metadata/gapic_metadata.proto\x12\x15google.gapic.metadata\"\xf0\x05\n\rGapicMetadata\x12\x0e\n\x06schema\x18\x01 \x01(\t\x12\x0f\n\x07\x63omment\x18\x02 \x01(\t\x12\x10\n\x08language\x18\x03 \x01(\t\x12\x15\n\rproto_package\x18\x04 \x01(\t\x12\x17\n\x0flibrary_package\x18\x05 \x01(\t\x12\x44\n\x08services\x18\x06 \x03(\x0b\x32\x32.google.gapic.metadata.GapicMetadata.ServicesEntry\x1ai\n\rServicesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12G\n\x05value\x18\x02 \x01(\x0b\x32\x38.google.gapic.metadata.GapicMetadata.ServiceForTransport:\x02\x38\x01\x1a\xd3\x01\n\x13ServiceForTransport\x12V\n\x07\x63lients\x18\x01 \x03(\x0b\x32\x45.google.gapic.metadata.GapicMetadata.ServiceForTransport.ClientsEntry\x1a\x64\n\x0c\x43lientsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x43\n\x05value\x18\x02 \x01(\x0b\x32\x34.google.gapic.metadata.GapicMetadata.ServiceAsClient:\x02\x38\x01\x1a\xd5\x01\n\x0fServiceAsClient\x12\x16\n\x0elibrary_client\x18\x01 \x01(\t\x12L\n\x04rpcs\x18\x02 \x03(\x0b\x32>.google.gapic.metadata.GapicMetadata.ServiceAsClient.RpcsEntry\x1a\\\n\tRpcsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12>\n\x05value\x18\x02 \x01(\x0b\x32/.google.gapic.metadata.GapicMetadata.MethodList:\x02\x38\x01\x1a\x1d\n\nMethodList\x12\x0f\n\x07methods\x18\x01 \x03(\tB\xba\x01\n\x19\x63om.google.gapic.metadataB\x12GapicMetadataProtoP\x01Z=google.golang.org/genproto/googleapis/gapic/metadata;metadata\xaa\x02\x15Google.Gapic.Metadata\xca\x02\x15Google\\Gapic\\Metadata\xea\x02\x17Google::Gapic::Metadatab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gapic.metadata.gapic_metadata_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031com.google.gapic.metadataB\022GapicMetadataProtoP\001Z=google.golang.org/genproto/googleapis/gapic/metadata;metadata\252\002\025Google.Gapic.Metadata\312\002\025Google\\Gapic\\Metadata\352\002\027Google::Gapic::Metadata'
  _globals['_GAPICMETADATA_SERVICESENTRY']._options = None
  _globals['_GAPICMETADATA_SERVICESENTRY']._serialized_options = b'8\001'
  _globals['_GAPICMETADATA_SERVICEFORTRANSPORT_CLIENTSENTRY']._options = None
  _globals['_GAPICMETADATA_SERVICEFORTRANSPORT_CLIENTSENTRY']._serialized_options = b'8\001'
  _globals['_GAPICMETADATA_SERVICEASCLIENT_RPCSENTRY']._options = None
  _globals['_GAPICMETADATA_SERVICEASCLIENT_RPCSENTRY']._serialized_options = b'8\001'
  _globals['_GAPICMETADATA']._serialized_start=63
  _globals['_GAPICMETADATA']._serialized_end=815
  _globals['_GAPICMETADATA_SERVICESENTRY']._serialized_start=249
  _globals['_GAPICMETADATA_SERVICESENTRY']._serialized_end=354
  _globals['_GAPICMETADATA_SERVICEFORTRANSPORT']._serialized_start=357
  _globals['_GAPICMETADATA_SERVICEFORTRANSPORT']._serialized_end=568
  _globals['_GAPICMETADATA_SERVICEFORTRANSPORT_CLIENTSENTRY']._serialized_start=468
  _globals['_GAPICMETADATA_SERVICEFORTRANSPORT_CLIENTSENTRY']._serialized_end=568
  _globals['_GAPICMETADATA_SERVICEASCLIENT']._serialized_start=571
  _globals['_GAPICMETADATA_SERVICEASCLIENT']._serialized_end=784
  _globals['_GAPICMETADATA_SERVICEASCLIENT_RPCSENTRY']._serialized_start=692
  _globals['_GAPICMETADATA_SERVICEASCLIENT_RPCSENTRY']._serialized_end=784
  _globals['_GAPICMETADATA_METHODLIST']._serialized_start=786
  _globals['_GAPICMETADATA_METHODLIST']._serialized_end=815
# @@protoc_insertion_point(module_scope)

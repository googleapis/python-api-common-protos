# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/backend.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x18google/api/backend.proto\x12\ngoogle.api"1\n\x07\x42\x61\x63kend\x12&\n\x05rules\x18\x01 \x03(\x0b\x32\x17.google.api.BackendRule"\xb2\x04\n\x0b\x42\x61\x63kendRule\x12\x10\n\x08selector\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x10\n\x08\x64\x65\x61\x64line\x18\x03 \x01(\x01\x12\x18\n\x0cmin_deadline\x18\x04 \x01(\x01\x42\x02\x18\x01\x12\x1a\n\x12operation_deadline\x18\x05 \x01(\x01\x12\x41\n\x10path_translation\x18\x06 \x01(\x0e\x32\'.google.api.BackendRule.PathTranslation\x12\x16\n\x0cjwt_audience\x18\x07 \x01(\tH\x00\x12\x16\n\x0c\x64isable_auth\x18\x08 \x01(\x08H\x00\x12\x10\n\x08protocol\x18\t \x01(\t\x12^\n\x1doverrides_by_request_protocol\x18\n \x03(\x0b\x32\x37.google.api.BackendRule.OverridesByRequestProtocolEntry\x1aZ\n\x1fOverridesByRequestProtocolEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.google.api.BackendRule:\x02\x38\x01"e\n\x0fPathTranslation\x12 \n\x1cPATH_TRANSLATION_UNSPECIFIED\x10\x00\x12\x14\n\x10\x43ONSTANT_ADDRESS\x10\x01\x12\x1a\n\x16\x41PPEND_PATH_TO_ADDRESS\x10\x02\x42\x10\n\x0e\x61uthenticationBn\n\x0e\x63om.google.apiB\x0c\x42\x61\x63kendProtoP\x01ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\xa2\x02\x04GAPIb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "google.api.backend_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n\016com.google.apiB\014BackendProtoP\001ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\242\002\004GAPI"
    _globals["_BACKENDRULE_OVERRIDESBYREQUESTPROTOCOLENTRY"]._options = None
    _globals[
        "_BACKENDRULE_OVERRIDESBYREQUESTPROTOCOLENTRY"
    ]._serialized_options = b"8\001"
    _globals["_BACKENDRULE"].fields_by_name["min_deadline"]._options = None
    _globals["_BACKENDRULE"].fields_by_name[
        "min_deadline"
    ]._serialized_options = b"\030\001"
    _globals["_BACKEND"]._serialized_start = 40
    _globals["_BACKEND"]._serialized_end = 89
    _globals["_BACKENDRULE"]._serialized_start = 92
    _globals["_BACKENDRULE"]._serialized_end = 654
    _globals["_BACKENDRULE_OVERRIDESBYREQUESTPROTOCOLENTRY"]._serialized_start = 443
    _globals["_BACKENDRULE_OVERRIDESBYREQUESTPROTOCOLENTRY"]._serialized_end = 533
    _globals["_BACKENDRULE_PATHTRANSLATION"]._serialized_start = 535
    _globals["_BACKENDRULE_PATHTRANSLATION"]._serialized_end = 636
# @@protoc_insertion_point(module_scope)

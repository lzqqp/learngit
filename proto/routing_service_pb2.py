# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: routing_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import routing_pb2 as routing__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='routing_service.proto',
  package='adu.common.routing',
  syntax='proto2',
  serialized_pb=_b('\n\x15routing_service.proto\x12\x12\x61\x64u.common.routing\x1a\rrouting.proto2[\n\x03RPC\x12T\n\tRunRouter\x12\".adu.common.routing.RoutingRequest\x1a!.adu.common.routing.RoutingResult\"\x00')
  ,
  dependencies=[routing__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_RPC = _descriptor.ServiceDescriptor(
  name='RPC',
  full_name='adu.common.routing.RPC',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=60,
  serialized_end=151,
  methods=[
  _descriptor.MethodDescriptor(
    name='RunRouter',
    full_name='adu.common.routing.RPC.RunRouter',
    index=0,
    containing_service=None,
    input_type=routing__pb2._ROUTINGREQUEST,
    output_type=routing__pb2._ROUTINGRESULT,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_RPC)

DESCRIPTOR.services_by_name['RPC'] = _RPC

# @@protoc_insertion_point(module_scope)
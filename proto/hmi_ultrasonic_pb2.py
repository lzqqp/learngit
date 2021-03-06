# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hmi_ultrasonic.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import hmi_common_pb2 as hmi__common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hmi_ultrasonic.proto',
  package='adu.hmi',
  syntax='proto2',
  serialized_pb=_b('\n\x14hmi_ultrasonic.proto\x12\x07\x61\x64u.hmi\x1a\x10hmi_common.proto\"w\n\x16ImpendingCollisionEdge\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x14\n\x0c\x63one_id_list\x18\x02 \x03(\x05\x12$\n\x05point\x18\x03 \x03(\x0b\x32\x15.adu.hmi.PolygonPoint\x12\x15\n\rtracking_time\x18\x04 \x01(\x01\"o\n\x17ImpendingCollisionEdges\x12\x41\n\x18impending_collision_edge\x18\x01 \x03(\x0b\x32\x1f.adu.hmi.ImpendingCollisionEdge\x12\x11\n\ttimestamp\x18\x02 \x02(\x01\x42\x02P\x01')
  ,
  dependencies=[hmi__common__pb2.DESCRIPTOR,])




_IMPENDINGCOLLISIONEDGE = _descriptor.Descriptor(
  name='ImpendingCollisionEdge',
  full_name='adu.hmi.ImpendingCollisionEdge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='adu.hmi.ImpendingCollisionEdge.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cone_id_list', full_name='adu.hmi.ImpendingCollisionEdge.cone_id_list', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='point', full_name='adu.hmi.ImpendingCollisionEdge.point', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tracking_time', full_name='adu.hmi.ImpendingCollisionEdge.tracking_time', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=170,
)


_IMPENDINGCOLLISIONEDGES = _descriptor.Descriptor(
  name='ImpendingCollisionEdges',
  full_name='adu.hmi.ImpendingCollisionEdges',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='impending_collision_edge', full_name='adu.hmi.ImpendingCollisionEdges.impending_collision_edge', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='adu.hmi.ImpendingCollisionEdges.timestamp', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=172,
  serialized_end=283,
)

_IMPENDINGCOLLISIONEDGE.fields_by_name['point'].message_type = hmi__common__pb2._POLYGONPOINT
_IMPENDINGCOLLISIONEDGES.fields_by_name['impending_collision_edge'].message_type = _IMPENDINGCOLLISIONEDGE
DESCRIPTOR.message_types_by_name['ImpendingCollisionEdge'] = _IMPENDINGCOLLISIONEDGE
DESCRIPTOR.message_types_by_name['ImpendingCollisionEdges'] = _IMPENDINGCOLLISIONEDGES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImpendingCollisionEdge = _reflection.GeneratedProtocolMessageType('ImpendingCollisionEdge', (_message.Message,), dict(
  DESCRIPTOR = _IMPENDINGCOLLISIONEDGE,
  __module__ = 'hmi_ultrasonic_pb2'
  # @@protoc_insertion_point(class_scope:adu.hmi.ImpendingCollisionEdge)
  ))
_sym_db.RegisterMessage(ImpendingCollisionEdge)

ImpendingCollisionEdges = _reflection.GeneratedProtocolMessageType('ImpendingCollisionEdges', (_message.Message,), dict(
  DESCRIPTOR = _IMPENDINGCOLLISIONEDGES,
  __module__ = 'hmi_ultrasonic_pb2'
  # @@protoc_insertion_point(class_scope:adu.hmi.ImpendingCollisionEdges)
  ))
_sym_db.RegisterMessage(ImpendingCollisionEdges)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('P\001'))
# @@protoc_insertion_point(module_scope)

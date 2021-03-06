# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: closeloop_hdmap.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='closeloop_hdmap.proto',
  package='adu.workers.closeloop',
  syntax='proto2',
  serialized_pb=_b('\n\x15\x63loseloop_hdmap.proto\x12\x15\x61\x64u.workers.closeloop\"\\\n\x0bHDMapParams\x12\x11\n\tnearest_s\x18\x01 \x02(\x01\x12\x11\n\tnearest_l\x18\x02 \x02(\x01\x12\x12\n\nleft_width\x18\x03 \x02(\x01\x12\x13\n\x0bright_width\x18\x04 \x02(\x01')
)




_HDMAPPARAMS = _descriptor.Descriptor(
  name='HDMapParams',
  full_name='adu.workers.closeloop.HDMapParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nearest_s', full_name='adu.workers.closeloop.HDMapParams.nearest_s', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nearest_l', full_name='adu.workers.closeloop.HDMapParams.nearest_l', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='left_width', full_name='adu.workers.closeloop.HDMapParams.left_width', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='right_width', full_name='adu.workers.closeloop.HDMapParams.right_width', index=3,
      number=4, type=1, cpp_type=5, label=2,
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
  serialized_start=48,
  serialized_end=140,
)

DESCRIPTOR.message_types_by_name['HDMapParams'] = _HDMAPPARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HDMapParams = _reflection.GeneratedProtocolMessageType('HDMapParams', (_message.Message,), dict(
  DESCRIPTOR = _HDMAPPARAMS,
  __module__ = 'closeloop_hdmap_pb2'
  # @@protoc_insertion_point(class_scope:adu.workers.closeloop.HDMapParams)
  ))
_sym_db.RegisterMessage(HDMapParams)


# @@protoc_insertion_point(module_scope)

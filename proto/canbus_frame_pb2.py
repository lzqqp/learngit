# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: canbus_frame.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import header_pb2 as header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='canbus_frame.proto',
  package='baidu.idl_car.canbus',
  syntax='proto2',
  serialized_pb=_b('\n\x12\x63\x61nbus_frame.proto\x12\x14\x62\x61idu.idl_car.canbus\x1a\x0cheader.proto\"^\n\x0b\x43\x61nbusFrame\x12\x18\n\x10measurement_time\x18\x01 \x01(\x01\x12\x12\n\nmessage_id\x18\x02 \x01(\r\x12\x13\n\x0b\x64\x61ta_length\x18\x03 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\"l\n\x0c\x43\x61nbusFrames\x12)\n\x06header\x18\x01 \x01(\x0b\x32\x19.adu.common.header.Header\x12\x31\n\x06\x66rames\x18\x02 \x03(\x0b\x32!.baidu.idl_car.canbus.CanbusFrame')
  ,
  dependencies=[header__pb2.DESCRIPTOR,])




_CANBUSFRAME = _descriptor.Descriptor(
  name='CanbusFrame',
  full_name='baidu.idl_car.canbus.CanbusFrame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='measurement_time', full_name='baidu.idl_car.canbus.CanbusFrame.measurement_time', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_id', full_name='baidu.idl_car.canbus.CanbusFrame.message_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data_length', full_name='baidu.idl_car.canbus.CanbusFrame.data_length', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='baidu.idl_car.canbus.CanbusFrame.data', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=58,
  serialized_end=152,
)


_CANBUSFRAMES = _descriptor.Descriptor(
  name='CanbusFrames',
  full_name='baidu.idl_car.canbus.CanbusFrames',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='baidu.idl_car.canbus.CanbusFrames.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='frames', full_name='baidu.idl_car.canbus.CanbusFrames.frames', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=154,
  serialized_end=262,
)

_CANBUSFRAMES.fields_by_name['header'].message_type = header__pb2._HEADER
_CANBUSFRAMES.fields_by_name['frames'].message_type = _CANBUSFRAME
DESCRIPTOR.message_types_by_name['CanbusFrame'] = _CANBUSFRAME
DESCRIPTOR.message_types_by_name['CanbusFrames'] = _CANBUSFRAMES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CanbusFrame = _reflection.GeneratedProtocolMessageType('CanbusFrame', (_message.Message,), dict(
  DESCRIPTOR = _CANBUSFRAME,
  __module__ = 'canbus_frame_pb2'
  # @@protoc_insertion_point(class_scope:baidu.idl_car.canbus.CanbusFrame)
  ))
_sym_db.RegisterMessage(CanbusFrame)

CanbusFrames = _reflection.GeneratedProtocolMessageType('CanbusFrames', (_message.Message,), dict(
  DESCRIPTOR = _CANBUSFRAMES,
  __module__ = 'canbus_frame_pb2'
  # @@protoc_insertion_point(class_scope:baidu.idl_car.canbus.CanbusFrames)
  ))
_sym_db.RegisterMessage(CanbusFrames)


# @@protoc_insertion_point(module_scope)

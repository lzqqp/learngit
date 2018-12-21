# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sensor_imu.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_geometry_pb2 as common__geometry__pb2
import header_pb2 as header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sensor_imu.proto',
  package='adu.common.sensor',
  syntax='proto2',
  serialized_pb=_b('\n\x10sensor_imu.proto\x12\x11\x61\x64u.common.sensor\x1a\x15\x63ommon_geometry.proto\x1a\x0cheader.proto\"\xc8\x01\n\x03Imu\x12)\n\x06header\x18\x01 \x01(\x0b\x32\x19.adu.common.header.Header\x12\x18\n\x10measurement_time\x18\x02 \x01(\x01\x12\x1b\n\x10measurement_span\x18\x03 \x01(\x02:\x01\x30\x12\x30\n\x13linear_acceleration\x18\x04 \x01(\x0b\x32\x13.adu.common.Point3D\x12-\n\x10\x61ngular_velocity\x18\x05 \x01(\x0b\x32\x13.adu.common.Point3D')
  ,
  dependencies=[common__geometry__pb2.DESCRIPTOR,header__pb2.DESCRIPTOR,])




_IMU = _descriptor.Descriptor(
  name='Imu',
  full_name='adu.common.sensor.Imu',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='adu.common.sensor.Imu.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='measurement_time', full_name='adu.common.sensor.Imu.measurement_time', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='measurement_span', full_name='adu.common.sensor.Imu.measurement_span', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='linear_acceleration', full_name='adu.common.sensor.Imu.linear_acceleration', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='angular_velocity', full_name='adu.common.sensor.Imu.angular_velocity', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=77,
  serialized_end=277,
)

_IMU.fields_by_name['header'].message_type = header__pb2._HEADER
_IMU.fields_by_name['linear_acceleration'].message_type = common__geometry__pb2._POINT3D
_IMU.fields_by_name['angular_velocity'].message_type = common__geometry__pb2._POINT3D
DESCRIPTOR.message_types_by_name['Imu'] = _IMU
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Imu = _reflection.GeneratedProtocolMessageType('Imu', (_message.Message,), dict(
  DESCRIPTOR = _IMU,
  __module__ = 'sensor_imu_pb2'
  # @@protoc_insertion_point(class_scope:adu.common.sensor.Imu)
  ))
_sym_db.RegisterMessage(Imu)


# @@protoc_insertion_point(module_scope)

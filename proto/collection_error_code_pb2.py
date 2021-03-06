# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: collection_error_code.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='collection_error_code.proto',
  package='adu.workers.collection',
  syntax='proto2',
  serialized_pb=_b('\n\x1b\x63ollection_error_code.proto\x12\x16\x61\x64u.workers.collection*\x9e\x04\n\tErrorCode\x12\x0b\n\x07SUCCESS\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x12\x11\n\rERROR_REQUEST\x10\x02\x12\x1d\n\x19\x45RROR_SERVICE_NO_RESPONSE\x10\x03\x12\x18\n\x14\x45RROR_REPEATED_START\x10\x04\x12\x1c\n\x18\x45RROR_CHECK_BEFORE_START\x10\x05\x12\x18\n\x14\x45RROR_DISKINFO_ERROR\x10\x66\x12\x16\n\x12\x45RROR_DISK_UNMOUNT\x10g\x12\x14\n\x10\x45RROR_SPEED_LACK\x10i\x12\x19\n\x15WARNING_ODOMETER_LACK\x10j\x12\x19\n\x15\x45RROR_RTKSTATUS_EMPTY\x10k\x12\x1e\n\x19\x45RROR_MAPGRPC_NOT_CONNECT\x10\xc9\x01\x12\x19\n\x14WARNING_NOT_STRAIGHT\x10\xd4\x01\x12\x1e\n\x19WARNING_PROGRESS_ROLLBACK\x10\xd5\x01\x12\x1c\n\x17WARNING_NOT_EIGHT_ROUTE\x10\xde\x01\x12 \n\x1b\x45RROR_DATAVERIFY_TASK_EMPTY\x10\xe8\x01\x12\"\n\x1d\x45RROR_DATAVERIFY_NO_RECORDERS\x10\xe9\x01\x12 \n\x1b\x45RROR_DATAVERIFY_TOPIC_LACK\x10\xea\x01\x12\x17\n\x12SUCCESS_TASK_EMPTY\x10\xad\x02\x12\x17\n\x12SUCCESS_TASK_STOCK\x10\xae\x02')
)

_ERRORCODE = _descriptor.EnumDescriptor(
  name='ErrorCode',
  full_name='adu.workers.collection.ErrorCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_REQUEST', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_SERVICE_NO_RESPONSE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_REPEATED_START', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_CHECK_BEFORE_START', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_DISKINFO_ERROR', index=6, number=102,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_DISK_UNMOUNT', index=7, number=103,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_SPEED_LACK', index=8, number=105,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WARNING_ODOMETER_LACK', index=9, number=106,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_RTKSTATUS_EMPTY', index=10, number=107,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_MAPGRPC_NOT_CONNECT', index=11, number=201,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WARNING_NOT_STRAIGHT', index=12, number=212,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WARNING_PROGRESS_ROLLBACK', index=13, number=213,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WARNING_NOT_EIGHT_ROUTE', index=14, number=222,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_DATAVERIFY_TASK_EMPTY', index=15, number=232,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_DATAVERIFY_NO_RECORDERS', index=16, number=233,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_DATAVERIFY_TOPIC_LACK', index=17, number=234,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS_TASK_EMPTY', index=18, number=301,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS_TASK_STOCK', index=19, number=302,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=56,
  serialized_end=598,
)
_sym_db.RegisterEnumDescriptor(_ERRORCODE)

ErrorCode = enum_type_wrapper.EnumTypeWrapper(_ERRORCODE)
SUCCESS = 0
ERROR = 1
ERROR_REQUEST = 2
ERROR_SERVICE_NO_RESPONSE = 3
ERROR_REPEATED_START = 4
ERROR_CHECK_BEFORE_START = 5
ERROR_DISKINFO_ERROR = 102
ERROR_DISK_UNMOUNT = 103
ERROR_SPEED_LACK = 105
WARNING_ODOMETER_LACK = 106
ERROR_RTKSTATUS_EMPTY = 107
ERROR_MAPGRPC_NOT_CONNECT = 201
WARNING_NOT_STRAIGHT = 212
WARNING_PROGRESS_ROLLBACK = 213
WARNING_NOT_EIGHT_ROUTE = 222
ERROR_DATAVERIFY_TASK_EMPTY = 232
ERROR_DATAVERIFY_NO_RECORDERS = 233
ERROR_DATAVERIFY_TOPIC_LACK = 234
SUCCESS_TASK_EMPTY = 301
SUCCESS_TASK_STOCK = 302


DESCRIPTOR.enum_types_by_name['ErrorCode'] = _ERRORCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)

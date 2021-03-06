# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: collection_status_message.proto

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


import collection_data_message_pb2 as collection__data__message__pb2
import collection_error_code_pb2 as collection__error__code__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='collection_status_message.proto',
  package='adu.workers.collection',
  syntax='proto2',
  serialized_pb=_b('\n\x1f\x63ollection_status_message.proto\x12\x16\x61\x64u.workers.collection\x1a\x1d\x63ollection_data_message.proto\x1a\x1b\x63ollection_error_code.proto\"{\n\tRtkStatus\x12\x35\n\x03rtk\x18\x01 \x01(\x0e\x32(.adu.workers.collection.RtkStatus.Status\"7\n\x06Status\x12\x0f\n\x0bOUTSTANDING\x10\x01\x12\x08\n\x04GOOD\x10\x02\x12\x08\n\x04PASS\x10\x03\x12\x08\n\x04\x46\x41IL\x10\x04\"-\n\tCarStatus\x12\r\n\x05speed\x18\x01 \x01(\x01\x12\x11\n\todo_meter\x18\x02 \x01(\x01\"O\n\x13\x46\x65tchCollectionKeys\x12\x38\n\x04keys\x18\x01 \x03(\x0e\x32*.adu.workers.collection.FetchCollectionKey\"\xf9\x01\n\x16\x46\x65tchCollectionPackage\x12/\n\x04\x63ode\x18\x01 \x02(\x0e\x32!.adu.workers.collection.ErrorCode\x12\x32\n\x08\x64iskinfo\x18\x02 \x01(\x0b\x32 .adu.workers.collection.DiskInfo\x12\x34\n\tcarstatus\x18\x03 \x01(\x0b\x32!.adu.workers.collection.CarStatus\x12\x34\n\trtkstatus\x18\x04 \x01(\x0b\x32!.adu.workers.collection.RtkStatus\x12\x0e\n\x06\x62sinfo\x18\x05 \x01(\t\"X\n\x0bTaskRequest\x12\x12\n\ncollect_id\x18\x01 \x01(\t\x12\x35\n\x04type\x18\x02 \x01(\x0e\x32\'.adu.workers.collection.TaskHandlerType\"Q\n\x0eStatusResponse\x12/\n\x04\x63ode\x18\x01 \x02(\x0e\x32!.adu.workers.collection.ErrorCode\x12\x0e\n\x06\x65rrmsg\x18\x02 \x01(\t*C\n\x12\x46\x65tchCollectionKey\x12\x0c\n\x08\x44ISKINFO\x10\x01\x12\x07\n\x03RTK\x10\x02\x12\n\n\x06\x44\x45VICE\x10\x03\x12\n\n\x06\x42SINFO\x10\x04*P\n\x0fTaskHandlerType\x12\x0e\n\nTASK_QUERY\x10\x00\x12\x0e\n\nTASK_CLEAR\x10\x01\x12\x0e\n\nTASK_START\x10\x02\x12\r\n\tTASK_STOP\x10\x03')
  ,
  dependencies=[collection__data__message__pb2.DESCRIPTOR,collection__error__code__pb2.DESCRIPTOR,])

_FETCHCOLLECTIONKEY = _descriptor.EnumDescriptor(
  name='FetchCollectionKey',
  full_name='adu.workers.collection.FetchCollectionKey',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DISKINFO', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RTK', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICE', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BSINFO', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=797,
  serialized_end=864,
)
_sym_db.RegisterEnumDescriptor(_FETCHCOLLECTIONKEY)

FetchCollectionKey = enum_type_wrapper.EnumTypeWrapper(_FETCHCOLLECTIONKEY)
_TASKHANDLERTYPE = _descriptor.EnumDescriptor(
  name='TaskHandlerType',
  full_name='adu.workers.collection.TaskHandlerType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TASK_QUERY', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TASK_CLEAR', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TASK_START', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TASK_STOP', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=866,
  serialized_end=946,
)
_sym_db.RegisterEnumDescriptor(_TASKHANDLERTYPE)

TaskHandlerType = enum_type_wrapper.EnumTypeWrapper(_TASKHANDLERTYPE)
DISKINFO = 1
RTK = 2
DEVICE = 3
BSINFO = 4
TASK_QUERY = 0
TASK_CLEAR = 1
TASK_START = 2
TASK_STOP = 3


_RTKSTATUS_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='adu.workers.collection.RtkStatus.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OUTSTANDING', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GOOD', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PASS', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAIL', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=187,
  serialized_end=242,
)
_sym_db.RegisterEnumDescriptor(_RTKSTATUS_STATUS)


_RTKSTATUS = _descriptor.Descriptor(
  name='RtkStatus',
  full_name='adu.workers.collection.RtkStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rtk', full_name='adu.workers.collection.RtkStatus.rtk', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RTKSTATUS_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=119,
  serialized_end=242,
)


_CARSTATUS = _descriptor.Descriptor(
  name='CarStatus',
  full_name='adu.workers.collection.CarStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='speed', full_name='adu.workers.collection.CarStatus.speed', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='odo_meter', full_name='adu.workers.collection.CarStatus.odo_meter', index=1,
      number=2, type=1, cpp_type=5, label=1,
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
  serialized_start=244,
  serialized_end=289,
)


_FETCHCOLLECTIONKEYS = _descriptor.Descriptor(
  name='FetchCollectionKeys',
  full_name='adu.workers.collection.FetchCollectionKeys',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keys', full_name='adu.workers.collection.FetchCollectionKeys.keys', index=0,
      number=1, type=14, cpp_type=8, label=3,
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
  serialized_start=291,
  serialized_end=370,
)


_FETCHCOLLECTIONPACKAGE = _descriptor.Descriptor(
  name='FetchCollectionPackage',
  full_name='adu.workers.collection.FetchCollectionPackage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='adu.workers.collection.FetchCollectionPackage.code', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='diskinfo', full_name='adu.workers.collection.FetchCollectionPackage.diskinfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='carstatus', full_name='adu.workers.collection.FetchCollectionPackage.carstatus', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rtkstatus', full_name='adu.workers.collection.FetchCollectionPackage.rtkstatus', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bsinfo', full_name='adu.workers.collection.FetchCollectionPackage.bsinfo', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=373,
  serialized_end=622,
)


_TASKREQUEST = _descriptor.Descriptor(
  name='TaskRequest',
  full_name='adu.workers.collection.TaskRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='collect_id', full_name='adu.workers.collection.TaskRequest.collect_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='adu.workers.collection.TaskRequest.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=624,
  serialized_end=712,
)


_STATUSRESPONSE = _descriptor.Descriptor(
  name='StatusResponse',
  full_name='adu.workers.collection.StatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='adu.workers.collection.StatusResponse.code', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='errmsg', full_name='adu.workers.collection.StatusResponse.errmsg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=714,
  serialized_end=795,
)

_RTKSTATUS.fields_by_name['rtk'].enum_type = _RTKSTATUS_STATUS
_RTKSTATUS_STATUS.containing_type = _RTKSTATUS
_FETCHCOLLECTIONKEYS.fields_by_name['keys'].enum_type = _FETCHCOLLECTIONKEY
_FETCHCOLLECTIONPACKAGE.fields_by_name['code'].enum_type = collection__error__code__pb2._ERRORCODE
_FETCHCOLLECTIONPACKAGE.fields_by_name['diskinfo'].message_type = collection__data__message__pb2._DISKINFO
_FETCHCOLLECTIONPACKAGE.fields_by_name['carstatus'].message_type = _CARSTATUS
_FETCHCOLLECTIONPACKAGE.fields_by_name['rtkstatus'].message_type = _RTKSTATUS
_TASKREQUEST.fields_by_name['type'].enum_type = _TASKHANDLERTYPE
_STATUSRESPONSE.fields_by_name['code'].enum_type = collection__error__code__pb2._ERRORCODE
DESCRIPTOR.message_types_by_name['RtkStatus'] = _RTKSTATUS
DESCRIPTOR.message_types_by_name['CarStatus'] = _CARSTATUS
DESCRIPTOR.message_types_by_name['FetchCollectionKeys'] = _FETCHCOLLECTIONKEYS
DESCRIPTOR.message_types_by_name['FetchCollectionPackage'] = _FETCHCOLLECTIONPACKAGE
DESCRIPTOR.message_types_by_name['TaskRequest'] = _TASKREQUEST
DESCRIPTOR.message_types_by_name['StatusResponse'] = _STATUSRESPONSE
DESCRIPTOR.enum_types_by_name['FetchCollectionKey'] = _FETCHCOLLECTIONKEY
DESCRIPTOR.enum_types_by_name['TaskHandlerType'] = _TASKHANDLERTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RtkStatus = _reflection.GeneratedProtocolMessageType('RtkStatus', (_message.Message,), dict(
  DESCRIPTOR = _RTKSTATUS,
  __module__ = 'collection_status_message_pb2'
  # @@protoc_insertion_point(class_scope:adu.workers.collection.RtkStatus)
  ))
_sym_db.RegisterMessage(RtkStatus)

CarStatus = _reflection.GeneratedProtocolMessageType('CarStatus', (_message.Message,), dict(
  DESCRIPTOR = _CARSTATUS,
  __module__ = 'collection_status_message_pb2'
  # @@protoc_insertion_point(class_scope:adu.workers.collection.CarStatus)
  ))
_sym_db.RegisterMessage(CarStatus)

FetchCollectionKeys = _reflection.GeneratedProtocolMessageType('FetchCollectionKeys', (_message.Message,), dict(
  DESCRIPTOR = _FETCHCOLLECTIONKEYS,
  __module__ = 'collection_status_message_pb2'
  # @@protoc_insertion_point(class_scope:adu.workers.collection.FetchCollectionKeys)
  ))
_sym_db.RegisterMessage(FetchCollectionKeys)

FetchCollectionPackage = _reflection.GeneratedProtocolMessageType('FetchCollectionPackage', (_message.Message,), dict(
  DESCRIPTOR = _FETCHCOLLECTIONPACKAGE,
  __module__ = 'collection_status_message_pb2'
  # @@protoc_insertion_point(class_scope:adu.workers.collection.FetchCollectionPackage)
  ))
_sym_db.RegisterMessage(FetchCollectionPackage)

TaskRequest = _reflection.GeneratedProtocolMessageType('TaskRequest', (_message.Message,), dict(
  DESCRIPTOR = _TASKREQUEST,
  __module__ = 'collection_status_message_pb2'
  # @@protoc_insertion_point(class_scope:adu.workers.collection.TaskRequest)
  ))
_sym_db.RegisterMessage(TaskRequest)

StatusResponse = _reflection.GeneratedProtocolMessageType('StatusResponse', (_message.Message,), dict(
  DESCRIPTOR = _STATUSRESPONSE,
  __module__ = 'collection_status_message_pb2'
  # @@protoc_insertion_point(class_scope:adu.workers.collection.StatusResponse)
  ))
_sym_db.RegisterMessage(StatusResponse)


# @@protoc_insertion_point(module_scope)

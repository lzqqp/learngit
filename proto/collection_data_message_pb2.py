# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: collection_data_message.proto

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


import collection_error_code_pb2 as collection__error__code__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='collection_data_message.proto',
  package='adu.workers.collection',
  syntax='proto2',
  serialized_pb=_b('\n\x1d\x63ollection_data_message.proto\x12\x16\x61\x64u.workers.collection\x1a\x1b\x63ollection_error_code.proto\"\"\n\x12\x44\x61taManagerRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"g\n\x13\x44\x61taManagerResponse\x12/\n\x04\x63ode\x18\x01 \x02(\x0e\x32!.adu.workers.collection.ErrorCode\x12\x11\n\ttask_path\x18\x02 \x03(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\t\"~\n\x0f\x44\x61taTaskRequest\x12\x12\n\ncollect_id\x18\x01 \x01(\t\x12:\n\x04type\x18\x02 \x01(\x0e\x32,.adu.workers.collection.DataTaskRequest.Type\"\x1b\n\x04Type\x12\t\n\x05START\x10\x00\x12\x08\n\x04STOP\x10\x01\"V\n\x10\x44\x61taTaskResponse\x12\x32\n\x07\x65rrcode\x18\x01 \x01(\x0e\x32!.adu.workers.collection.ErrorCode\x12\x0e\n\x06\x65rrmsg\x18\x02 \x01(\t\"\"\n\x0f\x44iskInfoRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\":\n\x08\x44iskInfo\x12\x12\n\nis_mounted\x18\x01 \x01(\x08\x12\x0c\n\x04size\x18\x02 \x01(\x04\x12\x0c\n\x04used\x18\x03 \x01(\x04\"v\n\x10\x44iskInfoResponse\x12\x32\n\x07\x65rrcode\x18\x01 \x01(\x0e\x32!.adu.workers.collection.ErrorCode\x12.\n\x04info\x18\x02 \x01(\x0b\x32 .adu.workers.collection.DiskInfo\"$\n\x11\x44iskFormatRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x85\x01\n\x12\x44iskFormatResponse\x12/\n\x04\x63ode\x18\x01 \x02(\x0e\x32!.adu.workers.collection.ErrorCode\x12\x0e\n\x06\x65rrmsg\x18\x02 \x01(\t\x12.\n\x06result\x18\x03 \x01(\x0e\x32\x1e.adu.workers.collection.Result\"%\n\x12\x43heckGPSbinRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x86\x01\n\x13\x43heckGPSbinResponse\x12/\n\x04\x63ode\x18\x01 \x02(\x0e\x32!.adu.workers.collection.ErrorCode\x12\x0e\n\x06\x65rrmsg\x18\x02 \x01(\t\x12.\n\x06result\x18\x03 \x01(\x0e\x32\x1e.adu.workers.collection.Result**\n\x06Result\x12\x08\n\x04PASS\x10\x01\x12\x08\n\x04\x46\x41IL\x10\x02\x12\x0c\n\x08ON_GOING\x10\x03')
  ,
  dependencies=[collection__error__code__pb2.DESCRIPTOR,])

_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='adu.workers.collection.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PASS', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAIL', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ON_GOING', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1009,
  serialized_end=1051,
)
_sym_db.RegisterEnumDescriptor(_RESULT)

Result = enum_type_wrapper.EnumTypeWrapper(_RESULT)
PASS = 1
FAIL = 2
ON_GOING = 3


_DATATASKREQUEST_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='adu.workers.collection.DataTaskRequest.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='START', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOP', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=326,
  serialized_end=353,
)
_sym_db.RegisterEnumDescriptor(_DATATASKREQUEST_TYPE)


_DATAMANAGERREQUEST = _descriptor.Descriptor(
  name='DataManagerRequest',
  full_name='adu.workers.collection.DataManagerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='adu.workers.collection.DataManagerRequest.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=86,
  serialized_end=120,
)


_DATAMANAGERRESPONSE = _descriptor.Descriptor(
  name='DataManagerResponse',
  full_name='adu.workers.collection.DataManagerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='adu.workers.collection.DataManagerResponse.code', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='task_path', full_name='adu.workers.collection.DataManagerResponse.task_path', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='adu.workers.collection.DataManagerResponse.data', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=122,
  serialized_end=225,
)


_DATATASKREQUEST = _descriptor.Descriptor(
  name='DataTaskRequest',
  full_name='adu.workers.collection.DataTaskRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='collect_id', full_name='adu.workers.collection.DataTaskRequest.collect_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='adu.workers.collection.DataTaskRequest.type', index=1,
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
    _DATATASKREQUEST_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=227,
  serialized_end=353,
)


_DATATASKRESPONSE = _descriptor.Descriptor(
  name='DataTaskResponse',
  full_name='adu.workers.collection.DataTaskResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='errcode', full_name='adu.workers.collection.DataTaskResponse.errcode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='errmsg', full_name='adu.workers.collection.DataTaskResponse.errmsg', index=1,
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
  serialized_start=355,
  serialized_end=441,
)


_DISKINFOREQUEST = _descriptor.Descriptor(
  name='DiskInfoRequest',
  full_name='adu.workers.collection.DiskInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='adu.workers.collection.DiskInfoRequest.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=443,
  serialized_end=477,
)


_DISKINFO = _descriptor.Descriptor(
  name='DiskInfo',
  full_name='adu.workers.collection.DiskInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_mounted', full_name='adu.workers.collection.DiskInfo.is_mounted', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size', full_name='adu.workers.collection.DiskInfo.size', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='used', full_name='adu.workers.collection.DiskInfo.used', index=2,
      number=3, type=4, cpp_type=4, label=1,
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
  serialized_start=479,
  serialized_end=537,
)


_DISKINFORESPONSE = _descriptor.Descriptor(
  name='DiskInfoResponse',
  full_name='adu.workers.collection.DiskInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='errcode', full_name='adu.workers.collection.DiskInfoResponse.errcode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='info', full_name='adu.workers.collection.DiskInfoResponse.info', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=539,
  serialized_end=657,
)


_DISKFORMATREQUEST = _descriptor.Descriptor(
  name='DiskFormatRequest',
  full_name='adu.workers.collection.DiskFormatRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='adu.workers.collection.DiskFormatRequest.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=659,
  serialized_end=695,
)


_DISKFORMATRESPONSE = _descriptor.Descriptor(
  name='DiskFormatResponse',
  full_name='adu.workers.collection.DiskFormatResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='adu.workers.collection.DiskFormatResponse.code', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='errmsg', full_name='adu.workers.collection.DiskFormatResponse.errmsg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='adu.workers.collection.DiskFormatResponse.result', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
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
  serialized_start=698,
  serialized_end=831,
)


_CHECKGPSBINREQUEST = _descriptor.Descriptor(
  name='CheckGPSbinRequest',
  full_name='adu.workers.collection.CheckGPSbinRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='adu.workers.collection.CheckGPSbinRequest.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=833,
  serialized_end=870,
)


_CHECKGPSBINRESPONSE = _descriptor.Descriptor(
  name='CheckGPSbinResponse',
  full_name='adu.workers.collection.CheckGPSbinResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='adu.workers.collection.CheckGPSbinResponse.code', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='errmsg', full_name='adu.workers.collection.CheckGPSbinResponse.errmsg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='adu.workers.collection.CheckGPSbinResponse.result', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
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
  serialized_start=873,
  serialized_end=1007,
)

_DATAMANAGERRESPONSE.fields_by_name['code'].enum_type = collection__error__code__pb2._ERRORCODE
_DATATASKREQUEST.fields_by_name['type'].enum_type = _DATATASKREQUEST_TYPE
_DATATASKREQUEST_TYPE.containing_type = _DATATASKREQUEST
_DATATASKRESPONSE.fields_by_name['errcode'].enum_type = collection__error__code__pb2._ERRORCODE
_DISKINFORESPONSE.fields_by_name['errcode'].enum_type = collection__error__code__pb2._ERRORCODE
_DISKINFORESPONSE.fields_by_name['info'].message_type = _DISKINFO
_DISKFORMATRESPONSE.fields_by_name['code'].enum_type = collection__error__code__pb2._ERRORCODE
_DISKFORMATRESPONSE.fields_by_name['result'].enum_type = _RESULT
_CHECKGPSBINRESPONSE.fields_by_name['code'].enum_type = collection__error__code__pb2._ERRORCODE
_CHECKGPSBINRESPONSE.fields_by_name['result'].enum_type = _RESULT
DESCRIPTOR.message_types_by_name['DataManagerRequest'] = _DATAMANAGERREQUEST
DESCRIPTOR.message_types_by_name['DataManagerResponse'] = _DATAMANAGERRESPONSE
DESCRIPTOR.message_types_by_name['DataTaskRequest'] = _DATATASKREQUEST
DESCRIPTOR.message_types_by_name['DataTaskResponse'] = _DATATASKRESPONSE
DESCRIPTOR.message_types_by_name['DiskInfoRequest'] = _DISKINFOREQUEST
DESCRIPTOR.message_types_by_name['DiskInfo'] = _DISKINFO
DESCRIPTOR.message_types_by_name['DiskInfoResponse'] = _DISKINFORESPONSE
DESCRIPTOR.message_types_by_name['DiskFormatRequest'] = _DISKFORMATREQUEST
DESCRIPTOR.message_types_by_name['DiskFormatResponse'] = _DISKFORMATRESPONSE
DESCRIPTOR.message_types_by_name['CheckGPSbinRequest'] = _CHECKGPSBINREQUEST
DESCRIPTOR.message_types_by_name['CheckGPSbinResponse'] = _CHECKGPSBINRESPONSE
DESCRIPTOR.enum_types_by_name['Result'] = _RESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataManagerRequest = _reflection.GeneratedProtocolMessageType('DataManagerRequest', (_message.Message,), dict(
  DESCRIPTOR = _DATAMANAGERREQUEST,
  __module__ = 'collection_data_message_pb2'
  # @@protoc_insertion_point(class_scope:adu.workers.collection.DataManagerRequest)
  ))
_sym_db.RegisterMessage(DataManagerRequest)

DataManagerResponse = _reflection.GeneratedProtocolMessageType('DataManagerResponse', (_message.Message,), dict(
  DESCRIPTOR = _DATAMANAGERRESPONSE,
  __module__ = 'collection_data_message_pb2'
  # @@protoc_insertion_point(class_scope:adu.workers.collection.DataManagerResponse)
  ))
_sym_db.RegisterMessage(DataManagerResponse)

DataTaskRequest = _reflection.GeneratedProtocolMessageType('DataTaskRequest', (_message.Message,), dict(
  DESCRIPTOR = _DATATASKREQUEST,
  __module__ = 'collection_data_message_pb2'
  # @@protoc_insertion_point(class_scope:adu.workers.collection.DataTaskRequest)
  ))
_sym_db.RegisterMessage(DataTaskRequest)

DataTaskResponse = _reflection.GeneratedProtocolMessageType('DataTaskResponse', (_message.Message,), dict(
  DESCRIPTOR = _DATATASKRESPONSE,
  __module__ = 'collection_data_message_pb2'
  # @@protoc_insertion_point(class_scope:adu.workers.collection.DataTaskResponse)
  ))
_sym_db.RegisterMessage(DataTaskResponse)

DiskInfoRequest = _reflection.GeneratedProtocolMessageType('DiskInfoRequest', (_message.Message,), dict(
  DESCRIPTOR = _DISKINFOREQUEST,
  __module__ = 'collection_data_message_pb2'
  # @@protoc_insertion_point(class_scope:adu.workers.collection.DiskInfoRequest)
  ))
_sym_db.RegisterMessage(DiskInfoRequest)

DiskInfo = _reflection.GeneratedProtocolMessageType('DiskInfo', (_message.Message,), dict(
  DESCRIPTOR = _DISKINFO,
  __module__ = 'collection_data_message_pb2'
  # @@protoc_insertion_point(class_scope:adu.workers.collection.DiskInfo)
  ))
_sym_db.RegisterMessage(DiskInfo)

DiskInfoResponse = _reflection.GeneratedProtocolMessageType('DiskInfoResponse', (_message.Message,), dict(
  DESCRIPTOR = _DISKINFORESPONSE,
  __module__ = 'collection_data_message_pb2'
  # @@protoc_insertion_point(class_scope:adu.workers.collection.DiskInfoResponse)
  ))
_sym_db.RegisterMessage(DiskInfoResponse)

DiskFormatRequest = _reflection.GeneratedProtocolMessageType('DiskFormatRequest', (_message.Message,), dict(
  DESCRIPTOR = _DISKFORMATREQUEST,
  __module__ = 'collection_data_message_pb2'
  # @@protoc_insertion_point(class_scope:adu.workers.collection.DiskFormatRequest)
  ))
_sym_db.RegisterMessage(DiskFormatRequest)

DiskFormatResponse = _reflection.GeneratedProtocolMessageType('DiskFormatResponse', (_message.Message,), dict(
  DESCRIPTOR = _DISKFORMATRESPONSE,
  __module__ = 'collection_data_message_pb2'
  # @@protoc_insertion_point(class_scope:adu.workers.collection.DiskFormatResponse)
  ))
_sym_db.RegisterMessage(DiskFormatResponse)

CheckGPSbinRequest = _reflection.GeneratedProtocolMessageType('CheckGPSbinRequest', (_message.Message,), dict(
  DESCRIPTOR = _CHECKGPSBINREQUEST,
  __module__ = 'collection_data_message_pb2'
  # @@protoc_insertion_point(class_scope:adu.workers.collection.CheckGPSbinRequest)
  ))
_sym_db.RegisterMessage(CheckGPSbinRequest)

CheckGPSbinResponse = _reflection.GeneratedProtocolMessageType('CheckGPSbinResponse', (_message.Message,), dict(
  DESCRIPTOR = _CHECKGPSBINRESPONSE,
  __module__ = 'collection_data_message_pb2'
  # @@protoc_insertion_point(class_scope:adu.workers.collection.CheckGPSbinResponse)
  ))
_sym_db.RegisterMessage(CheckGPSbinResponse)


# @@protoc_insertion_point(module_scope)

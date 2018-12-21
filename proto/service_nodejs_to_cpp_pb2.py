# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service_nodejs_to_cpp.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import disengage_pb2 as disengage__pb2
import map_pb2 as map__pb2
import simulation_common_pb2 as simulation__common__pb2
import simulation_grading_result_pb2 as simulation__grading__result__pb2
import simulation_local_player_pb2 as simulation__local__player__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='service_nodejs_to_cpp.proto',
  package='adu.simulation',
  syntax='proto2',
  serialized_pb=_b('\n\x1bservice_nodejs_to_cpp.proto\x12\x0e\x61\x64u.simulation\x1a\x0f\x64isengage.proto\x1a\tmap.proto\x1a\x17simulation_common.proto\x1a\x1fsimulation_grading_result.proto\x1a\x1dsimulation_local_player.proto\"\x1b\n\x0bLoadRequest\x12\x0c\n\x04\x66ile\x18\x01 \x02(\t\"\x1d\n\x0cStartRequest\x12\r\n\x05start\x18\x01 \x02(\x08\"\x10\n\x0eMapInfoRequest\":\n\x07MapInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x10\n\x08\x64istrict\x18\x03 \x01(\t\"\x94\x01\n\nPubRequest\x12\x15\n\rstart_point_x\x18\x01 \x02(\x01\x12\x15\n\rstart_point_y\x18\x02 \x02(\x01\x12\x13\n\x0b\x65nd_point_x\x18\x03 \x02(\x01\x12\x13\n\x0b\x65nd_point_y\x18\x04 \x02(\x01\x12.\n\x08waypoint\x18\x05 \x03(\x0b\x32\x1c.adu.simulation.PolygonPoint\";\n\x0bInitRequest\x12\x15\n\rstart_point_x\x18\x01 \x02(\x01\x12\x15\n\rstart_point_y\x18\x02 \x02(\x01\"\x96\x01\n\x07MapMeta\x12\x0c\n\x04lane\x18\x01 \x03(\t\x12\x11\n\tcrosswalk\x18\x02 \x03(\t\x12\x10\n\x08junction\x18\x03 \x03(\t\x12\x0e\n\x06signal\x18\x04 \x03(\t\x12\x11\n\tstop_sign\x18\x05 \x03(\t\x12\r\n\x05yield\x18\x06 \x03(\t\x12\x0f\n\x07overlap\x18\x07 \x03(\t\x12\x15\n\rparking_space\x18\x08 \x03(\t\"I\n\x0eStatusResponse\x12\x15\n\x06status\x18\x01 \x02(\x08:\x05\x66\x61lse\x12\x0c\n\x04info\x18\x02 \x01(\t\x12\x12\n\nerror_code\x18\x03 \x01(\x03\x32\xe7\n\n\x0bNodejsToCpp\x12U\n\x15LoadGradingResultFile\x12\x1b.adu.simulation.LoadRequest\x1a\x1d.adu.simulation.GradingResult\"\x00\x12H\n\x08GradeLog\x12\x1b.adu.simulation.LoadRequest\x1a\x1d.adu.simulation.GradingResult\"\x00\x12K\n\x0cLogDisengage\x12\x19.adu.simulation.Disengage\x1a\x1e.adu.simulation.StatusResponse\"\x00\x12I\n\nLogComment\x12\x19.adu.simulation.Disengage\x1a\x1e.adu.simulation.StatusResponse\"\x00\x12J\n\x0bLogCritical\x12\x19.adu.simulation.Disengage\x1a\x1e.adu.simulation.StatusResponse\"\x00\x12\x45\n\x11GetMapElementById\x12\x17.adu.simulation.MapMeta\x1a\x15.adu.common.hdmap.Map\"\x00\x12@\n\nGetMapDiff\x12\x17.adu.simulation.MapMeta\x1a\x17.adu.simulation.MapMeta\"\x00\x12L\n\nGetMapName\x12\x1c.adu.simulation.StartRequest\x1a\x1e.adu.simulation.StatusResponse\"\x00\x12G\n\nGetMapInfo\x12\x1e.adu.simulation.MapInfoRequest\x1a\x17.adu.simulation.MapInfo\"\x00\x12N\n\x0cStartRouting\x12\x1c.adu.simulation.StartRequest\x1a\x1e.adu.simulation.StatusResponse\"\x00\x12J\n\nPubRouting\x12\x1a.adu.simulation.PubRequest\x1a\x1e.adu.simulation.StatusResponse\"\x00\x12O\n\x0eInitStartPoint\x12\x1b.adu.simulation.InitRequest\x1a\x1e.adu.simulation.StatusResponse\"\x00\x12\x44\n\x0bLocalPlayer\x12\x19.adu.simulation.LPControl\x1a\x18.adu.simulation.LPStatus\"\x00\x12N\n\x0cStartControl\x12\x1c.adu.simulation.StartRequest\x1a\x1e.adu.simulation.StatusResponse\"\x00\x12M\n\x0eLogTaskPurpose\x12\x19.adu.simulation.Disengage\x1a\x1e.adu.simulation.StatusResponse\"\x00\x12J\n\x08StartAll\x12\x1c.adu.simulation.StartRequest\x1a\x1e.adu.simulation.StatusResponse\"\x00\x12I\n\x07ReCheck\x12\x1c.adu.simulation.StartRequest\x1a\x1e.adu.simulation.StatusResponse\"\x00\x12J\n\x08ShutDown\x12\x1c.adu.simulation.StartRequest\x1a\x1e.adu.simulation.StatusResponse\"\x00')
  ,
  dependencies=[disengage__pb2.DESCRIPTOR,map__pb2.DESCRIPTOR,simulation__common__pb2.DESCRIPTOR,simulation__grading__result__pb2.DESCRIPTOR,simulation__local__player__pb2.DESCRIPTOR,])




_LOADREQUEST = _descriptor.Descriptor(
  name='LoadRequest',
  full_name='adu.simulation.LoadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file', full_name='adu.simulation.LoadRequest.file', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  serialized_start=164,
  serialized_end=191,
)


_STARTREQUEST = _descriptor.Descriptor(
  name='StartRequest',
  full_name='adu.simulation.StartRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='adu.simulation.StartRequest.start', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  serialized_start=193,
  serialized_end=222,
)


_MAPINFOREQUEST = _descriptor.Descriptor(
  name='MapInfoRequest',
  full_name='adu.simulation.MapInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=224,
  serialized_end=240,
)


_MAPINFO = _descriptor.Descriptor(
  name='MapInfo',
  full_name='adu.simulation.MapInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='adu.simulation.MapInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='adu.simulation.MapInfo.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='district', full_name='adu.simulation.MapInfo.district', index=2,
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
  serialized_start=242,
  serialized_end=300,
)


_PUBREQUEST = _descriptor.Descriptor(
  name='PubRequest',
  full_name='adu.simulation.PubRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_point_x', full_name='adu.simulation.PubRequest.start_point_x', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_point_y', full_name='adu.simulation.PubRequest.start_point_y', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_point_x', full_name='adu.simulation.PubRequest.end_point_x', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_point_y', full_name='adu.simulation.PubRequest.end_point_y', index=3,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='waypoint', full_name='adu.simulation.PubRequest.waypoint', index=4,
      number=5, type=11, cpp_type=10, label=3,
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
  serialized_start=303,
  serialized_end=451,
)


_INITREQUEST = _descriptor.Descriptor(
  name='InitRequest',
  full_name='adu.simulation.InitRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_point_x', full_name='adu.simulation.InitRequest.start_point_x', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_point_y', full_name='adu.simulation.InitRequest.start_point_y', index=1,
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
  serialized_start=453,
  serialized_end=512,
)


_MAPMETA = _descriptor.Descriptor(
  name='MapMeta',
  full_name='adu.simulation.MapMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lane', full_name='adu.simulation.MapMeta.lane', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crosswalk', full_name='adu.simulation.MapMeta.crosswalk', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='junction', full_name='adu.simulation.MapMeta.junction', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signal', full_name='adu.simulation.MapMeta.signal', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stop_sign', full_name='adu.simulation.MapMeta.stop_sign', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='yield', full_name='adu.simulation.MapMeta.yield', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='overlap', full_name='adu.simulation.MapMeta.overlap', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parking_space', full_name='adu.simulation.MapMeta.parking_space', index=7,
      number=8, type=9, cpp_type=9, label=3,
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
  serialized_start=515,
  serialized_end=665,
)


_STATUSRESPONSE = _descriptor.Descriptor(
  name='StatusResponse',
  full_name='adu.simulation.StatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='adu.simulation.StatusResponse.status', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='info', full_name='adu.simulation.StatusResponse.info', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_code', full_name='adu.simulation.StatusResponse.error_code', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=667,
  serialized_end=740,
)

_PUBREQUEST.fields_by_name['waypoint'].message_type = simulation__common__pb2._POLYGONPOINT
DESCRIPTOR.message_types_by_name['LoadRequest'] = _LOADREQUEST
DESCRIPTOR.message_types_by_name['StartRequest'] = _STARTREQUEST
DESCRIPTOR.message_types_by_name['MapInfoRequest'] = _MAPINFOREQUEST
DESCRIPTOR.message_types_by_name['MapInfo'] = _MAPINFO
DESCRIPTOR.message_types_by_name['PubRequest'] = _PUBREQUEST
DESCRIPTOR.message_types_by_name['InitRequest'] = _INITREQUEST
DESCRIPTOR.message_types_by_name['MapMeta'] = _MAPMETA
DESCRIPTOR.message_types_by_name['StatusResponse'] = _STATUSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LoadRequest = _reflection.GeneratedProtocolMessageType('LoadRequest', (_message.Message,), dict(
  DESCRIPTOR = _LOADREQUEST,
  __module__ = 'service_nodejs_to_cpp_pb2'
  # @@protoc_insertion_point(class_scope:adu.simulation.LoadRequest)
  ))
_sym_db.RegisterMessage(LoadRequest)

StartRequest = _reflection.GeneratedProtocolMessageType('StartRequest', (_message.Message,), dict(
  DESCRIPTOR = _STARTREQUEST,
  __module__ = 'service_nodejs_to_cpp_pb2'
  # @@protoc_insertion_point(class_scope:adu.simulation.StartRequest)
  ))
_sym_db.RegisterMessage(StartRequest)

MapInfoRequest = _reflection.GeneratedProtocolMessageType('MapInfoRequest', (_message.Message,), dict(
  DESCRIPTOR = _MAPINFOREQUEST,
  __module__ = 'service_nodejs_to_cpp_pb2'
  # @@protoc_insertion_point(class_scope:adu.simulation.MapInfoRequest)
  ))
_sym_db.RegisterMessage(MapInfoRequest)

MapInfo = _reflection.GeneratedProtocolMessageType('MapInfo', (_message.Message,), dict(
  DESCRIPTOR = _MAPINFO,
  __module__ = 'service_nodejs_to_cpp_pb2'
  # @@protoc_insertion_point(class_scope:adu.simulation.MapInfo)
  ))
_sym_db.RegisterMessage(MapInfo)

PubRequest = _reflection.GeneratedProtocolMessageType('PubRequest', (_message.Message,), dict(
  DESCRIPTOR = _PUBREQUEST,
  __module__ = 'service_nodejs_to_cpp_pb2'
  # @@protoc_insertion_point(class_scope:adu.simulation.PubRequest)
  ))
_sym_db.RegisterMessage(PubRequest)

InitRequest = _reflection.GeneratedProtocolMessageType('InitRequest', (_message.Message,), dict(
  DESCRIPTOR = _INITREQUEST,
  __module__ = 'service_nodejs_to_cpp_pb2'
  # @@protoc_insertion_point(class_scope:adu.simulation.InitRequest)
  ))
_sym_db.RegisterMessage(InitRequest)

MapMeta = _reflection.GeneratedProtocolMessageType('MapMeta', (_message.Message,), dict(
  DESCRIPTOR = _MAPMETA,
  __module__ = 'service_nodejs_to_cpp_pb2'
  # @@protoc_insertion_point(class_scope:adu.simulation.MapMeta)
  ))
_sym_db.RegisterMessage(MapMeta)

StatusResponse = _reflection.GeneratedProtocolMessageType('StatusResponse', (_message.Message,), dict(
  DESCRIPTOR = _STATUSRESPONSE,
  __module__ = 'service_nodejs_to_cpp_pb2'
  # @@protoc_insertion_point(class_scope:adu.simulation.StatusResponse)
  ))
_sym_db.RegisterMessage(StatusResponse)



_NODEJSTOCPP = _descriptor.ServiceDescriptor(
  name='NodejsToCpp',
  full_name='adu.simulation.NodejsToCpp',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=743,
  serialized_end=2126,
  methods=[
  _descriptor.MethodDescriptor(
    name='LoadGradingResultFile',
    full_name='adu.simulation.NodejsToCpp.LoadGradingResultFile',
    index=0,
    containing_service=None,
    input_type=_LOADREQUEST,
    output_type=simulation__grading__result__pb2._GRADINGRESULT,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GradeLog',
    full_name='adu.simulation.NodejsToCpp.GradeLog',
    index=1,
    containing_service=None,
    input_type=_LOADREQUEST,
    output_type=simulation__grading__result__pb2._GRADINGRESULT,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='LogDisengage',
    full_name='adu.simulation.NodejsToCpp.LogDisengage',
    index=2,
    containing_service=None,
    input_type=disengage__pb2._DISENGAGE,
    output_type=_STATUSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='LogComment',
    full_name='adu.simulation.NodejsToCpp.LogComment',
    index=3,
    containing_service=None,
    input_type=disengage__pb2._DISENGAGE,
    output_type=_STATUSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='LogCritical',
    full_name='adu.simulation.NodejsToCpp.LogCritical',
    index=4,
    containing_service=None,
    input_type=disengage__pb2._DISENGAGE,
    output_type=_STATUSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetMapElementById',
    full_name='adu.simulation.NodejsToCpp.GetMapElementById',
    index=5,
    containing_service=None,
    input_type=_MAPMETA,
    output_type=map__pb2._MAP,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetMapDiff',
    full_name='adu.simulation.NodejsToCpp.GetMapDiff',
    index=6,
    containing_service=None,
    input_type=_MAPMETA,
    output_type=_MAPMETA,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetMapName',
    full_name='adu.simulation.NodejsToCpp.GetMapName',
    index=7,
    containing_service=None,
    input_type=_STARTREQUEST,
    output_type=_STATUSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetMapInfo',
    full_name='adu.simulation.NodejsToCpp.GetMapInfo',
    index=8,
    containing_service=None,
    input_type=_MAPINFOREQUEST,
    output_type=_MAPINFO,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StartRouting',
    full_name='adu.simulation.NodejsToCpp.StartRouting',
    index=9,
    containing_service=None,
    input_type=_STARTREQUEST,
    output_type=_STATUSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PubRouting',
    full_name='adu.simulation.NodejsToCpp.PubRouting',
    index=10,
    containing_service=None,
    input_type=_PUBREQUEST,
    output_type=_STATUSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='InitStartPoint',
    full_name='adu.simulation.NodejsToCpp.InitStartPoint',
    index=11,
    containing_service=None,
    input_type=_INITREQUEST,
    output_type=_STATUSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='LocalPlayer',
    full_name='adu.simulation.NodejsToCpp.LocalPlayer',
    index=12,
    containing_service=None,
    input_type=simulation__local__player__pb2._LPCONTROL,
    output_type=simulation__local__player__pb2._LPSTATUS,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StartControl',
    full_name='adu.simulation.NodejsToCpp.StartControl',
    index=13,
    containing_service=None,
    input_type=_STARTREQUEST,
    output_type=_STATUSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='LogTaskPurpose',
    full_name='adu.simulation.NodejsToCpp.LogTaskPurpose',
    index=14,
    containing_service=None,
    input_type=disengage__pb2._DISENGAGE,
    output_type=_STATUSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StartAll',
    full_name='adu.simulation.NodejsToCpp.StartAll',
    index=15,
    containing_service=None,
    input_type=_STARTREQUEST,
    output_type=_STATUSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ReCheck',
    full_name='adu.simulation.NodejsToCpp.ReCheck',
    index=16,
    containing_service=None,
    input_type=_STARTREQUEST,
    output_type=_STATUSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ShutDown',
    full_name='adu.simulation.NodejsToCpp.ShutDown',
    index=17,
    containing_service=None,
    input_type=_STARTREQUEST,
    output_type=_STATUSRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_NODEJSTOCPP)

DESCRIPTOR.services_by_name['NodejsToCpp'] = _NODEJSTOCPP

# @@protoc_insertion_point(module_scope)

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: prediction_obstacle.proto

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
import perception_obstacle_pb2 as perception__obstacle__pb2
import map_id_pb2 as map__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='prediction_obstacle.proto',
  package='adu.common.prediction',
  syntax='proto2',
  serialized_pb=_b('\n\x19prediction_obstacle.proto\x12\x15\x61\x64u.common.prediction\x1a\x0cheader.proto\x1a\x19perception_obstacle.proto\x1a\x0cmap_id.proto\"t\n\x0fTrajectoryPoint\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\x12\x10\n\x08velocity\x18\x04 \x01(\x01\x12\t\n\x01t\x18\x05 \x01(\x01\x12\x0f\n\x07heading\x18\x06 \x01(\x01\x12\x12\n\nconfidence\x18\x07 \x01(\x01\"\x8a\x01\n\nTrajectory\x12\x13\n\x0bprobability\x18\x01 \x01(\x01\x12@\n\x10trajectory_point\x18\x02 \x03(\x0b\x32&.adu.common.prediction.TrajectoryPoint\x12%\n\x07lane_id\x18\x03 \x03(\x0b\x32\x14.adu.common.hdmap.Id\"\xd0\x01\n\x12PredictionObstacle\x12\x46\n\x13perception_obstacle\x18\x01 \x01(\x0b\x32).adu.common.perception.PerceptionObstacle\x12\x12\n\ntime_stamp\x18\x02 \x01(\x01\x12\x18\n\x10predicted_period\x18\x03 \x01(\x01\x12\x35\n\ntrajectory\x18\x04 \x03(\x0b\x32!.adu.common.prediction.Trajectory\x12\r\n\x05\x63ross\x18\x05 \x01(\x08\"\x89\x02\n\x13PredictionObstacles\x12)\n\x06header\x18\x01 \x01(\x0b\x32\x19.adu.common.header.Header\x12\x46\n\x13prediction_obstacle\x18\x02 \x03(\x0b\x32).adu.common.prediction.PredictionObstacle\x12I\n\x15perception_error_code\x18\x03 \x01(\x0e\x32*.adu.common.perception.PerceptionErrorCode\x12\x34\n\nwatch_area\x18\x04 \x01(\x0b\x32 .adu.common.perception.WatchArea')
  ,
  dependencies=[header__pb2.DESCRIPTOR,perception__obstacle__pb2.DESCRIPTOR,map__id__pb2.DESCRIPTOR,])




_TRAJECTORYPOINT = _descriptor.Descriptor(
  name='TrajectoryPoint',
  full_name='adu.common.prediction.TrajectoryPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='adu.common.prediction.TrajectoryPoint.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='adu.common.prediction.TrajectoryPoint.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='adu.common.prediction.TrajectoryPoint.z', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='velocity', full_name='adu.common.prediction.TrajectoryPoint.velocity', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='t', full_name='adu.common.prediction.TrajectoryPoint.t', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heading', full_name='adu.common.prediction.TrajectoryPoint.heading', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='adu.common.prediction.TrajectoryPoint.confidence', index=6,
      number=7, type=1, cpp_type=5, label=1,
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
  serialized_start=107,
  serialized_end=223,
)


_TRAJECTORY = _descriptor.Descriptor(
  name='Trajectory',
  full_name='adu.common.prediction.Trajectory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='probability', full_name='adu.common.prediction.Trajectory.probability', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trajectory_point', full_name='adu.common.prediction.Trajectory.trajectory_point', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lane_id', full_name='adu.common.prediction.Trajectory.lane_id', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=226,
  serialized_end=364,
)


_PREDICTIONOBSTACLE = _descriptor.Descriptor(
  name='PredictionObstacle',
  full_name='adu.common.prediction.PredictionObstacle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='perception_obstacle', full_name='adu.common.prediction.PredictionObstacle.perception_obstacle', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_stamp', full_name='adu.common.prediction.PredictionObstacle.time_stamp', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='predicted_period', full_name='adu.common.prediction.PredictionObstacle.predicted_period', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trajectory', full_name='adu.common.prediction.PredictionObstacle.trajectory', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cross', full_name='adu.common.prediction.PredictionObstacle.cross', index=4,
      number=5, type=8, cpp_type=7, label=1,
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
  serialized_start=367,
  serialized_end=575,
)


_PREDICTIONOBSTACLES = _descriptor.Descriptor(
  name='PredictionObstacles',
  full_name='adu.common.prediction.PredictionObstacles',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='adu.common.prediction.PredictionObstacles.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prediction_obstacle', full_name='adu.common.prediction.PredictionObstacles.prediction_obstacle', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='perception_error_code', full_name='adu.common.prediction.PredictionObstacles.perception_error_code', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='watch_area', full_name='adu.common.prediction.PredictionObstacles.watch_area', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=578,
  serialized_end=843,
)

_TRAJECTORY.fields_by_name['trajectory_point'].message_type = _TRAJECTORYPOINT
_TRAJECTORY.fields_by_name['lane_id'].message_type = map__id__pb2._ID
_PREDICTIONOBSTACLE.fields_by_name['perception_obstacle'].message_type = perception__obstacle__pb2._PERCEPTIONOBSTACLE
_PREDICTIONOBSTACLE.fields_by_name['trajectory'].message_type = _TRAJECTORY
_PREDICTIONOBSTACLES.fields_by_name['header'].message_type = header__pb2._HEADER
_PREDICTIONOBSTACLES.fields_by_name['prediction_obstacle'].message_type = _PREDICTIONOBSTACLE
_PREDICTIONOBSTACLES.fields_by_name['perception_error_code'].enum_type = perception__obstacle__pb2._PERCEPTIONERRORCODE
_PREDICTIONOBSTACLES.fields_by_name['watch_area'].message_type = perception__obstacle__pb2._WATCHAREA
DESCRIPTOR.message_types_by_name['TrajectoryPoint'] = _TRAJECTORYPOINT
DESCRIPTOR.message_types_by_name['Trajectory'] = _TRAJECTORY
DESCRIPTOR.message_types_by_name['PredictionObstacle'] = _PREDICTIONOBSTACLE
DESCRIPTOR.message_types_by_name['PredictionObstacles'] = _PREDICTIONOBSTACLES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TrajectoryPoint = _reflection.GeneratedProtocolMessageType('TrajectoryPoint', (_message.Message,), dict(
  DESCRIPTOR = _TRAJECTORYPOINT,
  __module__ = 'prediction_obstacle_pb2'
  # @@protoc_insertion_point(class_scope:adu.common.prediction.TrajectoryPoint)
  ))
_sym_db.RegisterMessage(TrajectoryPoint)

Trajectory = _reflection.GeneratedProtocolMessageType('Trajectory', (_message.Message,), dict(
  DESCRIPTOR = _TRAJECTORY,
  __module__ = 'prediction_obstacle_pb2'
  # @@protoc_insertion_point(class_scope:adu.common.prediction.Trajectory)
  ))
_sym_db.RegisterMessage(Trajectory)

PredictionObstacle = _reflection.GeneratedProtocolMessageType('PredictionObstacle', (_message.Message,), dict(
  DESCRIPTOR = _PREDICTIONOBSTACLE,
  __module__ = 'prediction_obstacle_pb2'
  # @@protoc_insertion_point(class_scope:adu.common.prediction.PredictionObstacle)
  ))
_sym_db.RegisterMessage(PredictionObstacle)

PredictionObstacles = _reflection.GeneratedProtocolMessageType('PredictionObstacles', (_message.Message,), dict(
  DESCRIPTOR = _PREDICTIONOBSTACLES,
  __module__ = 'prediction_obstacle_pb2'
  # @@protoc_insertion_point(class_scope:adu.common.prediction.PredictionObstacles)
  ))
_sym_db.RegisterMessage(PredictionObstacles)


# @@protoc_insertion_point(module_scope)

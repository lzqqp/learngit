# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calibrator_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import calibrator_message_pb2 as calibrator__message__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='calibrator_service.proto',
  package='adu.workers.calibrator',
  syntax='proto2',
  serialized_pb=_b('\n\x18\x63\x61librator_service.proto\x12\x16\x61\x64u.workers.calibrator\x1a\x18\x63\x61librator_message.proto2\xa8\x02\n\x11\x43\x61libratorService\x12\x83\x01\n\x14\x43\x61meraLidarCalibrate\x12\x33.adu.workers.calibrator.CameraLidarCalibrateRequest\x1a\x34.adu.workers.calibrator.CameraLidarCalibrateResponse\"\x00\x12\x8c\x01\n\x17\x43\x61meraLidarUploadParams\x12\x36.adu.workers.calibrator.CameraLidarUploadParamsRequest\x1a\x37.adu.workers.calibrator.CameraLidarUploadParamsResponse\"\x00\x42\x02P\x01')
  ,
  dependencies=[calibrator__message__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('P\001'))

_CALIBRATORSERVICE = _descriptor.ServiceDescriptor(
  name='CalibratorService',
  full_name='adu.workers.calibrator.CalibratorService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=79,
  serialized_end=375,
  methods=[
  _descriptor.MethodDescriptor(
    name='CameraLidarCalibrate',
    full_name='adu.workers.calibrator.CalibratorService.CameraLidarCalibrate',
    index=0,
    containing_service=None,
    input_type=calibrator__message__pb2._CAMERALIDARCALIBRATEREQUEST,
    output_type=calibrator__message__pb2._CAMERALIDARCALIBRATERESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CameraLidarUploadParams',
    full_name='adu.workers.calibrator.CalibratorService.CameraLidarUploadParams',
    index=1,
    containing_service=None,
    input_type=calibrator__message__pb2._CAMERALIDARUPLOADPARAMSREQUEST,
    output_type=calibrator__message__pb2._CAMERALIDARUPLOADPARAMSRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALIBRATORSERVICE)

DESCRIPTOR.services_by_name['CalibratorService'] = _CALIBRATORSERVICE

# @@protoc_insertion_point(module_scope)

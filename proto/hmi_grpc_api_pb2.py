# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hmi_grpc_api.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import hmi_fetch_msg_pb2 as hmi__fetch__msg__pb2
import hmi_common_pb2 as hmi__common__pb2
import map_pb2 as map__pb2
import hmi_routing_pb2 as hmi__routing__pb2
import hmi_driving_control_pb2 as hmi__driving__control__pb2
import hmi_car_device_pb2 as hmi__car__device__pb2
import patrol_result_pb2 as patrol__result__pb2
import hmi_hudinfo_pb2 as hmi__hudinfo__pb2
import hmi_launch_pb2 as hmi__launch__pb2
import hmi_ota_pb2 as hmi__ota__pb2
import hmi_world_pb2 as hmi__world__pb2
import hmi_collect_data_pb2 as hmi__collect__data__pb2
import hmi_system_control_pb2 as hmi__system__control__pb2
import ota_pb2 as ota__pb2
import hmi_map_info_pb2 as hmi__map__info__pb2
import hmi_localization_init_pb2 as hmi__localization__init__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hmi_grpc_api.proto',
  package='adu.hmi',
  syntax='proto2',
  serialized_pb=_b('\n\x12hmi_grpc_api.proto\x12\x07\x61\x64u.hmi\x1a\x13hmi_fetch_msg.proto\x1a\x10hmi_common.proto\x1a\tmap.proto\x1a\x11hmi_routing.proto\x1a\x19hmi_driving_control.proto\x1a\x14hmi_car_device.proto\x1a\x13patrol_result.proto\x1a\x11hmi_hudinfo.proto\x1a\x10hmi_launch.proto\x1a\rhmi_ota.proto\x1a\x0fhmi_world.proto\x1a\x16hmi_collect_data.proto\x1a\x18hmi_system_control.proto\x1a\tota.proto\x1a\x12hmi_map_info.proto\x1a\x1bhmi_localization_init.proto2\xa1\x16\n\x0eHMIGrpcService\x12>\n\x0f\x46\x65tchSectionMsg\x12\x12.adu.hmi.FetchKeys\x1a\x15.adu.hmi.WorldPackage\"\x00\x12\x46\n\x0f\x46\x65tchMapElement\x12\x17.adu.hmi.MapFileRequest\x1a\x18.adu.hmi.MapFileResponse\"\x00\x12L\n\x0f\x46\x65tchMapVersion\x12\x1a.adu.hmi.MapVersionRequest\x1a\x1b.adu.hmi.MapVersionResponse\"\x00\x12O\n\x14\x46\x65tchSafeCheckResult\x12\x19.adu.hmi.SafeCheckRequest\x1a\x1a.adu.hmi.SafeCheckResponse\"\x00\x12Q\n\x0eShutdownSystem\x12\x1d.adu.hmi.SystemControlRequest\x1a\x1e.adu.hmi.SystemControlResponse\"\x00\x12\\\n\x15TransferSystemControl\x12\x1f.adu.hmi.TransferControlRequest\x1a .adu.hmi.TransferControlResponse\"\x00\x12\x41\n\nPreRouting\x12\x17.adu.hmi.RoutingRequest\x1a\x18.adu.hmi.RoutingResponse\"\x00\x12\x43\n\x0cStartRouting\x12\x17.adu.hmi.RoutingRequest\x1a\x18.adu.hmi.RoutingResponse\"\x00\x12;\n\x06Launch\x12\x16.adu.hmi.LaunchRequest\x1a\x17.adu.hmi.LaunchResponse\"\x00\x12\x44\n\tDisengage\x12\x19.adu.hmi.DisengageRequest\x1a\x1a.adu.hmi.DisengageResponse\"\x00\x12\x46\n\tStopAndGo\x12\x1e.adu.hmi.SwitchCarStateRequest\x1a\x17.adu.hmi.StatusResponse\"\x00\x12X\n\x13\x43heckPositionStatus\x12\x1e.adu.hmi.PositionStatusRequest\x1a\x1f.adu.hmi.PositionStatusResponse\"\x00\x12[\n\x14\x43heckParkingRelation\x12\x1f.adu.hmi.ParkingRelationRequest\x1a .adu.hmi.ParkingRelationResponse\"\x00\x12\x45\n\x0b\x41utoParking\x12\x1b.adu.hmi.AutoParkingRequest\x1a\x17.adu.hmi.StatusResponse\"\x00\x12I\n\rAutoOutGarage\x12\x1d.adu.hmi.AutoOutGarageRequest\x1a\x17.adu.hmi.StatusResponse\"\x00\x12\x41\n\tIntervene\x12\x19.adu.hmi.InterveneRequest\x1a\x17.adu.hmi.StatusResponse\"\x00\x12Q\n\x15\x44isengageTypeFeedback\x12\x1d.adu.hmi.DisengageTypeContent\x1a\x17.adu.hmi.StatusResponse\"\x00\x12\x46\n\nSwitchDoor\x12\x1d.adu.hmi.DeciveControlRequest\x1a\x17.adu.hmi.StatusResponse\"\x00\x12L\n\x10SwitchHeadLights\x12\x1d.adu.hmi.DeciveControlRequest\x1a\x17.adu.hmi.StatusResponse\"\x00\x12K\n\x0fSwitchFrontLamp\x12\x1d.adu.hmi.DeciveControlRequest\x1a\x17.adu.hmi.StatusResponse\"\x00\x12O\n\x13SwitchEmergencyLamp\x12\x1d.adu.hmi.DeciveControlRequest\x1a\x17.adu.hmi.StatusResponse\"\x00\x12N\n\x12SwitchCourtesyLamp\x12\x1d.adu.hmi.DeciveControlRequest\x1a\x17.adu.hmi.StatusResponse\"\x00\x12K\n\x10NotiAirCondition\x12\x1c.adu.hmi.AirConditionRequest\x1a\x17.adu.hmi.StatusResponse\"\x00\x12\x46\n\x10TriggerAlarmHorn\x12\x17.adu.hmi.TriggerRequest\x1a\x17.adu.hmi.StatusResponse\"\x00\x12J\n\x14TriggerEmergencyStop\x12\x17.adu.hmi.TriggerRequest\x1a\x17.adu.hmi.StatusResponse\"\x00\x12\x39\n\nSetHudInfo\x12\x10.adu.hmi.HudInfo\x1a\x17.adu.hmi.StatusResponse\"\x00\x12<\n\rNotiOTAClient\x12\x13.adu.hmi.OtaRequest\x1a\x14.adu.hmi.OtaResponse\"\x00\x12W\n\x13\x46\x65tchCollectDataMsg\x12\x1c.adu.hmi.FetchCollectDataKey\x1a .adu.hmi.FetchCollectDataPackage\"\x00\x12J\n\x10NotiWorkingState\x12\x1b.adu.hmi.WorkStationRequest\x1a\x17.adu.hmi.StatusResponse\"\x00\x12\x46\n\rNotiDataCheck\x12\x19.adu.hmi.DataCheckRequest\x1a\x18.adu.hmi.DataCheckResult\"\x00\x12O\n\x11SwitchCollectMode\x12\x1f.adu.hmi.CollectingStateRequest\x1a\x17.adu.hmi.StatusResponse\"\x00\x12X\n\x16\x46\x65tchPreProcTaskStatus\x12 .adu.hmi.FetchPreProcTaskRequest\x1a\x1a.adu.hmi.PreProcTaskResult\"\x00\x12g\n\x18\x43heckCalibrationValidity\x12#.adu.hmi.CalibrationValidityRequest\x1a$.adu.hmi.CalibrationValidityResponse\"\x00\x12\x41\n\x0eStreamOtaToHmi\x12\x13.adu.ota.OtaRequest\x1a\x14.adu.ota.OtaResponse\"\x00(\x01\x30\x01\x12\x41\n\x0eStreamHmiToOta\x12\x14.adu.ota.OtaResponse\x1a\x13.adu.ota.OtaRequest\"\x00(\x01\x30\x01\x12P\n\x18NotiLocalizationInitPose\x12\x1b.adu.hmi.PositionAndHeading\x1a\x15.adu.hmi.LocalInitRes\"\x00\x12N\n\x0bMoveLogSync\x12\x1d.adu.hmi.SystemControlRequest\x1a\x1e.adu.hmi.SystemControlResponse\"\x00\x42\x02P\x01')
  ,
  dependencies=[hmi__fetch__msg__pb2.DESCRIPTOR,hmi__common__pb2.DESCRIPTOR,map__pb2.DESCRIPTOR,hmi__routing__pb2.DESCRIPTOR,hmi__driving__control__pb2.DESCRIPTOR,hmi__car__device__pb2.DESCRIPTOR,patrol__result__pb2.DESCRIPTOR,hmi__hudinfo__pb2.DESCRIPTOR,hmi__launch__pb2.DESCRIPTOR,hmi__ota__pb2.DESCRIPTOR,hmi__world__pb2.DESCRIPTOR,hmi__collect__data__pb2.DESCRIPTOR,hmi__system__control__pb2.DESCRIPTOR,ota__pb2.DESCRIPTOR,hmi__map__info__pb2.DESCRIPTOR,hmi__localization__init__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('P\001'))

_HMIGRPCSERVICE = _descriptor.ServiceDescriptor(
  name='HMIGrpcService',
  full_name='adu.hmi.HMIGrpcService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=350,
  serialized_end=3199,
  methods=[
  _descriptor.MethodDescriptor(
    name='FetchSectionMsg',
    full_name='adu.hmi.HMIGrpcService.FetchSectionMsg',
    index=0,
    containing_service=None,
    input_type=hmi__fetch__msg__pb2._FETCHKEYS,
    output_type=hmi__fetch__msg__pb2._WORLDPACKAGE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FetchMapElement',
    full_name='adu.hmi.HMIGrpcService.FetchMapElement',
    index=1,
    containing_service=None,
    input_type=hmi__map__info__pb2._MAPFILEREQUEST,
    output_type=hmi__map__info__pb2._MAPFILERESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FetchMapVersion',
    full_name='adu.hmi.HMIGrpcService.FetchMapVersion',
    index=2,
    containing_service=None,
    input_type=hmi__fetch__msg__pb2._MAPVERSIONREQUEST,
    output_type=hmi__fetch__msg__pb2._MAPVERSIONRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FetchSafeCheckResult',
    full_name='adu.hmi.HMIGrpcService.FetchSafeCheckResult',
    index=3,
    containing_service=None,
    input_type=hmi__fetch__msg__pb2._SAFECHECKREQUEST,
    output_type=hmi__world__pb2._SAFECHECKRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ShutdownSystem',
    full_name='adu.hmi.HMIGrpcService.ShutdownSystem',
    index=4,
    containing_service=None,
    input_type=hmi__system__control__pb2._SYSTEMCONTROLREQUEST,
    output_type=hmi__system__control__pb2._SYSTEMCONTROLRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TransferSystemControl',
    full_name='adu.hmi.HMIGrpcService.TransferSystemControl',
    index=5,
    containing_service=None,
    input_type=hmi__system__control__pb2._TRANSFERCONTROLREQUEST,
    output_type=hmi__system__control__pb2._TRANSFERCONTROLRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PreRouting',
    full_name='adu.hmi.HMIGrpcService.PreRouting',
    index=6,
    containing_service=None,
    input_type=hmi__routing__pb2._ROUTINGREQUEST,
    output_type=hmi__routing__pb2._ROUTINGRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StartRouting',
    full_name='adu.hmi.HMIGrpcService.StartRouting',
    index=7,
    containing_service=None,
    input_type=hmi__routing__pb2._ROUTINGREQUEST,
    output_type=hmi__routing__pb2._ROUTINGRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Launch',
    full_name='adu.hmi.HMIGrpcService.Launch',
    index=8,
    containing_service=None,
    input_type=hmi__launch__pb2._LAUNCHREQUEST,
    output_type=hmi__launch__pb2._LAUNCHRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Disengage',
    full_name='adu.hmi.HMIGrpcService.Disengage',
    index=9,
    containing_service=None,
    input_type=hmi__launch__pb2._DISENGAGEREQUEST,
    output_type=hmi__launch__pb2._DISENGAGERESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StopAndGo',
    full_name='adu.hmi.HMIGrpcService.StopAndGo',
    index=10,
    containing_service=None,
    input_type=hmi__driving__control__pb2._SWITCHCARSTATEREQUEST,
    output_type=hmi__common__pb2._STATUSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CheckPositionStatus',
    full_name='adu.hmi.HMIGrpcService.CheckPositionStatus',
    index=11,
    containing_service=None,
    input_type=hmi__driving__control__pb2._POSITIONSTATUSREQUEST,
    output_type=hmi__driving__control__pb2._POSITIONSTATUSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CheckParkingRelation',
    full_name='adu.hmi.HMIGrpcService.CheckParkingRelation',
    index=12,
    containing_service=None,
    input_type=hmi__driving__control__pb2._PARKINGRELATIONREQUEST,
    output_type=hmi__driving__control__pb2._PARKINGRELATIONRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AutoParking',
    full_name='adu.hmi.HMIGrpcService.AutoParking',
    index=13,
    containing_service=None,
    input_type=hmi__driving__control__pb2._AUTOPARKINGREQUEST,
    output_type=hmi__common__pb2._STATUSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AutoOutGarage',
    full_name='adu.hmi.HMIGrpcService.AutoOutGarage',
    index=14,
    containing_service=None,
    input_type=hmi__driving__control__pb2._AUTOOUTGARAGEREQUEST,
    output_type=hmi__common__pb2._STATUSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Intervene',
    full_name='adu.hmi.HMIGrpcService.Intervene',
    index=15,
    containing_service=None,
    input_type=hmi__driving__control__pb2._INTERVENEREQUEST,
    output_type=hmi__common__pb2._STATUSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DisengageTypeFeedback',
    full_name='adu.hmi.HMIGrpcService.DisengageTypeFeedback',
    index=16,
    containing_service=None,
    input_type=hmi__driving__control__pb2._DISENGAGETYPECONTENT,
    output_type=hmi__common__pb2._STATUSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SwitchDoor',
    full_name='adu.hmi.HMIGrpcService.SwitchDoor',
    index=17,
    containing_service=None,
    input_type=hmi__car__device__pb2._DECIVECONTROLREQUEST,
    output_type=hmi__common__pb2._STATUSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SwitchHeadLights',
    full_name='adu.hmi.HMIGrpcService.SwitchHeadLights',
    index=18,
    containing_service=None,
    input_type=hmi__car__device__pb2._DECIVECONTROLREQUEST,
    output_type=hmi__common__pb2._STATUSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SwitchFrontLamp',
    full_name='adu.hmi.HMIGrpcService.SwitchFrontLamp',
    index=19,
    containing_service=None,
    input_type=hmi__car__device__pb2._DECIVECONTROLREQUEST,
    output_type=hmi__common__pb2._STATUSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SwitchEmergencyLamp',
    full_name='adu.hmi.HMIGrpcService.SwitchEmergencyLamp',
    index=20,
    containing_service=None,
    input_type=hmi__car__device__pb2._DECIVECONTROLREQUEST,
    output_type=hmi__common__pb2._STATUSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SwitchCourtesyLamp',
    full_name='adu.hmi.HMIGrpcService.SwitchCourtesyLamp',
    index=21,
    containing_service=None,
    input_type=hmi__car__device__pb2._DECIVECONTROLREQUEST,
    output_type=hmi__common__pb2._STATUSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='NotiAirCondition',
    full_name='adu.hmi.HMIGrpcService.NotiAirCondition',
    index=22,
    containing_service=None,
    input_type=hmi__car__device__pb2._AIRCONDITIONREQUEST,
    output_type=hmi__common__pb2._STATUSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TriggerAlarmHorn',
    full_name='adu.hmi.HMIGrpcService.TriggerAlarmHorn',
    index=23,
    containing_service=None,
    input_type=hmi__car__device__pb2._TRIGGERREQUEST,
    output_type=hmi__common__pb2._STATUSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TriggerEmergencyStop',
    full_name='adu.hmi.HMIGrpcService.TriggerEmergencyStop',
    index=24,
    containing_service=None,
    input_type=hmi__car__device__pb2._TRIGGERREQUEST,
    output_type=hmi__common__pb2._STATUSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetHudInfo',
    full_name='adu.hmi.HMIGrpcService.SetHudInfo',
    index=25,
    containing_service=None,
    input_type=hmi__hudinfo__pb2._HUDINFO,
    output_type=hmi__common__pb2._STATUSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='NotiOTAClient',
    full_name='adu.hmi.HMIGrpcService.NotiOTAClient',
    index=26,
    containing_service=None,
    input_type=hmi__ota__pb2._OTAREQUEST,
    output_type=hmi__ota__pb2._OTARESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FetchCollectDataMsg',
    full_name='adu.hmi.HMIGrpcService.FetchCollectDataMsg',
    index=27,
    containing_service=None,
    input_type=hmi__collect__data__pb2._FETCHCOLLECTDATAKEY,
    output_type=hmi__collect__data__pb2._FETCHCOLLECTDATAPACKAGE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='NotiWorkingState',
    full_name='adu.hmi.HMIGrpcService.NotiWorkingState',
    index=28,
    containing_service=None,
    input_type=hmi__collect__data__pb2._WORKSTATIONREQUEST,
    output_type=hmi__common__pb2._STATUSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='NotiDataCheck',
    full_name='adu.hmi.HMIGrpcService.NotiDataCheck',
    index=29,
    containing_service=None,
    input_type=hmi__collect__data__pb2._DATACHECKREQUEST,
    output_type=hmi__collect__data__pb2._DATACHECKRESULT,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SwitchCollectMode',
    full_name='adu.hmi.HMIGrpcService.SwitchCollectMode',
    index=30,
    containing_service=None,
    input_type=hmi__collect__data__pb2._COLLECTINGSTATEREQUEST,
    output_type=hmi__common__pb2._STATUSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FetchPreProcTaskStatus',
    full_name='adu.hmi.HMIGrpcService.FetchPreProcTaskStatus',
    index=31,
    containing_service=None,
    input_type=hmi__fetch__msg__pb2._FETCHPREPROCTASKREQUEST,
    output_type=hmi__fetch__msg__pb2._PREPROCTASKRESULT,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CheckCalibrationValidity',
    full_name='adu.hmi.HMIGrpcService.CheckCalibrationValidity',
    index=32,
    containing_service=None,
    input_type=hmi__world__pb2._CALIBRATIONVALIDITYREQUEST,
    output_type=hmi__world__pb2._CALIBRATIONVALIDITYRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StreamOtaToHmi',
    full_name='adu.hmi.HMIGrpcService.StreamOtaToHmi',
    index=33,
    containing_service=None,
    input_type=ota__pb2._OTAREQUEST,
    output_type=ota__pb2._OTARESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StreamHmiToOta',
    full_name='adu.hmi.HMIGrpcService.StreamHmiToOta',
    index=34,
    containing_service=None,
    input_type=ota__pb2._OTARESPONSE,
    output_type=ota__pb2._OTAREQUEST,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='NotiLocalizationInitPose',
    full_name='adu.hmi.HMIGrpcService.NotiLocalizationInitPose',
    index=35,
    containing_service=None,
    input_type=hmi__localization__init__pb2._POSITIONANDHEADING,
    output_type=hmi__localization__init__pb2._LOCALINITRES,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='MoveLogSync',
    full_name='adu.hmi.HMIGrpcService.MoveLogSync',
    index=36,
    containing_service=None,
    input_type=hmi__system__control__pb2._SYSTEMCONTROLREQUEST,
    output_type=hmi__system__control__pb2._SYSTEMCONTROLRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_HMIGRPCSERVICE)

DESCRIPTOR.services_by_name['HMIGrpcService'] = _HMIGRPCSERVICE

# @@protoc_insertion_point(module_scope)

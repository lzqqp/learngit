# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import calibration_common_pb2 as calibration__common__pb2


class CalibrationGrpcServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetVinCode = channel.unary_unary(
        '/adu.calibration.CalibrationGrpcService/GetVinCode',
        request_serializer=calibration__common__pb2.GetVinCodeRequest.SerializeToString,
        response_deserializer=calibration__common__pb2.VinCode.FromString,
        )
    self.SetVehicleLocation = channel.unary_unary(
        '/adu.calibration.CalibrationGrpcService/SetVehicleLocation',
        request_serializer=calibration__common__pb2.VehicleLocation.SerializeToString,
        response_deserializer=calibration__common__pb2.StatusResponse.FromString,
        )
    self.CheckUltrasonicRadarID = channel.stream_stream(
        '/adu.calibration.CalibrationGrpcService/CheckUltrasonicRadarID',
        request_serializer=calibration__common__pb2.CheckURIDRequest.SerializeToString,
        response_deserializer=calibration__common__pb2.CheckURIDResponse.FromString,
        )
    self.SaveUltrasonicRadarID = channel.unary_unary(
        '/adu.calibration.CalibrationGrpcService/SaveUltrasonicRadarID',
        request_serializer=calibration__common__pb2.SaveURIDRequest.SerializeToString,
        response_deserializer=calibration__common__pb2.StatusResponse.FromString,
        )
    self.CheckSensorStatus = channel.unary_unary(
        '/adu.calibration.CalibrationGrpcService/CheckSensorStatus',
        request_serializer=calibration__common__pb2.CheckRequest.SerializeToString,
        response_deserializer=calibration__common__pb2.SensorStatus.FromString,
        )
    self.AdjustSensorPosition = channel.stream_stream(
        '/adu.calibration.CalibrationGrpcService/AdjustSensorPosition',
        request_serializer=calibration__common__pb2.AdjustRequest.SerializeToString,
        response_deserializer=calibration__common__pb2.AdjustResponse.FromString,
        )
    self.CheckSensorPosition = channel.unary_unary(
        '/adu.calibration.CalibrationGrpcService/CheckSensorPosition',
        request_serializer=calibration__common__pb2.CheckRequest.SerializeToString,
        response_deserializer=calibration__common__pb2.StatusResponse.FromString,
        )
    self.StartSensorCalibration = channel.unary_stream(
        '/adu.calibration.CalibrationGrpcService/StartSensorCalibration',
        request_serializer=calibration__common__pb2.StartRequest.SerializeToString,
        response_deserializer=calibration__common__pb2.CalibrationResponse.FromString,
        )
    self.GetCalibrationResult = channel.unary_unary(
        '/adu.calibration.CalibrationGrpcService/GetCalibrationResult',
        request_serializer=calibration__common__pb2.GetResultRequest.SerializeToString,
        response_deserializer=calibration__common__pb2.CalibrationResult.FromString,
        )
    self.GetLocalizationStatus = channel.unary_stream(
        '/adu.calibration.CalibrationGrpcService/GetLocalizationStatus',
        request_serializer=calibration__common__pb2.CheckRequest.SerializeToString,
        response_deserializer=calibration__common__pb2.LocalizationResponse.FromString,
        )
    self.StartEightRouteCalibration = channel.unary_stream(
        '/adu.calibration.CalibrationGrpcService/StartEightRouteCalibration',
        request_serializer=calibration__common__pb2.StartRequest.SerializeToString,
        response_deserializer=calibration__common__pb2.CalibrationResponse.FromString,
        )
    self.StartSlowCalibration = channel.unary_stream(
        '/adu.calibration.CalibrationGrpcService/StartSlowCalibration',
        request_serializer=calibration__common__pb2.StartRequest.SerializeToString,
        response_deserializer=calibration__common__pb2.CalibrationResponse.FromString,
        )
    self.StartStraightCalibration = channel.unary_stream(
        '/adu.calibration.CalibrationGrpcService/StartStraightCalibration',
        request_serializer=calibration__common__pb2.StartRequest.SerializeToString,
        response_deserializer=calibration__common__pb2.CalibrationResponse.FromString,
        )
    self.StartEightRouteDriving = channel.unary_stream(
        '/adu.calibration.CalibrationGrpcService/StartEightRouteDriving',
        request_serializer=calibration__common__pb2.StartRequest.SerializeToString,
        response_deserializer=calibration__common__pb2.DrivingResponse.FromString,
        )
    self.StartStraightDriving = channel.unary_stream(
        '/adu.calibration.CalibrationGrpcService/StartStraightDriving',
        request_serializer=calibration__common__pb2.StartRequest.SerializeToString,
        response_deserializer=calibration__common__pb2.DrivingResponse.FromString,
        )
    self.StartEightRouteCalibrationOffline = channel.unary_stream(
        '/adu.calibration.CalibrationGrpcService/StartEightRouteCalibrationOffline',
        request_serializer=calibration__common__pb2.StartOffline.SerializeToString,
        response_deserializer=calibration__common__pb2.CalibrationResponse.FromString,
        )
    self.StartStraightCalibrationOffline = channel.unary_stream(
        '/adu.calibration.CalibrationGrpcService/StartStraightCalibrationOffline',
        request_serializer=calibration__common__pb2.StartOffline.SerializeToString,
        response_deserializer=calibration__common__pb2.CalibrationResponse.FromString,
        )


class CalibrationGrpcServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetVinCode(self, request, context):
    """get vin code
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetVehicleLocation(self, request, context):
    """set distance between left-front wheel and stop rod
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CheckUltrasonicRadarID(self, request_iterator, context):
    """check ultrasonic radar installation ID status
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SaveUltrasonicRadarID(self, request, context):
    """save ultrasonic radar ID status
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CheckSensorStatus(self, request, context):
    """check sensor installation status
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AdjustSensorPosition(self, request_iterator, context):
    """adjust sensor position
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CheckSensorPosition(self, request, context):
    """check sensor position
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StartSensorCalibration(self, request, context):
    """start sensor calibration
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetCalibrationResult(self, request, context):
    """get calibration result
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLocalizationStatus(self, request, context):
    """get localization status
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StartEightRouteCalibration(self, request, context):
    """start 8-route-calibration
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StartSlowCalibration(self, request, context):
    """start slow-calibration
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StartStraightCalibration(self, request, context):
    """start straight-calibration
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StartEightRouteDriving(self, request, context):
    """start 8-route-driving
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StartStraightDriving(self, request, context):
    """start straight-driving
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StartEightRouteCalibrationOffline(self, request, context):
    """start offline 8-route-calibration
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StartStraightCalibrationOffline(self, request, context):
    """start offline straight-calibration
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CalibrationGrpcServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetVinCode': grpc.unary_unary_rpc_method_handler(
          servicer.GetVinCode,
          request_deserializer=calibration__common__pb2.GetVinCodeRequest.FromString,
          response_serializer=calibration__common__pb2.VinCode.SerializeToString,
      ),
      'SetVehicleLocation': grpc.unary_unary_rpc_method_handler(
          servicer.SetVehicleLocation,
          request_deserializer=calibration__common__pb2.VehicleLocation.FromString,
          response_serializer=calibration__common__pb2.StatusResponse.SerializeToString,
      ),
      'CheckUltrasonicRadarID': grpc.stream_stream_rpc_method_handler(
          servicer.CheckUltrasonicRadarID,
          request_deserializer=calibration__common__pb2.CheckURIDRequest.FromString,
          response_serializer=calibration__common__pb2.CheckURIDResponse.SerializeToString,
      ),
      'SaveUltrasonicRadarID': grpc.unary_unary_rpc_method_handler(
          servicer.SaveUltrasonicRadarID,
          request_deserializer=calibration__common__pb2.SaveURIDRequest.FromString,
          response_serializer=calibration__common__pb2.StatusResponse.SerializeToString,
      ),
      'CheckSensorStatus': grpc.unary_unary_rpc_method_handler(
          servicer.CheckSensorStatus,
          request_deserializer=calibration__common__pb2.CheckRequest.FromString,
          response_serializer=calibration__common__pb2.SensorStatus.SerializeToString,
      ),
      'AdjustSensorPosition': grpc.stream_stream_rpc_method_handler(
          servicer.AdjustSensorPosition,
          request_deserializer=calibration__common__pb2.AdjustRequest.FromString,
          response_serializer=calibration__common__pb2.AdjustResponse.SerializeToString,
      ),
      'CheckSensorPosition': grpc.unary_unary_rpc_method_handler(
          servicer.CheckSensorPosition,
          request_deserializer=calibration__common__pb2.CheckRequest.FromString,
          response_serializer=calibration__common__pb2.StatusResponse.SerializeToString,
      ),
      'StartSensorCalibration': grpc.unary_stream_rpc_method_handler(
          servicer.StartSensorCalibration,
          request_deserializer=calibration__common__pb2.StartRequest.FromString,
          response_serializer=calibration__common__pb2.CalibrationResponse.SerializeToString,
      ),
      'GetCalibrationResult': grpc.unary_unary_rpc_method_handler(
          servicer.GetCalibrationResult,
          request_deserializer=calibration__common__pb2.GetResultRequest.FromString,
          response_serializer=calibration__common__pb2.CalibrationResult.SerializeToString,
      ),
      'GetLocalizationStatus': grpc.unary_stream_rpc_method_handler(
          servicer.GetLocalizationStatus,
          request_deserializer=calibration__common__pb2.CheckRequest.FromString,
          response_serializer=calibration__common__pb2.LocalizationResponse.SerializeToString,
      ),
      'StartEightRouteCalibration': grpc.unary_stream_rpc_method_handler(
          servicer.StartEightRouteCalibration,
          request_deserializer=calibration__common__pb2.StartRequest.FromString,
          response_serializer=calibration__common__pb2.CalibrationResponse.SerializeToString,
      ),
      'StartSlowCalibration': grpc.unary_stream_rpc_method_handler(
          servicer.StartSlowCalibration,
          request_deserializer=calibration__common__pb2.StartRequest.FromString,
          response_serializer=calibration__common__pb2.CalibrationResponse.SerializeToString,
      ),
      'StartStraightCalibration': grpc.unary_stream_rpc_method_handler(
          servicer.StartStraightCalibration,
          request_deserializer=calibration__common__pb2.StartRequest.FromString,
          response_serializer=calibration__common__pb2.CalibrationResponse.SerializeToString,
      ),
      'StartEightRouteDriving': grpc.unary_stream_rpc_method_handler(
          servicer.StartEightRouteDriving,
          request_deserializer=calibration__common__pb2.StartRequest.FromString,
          response_serializer=calibration__common__pb2.DrivingResponse.SerializeToString,
      ),
      'StartStraightDriving': grpc.unary_stream_rpc_method_handler(
          servicer.StartStraightDriving,
          request_deserializer=calibration__common__pb2.StartRequest.FromString,
          response_serializer=calibration__common__pb2.DrivingResponse.SerializeToString,
      ),
      'StartEightRouteCalibrationOffline': grpc.unary_stream_rpc_method_handler(
          servicer.StartEightRouteCalibrationOffline,
          request_deserializer=calibration__common__pb2.StartOffline.FromString,
          response_serializer=calibration__common__pb2.CalibrationResponse.SerializeToString,
      ),
      'StartStraightCalibrationOffline': grpc.unary_stream_rpc_method_handler(
          servicer.StartStraightCalibrationOffline,
          request_deserializer=calibration__common__pb2.StartOffline.FromString,
          response_serializer=calibration__common__pb2.CalibrationResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'adu.calibration.CalibrationGrpcService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

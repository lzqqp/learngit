# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import collection_check_message_pb2 as collection__check__message__pb2
import collection_data_message_pb2 as collection__data__message__pb2
import collection_status_message_pb2 as collection__status__message__pb2


class CollectionCheckerServiceStub(object):
  """MAP
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.DynamicAlign = channel.unary_unary(
        '/adu.workers.collection.CollectionCheckerService/DynamicAlign',
        request_serializer=collection__check__message__pb2.DynamicAlignRequest.SerializeToString,
        response_deserializer=collection__check__message__pb2.DynamicAlignResponse.FromString,
        )
    self.EightRoute = channel.unary_unary(
        '/adu.workers.collection.CollectionCheckerService/EightRoute',
        request_serializer=collection__check__message__pb2.EightRouteRequest.SerializeToString,
        response_deserializer=collection__check__message__pb2.EightRouteResponse.FromString,
        )
    self.DataVerify = channel.unary_unary(
        '/adu.workers.collection.CollectionCheckerService/DataVerify',
        request_serializer=collection__check__message__pb2.VerifyRequest.SerializeToString,
        response_deserializer=collection__check__message__pb2.VerifyResponse.FromString,
        )


class CollectionCheckerServiceServicer(object):
  """MAP
  """

  def DynamicAlign(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def EightRoute(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DataVerify(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CollectionCheckerServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'DynamicAlign': grpc.unary_unary_rpc_method_handler(
          servicer.DynamicAlign,
          request_deserializer=collection__check__message__pb2.DynamicAlignRequest.FromString,
          response_serializer=collection__check__message__pb2.DynamicAlignResponse.SerializeToString,
      ),
      'EightRoute': grpc.unary_unary_rpc_method_handler(
          servicer.EightRoute,
          request_deserializer=collection__check__message__pb2.EightRouteRequest.FromString,
          response_serializer=collection__check__message__pb2.EightRouteResponse.SerializeToString,
      ),
      'DataVerify': grpc.unary_unary_rpc_method_handler(
          servicer.DataVerify,
          request_deserializer=collection__check__message__pb2.VerifyRequest.FromString,
          response_serializer=collection__check__message__pb2.VerifyResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'adu.workers.collection.CollectionCheckerService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class CollectorServiceStub(object):
  """APP
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.FetchCollectionInfo = channel.unary_unary(
        '/adu.workers.collection.CollectorService/FetchCollectionInfo',
        request_serializer=collection__status__message__pb2.FetchCollectionKeys.SerializeToString,
        response_deserializer=collection__status__message__pb2.FetchCollectionPackage.FromString,
        )
    self.TaskHandler = channel.unary_unary(
        '/adu.workers.collection.CollectorService/TaskHandler',
        request_serializer=collection__status__message__pb2.TaskRequest.SerializeToString,
        response_deserializer=collection__status__message__pb2.StatusResponse.FromString,
        )
    self.CheckGPSbin = channel.unary_unary(
        '/adu.workers.collection.CollectorService/CheckGPSbin',
        request_serializer=collection__data__message__pb2.CheckGPSbinRequest.SerializeToString,
        response_deserializer=collection__data__message__pb2.CheckGPSbinResponse.FromString,
        )
    self.DiskFormat = channel.unary_unary(
        '/adu.workers.collection.CollectorService/DiskFormat',
        request_serializer=collection__data__message__pb2.DiskFormatRequest.SerializeToString,
        response_deserializer=collection__data__message__pb2.DiskFormatResponse.FromString,
        )
    self.DynamicAlign = channel.unary_unary(
        '/adu.workers.collection.CollectorService/DynamicAlign',
        request_serializer=collection__check__message__pb2.DynamicAlignRequest.SerializeToString,
        response_deserializer=collection__check__message__pb2.DynamicAlignResponse.FromString,
        )
    self.EightRoute = channel.unary_unary(
        '/adu.workers.collection.CollectorService/EightRoute',
        request_serializer=collection__check__message__pb2.EightRouteRequest.SerializeToString,
        response_deserializer=collection__check__message__pb2.EightRouteResponse.FromString,
        )
    self.DataVerify = channel.unary_unary(
        '/adu.workers.collection.CollectorService/DataVerify',
        request_serializer=collection__check__message__pb2.DataVerifyRequest.SerializeToString,
        response_deserializer=collection__check__message__pb2.DataVerifyResponse.FromString,
        )


class CollectorServiceServicer(object):
  """APP
  """

  def FetchCollectionInfo(self, request, context):
    """collection message fetch api
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TaskHandler(self, request, context):
    """task-recorder controller
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CheckGPSbin(self, request, context):
    """car gpsbin file checker
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DiskFormat(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DynamicAlign(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def EightRoute(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DataVerify(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CollectorServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'FetchCollectionInfo': grpc.unary_unary_rpc_method_handler(
          servicer.FetchCollectionInfo,
          request_deserializer=collection__status__message__pb2.FetchCollectionKeys.FromString,
          response_serializer=collection__status__message__pb2.FetchCollectionPackage.SerializeToString,
      ),
      'TaskHandler': grpc.unary_unary_rpc_method_handler(
          servicer.TaskHandler,
          request_deserializer=collection__status__message__pb2.TaskRequest.FromString,
          response_serializer=collection__status__message__pb2.StatusResponse.SerializeToString,
      ),
      'CheckGPSbin': grpc.unary_unary_rpc_method_handler(
          servicer.CheckGPSbin,
          request_deserializer=collection__data__message__pb2.CheckGPSbinRequest.FromString,
          response_serializer=collection__data__message__pb2.CheckGPSbinResponse.SerializeToString,
      ),
      'DiskFormat': grpc.unary_unary_rpc_method_handler(
          servicer.DiskFormat,
          request_deserializer=collection__data__message__pb2.DiskFormatRequest.FromString,
          response_serializer=collection__data__message__pb2.DiskFormatResponse.SerializeToString,
      ),
      'DynamicAlign': grpc.unary_unary_rpc_method_handler(
          servicer.DynamicAlign,
          request_deserializer=collection__check__message__pb2.DynamicAlignRequest.FromString,
          response_serializer=collection__check__message__pb2.DynamicAlignResponse.SerializeToString,
      ),
      'EightRoute': grpc.unary_unary_rpc_method_handler(
          servicer.EightRoute,
          request_deserializer=collection__check__message__pb2.EightRouteRequest.FromString,
          response_serializer=collection__check__message__pb2.EightRouteResponse.SerializeToString,
      ),
      'DataVerify': grpc.unary_unary_rpc_method_handler(
          servicer.DataVerify,
          request_deserializer=collection__check__message__pb2.DataVerifyRequest.FromString,
          response_serializer=collection__check__message__pb2.DataVerifyResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'adu.workers.collection.CollectorService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

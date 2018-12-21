# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import monitor_rpc_pb2 as monitor__rpc__pb2
import rpc_interface_pb2 as rpc__interface__pb2


class MonitorServiceStub(object):
  """The signature of the RPC service, provided by the decision module.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.MonitorRPC = channel.unary_unary(
        '/adu.common.rpc.MonitorService/MonitorRPC',
        request_serializer=rpc__interface__pb2.Request.SerializeToString,
        response_deserializer=monitor__rpc__pb2.RPCResponse.FromString,
        )


class MonitorServiceServicer(object):
  """The signature of the RPC service, provided by the decision module.
  """

  def MonitorRPC(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MonitorServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'MonitorRPC': grpc.unary_unary_rpc_method_handler(
          servicer.MonitorRPC,
          request_deserializer=rpc__interface__pb2.Request.FromString,
          response_serializer=monitor__rpc__pb2.RPCResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'adu.common.rpc.MonitorService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
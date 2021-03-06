# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import routing_pb2 as routing__pb2


class RPCStub(object):
  """The signature of the RPC service, provided by the Decision module.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.RunRouter = channel.unary_unary(
        '/adu.common.routing.RPC/RunRouter',
        request_serializer=routing__pb2.RoutingRequest.SerializeToString,
        response_deserializer=routing__pb2.RoutingResult.FromString,
        )


class RPCServicer(object):
  """The signature of the RPC service, provided by the Decision module.
  """

  def RunRouter(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RPCServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'RunRouter': grpc.unary_unary_rpc_method_handler(
          servicer.RunRouter,
          request_deserializer=routing__pb2.RoutingRequest.FromString,
          response_serializer=routing__pb2.RoutingResult.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'adu.common.routing.RPC', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import decision_pb2 as decision__pb2
import rpc_interface_pb2 as rpc__interface__pb2


class RPCStub(object):
  """The signature of the RPC service, provided by the Decision module.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.RunDecision = channel.unary_unary(
        '/adu.common.decision.RPC/RunDecision',
        request_serializer=rpc__interface__pb2.Request.SerializeToString,
        response_deserializer=decision__pb2.DecisionResult.FromString,
        )


class RPCServicer(object):
  """The signature of the RPC service, provided by the Decision module.
  """

  def RunDecision(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RPCServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'RunDecision': grpc.unary_unary_rpc_method_handler(
          servicer.RunDecision,
          request_deserializer=rpc__interface__pb2.Request.FromString,
          response_serializer=decision__pb2.DecisionResult.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'adu.common.decision.RPC', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

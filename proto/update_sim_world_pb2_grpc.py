# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import monitor_result_pb2 as monitor__result__pb2
import simulation_common_pb2 as simulation__common__pb2
import update_sim_world_pb2 as update__sim__world__pb2


class UpdateSimWorldStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.UpdateWorld = channel.unary_unary(
        '/adu.simulation.UpdateSimWorld/UpdateWorld',
        request_serializer=update__sim__world__pb2.PushWorld.SerializeToString,
        response_deserializer=simulation__common__pb2.UpdateStatus.FromString,
        )
    self.PushMonitorStatus = channel.unary_unary(
        '/adu.simulation.UpdateSimWorld/PushMonitorStatus',
        request_serializer=monitor__result__pb2.MonitortResult.SerializeToString,
        response_deserializer=simulation__common__pb2.UpdateStatus.FromString,
        )


class UpdateSimWorldServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def UpdateWorld(self, request, context):
    """Sends a request for pushing the updated simulation world.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PushMonitorStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_UpdateSimWorldServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'UpdateWorld': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateWorld,
          request_deserializer=update__sim__world__pb2.PushWorld.FromString,
          response_serializer=simulation__common__pb2.UpdateStatus.SerializeToString,
      ),
      'PushMonitorStatus': grpc.unary_unary_rpc_method_handler(
          servicer.PushMonitorStatus,
          request_deserializer=monitor__result__pb2.MonitortResult.FromString,
          response_serializer=simulation__common__pb2.UpdateStatus.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'adu.simulation.UpdateSimWorld', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import simulation_common_pb2 as simulation__common__pb2
import stats_monitor_pb2 as stats__monitor__pb2


class UpdateStatsStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.UpdateDelayStats = channel.unary_unary(
        '/adu.simulation.UpdateStats/UpdateDelayStats',
        request_serializer=stats__monitor__pb2.DelayStats.SerializeToString,
        response_deserializer=simulation__common__pb2.UpdateStatus.FromString,
        )


class UpdateStatsServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def UpdateDelayStats(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_UpdateStatsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'UpdateDelayStats': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateDelayStats,
          request_deserializer=stats__monitor__pb2.DelayStats.FromString,
          response_serializer=simulation__common__pb2.UpdateStatus.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'adu.simulation.UpdateStats', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

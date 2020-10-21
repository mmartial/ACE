# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ace import analytic_pb2 as ace_dot_analytic__pb2


class AnalyticStub(object):
    """Analytic service defines the functions for processing video frames via
    streaming or non-streaming (unary) RPC
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StreamVideoFrame = channel.stream_stream(
                '/ace.Analytic/StreamVideoFrame',
                request_serializer=ace_dot_analytic__pb2.InputFrame.SerializeToString,
                response_deserializer=ace_dot_analytic__pb2.ProcessedFrame.FromString,
                )
        self.ProcessVideoFrame = channel.unary_unary(
                '/ace.Analytic/ProcessVideoFrame',
                request_serializer=ace_dot_analytic__pb2.ProcessFrameRequest.SerializeToString,
                response_deserializer=ace_dot_analytic__pb2.ProcessedFrame.FromString,
                )
        self.ConfigVideoStream = channel.stream_stream(
                '/ace.Analytic/ConfigVideoStream',
                request_serializer=ace_dot_analytic__pb2.StreamRequest.SerializeToString,
                response_deserializer=ace_dot_analytic__pb2.ProcessedFrame.FromString,
                )
        self.GetFrame = channel.unary_unary(
                '/ace.Analytic/GetFrame',
                request_serializer=ace_dot_analytic__pb2.FrameRequest.SerializeToString,
                response_deserializer=ace_dot_analytic__pb2.CompositeResults.FromString,
                )
        self.CheckStatus = channel.unary_unary(
                '/ace.Analytic/CheckStatus',
                request_serializer=ace_dot_analytic__pb2.Empty.SerializeToString,
                response_deserializer=ace_dot_analytic__pb2.AnalyticStatus.FromString,
                )


class AnalyticServicer(object):
    """Analytic service defines the functions for processing video frames via
    streaming or non-streaming (unary) RPC
    """

    def StreamVideoFrame(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ProcessVideoFrame(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigVideoStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFrame(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AnalyticServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StreamVideoFrame': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamVideoFrame,
                    request_deserializer=ace_dot_analytic__pb2.InputFrame.FromString,
                    response_serializer=ace_dot_analytic__pb2.ProcessedFrame.SerializeToString,
            ),
            'ProcessVideoFrame': grpc.unary_unary_rpc_method_handler(
                    servicer.ProcessVideoFrame,
                    request_deserializer=ace_dot_analytic__pb2.ProcessFrameRequest.FromString,
                    response_serializer=ace_dot_analytic__pb2.ProcessedFrame.SerializeToString,
            ),
            'ConfigVideoStream': grpc.stream_stream_rpc_method_handler(
                    servicer.ConfigVideoStream,
                    request_deserializer=ace_dot_analytic__pb2.StreamRequest.FromString,
                    response_serializer=ace_dot_analytic__pb2.ProcessedFrame.SerializeToString,
            ),
            'GetFrame': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFrame,
                    request_deserializer=ace_dot_analytic__pb2.FrameRequest.FromString,
                    response_serializer=ace_dot_analytic__pb2.CompositeResults.SerializeToString,
            ),
            'CheckStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckStatus,
                    request_deserializer=ace_dot_analytic__pb2.Empty.FromString,
                    response_serializer=ace_dot_analytic__pb2.AnalyticStatus.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ace.Analytic', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Analytic(object):
    """Analytic service defines the functions for processing video frames via
    streaming or non-streaming (unary) RPC
    """

    @staticmethod
    def StreamVideoFrame(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/ace.Analytic/StreamVideoFrame',
            ace_dot_analytic__pb2.InputFrame.SerializeToString,
            ace_dot_analytic__pb2.ProcessedFrame.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ProcessVideoFrame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ace.Analytic/ProcessVideoFrame',
            ace_dot_analytic__pb2.ProcessFrameRequest.SerializeToString,
            ace_dot_analytic__pb2.ProcessedFrame.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigVideoStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/ace.Analytic/ConfigVideoStream',
            ace_dot_analytic__pb2.StreamRequest.SerializeToString,
            ace_dot_analytic__pb2.ProcessedFrame.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFrame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ace.Analytic/GetFrame',
            ace_dot_analytic__pb2.FrameRequest.SerializeToString,
            ace_dot_analytic__pb2.CompositeResults.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ace.Analytic/CheckStatus',
            ace_dot_analytic__pb2.Empty.SerializeToString,
            ace_dot_analytic__pb2.AnalyticStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

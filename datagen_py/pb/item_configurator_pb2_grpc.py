# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import item_configurator_pb2 as item__configurator__pb2


class ItemConfiguratorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Update = channel.unary_unary(
                '/item_configurator_proto.ItemConfigurator/Update',
                request_serializer=item__configurator__pb2.UpdateReq.SerializeToString,
                response_deserializer=item__configurator__pb2.UpdateRep.FromString,
                )
        self.List = channel.unary_unary(
                '/item_configurator_proto.ItemConfigurator/List',
                request_serializer=item__configurator__pb2.ListReq.SerializeToString,
                response_deserializer=item__configurator__pb2.ListRep.FromString,
                )
        self.ListCharacters = channel.unary_unary(
                '/item_configurator_proto.ItemConfigurator/ListCharacters',
                request_serializer=item__configurator__pb2.ListCharactersReq.SerializeToString,
                response_deserializer=item__configurator__pb2.ListCharactersRep.FromString,
                )
        self.AddCharacters = channel.unary_unary(
                '/item_configurator_proto.ItemConfigurator/AddCharacters',
                request_serializer=item__configurator__pb2.AddCharactersReq.SerializeToString,
                response_deserializer=item__configurator__pb2.AddCharactersRep.FromString,
                )
        self.DelCharacters = channel.unary_unary(
                '/item_configurator_proto.ItemConfigurator/DelCharacters',
                request_serializer=item__configurator__pb2.DelCharactersReq.SerializeToString,
                response_deserializer=item__configurator__pb2.DelCharactersRep.FromString,
                )
        self.BuybackContracts = channel.unary_unary(
                '/item_configurator_proto.ItemConfigurator/BuybackContracts',
                request_serializer=item__configurator__pb2.BuybackContractsReq.SerializeToString,
                response_deserializer=item__configurator__pb2.BuybackContractsRep.FromString,
                )


class ItemConfiguratorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCharacters(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddCharacters(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DelCharacters(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BuybackContracts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ItemConfiguratorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=item__configurator__pb2.UpdateReq.FromString,
                    response_serializer=item__configurator__pb2.UpdateRep.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=item__configurator__pb2.ListReq.FromString,
                    response_serializer=item__configurator__pb2.ListRep.SerializeToString,
            ),
            'ListCharacters': grpc.unary_unary_rpc_method_handler(
                    servicer.ListCharacters,
                    request_deserializer=item__configurator__pb2.ListCharactersReq.FromString,
                    response_serializer=item__configurator__pb2.ListCharactersRep.SerializeToString,
            ),
            'AddCharacters': grpc.unary_unary_rpc_method_handler(
                    servicer.AddCharacters,
                    request_deserializer=item__configurator__pb2.AddCharactersReq.FromString,
                    response_serializer=item__configurator__pb2.AddCharactersRep.SerializeToString,
            ),
            'DelCharacters': grpc.unary_unary_rpc_method_handler(
                    servicer.DelCharacters,
                    request_deserializer=item__configurator__pb2.DelCharactersReq.FromString,
                    response_serializer=item__configurator__pb2.DelCharactersRep.SerializeToString,
            ),
            'BuybackContracts': grpc.unary_unary_rpc_method_handler(
                    servicer.BuybackContracts,
                    request_deserializer=item__configurator__pb2.BuybackContractsReq.FromString,
                    response_serializer=item__configurator__pb2.BuybackContractsRep.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'item_configurator_proto.ItemConfigurator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ItemConfigurator(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/item_configurator_proto.ItemConfigurator/Update',
            item__configurator__pb2.UpdateReq.SerializeToString,
            item__configurator__pb2.UpdateRep.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/item_configurator_proto.ItemConfigurator/List',
            item__configurator__pb2.ListReq.SerializeToString,
            item__configurator__pb2.ListRep.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListCharacters(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/item_configurator_proto.ItemConfigurator/ListCharacters',
            item__configurator__pb2.ListCharactersReq.SerializeToString,
            item__configurator__pb2.ListCharactersRep.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddCharacters(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/item_configurator_proto.ItemConfigurator/AddCharacters',
            item__configurator__pb2.AddCharactersReq.SerializeToString,
            item__configurator__pb2.AddCharactersRep.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DelCharacters(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/item_configurator_proto.ItemConfigurator/DelCharacters',
            item__configurator__pb2.DelCharactersReq.SerializeToString,
            item__configurator__pb2.DelCharactersRep.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BuybackContracts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/item_configurator_proto.ItemConfigurator/BuybackContracts',
            item__configurator__pb2.BuybackContractsReq.SerializeToString,
            item__configurator__pb2.BuybackContractsRep.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

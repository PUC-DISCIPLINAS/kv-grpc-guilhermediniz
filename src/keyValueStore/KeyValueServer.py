from keyValueStore_pb2_grpc import KeyValueStoreServicer, add_KeyValueStoreServicer_to_server
import keyValueStore_pb2
import grpc
from concurrent import futures


class KeyValueService(KeyValueStoreServicer):
    def __init__(self):
        self.store: dict = {}

    def put(self, request, context):
        self.store[request.key] = request.value
        return keyValueStore_pb2.PutResponse()

    def get(self, request, context):
        value = self.store[request.key]
        return keyValueStore_pb2.GetResponse(value=value)

    def getAllKeys(self, request, context):
        for key in self.store.keys():
            yield keyValueStore_pb2.GetKeyResponse(key=key)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_KeyValueStoreServicer_to_server(KeyValueService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Server running...')
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

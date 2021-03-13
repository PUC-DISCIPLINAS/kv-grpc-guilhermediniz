import sys
import grpc
from keyValueStore_pb2_grpc import KeyValueStoreStub
import keyValueStore_pb2

HELP_MESSAGE = """
Available commands: 
    1 - put 'key' 'value'
    2 - get 'key'
    3 - getAllKeys 
"""


def generate_stub():
    channel = grpc.insecure_channel('localhost:50051')
    return KeyValueStoreStub(channel)


def put(key: str, value: str):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = KeyValueStoreStub(channel)
        stub.put(keyValueStore_pb2.PutRequest(key=key, value=value))
    return


def get(key: str):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = KeyValueStoreStub(channel)
        response = stub.get(keyValueStore_pb2.GetRequest(key=key))
    return response.value


def get_all_keys():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = KeyValueStoreStub(channel)
        responses = stub.getAllKeys(keyValueStore_pb2.GetAllKeysRequest())
        keys = [response.key for response in responses]
    return keys


def run():
    if len(sys.argv) < 2:
        print("No arguments were found")
        return

    user_command = sys.argv[1]

    if user_command == 'put':
        if len(sys.argv) != 4:
            print("Invalid put arguments")
            return

        put(sys.argv[2], sys.argv[3])
        print('Key/Value successfully put')
        return

    elif user_command == 'get':
        if len(sys.argv) != 3:
            print('Invalid get arguments')
            return
        value = get(sys.argv[2])
        print('Value: ' + value)
        return
    elif user_command == 'getAllKeys':
        if len(sys.argv) != 2:
            print('Invalid getAllKeys arguments')
            return
        all_keys = get_all_keys()
        print('All keys: ' + str(all_keys))
    elif user_command == 'help':
        print(HELP_MESSAGE)
        return
    else:
        print("Invalid command. Type 'help' to get list of available commands.")
        return


if __name__ == '__main__':
    run()

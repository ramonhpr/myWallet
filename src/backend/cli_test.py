from google.protobuf import empty_pb2
import grpc

from gen.stock_pb2 import Stock
from gen.stock_pb2_grpc import PortfolioStub

if __name__ == '__main__':
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = PortfolioStub(channel)
        stub.AddStock(Stock(symbol='TLT'))
        stub.AddStock(Stock(symbol='JNJ'))
        stub.AddStock(Stock(symbol='PTR4'))
        for response in stub.ListStock(empty_pb2.Empty()):
            print(response)

import os
from concurrent.futures import ThreadPoolExecutor
import grpc

from gen.stock_pb2 import Stock
from gen.stock_pb2_grpc import PortfolioServicer, add_PortfolioServicer_to_server
from repositories.stock_repository import StockRepository

repo = StockRepository()

class Portfolio(PortfolioServicer):
    def AddStock(self, request, context):
        repo.insert(request.symbol, request)
        return request

    def RemoveStock(self, request, context):
        repo.delete(request.symbol, request)
        return request

    def ListStock(self, request, context):
        for i in repo.data.values():
            yield i


if __name__ == '__main__':
    port = os.getenv('SERVICE_PORT', '8080')
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    add_PortfolioServicer_to_server(Portfolio(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()

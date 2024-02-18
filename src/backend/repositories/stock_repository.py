from repositories.in_memory_repository import InMemoryRepository


class StockRepository(InMemoryRepository):
    def __init__(self):
        super().__init__()


from repositories.abstract_repository import AbstractRepository


class InMemoryRepository(AbstractRepository):
    def __init__(self):
        self.data = {}

    def get(self, key):
        return self.data.get(key)

    def insert(self, key, value):
        self.data[key] = value

    def update(self, key, value):
        if key in self.data:
            self.data[key] = value
        else:
            raise KeyError(f"Key '{key}' not found.")

    def delete(self, key):
        if key in self.data:
            del self.data[key]
        else:
            raise KeyError(f"Key '{key}' not found.")
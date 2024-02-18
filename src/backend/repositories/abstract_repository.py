from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def insert(self, key, value):
        pass

    @abstractmethod
    def update(self, key, value):
        pass

    @abstractmethod
    def delete(self, key):
        pass

from abc import ABC, abstractmethod

class ResponeHandlerInterface(ABC):
    @abstractmethod
    def get_balance() -> int:
        pass

    @abstractmethod
    def get_activation_number() -> int:
        pass

    @abstractmethod
    def get_phone_number() -> str:
        pass
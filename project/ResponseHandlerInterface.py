from abc import ABC, abstractmethod

class ResponseHandlerInterface(ABC):
    @abstractmethod
    def get_balance() -> float:
        pass

    @abstractmethod
    def get_activation_number() -> int:
        pass

    @abstractmethod
    def get_phone_number() -> str:
        pass

    @abstractmethod
    def get_verification_code() -> int:
        pass
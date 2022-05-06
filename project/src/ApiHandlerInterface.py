from Status import Status
from abc import ABC, abstractmethod

class ApiHandlerInterface(ABC):
    @abstractmethod
    def request_balance() -> str:
        pass

    @abstractmethod
    def request_available_numbers() -> str:
        pass

    @abstractmethod
    def request_phone_number(country_code: int) -> str:
        pass

    @abstractmethod
    def request_activation_status(phone_id: int) -> str:
        pass

    @abstractmethod
    def change_activation_status(phone_id: int, status: Status) -> str:
        pass

    @abstractmethod
    def request_all_countries() -> str:
        pass

    @abstractmethod
    def request_all_services() -> str:
        pass
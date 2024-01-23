from abc import ABC, abstractmethod

class IERC20(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def symbol(self) -> str:
        pass

    @property
    @abstractmethod
    def decimals(self) -> int:
        pass

    @property
    @abstractmethod
    def totalSupply(self) -> int:
        pass

    @abstractmethod
    def balanceOf(self, account: str) -> int:
        pass

    @abstractmethod
    def transfer(self, from_: str, to: str, value: int) -> bool:
        pass

    @abstractmethod
    def allowance(self, owner: str, spender: str) -> int:
        pass

    @abstractmethod
    def approve(self, owner: str, spender: str, value: int) -> bool:
        pass

    @abstractmethod
    def transferFrom(self, from_: str, to: str, spender: str, value: int) -> bool:
        pass

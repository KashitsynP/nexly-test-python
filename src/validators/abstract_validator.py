from abc import ABC, abstractmethod
from typing import Optional


# An abstract class for validators
class AbstractValidator(ABC):
    @abstractmethod
    def validate(self, extracted_value: Optional[str]) -> bool:
        pass

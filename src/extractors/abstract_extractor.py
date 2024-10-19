from abc import ABC, abstractmethod
from typing import Optional


# An abstract class for extractors
class AbstractExtractor(ABC):
    @abstractmethod
    def extract(self, file_path: str) -> Optional[str]:
        pass

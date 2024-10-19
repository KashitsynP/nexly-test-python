import re
from typing import Optional

from src.extractors.abstract_extractor import AbstractExtractor
from src.reader import PDFReader


class DateExtractor(AbstractExtractor):
    def __init__(self, expected_date: str):
        self.expected_date = expected_date

    def extract(self, file_path: str) -> Optional[str]:
        reader = PDFReader(file_path)
        text = reader.read_first_page()
        if not text:
            return None
        # Regular expressions for searching for dates in different formats
        date_patterns = [
            r'([A-Za-z]+ \d{1,2}, \d{4})',  # December 31, 2023
            r'(\d{1,2} [A-Za-z]+ \d{4})',  # 31 December 2023
            r'(\d{4}-\d{2}-\d{2})',  # 2023-12-31
            r'(\d{2}/\d{2}/\d{4})',  # 31/12/2023
            r'(\d{2}-\d{2}-\d{4})'  # 31-12-2023
        ]
        try:
            for pattern in date_patterns:
                matches = re.findall(pattern, text)
                if matches:
                    return matches[0]  # Returning the first match found
        except Exception as e:
            print(f"Error extracting date: {e}")
        return None

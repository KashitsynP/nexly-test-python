from typing import Optional

from src.reader import PDFReader
from src.extractors.abstract_extractor import AbstractExtractor
import fitz


class CompanyNameExtractor(AbstractExtractor):
    def __init__(self, expected_company_name: str):
        self.expected_company_name = expected_company_name.lower()

    def extract(self, file_path: str) -> Optional[str]:
        reader = PDFReader(file_path)

        # Define an area from 10% to 30% of the height of the first page
        try:
            page = reader.doc[0]
            rect = fitz.Rect(0, page.rect.height * 0.1, page.rect.width, page.rect.height * 0.3)
            text_in_area = reader.read_text_in_area(0, rect)  # Reading text from the field
            if text_in_area:
                return ' '.join(text_in_area.split('\n')).strip()
        except Exception as e:
            print(f"Error extracting company name: {e}")

        return None




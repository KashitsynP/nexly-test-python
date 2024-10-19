from datetime import datetime
from typing import Optional

from src.validators.abstract_validator import AbstractValidator


class DateValidator(AbstractValidator):
    def __init__(self, expected_date: str):
        self.expected_date = expected_date

    def validate(self, extracted_date: Optional[str]) -> bool:
        if not extracted_date:
            return False

        # Defining formats for date parsing
        date_formats = [
            "%B %d, %Y",  # December 31, 2023
            "%d %B %Y",   # 31 December 2023
            "%Y-%m-%d",   # 2023-12-31
            "%d/%m/%Y",   # 31/12/2023
            "%d-%m-%Y"    # 31-12-2023
        ]

        # Expected date in YYYY-MM-DD format
        try:
            expected_date_parsed = datetime.strptime(self.expected_date, "%Y-%m-%d")
        except ValueError:
            print(f"Error: Expected date format should be YYYY-MM-DD.")
            return False

        # An attempt to parse the actual date in various formats
        for date_format in date_formats:
            try:
                extracted_date_parsed = datetime.strptime(extracted_date, date_format)
                # If the dates match, returned True
                if expected_date_parsed == extracted_date_parsed:
                    return True
            except ValueError:
                continue  # Moving on to the next format if it was not possible to parse

        return False

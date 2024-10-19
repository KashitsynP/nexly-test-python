from typing import Optional

from src.validators.abstract_validator import AbstractValidator


class CompanyNameValidator(AbstractValidator):
    def __init__(self, expected_company_name: str):
        self.expected_company_name = expected_company_name

    def validate(self, extracted_company_name: Optional[str]) -> bool:
        if not extracted_company_name:
            return False
        # Case-insensitive verification of the company name has been implemented
        return self.expected_company_name.lower() == extracted_company_name.lower()

from typing import Optional

from src.extractors.company_name_extractor import CompanyNameExtractor
from src.extractors.date_extractor import DateExtractor
from src.validators.company_name_validator import CompanyNameValidator
from src.validators.date_validator import DateValidator


class Pipeline:
    def __init__(self, company_name: str, date: str):
        self.company_name = company_name
        self.date = date

    def run(self, file_path: str) -> None:
        # Extraction stages
        extracted_company_name: Optional[str] = CompanyNameExtractor(self.company_name).extract(file_path)
        extracted_date: Optional[str] = DateExtractor(self.date).extract(file_path)

        # Validation stages
        company_name_validation: bool = CompanyNameValidator(self.company_name).validate(extracted_company_name)
        date_validation: bool = DateValidator(self.date).validate(extracted_date)

        # Output of results
        if company_name_validation:
            print("\033[32m[\u2713] Company name validation passed.\033[0m")
        else:
            print(f"\033[31m[-] Company name validation failed: expected '{self.company_name}', found '{extracted_company_name}'.\033[0m")

        if date_validation:
            print("\033[32m[\u2713] Date validation passed.\033[0m")
        else:
            print(f"\033[31m[-] Date validation failed: expected '{self.date}', found '{extracted_date}'.\033[0m")

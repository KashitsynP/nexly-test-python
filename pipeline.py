import argparse
from src.pipeline import Pipeline
from src.reader import PDFReader


def main():
    # Configuring command line argument parsing
    parser = argparse.ArgumentParser(description="PDF Data Extraction and Validation Pipeline")
    parser.add_argument('--company_name', required=True, help="Expected company name to validate")
    parser.add_argument('--date', required=True, help="Expected date to validate (format: YYYY-MM-DD)")

    file_path = 'data/report.pdf'
    args = parser.parse_args()

    reader = PDFReader(file_path)
    if not reader.is_valid():
        return  # Stop further execution if the file is not open

    # Starting the pipeline with the specified parameters
    pipeline = Pipeline(company_name=args.company_name, date=args.date)
    pipeline.run(file_path=file_path)


if __name__ == "__main__":
    main()

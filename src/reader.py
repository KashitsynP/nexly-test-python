from typing import Optional

import fitz


class PDFReader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.doc = None
        try:
            self.doc = fitz.open(file_path)
        except fitz.FileNotFoundError:
            print(f"Error: The file {self.file_path} was not found.")
            return None
        except Exception as e:
            print(f"Error opening PDF file: {e}")

    def is_valid(self) -> bool:
        """
        Checks whether the document has been opened successfully.
        :return: True if the document is open, otherwise False.
        """
        return self.doc is not None

    def read_first_page(self) -> Optional[str]:
        """
        Extracts the entire text from the first page of the PDF.
        :return: A string of text or None in case of an error.
        """
        try:
            page = self.doc[0]  # Reading the first page
            return page.get_text("text")
        except fitz.FileDataError:
            print(f"Error: The file {self.file_path} is not a valid PDF.")
            return None
        except Exception as e:
            print(f"Error reading first page: {e}")
            return None

    def read_text_in_area(self, page_number: int, rect: fitz.Rect) -> Optional[str]:
        """
        Extracts text from the specified area on the specified page
        :param page_number: The number of the page to read;
        :param rect: Rectangular area for text extraction.
        :return: A string of text from the specified area, or None in case of an error.
        """
        try:
            page = self.doc[page_number]
            return page.get_text("text", clip=rect)
        except Exception as e:
            print(f"Error reading text in area: {e}")
            return None

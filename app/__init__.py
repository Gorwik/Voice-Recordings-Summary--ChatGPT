from .create_summarize import summarize_all_records
from .pdf_maker import create_pdf_from_text_files


def main():
    summarize_all_records()
    create_pdf_from_text_files()

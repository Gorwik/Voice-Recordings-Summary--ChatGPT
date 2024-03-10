from fpdf import FPDF
import os
from unidecode import unidecode
import textwrap

from app.setting import INPUT_FOLDER, OUTPUT_FILE


class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Records summarize", 0, 1, "C")

    def chapter_title(self, num, label):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, f"Record {num} - {label}", 0, 1, "C")
        self.ln(5)

    def chapter_body(self, content):
        self.set_font("Arial", "", 12)
        self.multi_cell(0, 10, content)
        self.ln(10)


def create_pdf_from_text_files():
    pdf = PDF()
    pdf.add_page()

    text_files = [f for f in os.listdir(INPUT_FOLDER) if f.endswith(".txt")]

    for idx, text_file in enumerate(text_files):
        file_path = os.path.join(INPUT_FOLDER, text_file)

        with open(file_path, "r") as file:
            content = file.read()

        content = unidecode(content)
        first_sentence = " ".join(content.split(" ")[:8])
        first_sentence = textwrap.wrap(first_sentence, width=80)

        paragraphs = textwrap.wrap(content, width=80)

        pdf.chapter_title(idx + 1, first_sentence)

        full_content = "\n".join(paragraphs)
        pdf.chapter_body(full_content)

    pdf.output(OUTPUT_FILE)


if __name__ == "__main__":
    create_pdf_from_text_files()

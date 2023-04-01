import os
import sys
from pdf2docx import Converter
import pypandoc

pypandoc.download_pandoc()

def convert_pdf_to_docx(input_pdf, output_docx):
    cv = Converter(input_pdf)
    cv.convert(output_docx, start=0, end=None)
    cv.close()

def convert_docx_to_epub(input_docx, output_epub):
    pypandoc.convert_file(input_docx, 'epub', outputfile=output_epub)

def convert_pdf_to_epub(input_pdf, output_epub):
    output_docx = 'temp.docx'

    convert_pdf_to_docx(input_pdf, output_docx)
    convert_docx_to_epub(output_docx, output_epub)

    os.remove(output_docx)

def main():
    if len(sys.argv) != 2:
        print("Usage: python pdf_to_epub.py <path_to_pdf>")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_epub = os.path.splitext(input_pdf)[0] + '.epub'

    convert_pdf_to_epub(input_pdf, output_epub)

if __name__ == '__main__':
    main()

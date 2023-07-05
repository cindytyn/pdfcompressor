# PDF Compressor

"I am not paying Adobe and I am not uploading my PDF files onto some random website for compression."

PDF Compressor is a Python application with a graphical user interface (GUI) built using the Tkinter library. It allows you to compress PDF files, reducing their file size while preserving the content.

## Features

- Select input PDF file to compress
- Choose output file location and name
- Compresses PDF pages by reducing content streams
- Reduces image quality to further reduce file size

## Requirements

- Python 3.x
- PyPDF2 library (install using `pip install PyPDF2`)
- Tkinter library (usually included with Python)

## Usage

1. Clone the repository or download the source code.

2. Install the required dependencies:
pip install PyPDF2

3. Run the application:
python compress_pdf.py

4. The application window will open. Click on the "Compress PDF" button.

5. In the file dialog, select the PDF file you want to compress.

6. Choose the location and name for the output file. The default extension is `.pdf`.

7. Click the "Save" button.

8. The compression process will begin, and the status will be displayed in the console.

9. Once the compression is completed, the console will display a success message.

10. The compressed PDF file will be saved at the location you specified.

## Additional Notes

- See PyPDF2 documentation under Lossless Compression section for the method used: https://pypdf2.readthedocs.io/en/3.0.0/user/file-size.html

- Image quality reduction: By default, the code reduces the image quality to a value of 50. You can modify the quality value in the code to achieve different levels of compression and image quality.

- Please note that this application was developed with the primary goal of achieving its intended purpose. It is important to be aware that extensive testing or consideration of edge cases may not have been conducted.

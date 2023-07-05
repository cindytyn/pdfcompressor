import tkinter as tk
from tkinter import filedialog
import PyPDF2
import os

def compress_pdf():
    # Select input PDF file
    input_file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if not input_file_path:
        return

    # Get the old filename
    input_filename = os.path.basename(input_file_path)

    # Select output PDF file
    output_file_path = filedialog.asksaveasfilename(filetypes=[("PDF Files", "*.pdf")],
                                                   defaultextension=".pdf",
                                                   initialfile="compressed.pdf")
    if not output_file_path:
        return

    # Get the new filename
    output_filename = os.path.basename(output_file_path)

    # Open the input PDF file
    input_pdf = open(input_file_path, 'rb')

    # Create a PDF writer object
    pdf_writer = PyPDF2.PdfWriter()

    # Read the input PDF file
    pdf_reader = PyPDF2.PdfReader(input_pdf)
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        # Compress the page content
        page.compress_content_streams()
        
        # Reduce image quality
        for obj in page['/Resources']:
            if page['/Resources'][obj].__class__.__name__ == '/XObject':
                if page['/Resources'][obj]['/Subtype'] == '/Image':
                    page['/Resources'][obj]['/ColorSpace'] = '/DeviceRGB'
                    page['/Resources'][obj]['/BitsPerComponent'] = 8
                    page['/Resources'][obj]['/Filter'] = '/DCTDecode'
                    page['/Resources'][obj]['/DecodeParms'] = {'/Quality': 50}  # Adjust image quality here
        
        # Add the compressed page to the writer object
        pdf_writer.add_page(page)

    # Write the compressed PDF to the output file
    with open(output_file_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

    # Close the input PDF file
    input_pdf.close()

    # Get the file sizes before and after compression
    input_file_size = os.path.getsize(input_file_path)
    output_file_size = os.path.getsize(output_file_path)

    status_label.configure(text="PDF compression completed successfully!")
    size_label.configure(text=f"Old Size: {input_file_size} bytes   New Size: {output_file_size} bytes")
    old_filename_label.configure(text=f"Old Filename: {input_filename}")
    new_filename_label.configure(text=f"New Filename: {output_filename}")


def main():
    window = tk.Tk()
    window.title("PDF Compressor")
    window.geometry("600x400")

    compress_button = tk.Button(window, text="Compress PDF", command=compress_pdf)
    compress_button.pack(pady=20)

    global status_label
    status_label = tk.Label(window, text="")
    status_label.pack()

    global size_label
    size_label = tk.Label(window, text="")
    size_label.pack()

    global old_filename_label
    old_filename_label = tk.Label(window, text="")
    old_filename_label.pack()

    global new_filename_label
    new_filename_label = tk.Label(window, text="")
    new_filename_label.pack()

    window.mainloop()


if __name__ == "__main__":
    main()

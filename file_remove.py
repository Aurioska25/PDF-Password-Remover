import pikepdf

def unlock_pdf(input_pdf, output_pdf, password):
    try:
        # Open the encrypted PDF with pikepdf
        with pikepdf.open(input_pdf, password=password) as pdf:
            # Save the unlocked PDF to the specified output file
            pdf.save(output_pdf)
            print(f"PDF unlocked successfully! Saved as {output_pdf}.")
    
    except pikepdf._qpdf.PasswordError:
        print("Failed to decrypt PDF. Incorrect password.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    input_pdf = "your_pdf_name.pdf"  # Name of the password-protected PDF file
    output_pdf = "unlocked.pdf"  # Name of the output PDF file without the password
    password = "Your_password"  # The password for the PDF

    unlock_pdf(input_pdf, output_pdf, password)

import openai, os, textwrap
from reportlab.pdfgen import canvas
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def convert_to_pdf(letter, output_file_path, address, company_name, location, postal_code):
    # create PDF object
    c = canvas.Canvas(output_file_path)

    today = datetime.today()
    date_string = today.strftime("%B %d, %Y")
   
    c.setFont('Times-Roman', 12)

    # split text into paragraphs
    paragraphs = letter.split('\n\n')
    
    # set the starting position
    y = 750
    # write date, address, company name, location/postal code
    c.drawString(36, y, f"{date_string}")
    y -= 30
    c.drawString(36, y, f"{company_name}")
    y -= 20
    c.drawString(36, y, f"{address}")
    y -= 20
    c.drawString(36, y, f"{location}" + " " + f"{postal_code}")
    y -= 30
    
    # write each paragraph
    for paragraph in paragraphs:
        # wrap text to fit within margins
        wrapper = textwrap.TextWrapper(width=95)
        wrapped_lines = wrapper.wrap(paragraph)
        # write each line of text
        for line in wrapped_lines:
            c.drawString(36, y, line) # 72 = 1 inch margins (36 for 0.5)
            y -= 20  # add newline between lines
        # add new line between paragraphs
        y -= 20
    # save PDF and close canvas
    c.save()

def generate_letter(name, company, job_title, job_type, term, term_length):
    letter = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user", 
            "content": f"Write me a cover letter for a {job_type} {job_title} for {term} at {company} for {term_length} do not include a address boiler template, sincerely -{name}"
        }]
    )
    # returns GPT's response
    return letter.choices[0].message.content

# ask the user for job information
name = input("Enter your First and Last name: ")
company_name = input("Enter the company you are applying to: ")
address = input("Enter the company's address: ")
location = input("Enter the company's location: ")
postal_code = input("Enter the company's postal code: ")
job_title = input("Enter the role you are applying for: ")
job_type = input("What type of job is it? (i.e Internship, Full-Time, Part-time?) ")

if job_type.lower() == "internship":
    term = input("Enter the term: (i.e Summer '23) ")
    term_length = input("Enter the term-length (i.e 4 months): ")
else:
    term = ""
    term_length = ""

print("\nGenerating Cover Letter...\n")

# Generates the cover letter
letter = generate_letter(name, company_name, job_title, job_type, term=term, term_length=term_length)

# file name format
output_file_path = f'{name}_{company_name}_{job_title}_{term}.pdf'
output_file_path = output_file_path.replace(' ', '') # remove spaces


# Convert the letter to PDF
convert_to_pdf(letter, output_file_path, address, company_name, location, postal_code)

# Save cover letter to current directory
print(f"Cover Letter saved to '{os.path.abspath(output_file_path)}'")


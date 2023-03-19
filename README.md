# cover_letter_generator

Python script that utilizes Open AI's API to generate custom cover letters. Cover letter is generated after the user enters job/company's information

# Installation

Ensure Python3 is installed on your local machine

# Usage

Receive your API Key from https://platform.openai.com/account/api-keys

Add your API Key to your .env file

```
OPENAI_API_KEY = "YOURAPIKEY"
```

Install the required packages 

reportlab
``` 
pip install reportlab
```

dotenv
```
pip install python-dotenv
```

OpenAI
```
pip install openai
```

# To Run
```python

cd src

python3 cv_generator.py
```

# Sample Output

```
Enter your First and Last name: Andrew Chow
Enter the company you are applying to: Google
Enter the company's address: Street 123
Enter the company's location: Toronto, ON
Enter the company's postal code: ABC 123
Enter the role you are applying for: Software Engineer
What type of job is it? (i.e Internship, Full-Time, Part-time?) Internship
Enter the term: (i.e Summer '23) Summer 2023
Enter the term-length (i.e 4 months): 4 months

Generating Cover Letter...

Cover Letter saved to '../AndrewChow_Google_SoftwareEngineer_Summer2023.pdf'
```

![Screenshot 2023-03-18 at 11 49 28 PM](https://user-images.githubusercontent.com/40132839/226152514-524685ef-f9c9-484a-a89f-babc0485a0b1.png)


# Next Steps

1. Implement user-friendly GUI
2. Input user's experiences and skills to create more detailed/personal letters








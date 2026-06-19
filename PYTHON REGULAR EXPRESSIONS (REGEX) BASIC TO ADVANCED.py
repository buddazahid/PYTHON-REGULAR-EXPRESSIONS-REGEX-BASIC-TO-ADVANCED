# ========================================================
#     PYTHON REGULAR EXPRESSIONS (REGEX)
#              BASIC TO ADVANCED
# ========================================================

# Regex:
#
# Regular Expressions are used for:
#
# 1. Pattern Matching
# 2. Data Validation
# 3. Searching Text
# 4. Replacing Text
# 5. Data Cleaning
#
# Module Used:
#
# re
#
# ========================================================


# ========================================================
#           IMPORT REGEX MODULE
# ========================================================

import re

print("Regex Module Imported")


# ========================================================
#           SIMPLE SEARCH
# ========================================================

text = "Python is powerful"

result = re.search(

    "Python",

    text
)

print("\nSearch Result")

print(result)


# ========================================================
#           FIND MATCH
# ========================================================

if result:

    print("Match Found")

else:

    print("Match Not Found")


# ========================================================
#           FIND ALL MATCHES
# ========================================================

text = "Python Java Python PHP Python"

result = re.findall(

    "Python",

    text
)

print("\nFind All")

print(result)


# ========================================================
#           SPLIT STRING
# ========================================================

text = "Python,Java,PHP,C++"

result = re.split(

    ",",

    text
)

print("\nSplit")

print(result)


# ========================================================
#           SUBSTITUTE TEXT
# ========================================================

text = "I love Java"

result = re.sub(

    "Java",

    "Python",

    text
)

print("\nReplace")

print(result)


# ========================================================
#           MATCH FROM START
# ========================================================

text = "Python Programming"

result = re.match(

    "Python",

    text
)

print("\nMatch Start")

print(result)


# ========================================================
#           DOT CHARACTER
# ========================================================

text = "cat bat mat"

result = re.findall(

    ".at",

    text
)

print("\nDot Character")

print(result)


# ========================================================
#           DIGITS
# ========================================================

text = "My Number is 9876543210"

result = re.findall(

    r"\d",

    text
)

print("\nDigits")

print(result)


# ========================================================
#           MULTIPLE DIGITS
# ========================================================

result = re.findall(

    r"\d+",

    text
)

print("\nFull Number")

print(result)


# ========================================================
#           ALPHABETS
# ========================================================

text = "Python123"

result = re.findall(

    r"[A-Za-z]+",

    text
)

print("\nAlphabets")

print(result)


# ========================================================
#           ONLY LOWERCASE
# ========================================================

text = "Python java PHP"

result = re.findall(

    r"[a-z]+",

    text
)

print("\nLowercase")

print(result)


# ========================================================
#           ONLY UPPERCASE
# ========================================================

result = re.findall(

    r"[A-Z]+",

    text
)

print("\nUppercase")

print(result)


# ========================================================
#           WORDS
# ========================================================

text = "Python is easy"

result = re.findall(

    r"\w+",

    text
)

print("\nWords")

print(result)


# ========================================================
#           SPACES
# ========================================================

text = "Python Java PHP"

result = re.findall(

    r"\s",

    text
)

print("\nSpaces")

print(result)


# ========================================================
#           STARTS WITH
# ========================================================

text = "Python"

result = re.findall(

    r"^P",

    text
)

print("\nStarts With P")

print(result)


# ========================================================
#           ENDS WITH
# ========================================================

result = re.findall(

    r"n$",

    text
)

print("\nEnds With n")

print(result)


# ========================================================
#           EMAIL VALIDATION
# ========================================================

email = "zahid@gmail.com"

pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

if re.match(pattern, email):

    print("\nValid Email")

else:

    print("\nInvalid Email")


# ========================================================
#           PHONE NUMBER VALIDATION
# ========================================================

phone = "9876543210"

pattern = r"^[0-9]{10}$"

if re.match(pattern, phone):

    print("Valid Phone Number")

else:

    print("Invalid Phone Number")


# ========================================================
#           PASSWORD VALIDATION
# ========================================================

password = "Python@123"

pattern = (

    r"^(?=.*[A-Z])"

    r"(?=.*[a-z])"

    r"(?=.*\d)"

    r"(?=.*[@#$%^&+=])"

    r".{8,}$"
)

if re.match(pattern, password):

    print("Strong Password")

else:

    print("Weak Password")


# ========================================================
#           EXTRACT EMAILS
# ========================================================

text = """

zahid@gmail.com

admin@yahoo.com

test@outlook.com

"""

emails = re.findall(

    r"[a-zA-Z0-9._%+-]+"

    r"@[a-zA-Z0-9.-]+"

    r"\.[a-zA-Z]{2,}",

    text
)

print("\nEmails")

print(emails)


# ========================================================
#           EXTRACT NUMBERS
# ========================================================

text = "Marks: 85, 90, 78, 95"

numbers = re.findall(

    r"\d+",

    text
)

print("\nNumbers")

print(numbers)


# ========================================================
#           EXTRACT URL
# ========================================================

text = """

https://google.com

https://github.com

"""

urls = re.findall(

    r"https?://[^\s]+",

    text
)

print("\nURLs")

print(urls)


# ========================================================
#           REMOVE SPECIAL CHARACTERS
# ========================================================

text = "Python@#123!!"

clean = re.sub(

    r"[^A-Za-z0-9]",

    "",

    text
)

print("\nClean Text")

print(clean)


# ========================================================
#           REMOVE EXTRA SPACES
# ========================================================

text = "Python     Java     PHP"

clean = re.sub(

    r"\s+",

    " ",

    text
)

print("\nRemove Extra Spaces")

print(clean)


# ========================================================
#           STUDENT USN VALIDATION
# ========================================================

usn = "4BY23CA001"

pattern = r"^[0-9][A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{3}$"

if re.match(pattern, usn):

    print("\nValid USN")

else:

    print("\nInvalid USN")


# ========================================================
#           VEHICLE NUMBER VALIDATION
# ========================================================

vehicle = "KA19AB1234"

pattern = r"^[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}$"

if re.match(pattern, vehicle):

    print("\nValid Vehicle Number")

else:

    print("\nInvalid Vehicle Number")


# ========================================================
#           REAL WORLD EXAMPLE
#           RESUME EMAIL EXTRACTOR
# ========================================================

resume = """

Mohammed Zahid

Email: zahid@gmail.com

Phone: 9876543210

"""

emails = re.findall(

    r"[a-zA-Z0-9._%+-]+"

    r"@[a-zA-Z0-9.-]+"

    r"\.[a-zA-Z]{2,}",

    resume
)

print("\nResume Emails")

print(emails)


# ========================================================
#           REAL WORLD EXAMPLE
#           LOG FILE ANALYSIS
# ========================================================

log = """

ERROR 101

ERROR 205

ERROR 500

"""

errors = re.findall(

    r"\d+",

    log
)

print("\nError Codes")

print(errors)


# ========================================================
#           PROGRAM END
# ========================================================

# Important Regex Symbols:
#
# .      Any Character
# ^      Start
# $      End
# *      Zero or More
# +      One or More
# ?      Optional
# []     Character Set
# {}     Number of Occurrences
# \d     Digit
# \D     Non-Digit
# \w     Word
# \W     Non-Word
# \s     Space
# \S     Non-Space
#
# Important Functions:
#
# re.search()
# re.match()
# re.findall()
# re.split()
# re.sub()
#
# Applications:
#
# - Email Validation
# - Password Validation
# - Phone Validation
# - Data Cleaning
# - Resume Parsing
# - Web Scraping
# - Data Science
# - AI Projects
#
# ========================================================
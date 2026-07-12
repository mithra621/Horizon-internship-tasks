import re

# Read the input file
with open("input.txt", "r") as file:
    text = file.read()

# Regular expression to find email addresses
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

# Save extracted emails
with open("extracted_emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Email Extraction Completed!")
print(f"Total Emails Found: {len(emails)}")

print("\nExtracted Emails:")
for email in emails:
    print(email)
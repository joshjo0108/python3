# EX) SCRAPPING DATA FROM EMAIL

with open('emails.txt','r') as emails:
    emails = emails.readlines()    # STORES EACH LINE AS AN ARRAY

for email in emails:
    if "hotmail"  not in email:
        print("Looking for a email account except for hotmail")
        print(email.rstrip())       # REMOVING '\n' :  WILL MAKE A SPACE IN EACH print()
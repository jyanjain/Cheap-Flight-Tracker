import requests 
import sheety



print("Welcome to the FLight CLub")
print("We find the best Flight deals and email you")

first_name = input("What's your first name?\n").title()

last_name = input("What's your last name?\n").title()

email1 = "email1"
email2 = "email2"
while email1 != email2:
    email1 = input("What is your email? ")
    if email1.lower() == "quit" \
            or email1.lower() == "exit":
        exit()
    email2 = input("Please verify your email : ")
    if email2.lower() == "quit" \
            or email2.lower() == "exit":
        exit()
    
print("You're in CLub")

sheety.post_new_rows(first_name, last_name, email1)
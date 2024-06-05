import re

email = input("what's your email: ")
if re.search(r"^\w+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):
     print("valid")
else:
    print("invalid")

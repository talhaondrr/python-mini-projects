email = input("Enter your email: ")

if "@" in email:
    username, domain = email.split("@")

    print(f"Username: {username}")
    print(f"Domain: {domain}")
else:
    print("Geçersiz e-posta adresi!")
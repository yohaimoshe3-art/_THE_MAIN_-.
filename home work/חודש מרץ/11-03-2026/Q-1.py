name = input("Enter name: ")
email = input("Enter email: ")
phone = input("Enter phone: ")
job_title = input("Enter job title: ")

person = {
    "name": name,
    "email": email,
    "phone": phone,
    "job_title": job_title
}
print(person)

print("\n--- Business Card ---")
print(f"Name: {person['name']}")
print(f"Email: {person['email']}")
print(f"Phone: {person['phone']}")
print(f"Job Title: {person['job_title']}")
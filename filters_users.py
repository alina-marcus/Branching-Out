import json

def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)

def filter_users_by_age(age):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["age"] == age]

    for user in filtered_users:
        print(user)

def filter_users_by_email(email):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"] == email]

    for user in filtered_users:
        print(user)

if __name__ == "__main__":
    filter_option = input("What would you like to filter by? Type 'age', 'email' or 'name': ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        while True:
            try:
                age_to_search = int(input("Enter age to filter users: ").strip())
                filter_users_by_age(age_to_search)
                break
            except ValueError:
                print("Please enter a number.")
    elif filter_option == "email":
        while True:
            email_to_search = input("Enter an email to filter users: ").strip()
            if "@" not in email_to_search:
                print("Please enter a valid email address.")
            elif "." not in email_to_search:
                print("Please enter a valid email address.")
            else:
                break
        filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")
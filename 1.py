###############  Useriniput #############

username = input("Enter your name :")
location = input("Enter your location :- ")
# This "f" string format is using only ver 3.6 or later
user_message = f"Hi {username}! and you are located in {location}"

print(user_message.title())

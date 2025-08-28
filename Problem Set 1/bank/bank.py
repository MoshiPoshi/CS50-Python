# define user input
def get_user_input():
    user_input = input("Greeting: ").strip().lower()
    return user_input

# compare the user input with our goal
user_input = get_user_input()
if user_input.startswith("hello"):
    print("$0")
elif user_input.startswith("h"):
    print("$20")
else:
    print("$100")
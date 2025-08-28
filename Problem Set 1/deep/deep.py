# define the user input
def get_user_input():
    user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
    return user_input

# compare the user input 
user_input = get_user_input()
if user_input == "42":
    print("Yes")
elif user_input == "forty-two":
    print("Yes")
elif user_input == "forty two":
    print("Yes")
else:
    print("No")
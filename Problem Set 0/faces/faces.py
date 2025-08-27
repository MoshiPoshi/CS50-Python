# get the input from user
def convert(input_string):
    return input_string.replace(":)", "🙂").replace(":(", "🙁")

# print the converted emoji string
def main():
    print(convert(input()))

# call the main function
main()

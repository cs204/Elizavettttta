def convert(text):
    text = text.replace(":)", "🙂").replace(":(", "🙁")
    return text
def main():
    user_input = input("")
    converted_text = convert(user_input)
    print(converted_text)
main()



user_input = input("Какой ответ на главный вопрос жизни, вселенной и всего такого? ").lower()

match user_input:
    case "42" | "сорок два":
        print("Да")
    case _:
        print("Нет")

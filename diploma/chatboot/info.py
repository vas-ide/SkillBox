INTENTS = [
    {
        "name": "Date to inspect",
        "tokens": ("когда", "дата", "день", "", ""),
        "scenario": None,
        "answer": f"At your convenience",
        "idea": "",
    },
    {
        "name": "Place for pet inspection",
        "tokens": ("где", "место", "локация", "адрес", "улица", "дом"),
        "scenario": None,
        "answer": f"Eysk city, Rostovskay street №___",
        "idea": "",
    },
    {
        "name": "Coast",
        "tokens": ("стоит", "", "", "", ""),
        "scenario": None,
        "answer": f"Initial examination by a pet doctor about 10 dollars",
        "idea": "",
    },
    {
        "name": "Registration",
        "tokens": ("регистрация", "авторизация", "добавить", "зайти", ""),
        "scenario": f"registration",
        "answer": None,
        "idea": "",
    },
    {
        "name": "Example",
        "tokens": ("", "", "", "", ""),
        "scenario": None,
        "answer": f"",
        "idea": "",
    },
]

SCENARIOS = {
    "registration": {
        "first_step": "step1",
        "step1": {
            "text": "Для регистрации введите имя.",
            "failure_text": "Вы введи непраильное(менее 5 или более 35 символов) имя или имя которого не существует",
            "handler": "handle_name",
            "next_step": "step2",
        },
        "step2": {
            "text": "Введите ваш Email. Для обратной связи",
            "failure_text": "Неправильный адрес. Проверьте и введите еще раз.",
            "handler": "handler_email",
            "next_step": "step3",
        },
        "step3": {
            "text": "Congratulation {name} we send details to {email}",
            "failure_text": None,
            "handler": None,
            "next_step": None,
        },
        "step4": {
            "text": "",
            "failure_text": "",
            "handler": "",
            "next_step": "",
        },
        "step5": {
            "text": "",
            "failure_text": "",
            "handler": "",
            "next_step": "",
        },
    }
}

DEFAULT_ANSWER = "Please tell me about you problem and we try to solve it or inform you how avoid issue"


dict_questions = {
    "hello": "How are you?",
    "date": "Today's date",

    "problem": "Please tell me about you problem.",
    "describe": "Describe your problem.",

    "what": "We didn't catch you question",
    "why": "We didn't have full information to analyze your issue",

    "pet": "Please chose a category you pets",
    "cat": "What is the problem with you Cat?",
    "dog": "What is the problem with you Dog?",

}

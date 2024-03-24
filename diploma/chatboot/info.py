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
            "text": "",
            "failure_text": "",
            "handler": "",
            "next_step": "",
        },
        "step2": {
            "text": "",
            "failure_text": "",
            "handler": "",
            "next_step": "",
        },
        "step3": {
            "text": "",
            "failure_text": "",
            "handler": "",
            "next_step": "",
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

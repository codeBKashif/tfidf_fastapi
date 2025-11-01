def tokenize(text: str) -> list[str]:
    return [word.strip().lower() for word in text.split() if word.isalpha()]
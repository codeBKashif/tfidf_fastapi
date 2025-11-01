def tokenize(text: str) -> list[str]:
    remainder = ""
    words = text.split()
    
    if words[-1].isspace():
        remainder = ""
    else:
        remainder = words.pop() if words else ""

    return [word.strip().lower() for word in words if word.isalpha()], remainder
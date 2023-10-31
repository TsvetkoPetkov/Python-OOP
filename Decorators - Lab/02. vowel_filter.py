def vowel_filter(function):
    VOWELS = "auoeiy"

    def wrapper():
        return [ch for ch in function() if ch in VOWELS]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())

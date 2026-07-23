def sentence_maker(phrase):
    interrogatives = ("how", "why", "what", "where")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return f"{capitalized}?"
    elif phrase.endswith("?"):
        return f"{capitalized}"
    elif phrase.endswith("."):
        return f"{capitalized}"
    else:
        return f"{capitalized}."
    

result = []

while True:
    mySentence = input("Say Something: ")
    if mySentence == r"\end":
        break
    else:
        result.append(sentence_maker(mySentence))
print(" ".join(result))
for sentence in result:
    print(" ".join(sentence))
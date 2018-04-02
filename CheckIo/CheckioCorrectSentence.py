def correct_sentence(sentence):

    text = text.capitalize()
    if text[-1] != ".":
        text = text + "."

#correct_sentence = lambda t: t.capitalize() + "." * (t[-1]!=".")
print(correct_sentence("greetings, friends"))# == "Greetings, friends."
print(correct_sentence("Greetings, friends"))# == "Greetings, friends."
print(correct_sentence("Greetings, friends."))# == "Greetings, friends."
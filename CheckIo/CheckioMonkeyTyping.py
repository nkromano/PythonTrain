def count_words(monkey, word):
  return len(list(filter(lambda x: monkey.lower().count(x) > 0, word)))
  #return sum([1 for w in words if w in text.lower()])

print(count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}))# == 3
print(count_words("Bananas, give me bananas!!!", {"banana", "bananas"}))# == 2
print(count_words("Lorem Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",{"sum", "hamlet", "infinity", "anything"}))# == 1


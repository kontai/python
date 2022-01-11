word = "letter"
spell_word = {letter: word.count(letter) for letter in word}
print(spell_word)

spell_word = {letter: word.count(letter) for letter in set(word)}
print(spell_word)
print(set(word))

getnerator_list=(x for x in range(10))
print(type(getnerator_list))
print(list(getnerator_list))
print(list(getnerator_list))

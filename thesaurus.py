thesaurus = {}
base_word = input('Enter the base word: ')
similar_word = input('Enter a similar word: ')
if base_word in thesaurus:
    thesaurus[base_word].add(similar_word)
else:
    thesaurus[base_word] = {similar_word}
new_var = thesaurus
print(new_var)
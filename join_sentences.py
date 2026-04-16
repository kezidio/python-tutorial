


list_of_sentences = [['I think', 'today is', 'a really', 'good', 'day.'], \
                     ['Apples might not', 'be my', 'favorite', 'fruit.']]

def join_sentence(list_of_sentences, index):
    sentence = " ".join(list_of_sentences[index])
    return sentence

#First list index 0 like the first element of an array
first_sentence = join_sentence(list_of_sentences, 0)
print(first_sentence)

#second list has index 1 like the second element of an array
second_sentence = join_sentence(list_of_sentences, 1)
print(second_sentence)

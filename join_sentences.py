


list_of_sentences = [['I thibk', ' today is', 'a really', 'good', 'day.'], \
                     ['Apples might not', 'be my', 'favorite', 'fruit.']]

def join_sentence(list_of_sentences, index):
    sentence = " ".join(list_of_sentences[index])
    return sentence

first_sentence = join_sentence(list_of_sentences, 0)
print(first_sentence)

second_sentence = join_sentence(list_of_sentences, 1)
print(second_sentence)

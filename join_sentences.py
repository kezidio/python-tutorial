#This program stores groups of words in a list inside a list and turns them into full sentences.
#Each inner list holds parts of a sentence. The function join_sentence takes one of those inner 
#lists (using an index) and joins the words together into a single string with spaces in between.

#create a list of lists to store the words or sentences
list_of_sentences = [['I think', 'today is', 'a really', 'good', 'day.'], \
                     ['Apples might not', 'be my', 'favorite', 'fruit.']]

#define a function with 2 parameters to join the elements of a given inner list
def join_sentence(list_of_sentences, index): #the function takes the list of list as a parameter as well as an index number
    sentence = " ".join(list_of_sentences[index])
    return sentence #it then returns the full sentence

#First inner list index is 0 like the first element of an array
first_sentence = join_sentence(list_of_sentences, 0)
print(first_sentence) #display sentence

#second list has index 1 like the second element of an array
second_sentence = join_sentence(list_of_sentences, 1)
print(second_sentence)

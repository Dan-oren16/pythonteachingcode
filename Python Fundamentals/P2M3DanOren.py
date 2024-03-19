# [] create poem mixer function, call the function with the provided test string
# [] test string: `Little fly, Thy summer’s play My thoughtless hand Has brushed away. Am not I A fly like thee? Or art not thou A man like me?`  
full_name = "Dan Oren"

# Define the word_mixer function
def word_mixer(word_list):
    new_words = []
    word_list.sort()
    while len(word_list) > 5: 
        new_words.append(word_list.pop(-5))
        new_words.append(word_list.pop(0))
        new_words.append(word_list.pop())
    else: 
        return new_words
    
# Program Flow 
user_input = input("Welcome " + full_name + ", enter a saying or poem: ")
words_list = user_input.split()
lenght = len(words_list)

for word in range(lenght):
    if len(words_list[word]) <= 3:
        words_list[word] = words_list[word].lower()
    elif len(words_list[word]) >= 7: 
        words_list[word] = words_list[word].upper()
    else: 
        pass 
print(" ".join(word_mixer(words_list)))
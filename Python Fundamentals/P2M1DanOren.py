# [] create words after "G" following the Assignment requirements use of functions, menhods and kwyowrds
# Sample quote: "Wheresoever you go, go with all your heart" ~ Confucius (551 BC - 479 BC)
full_name = "Dan Oren"
word = ""
quote = input("Welcome, " + full_name +". Enter a one sentence quote that inspires you: ")
for ltr in quote:
    if ltr.isalpha():
        word += ltr
    else:
        if word.lower() >= "h":
            print(word.upper())
            word = ""
        else:
            word = ""

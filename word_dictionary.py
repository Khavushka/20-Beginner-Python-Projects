# word dictionary using Python
# have a python dictionary 
#that has a key/value pair that represents a word and it's definition
# collect input from the user, input is a word
# print the definition

def main():
    word_dictionary = {
        'hi': 'A way of greeting',
        'eyes': 'an organ for seeing',
        'earth': 'a planet in space'
    }

    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        if word in word_dictionary:
            print(word, ":", word_dictionary)

main()
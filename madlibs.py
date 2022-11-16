# string concatination
word = "hello"

print("this is my word: " + word)
print("this is my word: {}".format(word))
print(f"this is my word: {word}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"
print(madlib)

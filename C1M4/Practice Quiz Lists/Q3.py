def pig_latin(text):
    say = "ay"
    # Separate the text into words
    words = text.split()
    pig = []
    for word in words:
        # Create the pig latin word and add it to the list
        word = word[1::] + word[0] + say
        pig.append(word)

        # Turn the list back into a phrase
    pig = " ".join(pig)
    return pig

print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"
VOWELS = "aeiouyAEIOUY"


# Converts any english word into a pig latin language
def convert_to_pig_latin(word):
    if word[0] in VOWELS:
        return word + "yay"
    elif len(word) == 1:
        return word + "ay"
    consonant_cluster = word[0]     # Storing consonant cluster data f.e. gr or ch
    for letter in word[1:]:
        if letter in VOWELS:
            return word[len(consonant_cluster):] + consonant_cluster + "ay"
        else:
            consonant_cluster += letter


if __name__ == "__main__":
    sentence = input("Enter the sentence to convert into pig latin: ")
    converted_list = [convert_to_pig_latin(word) for word in sentence.strip().split()]
    converted = " ".join(converted_list)
    print(f"Sentence in pig latin: {converted}")

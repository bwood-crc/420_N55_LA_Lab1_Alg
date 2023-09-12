import re

def find_average(input_phrase: str):
    input_phrase = re.sub(r'[^A-Za-z0-9 ]+', '', input_phrase)
    words = input_phrase.split()
    num_letters = sum([len(x) for x in words])
    num_words = len(words)
    return num_letters / num_words


sample = "The quick brown fox jumped over the lazy dog."
print(find_average(sample))

sample = "The quick brown fox jumped over the lazy dog"
print(find_average(sample))

sample = "The quick brown fox            jumped over the lazy dog."
print(find_average(sample))

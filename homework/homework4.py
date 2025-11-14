def string_to_list(words_str):
    return words_str.split()

def word_occurrence_dict(lyrics):
    words = string_to_list(lyrics)
    word_positions = {}

    for i in range(len(words)):
        word = words[i]
        if word in word_positions:
            word_positions[word].append(i)
        else:
            word_positions[word] = [i]

    return word_positions

print(string_to_list("imagine all the people living life in peace"))

print(string_to_list("hello world python"))

print(string_to_list(""))

some_lyrics = "never gonna give you up never gonna let you down never gonna run around and desert you"
print(word_occurrence_dict(some_lyrics))

test_lyrics = "the cat in the hat"
print(word_occurrence_dict(test_lyrics))

empty_lyrics = ""
print(word_occurrence_dict(empty_lyrics))
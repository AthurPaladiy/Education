def has_common_part(word1, word2):
    word1, word2 = word1.lower(), word2.lower()
    return (
            word1.startswith(word2) or word1.endswith(word2) or
            word2.startswith(word1) or word2.endswith(word1) or
            word1 in word2 or word2 in word1
    )


def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if has_common_part(root_word, word):
            same_words.append(word)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)

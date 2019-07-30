# Is an anonymous letter constructible?

# Prompt: 
# -> A program that takes text from an anonymous letter and text from a magazine
# -> Determines if it is possible to write the letter using the magazine
# -> The letter can be written using the magazine if for each character in the letter, the number of times it appears in the letter is no more than that of the magazine

import collections


# Time: O(n + m); n - number of letter's chars; m - number of magazine's chars
# Space: O(c) - number of unique chars

def is_letter_constructible_from_magazine_v1(letter_text, magazine_text):
    # Conpute the frequencies for all chars in letter_text.
    char_frequency_for_letter = collections.Counter(letter_text)
    # Checks if characters in magazine_text can cover characters in char_frequency_for_letter.
    for c in magazine_text:
        if c in char_frequency_for_letter:
            char_frequency_for_letter[c] -= 1
            if char_frequency_for_letter[c] == 0:
                del char_frequency_for_letter[c]
                if not char_frequency_for_letter:
                    # All characters .for .letter_text are matched.
                    return True
    # Empty char_frequency_for_letter means every char in letter_text can be
    # covered by a character in magazine_text.
    return not char_frequency_for_letter

    

def is_letter_constructible_from_magazine_v2(letter_text, magazine_text):
    return not collections.Counter(letter_text) - collections.Counter(magazine_text)

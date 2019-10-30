#!/usr/bin/env python
# coding: utf-8

import argparse

value_dict = {1: ("A", "E", "I", "O", "U", "N", "R", "S", "T"),
              2: ("D", "G"),
              3: ("B", "C", "M", "P"),
              4: ("F", "H", "V", "W", "Y"),
              5: ("K"),
              8: ("J", "X"),
              10: ("Q", "Z")}

inv_map = {}
for k, v in value_dict.items():
    for letter in v:
        inv_map[letter.lower()] = k


def scrabble_score(word, value_dict, letter_multiplicator={}, word_multiplicator=1):
    score = 0
    length_word = len(word)

    if letter_multiplicator != {} and max(letter_multiplicator.keys()) >= length_word:
        raise ValueError(
            "The index of the doubled or tripled letter is incorrect.")
    if letter_multiplicator != {} and min(letter_multiplicator.keys()) <0:
        print("Warning: a negative index has been given for the letter multiplicator argument.")

    for i, let in enumerate(word):
        if i in letter_multiplicator and letter_multiplicator[i] in (2, 3):
            score += value_dict[let]*letter_multiplicator[i]
        elif i in letter_multiplicator and letter_multiplicator[i] not in (2, 3):
            raise ValueError(
                f"The letter multiplicator is not acceptable (only 2 or 3 are ok). {letter_multiplicator[i]} was given")
        else:
            score += value_dict[let]

    score *= word_multiplicator
    return score


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='Calculates the score of a word in Scrabble.')
    parser.add_argument('word', type=str,
                        help='the word to check')
    parser.add_argument('--word_multiplicator', type=int, default=1, choices=[1, 2, 3, 4, 9],
                        help='The word multiplicator')
    parser.add_argument('--letter_multiplicator', default=[], type=int, nargs=2, action='append',
                        help='The letter multiplicator in the format "index multiplicator". You can repeat this optional argument if you have several letters with a multiplicator.')

    args = parser.parse_args()
    letter_multiplicator = {}
    for element in args.letter_multiplicator:
        letter_multiplicator[element[0]] = element[1]

    score = scrabble_score(args.word, inv_map, letter_multiplicator=letter_multiplicator,
                           word_multiplicator=args.word_multiplicator)

    print(f"The score of {args.word} is {score}.")

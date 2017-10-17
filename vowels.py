#!/usr/bin/env python

def vowels(word):
    
    # return [True if char in 'aeiou' else False for char in word]
    is_vowel = lambda letter: letter in 'aeiou'
    for char in word:
        print char + "-"  + str(is_vowel(char))

vowels('encyclopedia')

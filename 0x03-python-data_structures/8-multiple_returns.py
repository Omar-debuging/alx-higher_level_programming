#!/usr/bin/python3
def multiple_returns(sentence):
    x = len(sentence)
    if x == 0:
        length = x
        first = None
    if x >= 1:
        length = x
        first = sentence[0]
    return (length, first)

#!/usr/bin/env python

import sys

test_strings = [
    'I', 
    'II',
    'IX',
    'IV',
    'MCMLXXXVII',
    'IM',
]

conversions = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000,
}

# Goal
# 'IM' -> ['D','CCCC','L','XXXX','V','IIII']

order = {
    'I' : 0,
    'V' : 1,
    'X' : 2,
    'L' : 3,
    'C' : 4,
    'D' : 5,
    'M' : 6,
}

order_list = ['I','V','X','L','C','D','M']


def tokenise( input_str ):
    """ Convert a string to baconical form """
    
    # .^
    # Is IVM allowed?

    # Compare pair wise
    # We are making the assumption there are no chains, eg:
    # I X L would be a chain of two ascending pairs (IX,XL)
    # In fact lets sanity check that

    for idx in range(len(input_str)-2):
        if order[input_str[idx]] < order[input_str[idx+1]]:
            if order[input_str[idx+1]] < order[input_str[idx+2]]:
                raise Exception("We don't support chained ascending pairs")
    
    # Now convert any ascending pairs into tokens
    output = []
    idx = 0
    while idx < len(input_str)-1:
        if order[input_str[idx]] < order[input_str[idx+1]]:
            # Ascending pair, replace with a token
            output += [input_str[idx] + input_str[idx+1]]
            idx += 2
        else:   
            # Not an ascending pair, just copy over the character
            output += [input_str[idx]]
            idx += 1

    if idx < len(input_str):
        output += [input_str[idx]]

    
    
    return output

def replace_token(token):
    if len(token) == 2:
        # Divide the value of the second character by the 
        # first, then use this to generate a number of 
        # output characters
        count = conversions[token[1]] / conversions[token[0]]
        return token[0] + (token[0] * count)
    return token

def replace_token2(token):
    """ Using integers, yes we're naughty """
    if len(token) == 2:
        value = conversions[token[1]] - conversions[token[0]]
        # We cannot go smaller than token[0] or we'll create more
        # ascending sequences, I think...
        
        # Lets generate out the values
        output = []
        while value > conversions[token[0]]:
            for key in order_list[::-1]:
                if value - conversions[key] > 0:
                    output += key
                    value -= conversions[key]
                    break
        output += token[0]
        return ''.join(output)
    else:
        return token
        
    

from canon import canon
from add import add

def tokenise_str(input_str):
    return ''.join([replace_token2(c) for c in tokenise(input_str)])
    

if __name__ == '__main__':
    
    if len(sys.argv) == 1:

        # Run the expansion demo
        for t in test_strings:
            print "Running conversion process for %s" % t
            print "After tokenisation: %s" % tokenise(t)
            simple_swap = [replace_token(c) for c in tokenise(t)]
            print "After basic expansion: %s" % simple_swap
            clever_swap = [replace_token2(c) for c in tokenise(t)]
            print "After smart expansion: %s" % clever_swap
            result = canon(''.join(clever_swap))
            print "After canonicalisation: %s" % result 
            print
            print

    elif len(sys.argv) == 3:
        # Add two strings
        input_a = sys.argv[1]
        input_b = sys.argv[2]

        print "First input %s simplifies to %s" % (input_a, tokenise_str(input_a))
        print "Second input %s simplifies to %s" % (input_b, tokenise_str(input_b))
        result = add(tokenise_str(input_a), tokenise_str(input_b))
        print "Result after addition: %s" % result
        print "Canonical result: %s" % canon(result)
   
    else:
        print "Something amusing an error message"
        



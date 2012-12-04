

def add(augend, addend):
    simple_sum = augend + addend
    print 'simple', simple_sum
    return order(
        convert_ls(convert_xs(convert_vs(simple_sum)))
    )

def convert_ls(number):
    print 'convert ls', number
    return number.replace('XXXXX','L')

def convert_xs(number):
    return number.replace('VV', 'X')

def convert_vs(number):
    return number.replace('IIIII', 'V')

def order(number):
    return ''.join(reversed(sorted(number, key=get_ordering_of)))

def get_ordering_of(numeral):
    return {
            'I': 'a',
            'V': 'b',
            'X': 'c',
            'L': 'd',
            }[numeral]

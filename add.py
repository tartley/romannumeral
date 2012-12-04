def add(augend, addend):
    simple_sum = augend + addend
    print 'simple', simple_sum
    return convert_ls(convert_xs(convert_vs(simple_sum)))


def order(number):
    return ''.join(reversed(sorted(number, key=get_ordering_of)))

def ordered(fn):
    def ordered_fn(*args):
        return order(fn(*args))
    return ordered_fn

def get_ordering_of(numeral):
    return {
            'I': 'a',
            'V': 'b',
            'X': 'c',
            'L': 'd',
            }[numeral]

@ordered
def convert_ls(number):
    return number.replace('XXXXX','L')

@ordered
def convert_xs(number):
    return number.replace('VV', 'X')

@ordered
def convert_vs(number):
    return number.replace('IIIII', 'V')

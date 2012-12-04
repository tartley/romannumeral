def add(augend, addend):
    simple_sum = augend + addend
    return convert_ls(convert_xs(convert_vs(simple_sum)))


def order(number):
    return ''.join(reversed(sorted(number, key=get_ordering_of)))

def ordered(original_function):

    def ordered_fn(number):
        original_result = original_function(number)
        return order(original_result)

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

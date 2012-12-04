

def canon(bacon):
    replacements = [
        ('IIII', 'IV'),
        ('VIV', 'IX'),
        ('XXXXIX', 'IL'),
        ('LXXXX', 'XC'),
        ('XXXX', 'XL'),
    ]
    print
    print bacon
    bacon = bacon.upper()
    for old, new in replacements:
        bacon = bacon.replace(old, new)
        print bacon
    return bacon


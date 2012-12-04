

def canon(bacon):
    replacements = [
        ('iiii', 'iv'),
        ('viv', 'ix'),
        ('xxxxix', 'il'),
        ('xxxx', 'xl'),
    ]
    print
    print bacon
    for old, new in replacements:
        bacon = bacon.replace(old, new)
        print bacon
    return bacon


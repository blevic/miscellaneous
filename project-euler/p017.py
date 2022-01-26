# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

def spell(num):
    dict = {0: 'zero',
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
            10: 'ten',
            11: 'eleven',
            12: 'twelve',
            13: 'thirteen',
            14: 'fourteen',
            15: 'fifteen',
            16: 'sixteen',
            17: 'seventeen',
            18: 'eighteen',
            19: 'nineteen',
            20: 'twenty',
            30: 'thirty',
            40: 'forty',
            50: 'fifty',
            60: 'sixty',
            70: 'seventy',
            80: 'eighty',
            90: 'ninety'}

    if num < 20:
        return dict[num]

    if num < 100:
        if num % 10 == 0:
            return dict[num]
        else:
            return dict[num // 10 * 10] + '-' + dict[num % 10]

    if num < 1000:
        if num % 100 == 0:
            return dict[num // 100] + ' hundred'
        else:
            return dict[num // 100] + ' hundred and ' + spell(num % 100)

    if num == 1000:
        return 'one thousand'


total = 0
for r in range(1, 1001):
    stripped = spell(r).strip().replace(" ", "").replace("-", "")
    total += len(stripped)

print(total)
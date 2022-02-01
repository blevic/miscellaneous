# A common security method used for online banking is to ask the user for three random characters from a passcode.
# For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply
# would be: 317. Fifty successful login attempts are provided.
# Given that the three characters are always asked for in order, analyse the file so as to determine the shortest
# possible secret passcode of unknown length.

login = "319 680 180 690 129 620 762 689 762 318 368 710 720 710 629 168 160 689 716 731 736 729 316 729 729 710 769 290 719 680 318 389 162 289 162 718 729 319 790 680 890 362 319 760 316 729 380 319 728 716"


def shrink(lst, digit):
    shrunk_list = []
    for e in lst:
        if e[-1] == digit and digit not in e[:-1]:
            new_e = e[:-1]
            if new_e != '':
                shrunk_list.append(new_e)
        else:
            shrunk_list.append(e)
    return shrunk_list


all_characters = set(login.replace(" ", ""))
shrinking_list = login.split(" ")

passcode = ''
while shrinking_list:
    last_digit = ''
    for d in all_characters:
        if any(e[-1] == d for e in shrinking_list) and not any(d in e[:-1] for e in shrinking_list):
            last_digit = d
            passcode = last_digit + passcode
            break
    shrinking_list = shrink(shrinking_list, last_digit)

print(passcode)

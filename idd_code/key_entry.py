import serial

ser = serial.Serial('/dev/cu.usbmodem1421', 9600)

# R = 82
# G = 71
# B = 66
# U = 85

letters = 'abcdefghijklmnopqrstuvwxyz '
# letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '

# 0 = red, 1 = green, 2 = blue, 3 = white/gray/blank

# starting_state = [('A', 0), ('B', 0), ('C', 0), ('D', 0), ('E', 0), ('F', 0),
# ('G', 0), ('H', 0), ('I', 0), ('J', 1), ('K', 1), ('L', 1), ('M', 1), ('N', 1),
# ('O', 1), ('P', 1), ('Q', 1), ('R', 1), ('S', 2), ('T', 2), ('U', 2), ('V', 2),
# ('W', 2), ('X', 2), ('Y', 2), ('Z', 2), (' ', 2)]
starting_state = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0,
'g': 0, 'h': 0, 'i': 0, 'j': 1, 'k': 1, 'l': 1, 'm': 1, 'n': 1,
'o': 1, 'p': 1, 'q': 1, 'r': 1, 's': 2, 't': 2, 'u': 2, 'v': 2,
'w': 2, 'x': 2, 'y': 2, 'z': 2, ' ': 2}

word = ''
all_info = (word, starting_state)


def listen():
    # total = len(starting_state)
    # prev = ''
    selected = letters
    new_state = starting_state
    global word
    global all_info

    while True:
        line = ser.readline()
        if line:
            data = line[0]
            print("data = " + str(data))
            remaining = len(selected)
            print("remaining length: " + str(remaining))

            if data != 85:

                if data == 82:
                    left = int(remaining/3)
                    print(left)
                    selected = selected[0:left]
                    new_division_l = int(left/3)
                    new_division_r = int(2*left/3)
                    print(selected)


                elif data == 71:
                    # left = mid_l
                    left = int(remaining/3)
                    mid_r = int(2*remaining/3)
                    selected = selected[left:mid_r]
                    print(selected)

                    new_division_l = int((left)/3)
                    new_division_r = int(2*(left)/3)


                elif data == 66:
                    left = int(remaining/3)
                    right = int(2*remaining/3)
                    selected = selected[right:remaining]
                    print(selected)
                    new_division_l = int(left/3)
                    new_division_r = int(2*left/3)

                # replace everything with 3
                new_state = {x: 3 for x in new_state}

                i = 0
                while i < new_division_l:
                    new_state[selected[i]] = 0
                    i += 1
                while i < new_division_r:
                    new_state[selected[i]] = 1
                    i += 1
                while i < left:
                    new_state[selected[i]] = 2
                    i += 1
                all_info = (word, new_state)
                print(all_info)


            elif data == 85:
                if (selected == letters) and len(word) > 0:  # you haven't started selecting for this letter
                    word = word[:-1]  # delete the latest letters

                selected = letters
                new_state = starting_state
                print("Word so far: " + word)
                print(selected)
                all_info = (word, new_state)
                print(all_info)



            if len(selected) <= 1:  # if we've made the third selection
                print("Selected letter is: " + selected)
                word = word + selected
                print("Word so far: " + word)
                selected = letters
                new_state = starting_state
                all_info = (word, new_state)

                print(new_state)
                # reset everything



    # while True:
    #   line = ser.readline()
    #   if line:
    #       data = line[0]
    #       print("data = " + str(data))
    #       remaining = len(selected)
    #       print("remaining length: " + str(remaining))

    #       if data == 82:
    #           left = int(remaining/3)
    #           print(left)
    #           selected = selected[0:left]
    #           print(selected)
    #       elif data == 71:
    #           mid_l = int(remaining/3)
    #           mid_r = int(2*remaining/3)
    #           selected = selected[mid_l:mid_r]
    #           print(selected)
    #       elif data == 66:
    #           right = int(2*remaining/3)
    #           selected = selected[right:remaining]
    #           print(selected)
    #       elif data == 85:
    #           if (selected == letters) and len(word) > 0: #you haven't started selecting for this letter
    #               word = word[:-1] #delete the latest letters

    #           selected = letters
    #           print("Word so far: " + word)

    #           print(selected)

    #       if len(selected) <= 1: #if we've made the third selection
    #           print("Selected letter is: " + selected)
    #           word = word + selected
    #           print("Word so far: " + word)
    #           selected = letters
    #           #reset everything

#program for  rotate  a given string in the specific direction
word = input("Enter the String:")
original_word = word
rotation = input("Enter the number of rotation:")
rotation = int(rotation)

def split(word):
    return [char for char in word]

def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result

def anagram_string_maker(string1, s):
    a = split(string1)
    b = []
    for i in range(0, s):
        char_mov_direction = input('Enter the direction L or R :')
        char_number_of_movements = input('Enter the number of movements: ')
        char_number_of_movements = int(char_number_of_movements)

        if(char_mov_direction == 'L'):
            b.append(a[char_number_of_movements])
        elif(char_mov_direction == 'R'):
            b.append(a[-(char_number_of_movements)])
    result = concatenate_list_data(b)
    return result

def is_anagram(str1, str2):
    list_str1 = list(str1)
    list_str1.sort()
    list_str2 = list(str2)
    list_str2.sort()


    if(list_str1 == list_str2):
        print("Yes")
    else:
        print("No")

word = anagram_string_maker(word, rotation)
is_anagram(original_word, word)

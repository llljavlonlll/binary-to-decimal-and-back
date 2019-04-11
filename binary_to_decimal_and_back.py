from math import log2
import pdb
import os

#   Decimal to Binary
###################################################################################
def determine_binary_places(input):
    list_of_powers = []
    list_of_binary_places = []
    while input > 0:
        for i in range(0,input):
            if 2**i <= input:
                list_of_powers.append(2**i)
            else:
                break
        list_of_binary_places.append(max(list_of_powers))
        input = input - max(list_of_powers)
        list_of_powers = []
        # pdb.set_trace()
    return list_of_binary_places

def convert_to_binary(list_of_binary_places):
    binary_list = [0] * (int(log2(max(list_of_binary_places))) + 1)
    #pdb.set_trace()
    for i in list_of_binary_places:
        binary_list[int(log2(i))] = 1
    return binary_list

def decimal_to_binary():
    return list(reversed(convert_to_binary(determine_binary_places(int(input('Decimal: '))))))
#################################################################################################


#   Binary to Decimal
#############################################################################################
def binary_to_decimal():
    user_binary = input('Binary: ')
    binary_list = list(reversed(list(map(int, list(user_binary)))))
    #pdb.set_trace()
    index = 0
    result = 0
    for i in binary_list:
        if i == 1:
            result += 2**index
        index += 1
    return result
#############################################################################################


#   Menu
#############################################################################################
def print_menu():
    print (30 * "-" , "MENU" , 30 * "-")
    print ("1. Decimal to Binary")
    print ("2. Binary to Decimal")
    print ("3. Exit")
    print (67 * "-")
#############################################################################################

# print(binary_to_decimal())
if __name__ == '__main__':
    clear = lambda: os.system('cls')
    clear()
    print_menu()
    while True:
        try:
            menu_choice = int(input('Chose an option: '))
        except:
            print('Enter a valid choice')
            continue
        else:
            break

    if menu_choice == 1:
        print('Decimal to Binary')
        print(decimal_to_binary())
    elif menu_choice == 2:
        print('Binary to Decimal')
        print(binary_to_decimal())
    elif menu_choice == 3:
        quit()
    else:
        print('Invalid choice')
        input()

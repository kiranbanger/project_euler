def check_hand(s, v):
    #check all 9 possibilities:
    high_card = get_high_card(v)
    print(high_card)

    one_pair_flag = check_same_value(v, 2)
    print('One pair: ', one_pair_flag)

    two_pair_flag = check_two_pair(v)
    print('Two Pairs: ', two_pair_flag)

    three_kind_flag = check_same_value(v,3)
    print('Three of a kind: ', three_kind_flag)

    straight_flag = check_consecutive_values(v)
    print('Straight: ', straight_flag)

    flush_flag = check_same_suit(s)
    print('Flush: ', flush_flag)

    full_house_flag = check_same_value(v,3) and check_same_value(v,2)
    print('Full house: ', full_house_flag)

    four_kind_flag = check_same_value(v, 4)
    print('Four of a kind: ', four_kind_flag)

    straight_flush_flag = check_straight_flush(s,v)
    print('Straight Flush: ', straight_flush_flag)

    royal_flush_flag = check_royal_flush(s, v)
    print('Royal Flush: ', royal_flush_flag)

def get_high_card(v):
    card_array = []
    for key in v:
        print(key)
        card_array.append(key)

    card_array.sort(reverse = True)
    return card_array

def check_same_suit(suit_dict):
    return len(suit_dict) == 1

def check_consecutive_values(value_dict):
    #print(value_dict)
    value_list = []
    for key in value_dict:
        for i in range(0,value_dict[key]):
            value_list.append(key)
    value_list.sort()

    # make sure diff between each consecutive value is 1
    consecutive_flag = True
    for i in range(1, len(value_list)):
        if value_list[i] - value_list[i-1] != 1:
            consecutive_flag = False
            break

    return consecutive_flag

def check_two_pair(v):
    flag1 = False
    flag2 = False
    for key in v:
        if v[key] == 2:
            # if flag1 is false, then we have not see any pairs yet,
            # and this is the first pair, so we set the first flag to true
            if flag1 == False:
                flag1 = True
            # if flag1 is true, then we already have one pair,
            # which means this is the second pair, so we set flag2 to true
            elif flag1 == True:
                flag2 = True
    return flag1 and flag2

# this function will check for one pair, three of a kind, four of a kind
def check_same_value(value_dict, count):
    count_flag = False
    for key in value_dict:
        if value_dict[key] == count:
            count_flag = True
            break
    return count_flag

def check_straight_flush(s,v):
    return check_same_suit(s) and check_consecutive_values(v)
# this will return true for royal flush

def check_royal_flush(s,v):
    return 10 in v and 11 in v and 12 in v and 13 in v and 14 in v and check_same_suit(s)


def disect_hand(hand):
    # separate values from suit
    value_conversion_dict = {'2':2,
                             '3':3,
                             '4':4,
                             '5':5,
                             '6':6,
                             '7':7,
                             '8':8,
                             '9':9,
                             'T':10,
                             'J':11,
                             'Q':12,
                             'K':13,
                             'A':14
                             }
    suit_dict = {}
    value_dict = {}
    for i in hand:
        suit_dict[i[-1]] = suit_dict.get(i[-1], 0) + 1
        value_conv = value_conversion_dict[i[0]]
        value_dict[value_conv] = value_dict.get(value_conv, 0) + 1
    print(value_dict)
    return suit_dict, value_dict


#file_handle = open('poker.txt')
#for line in file_handle:
#    line = line.strip().split(' ')
#    print(line)

# example hands for testing
# line = ['9C', 'JD', '7C', '6D', 'TC', '6H', '6C', 'JC', '3D', '3S']
# line = ['9D', 'JD', 'QD', 'KD', 'TD', '6H', '6C', 'JC', '3D', '3S']
line = ['KD', 'KS', '5H', '5D', '2D', '6H', '6C', 'JC', '3D', '3S']
h1 = line[0:5]
h2 = line[5:11]

suits, values = disect_hand(h2)
hand_analysis = check_hand(suits, values)
    # change this function to return a dict or array of results,
    # including a numerical value that is assigned to each hand
    # and the list of 'high cards', in order from highest to lowest,
    # in the case of ties
    # for example, if a hand has two pair, it should have two pair, along with 2
    # and the high card (and subsequent high cards, in the case of ties)




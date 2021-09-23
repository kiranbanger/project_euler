def compare_hands(h1,h2):
    suits1, values1 = disect_hand(h1)
    hand_analysis1 = check_hand(suits1, values1)

    suits2, values2 = disect_hand(h2)
    hand_analysis2 = check_hand(suits2, values2)

    # get max value from arrays, excluding last value, which is the array of high cards
    if len(hand_analysis1) > 1:  # make sure there was a hand
        h1_score = max(hand_analysis1[0:len(hand_analysis1)-1])
    else:  # if there wasn't a hand, set score to 0
        h1_score = 0
    if len(hand_analysis2) > 1:
        h2_score = max(hand_analysis2[0:len(hand_analysis2) - 1])
    else:
        h2_score = 0

    # in the case of a tie
    i = 0
    tie_flag = False
    while h1_score == h2_score and i<min(len(hand_analysis1),len(hand_analysis2)):
        if h1_score not in [1,2,3,6,7] or tie_flag:
            h1_score = hand_analysis1[-1][i]
            h2_score = hand_analysis2[-1][i]
            i += 1
        else:
            tie_flag = True
            if h1_score == 1:
                # in values dict, find the one value of 2
                for key in values1:
                    if values1[key] == 2:
                        h1_score = key
                for key in values2:
                    if values2[key] == 2:
                        h2_score = key
            if h1_score == 2:
                # get high pair value
                h1_tp_array = []
                h2_tp_array = []
                for key in values1:
                    if values1[key] == 2:
                        h1_tp_array.append(key)
                for key in values2:
                    if values2[key] == 2:
                        h2_tp_array.append(key)
                h1_score = max(h1_tp_array)
                h2_score = max(h2_tp_array)
                # if still tied, get second high pair value
                if h1_score == h2_score:
                    h1_score = min(h1_tp_array)
                    h2_score = min(h2_tp_array)
            if h1_score == 3:
                # get value of three of a kind
                for key in values1:
                    if values1[key] == 3:
                        h1_score = key
                for key in values2:
                    if values2[key] == 3:
                        h2_score = key
            if h1_score == 6:
                # get value of three of a kind
                for key in values1:
                    if values1[key] == 3:
                        h1_score = key
                for key in values2:
                    if values2[key] == 3:
                        h2_score = key
                # if score is still tied, get value of pair
                if h1_score == h2_score:
                    for key in values1:
                        if values1[key] == 2:
                            h1_score = key
                    for key in values2:
                        if values2[key] == 2:
                            h2_score = key
            if h1_score == 7:
                # get value of four of a kind
                for key in values1:
                    if values1[key] == 4:
                        h1_score = key
                for key in values2:
                    if values2[key] == 4:
                        h2_score = key


    # return winner
    if h1_score > h2_score: return 'player 1'
    elif h1_score < h2_score: return 'player 2'

    return


def check_hand(s, v):
    # check all 9 possibilities, and get card order:
    hand_result_dict = {
        1: check_same_value(v, 2),  # one pair
        2: check_two_pair(v),  # two pair
        3: check_same_value(v,3),  # three of a kind
        4: check_consecutive_values(v),  # straight
        5: check_same_suit(s),  # flush
        6: check_same_value(v,3) and check_same_value(v,2),  # full house
        7: check_same_value(v, 4),  # four of a kind
        8: check_straight_flush(s,v),  # straight flush
        9: check_royal_flush(s, v),  # royal flush
        'high_card': get_high_card(v)  # value of cards in descending order, for ties
    }

    hand_result_array = []
    for hand in hand_result_dict:
        if hand_result_dict[hand] and hand != 'high_card':
            hand_result_array.append(hand)
    hand_result_array.append(hand_result_dict['high_card'])

    return hand_result_array


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
    #print(value_dict)
    return suit_dict, value_dict

def get_high_card(v):
    card_array = []
    for key in v:
        card_array.append(key)

    card_array.sort(reverse = True)
    return card_array

def check_same_suit(suit_dict):
    return len(suit_dict) == 1

def check_consecutive_values(value_dict):
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
            if not flag1:
                flag1 = True
            # if flag1 is true, then we already have one pair,
            # which means this is the second pair, so we set flag2 to true
            elif flag1:
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


file_handle = open('poker.txt')
p1_wins = 0
p2_wins = 0
ties = 0

for line in file_handle:
    line = line.strip().split(' ')

    winner = compare_hands(line[0:5], line[5:11])

    if winner == 'player 1':
        p1_wins +=1
    elif winner == 'player 2':
        p2_wins +=1
    elif winner is None: # to see if anything unexpected is happening
        print(line)
        ties +=1

print('Player 1 won',p1_wins, 'times. Player 2 won', p2_wins, 'times. There were',ties, 'ties.')
import random

# identify if there is one or more pairs in the hand

Rank = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
Suit = ['s', 'h', 'd', 'c']
# 2 example poker hands
# CurrentHand1 = ['Ad', '2d', '2c']
# CurrentHand2 = ['5s', '5c', '5d']
# Randomly generate two hands of n cards
# def generate_2hands(nn_card=3):
def generate_2hands(Rank, Suit):
    deck = []
    # print(R,S)
    # print(str(R)+str(S))
    for i in Rank:
        for j in Suit:
            deck.append(i+j)

        # R=random.choice(Rank)
        # S=random.choice(Suit)
    #slctd_cards = (random.sample(deck, 6))
    return deck


# generate_2hands(Rank,Suit)

# identify hand category using IF-THEN rule


#########################
#      Game flow        #
#########################


#########################
# phase 1: Card Dealing #
#########################
player1=[]
player2=[]
def card_dealing():
    d = generate_2hands(Rank, Suit)
    # print(d)
    # print(len(d))

    shuffle = random.sample(d,6)
    print(shuffle)
    player1 = random.sample(shuffle,3)
    player2 = list(set(shuffle)-set(player1))

    return player1,player2



#########################
# phase 2:   Bidding    #
#########################

def randombidding():
    bid=[]
    for i in range(3):
        bid.append(random.randint(0,50))
    return bid

def fixed_bidding():
    bid=[]
    for i in [12,33,44]:
        bid.append(i)
    return bid
def reflex_agent():
    c3=[]
    c4=[]
    ct1 = 0
    ct2 = 0
    for i in range(3):
        b1 = 0
        b2 = 0
        player1, player2 = card_dealing()
        print('player1: ', player1, '\nplayer2: ', player2)
        P1 = analyseHand(player1)
        P2 = analyseHand(player2)
        opt = input("Press 1 for Fixed Agent VS Reflex Agent or 2 for Random Agent VS Reflex Agent: ")
        bid1 = []
        bid2 = []
        if (opt == '1'):
            bid2 = fixed_bidding()
            if (P1['name'] == 'Three of a kind'):
                bid1.append(50)
                if ((bid1[0] >= bid2[0]) and (Rank.index(P1['rank'], 0, len(Rank))) > 10):
                    bid1.append(43)
                else:
                    bid1.append(30)
                if (bid1[1] >= bid2[1]):
                    bid1.append(50)
                else:
                    bid1.append(37)
                print( bid1,bid2)

            elif (P1['name'] == 'pair'):
                bid1.append(37)
                if ((bid1[0] >= bid2[0]) and (Rank.index(P1['rank'], 0, len(Rank))) > 11):
                    bid1.append(42)
                else:
                    bid1.append(30)
                if (bid1[1] >= bid2[1]):
                    bid1.append(40)
                else:
                    bid1.append(20)
                print(bid1, bid2)
            elif (P1['name'] == 'High Cards'):
                bid1.append(25)
                if ((bid1[0] >= bid2[0]) and (Rank.index(P1['rank'], 0, len(Rank))) > 10):
                    bid1.append(37)
                else:
                    bid1.append(22)
                if (bid1[1] >= bid2[1]):
                    bid1.append(30)
                else:
                    bid1.append(0)
                print(bid1, bid2)

        if (opt == '2'):
            bid1 = []
            bid2 = randombidding()
            if (P1['name'] == 'Three of a kind'):
                bid1.append(50)
                if ((bid1[0] >= bid2[0]) and (Rank.index(P1['rank'], 0, len(Rank))) > 10):
                    bid1.append(47)
                else:
                    bid1.append(30)
                if (bid1[1] >= bid2[1]):
                    bid1.append(50)
                else:
                    bid1.append(25)

            elif (P1['name'] == 'pair'):
                bid1.append(37)
                if ((bid1[0] >= bid2[0]) and (Rank.index(P1['rank'], 0, len(Rank))) > 11):
                    bid1.append(42)
                else:
                    bid1.append(28)
                if (bid1[1] >= bid2[1]):
                    bid1.append(38)
                else:
                    bid1.append(10)

            elif (P1['name'] == 'High Cards'):
                bid1.append(27)
                if ((bid1[0] >= bid2[0]) and (Rank.index(P1['rank'], 0, len(Rank))) > 11):
                    bid1.append(37)
                else:
                    bid1.append(17)
                if (bid1[1] >= bid2[1]):
                    bid1.append(35)
                else:
                    bid1.append(0)

        for b in range(len(bid1)):
            b1 += bid1[b]
        print("Amount Bidded by Player1: ", bid1)
        for b in range(len(bid2)):
            b2 += bid2[b]
        print("Amount Bidded by Player2: ", bid2)
        Pot = b1 + b2
        if (P1['name'] == P2['name']):
            print("Player 1 has: ", P1['name'], "\nPlayer 2 has: ", P2['name'])
            c1, c2 = Samecards(player1, player2, Pot, count1, count2)
            c3.append(c1)
            c4.append(c2)
            ct1 += c3[i]
            ct2 += c4[i]
        elif (P1['name'] != P2['name']):
            print("Player 1 has: ", P1['name'], "\nPlayer 2 has: ", P2['name'])
            c1, c2 = DiffCards(P1, P2, Pot, count1, count1)
            c3.append(c1)
            c4.append(c2)
            ct1 += c3[i]
            ct2 += c4[i]
        print("No of Games Won by Player1: ", ct1, "\nNo of Games Won by Player2: ", ct2)
        if (ct1 > ct2):
            print("Player 1 Won")
        elif (ct1 == ct2):
            print("Tie")
        else:
            print("Player 2 Won")


#########################
# phase 2:   Showdown   #
#########################
#def Showdown():
def Highcard(Hand_):
    if(len(Hand_)==2):
        ind1 = Rank.index(Hand_[0][0], 0, len(Rank))
        ind2 = Rank.index(Hand_[1][0], 0, len(Rank))
        if (ind1 > ind2):
            yield dict(name='High Cards', rank=Hand_[0][0], suit1=Hand_[0][1], suit2='', suit3='')
            return
        if (ind2 > ind1):
            yield dict(name='High Cards', rank=Hand_[1][0], suit1=Hand_[1][1], suit2='', suit3='')
            return


def identifyHand(Hand_):
    if (Hand_[0][0]==Hand_[1][0]==Hand_[2][0]) :
        print ("You have 3 of kinds")
        yield dict(name = 'Three of a kind', rank = Hand_[0][0], suit1 = Hand_[0][1], suit2 = Hand_[1][1], suit3 = Hand_[2][1])
        return
    for c1 in Hand_:
        for c2 in Hand_:
            if (c1[0] == c2[0]) and (c1[1] < c2[1]):
                yield dict(name='pair', rank=c1[0], suit1=c1[1], suit2=c2[1], suit3='')
                return
    if(len(Hand_)==3):
        ind1 = Rank.index(Hand_[0][0], 0, len(Rank))
        ind2 = Rank.index(Hand_[1][0], 0, len(Rank))
        ind3 = Rank.index(Hand_[2][0], 0, len(Rank))
        if ((ind1 > ind2) and (ind1 > ind3)):
            yield dict(name='High Cards', rank=Hand_[0][0], suit1=Hand_[0][1], suit2='', suit3='')

        elif ((ind2 > ind1) and (ind2 > ind3)):
            yield dict(name='High Cards', rank=Hand_[1][0], suit1=Hand_[1][1], suit2='', suit3='')

        elif ((ind3 > ind1) and (ind3 > ind2)):
            yield dict(name='High Cards', rank=Hand_[2][0], suit1=Hand_[2][1], suit2='', suit3='')

    Highcard(Hand_)


# Print out the result
def analyseHand(Hand_):
    HandCategory = dict()
    functionToUse = identifyHand
    #print(functionToUse)
    for category in functionToUse(Hand_):
        #print('Category: ')
        for key in "name rank suit1 suit2 suit3".split():
            #print(key, "=", category[key])
            HandCategory[key]=category[key]
        return HandCategory

def analyseHand1(Hand_):
    HandCategory = dict()
    functionToUse = Highcard
    #print(functionToUse)
    for category in functionToUse(Hand_):
        #print('Category: ')
        for key in "name rank suit1 suit2 suit3".split():
            #print(key, "=", category[key])
            HandCategory[key]=category[key]
        return HandCategory

#analyseHand(player1)
# for i in range(3):
def Samecards(player1,player2,Pot,count1,count2):
    P1 = analyseHand(player1)
    P2 = analyseHand(player2)
    if ((P1['name'] == "High Cards") and (P2['name'] == "High Cards")):
        if (Rank.index(P1['rank'], 0, len(Rank)) > Rank.index(P2['rank'], 0, len(Rank))):
            print("Player 1 is winner")
            count1 +=1
            print("Total Amount Won is: ", Pot, "$")
        elif (Rank.index(P1['rank'], 0, len(Rank)) < Rank.index(P2['rank'], 0, len(Rank))):
            print("Player 2 is winner")
            count2 += 1
            print("Total Amount Won is: ", Pot, "$")
        elif (Rank.index(P1['rank'], 0, len(Rank)) == Rank.index(P2['rank'], 0, len(Rank))):
            player1.remove(P1['rank'] + P1['suit1'])
            player2.remove(P2['rank'] + P2['suit1'])
            P1 = analyseHand1(player1)
            P2 = analyseHand1(player2)
            if (Rank.index(P1['rank'], 0, len(Rank)) > Rank.index(P2['rank'], 0, len(Rank))):
                print("Player 1 is winner")
                count1 += 1
                print("Total Amount Won is: ", Pot, "$")
            elif (Rank.index(P1['rank'], 0, len(Rank)) < Rank.index(P2['rank'], 0, len(Rank))):
                print("Player 2 is winner")
                count2 += 1
                print("Total Amount Won is: ", Pot, "$")
            elif (Rank.index(P1['rank'], 0, len(Rank)) == Rank.index(P2['rank'], 0, len(Rank))):
                player1.remove(P1['rank'] + P1['suit1'])
                player2.remove(P2['rank'] + P2['suit1'])
                if (Rank.index(player1[0][0], 0, len(Rank)) > Rank.index(player2[0][0], 0, len(Rank))):
                    print("Player 1 is winner")
                    count1 += 1
                    print("Total Amount Won is: ", Pot, "$")
                elif (Rank.index(player1[0][0], 0, len(Rank)) < Rank.index(player2[0][0], 0, len(Rank))):
                    print("Player 2 is winner")
                    count2 += 1
                    print("Total Amount Won is: ", Pot, "$")
                elif (Rank.index(player1[0][0], 0, len(Rank)) == Rank.index(player2[0][0], 0, len(Rank))):
                    print("Its a Tie")

    elif ((P1['name'] == "pair") and (P2['name'] == "pair")):
        if (Rank.index(P1['rank'], 0, len(Rank)) > Rank.index(P2['rank'], 0, len(Rank))):
            print("Player 1 is winner")
            count1 += 1
            print("Total Amount Won is: ", Pot, "$")
        elif (Rank.index(P1['rank'], 0, len(Rank)) < Rank.index(P2['rank'], 0, len(Rank))):
            print("Player 2 is winner")
            count2 += 1
            print("Total Amount Won is: ", Pot, "$")
        elif (Rank.index(P1['rank'], 0, len(Rank)) == Rank.index(P2['rank'], 0, len(Rank))):
            player1.remove(P1['rank'] + P1['suit1'])
            player1.remove(P1['rank'] + P1['suit2'])
            player2.remove(P2['rank'] + P2['suit1'])
            player2.remove(P2['rank'] + P2['suit2'])
            P1 = analyseHand1(player1)
            P2 = analyseHand1(player2)
            if (Rank.index(P1['rank'], 0, len(Rank)) > Rank.index(P2['rank'], 0, len(Rank))):
                print("Player 1 is winner")
                count1 += 1
                print("Total Amount Won is: ", Pot, "$")
            elif (Rank.index(P1['rank'], 0, len(Rank)) < Rank.index(P2['rank'], 0, len(Rank))):
                print("Player 2 is winner")
                count2 += 1
                print("Total Amount Won is: ", Pot, "$")
            else:
                print("Its a Tie")

    elif ((P1['name'] == 'Three of a kind') and (P2['name'] == 'Three of a kind')):
        if (Rank.index(P1['rank'], 0, len(Rank)) > Rank.index(P2['rank'], 0, len(Rank))):
            print("Player 1 is winner")
            count1 += 1
            print("Total Amount Won is: ", Pot, "$")
        elif (Rank.index(P1['rank'], 0, len(Rank)) < Rank.index(P2['rank'], 0, len(Rank))):
            print("Player 2 is winner")
            count2 += 1
            print("Total Amount Won is: ", Pot, "$")
    return count1,count2

def DiffCards(P1,P2,Pot,count1,count2):
    if ((P1['name'] == 'pair') and (P2['name'] == 'Three of a kind')):
        print("Player 2 is winner")
        count2 +=1
        print("Total Amount Won is: ", Pot, "$")
    elif ((P1['name'] == 'Three of a kind') and (P2['name'] == 'pair')):
        print("Player 1 is winner")
        count1 +=1
        print("Total Amount Won is: ", Pot, "$")
    elif ((P1['name'] == 'Three of a kind') and (P2['name'] == 'High Cards')):
        print("Player 1 is winner")
        count1 +=1
        print("Total Amount Won is: ", Pot, "$")
    elif ((P1['name'] == 'High Cards') and (P2['name'] == 'Three of a kind')):
        print("Player 2 is winner")
        count2 +=1
        print("Total Amount Won is: ", Pot, "$")
    elif ((P1['name'] == 'High Cards') and (P2['name'] == 'pair')):
        print("Player 2 is winner")
        count2 +=1
        print("Total Amount Won is: ", Pot, "$")
    elif ((P1['name'] == 'pair') and (P2['name'] == 'High Cards')):
        print("Player 1 is winner")
        count1 +=1
        print("Total Amount Won is: ", Pot, "$")
    return count1,count2

count1 = 0
count2 = 0
def Gameflow():
    c3=[]
    c4=[]
    ct1 = 0
    ct2 = 0
    for i in range(50):
        bid1 = 0
        bid2 = 0
        player1, player2 = card_dealing()
        print('player1: ', player1, '\nplayer2: ', player2)
        P1 = analyseHand(player1)
        P2 = analyseHand(player2)
        b1 = randombidding()
        b2 = fixed_bidding()
        print("Amount Bidded by Player1: ", b1)
        for b in range(len(b1)):
            bid1 += b1[b]
        print("Amount Bidded by Player2: ", b2)
        for b in range(len(b2)):
            bid2 += b2[b]
        Pot = bid1 + bid2
        if (P1['name'] == P2['name']):
            print("Player 1 has: ", P1['name'], "\nPlayer 2 has: ", P2['name'])
            c1,c2 = Samecards(player1, player2, Pot,count1,count2)
            c3.append(c1)
            c4.append(c2)
            ct1 += c3[i]
            ct2 += c4[i]
        elif (P1['name'] != P2['name']):
            print("Player 1 has: ", P1['name'], "\nPlayer 2 has: ", P2['name'])
            c1,c2 = DiffCards(P1, P2, Pot,count1,count1)
            c3.append(c1)
            c4.append(c2)
            ct1 += c3[i]
            ct2 += c4[i]
        print("No of Games Won by Player1: ",ct1,"\nNo of Games Won by Player2: ",ct2)
        if (ct1 > ct2):
            print("Player 1 Won")
        elif (ct1 == ct2):
            print("Tie")
        else:
            print("Player 2 Won")


#Gameflow()
#reflex_agent()
Input = input("Press 1 for Random VS fixed agent or 2 for Reflex VS Random or Fixed Agent: ")
if (Input == '1'):
    Gameflow()
elif (Input == '2'):
    reflex_agent()
else:
    print("Invalid Input")

import random

def create_deck():
    dealerDeck = {
    'Ace of Spades': [1,11], '2 of Spades': 2, '3 of Spades': 3
    , '4 of Spades': 4, '5 of Spades': 5, '6 of Spades': 6
    , '7 of Spades': 7, '8 of Spades': 8, '9 of Spades': 9
    , '10 of Spades': 10, 'Jack of Spades': 10, 'Queen of Spades': 10
    , 'King of Spades': 10
    
    , 'Ace OF Hearts': [1,11], '2 of Hearts': 2, '3 of Hearts': 3
    , '4 of Hearts': 4, '5 of Hearts': 5, '6 of Hearts': 6
    , '7 of Hearts': 7, '8 of Hearts': 8, '9 of Hearts': 9
    , '10 of Hearts': 10, 'Jack of Hearts': 10, 'Queen of Hearts': 10
    , 'King of Hearts': 10
    
    , 'Ace OF Diamonds': [1,11], '2 of Diamonds': 2, '3 of Diamonds': 3
    , '4 of Diamonds': 4, '5 of Diamonds': 5, '6 of Diamonds': 6
    , '7 of Diamonds': 7, '8 of Diamonds': 8, '9 of Diamonds': 9
    , '10 of Diamonds': 10, 'Jack of Diamonds': 10, 'Queen of Diamonds': 10
    , 'King of Diamonds': 10
    
    , 'Ace OF Clubs': [1,11], '2 of Clubs': 2, '3 of Clubs': 3
    , '4 of Clubs': 4, '5 of Clubs': 5, '6 of Clubs': 6
    , '7 of Clubs': 7, '8 of Clubs': 8, '9 of Clubs': 9
    , '10 of Clubs': 10, 'Jack of Clubs': 10, 'Queen of Clubs': 10
    , 'King of Clubs': 10
    }

    testList = list(dealerDeck.items())
    for i in range(0,10):
        random.shuffle(testList)
    
    shuffledDeck = dict(testList)

    return shuffledDeck 

def deal_cards(dealerDeck, player1Points, player2Points):
    #handle condition where no more cards to draw
    
    player1Card = ''
    player2Card = ''
    #player 1 card draw
    if len(dealerDeck) != 0:
        cardInfo = dealerDeck.popitem()
        if cardInfo[0] in ['Ace of Spades', 'Ace OF Hearts', 'Ace OF Diamonds', 'Ace OF Clubs']:
            #condition for ace
            if (player1Points + 11) > 21:
                player1Points += 1
            else:
                player1Points += 11
            player1Card = cardInfo[0]
        else:
            #normal condition
            player1Card = cardInfo[0]
            player1Points += cardInfo[1]


    #player 2 card draw
    if len(dealerDeck) != 0:
        cardInfo = dealerDeck.popitem()
        if cardInfo[0] in ['Ace of Spades', 'Ace OF Hearts', 'Ace OF Diamonds', 'Ace OF Clubs']:
            #condition for ace
            if (player2Points + 11) > 21:
                player2Points += 1
            else:
                player2Points += 11
            player2Card = cardInfo[0]
        else:
            player2Card = cardInfo[0]
            player2Points += cardInfo[1]

    
    return player1Card, player1Points, player2Card, player2Points, dealerDeck
    

def game_start(dealerDeck):
    #runs until no more cards in deck

    numberRounds = 0
    player1Wins = 0
    player2Wins = 0
    while len(dealerDeck) != 0:
        numberRounds += 1
        player1Points = 0 
        player2Points = 0

        roundInfo = roundStart(dealerDeck, player1Points, player2Points)
        dealerDeck = roundInfo[0]
        player1Wins += roundInfo[1]
        player2Wins += roundInfo[2]
    print('')
    print('**SUMMARY GAME STATISTICS**')
    print('Rounds played: ', numberRounds)
    print('Cards played: 52')
    print('Player 1 wins: ', player1Wins)
    print('Player 2 wins: ', player2Wins)


def roundStart(dealerDeck, player1Points, player2Points):
    print('')
    print('-->**NEW ROUND**')
    print(format('Deal', '10s'), format('Player 1', '25s'), format('Player 2', '25s'))
    print(format('----', '10s'), format('--------', '25s'), format('--------', '25s'))
    turnDeal = 0
    while True:
        turnDeal += 1
        turnInfo = deal_cards(dealerDeck, player1Points, player2Points)
        print(format(turnDeal, '<10'), format(turnInfo[0], '25s'), format(turnInfo[2], '25s'))
        #get cards and print deal turn
        dealerDeck = turnInfo[4]
        player1Points = turnInfo[1]
        player2Points = turnInfo[3]

        #check if round is over
        if player1Points > 21 and player2Points > 21:
            print(format('==========', '10s'), format('===========', '25s'), format('===========', '25s'))
            print(format('Hand Value', '10s'), format(player1Points, '7'), format(player2Points, '25'))
            print('')
            print('Draw! Both players bust')
            return dealerDeck, 0, 0 
        elif player1Points == 21 and player2Points == 21:
            print(format('==========', '10s'), format('===========', '25s'), format('===========', '25s'))
            print(format('Hand Value', '10s'), format(player1Points, '7'), format(player2Points, '25'))
            print('')
            print('Draw! Both players have 21')
            return dealerDeck, 0, 0 
        elif player1Points > 21:
            print(format('==========', '10s'), format('===========', '25s'), format('===========', '25s'))
            print(format('Hand Value', '10s'), format(player1Points, '7'), format(player2Points, '25'))
            print('')
            print('Player 2 wins! Player 1 busts')
            return dealerDeck, 0, 1 
        elif player2Points > 21:
            print(format('==========', '10s'), format('===========', '25s'), format('===========', '25s'))
            print(format('Hand Value', '10s'), format(player1Points, '7'), format(player2Points, '25'))
            print('')
            print('Player 1 wins! Player 2 busts')
            return dealerDeck, 1, 0 
        elif len(dealerDeck) == 0:
            if player1Points == player2Points:
                print(format('==========', '10s'), format('===========', '25s'), format('===========', '25s'))
                print(format('Hand Value', '10s'), format(player1Points, '7'), format(player2Points, '25'))
                print('')
                print('The deck is finished!')
                print('Final match is Draw!')
                return dealerDeck, 0, 0 
            elif player1Points > player2Points:
                print(format('==========', '10s'), format('===========', '25s'), format('===========', '25s'))
                print(format('Hand Value', '10s'), format(player1Points, '7'), format(player2Points, '25'))
                print('')
                print('The deck is finished!')
                print('Player 1 wins!')
                return dealerDeck, 1, 0 
            elif player1Points < player2Points:
                print(format('==========', '10s'), format('===========', '25s'), format('===========', '25s'))
                print(format('Hand Value', '10s'), format(player1Points, '7'), format(player2Points, '25'))
                print('')
                print('The deck is finished!')
                print('Player 2 wins!')
                return dealerDeck, 0, 1 
        
        # if a player score is above 21 they lose

def main():
    dealerDeck = create_deck()

    game_start(dealerDeck)


main()

'''
-->**NEW ROUND**
Deal       Player 1                  Player 2
----       --------                  --------
1          Jack of Hearts            2 of Hearts
2          9 of Diamonds             5 of Hearts
3          5 of Spades               7 of Diamonds
========== ===========               ===========
Hand Value      24                        14

Player 2 wins! Player 1 busts

-->**NEW ROUND**
Deal       Player 1                  Player 2
----       --------                  --------
1          Queen of Clubs            King of Spades
2          10 of Hearts              7 of Clubs
3          6 of Hearts               Ace OF Clubs
========== ===========               ===========
Hand Value      26                        18

Player 2 wins! Player 1 busts

-->**NEW ROUND**
Deal       Player 1                  Player 2
----       --------                  --------
1          10 of Diamonds            10 of Clubs
2          8 of Spades               Jack of Clubs
3          Ace OF Hearts             8 of Diamonds
========== ===========               ===========
Hand Value      19                        28

Player 1 wins! Player 2 busts

-->**NEW ROUND**
Deal       Player 1                  Player 2
----       --------                  --------
1          3 of Hearts               Jack of Diamonds
2          3 of Diamonds             2 of Diamonds
3          King of Diamonds          Jack of Spades
========== ===========               ===========
Hand Value      16                        22

Player 1 wins! Player 2 busts

-->**NEW ROUND**
Deal       Player 1                  Player 2
----       --------                  --------
1          8 of Hearts               6 of Diamonds
2          7 of Hearts               9 of Spades
3          3 of Spades               2 of Clubs
4          4 of Diamonds             7 of Spades
========== ===========               ===========
Hand Value      22                        24

Draw! Both players bust

-->**NEW ROUND**
Deal       Player 1                  Player 2
----       --------                  --------
1          6 of Clubs                5 of Diamonds
2          9 of Hearts               4 of Hearts
3          Ace of Spades             Queen of Diamonds
4          Queen of Hearts           King of Hearts
========== ===========               ===========
Hand Value      26                        29

Draw! Both players bust

-->**NEW ROUND**
Deal       Player 1                  Player 2
----       --------                  --------
1          4 of Spades               3 of Clubs
2          10 of Spades              4 of Clubs
3          6 of Spades               Queen of Spades
4          8 of Clubs                Ace OF Diamonds
========== ===========               ===========
Hand Value      28                        18

Player 2 wins! Player 1 busts

-->**NEW ROUND**
Deal       Player 1                  Player 2
----       --------                  --------
1          King of Clubs             9 of Clubs
2          5 of Clubs                2 of Spades
========== ===========               ===========
Hand Value      15                        11

The deck is finished!
Player 1 wins!

**SUMMARY GAME STATISTICS**
Rounds played:  8
Cards played: 52
Player 1 wins:  3
Player 2 wins:  3
'''
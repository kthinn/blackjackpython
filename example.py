import random

#say hello
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank +' of '+self.suit

class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_compo = ''
        for card in self.deck:
            deck_compo += '\n' + card.__str__()
        return 'Your deck has '+deck_compo

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.ace += 1

    def adjust_for_ace(self):
        if self.value > 21 and self.ace:
            self.value -= 10
            self.ace -= 1

class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How much would you like to bet?'))
        except:
            print('Sorry please type an integer')
        else:
            if chips.bet > chips.total:
                print('Sorry you dont have enough chips to bet. You have {}'.format(chips.total))
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    playing = True

    while playing:
        x = input('Hit or Stand? Enter h or s')

        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print('Player stands Dealers turn')
            playing = False
        else:
            print('Sorry I did not understand that. Please enter h or s')
            continue
        break

def show_some(player,dealer):
    print('\n DEALERS HANDS:')
    print(' <card hidden>')
    print(' ',dealer.cards[1])
    print('\n')
    print('PLAYERS HANDS:')
    for card in player.cards:
        print(' ',card)

def show_all(player,dealer):
    print('\n DEALERS HAND:')
    for card in dealer.cards:
        print(' ',card)
        print(dealer.value)
    print('\n')
    print('PLAYERS HAND:')
    for card in player.cards:
        print(' ',card)
        print(player.value)

def player_busts(player,dealer,chips):
    print('BUST PLAYER!')
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('PLAYER WINS!')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('BUST DEALER!')
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print('DEALER WINS!')
    chips.lose_bet()

def push(player,dealer):
    print('Dealer and player tie! PUSH')

###################IT'S TIME TO START##############
while True:
    print('WELCOME TO BLACKJACK')

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand,dealer_hand)

    while playing:
        hit_or_stand(deck,player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand,player_chips)
            break

    # if player_hand.value <= 21:
    #
    #     while dealer_hand.value < 17:
    #         hit(deck, dealer_hand)
    #
    #     show_all(player_hand, dealer_hand)

    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

            # Show all cards
        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif player_hand.value > dealer_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)

    print('\n Player Total Chips are at :{}'.format(player_chips.total))

    new_game = input('Would you like to play a new game? Enter Y or N.')
    if new_game[0].lower() == 'y':
        playing = True
    else:
        print('Thanks for playing the black jack game')
        break


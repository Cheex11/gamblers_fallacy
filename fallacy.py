import random

def Main():
    cash = 50000
    trial = 0
    bet_amount = 0
    prediction = 0
    flips = [0]
    response = ''
    max_cash = 50000

    while cash > 0 and trial < 500000:
        if three_in_a_row(flips) != False :
            prediction = three_in_a_row(flips)
            bet_amount = define_bet(flips)
        else:
            bet_amount = 0
        flip_coin(flips)
        if flips[-1] == prediction:
            cash = cash + bet_amount
            if cash > max_cash:
                max_cash = cash
        else:
            cash = cash - bet_amount

        trial += 1

    print "We left with",cash,"cash after",trial,"trials."
    print "The most money we ever had was",max_cash

def define_bet(flips):
    if three_in_a_row(flips) == False:
        return 0
    else:
        return 100

def three_in_a_row(flips):
    if len(flips) > 3:
        if flips[-1] == 1 and flips[-2] == 1 and flips[-3] == 1:
            return 1
        elif flips[-1] == 2 and flips[-2] == 2 and flips[-3] == 2:
            return 2
        else:
            return False
    else:
        return False

def flip_coin(flips):
    return flips.append(random.randrange(1,3))

if __name__ == '__main__':
    Main()

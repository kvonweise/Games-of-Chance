import random

money = 100

#Write your game of chance functions here
def coin_flip(guess, bet):
  print("Lets play the coin flip game!")
  print("For your guess, 1 equals heads and 2 equals tails")
  print("Your guess is", str(guess))
  if bet > 100: 
  	print("bet is too large, place a smaller bet")
  elif bet <= 0:
    print("No bet has been placed")
  num = random.randint(1,2)
  if num == 1:
    print("Heads!")
  elif num == 2: 
    print("Tails!")
  if num == guess: 
    print("You have won $", str(bet))
    return bet
  else: 
    print("You have lost $", str(bet))
    return -bet

#Call your game of chance functions here
def cho_han(guess, bet):
  print("Lets play the Cho Han!")
  print("For your guess, 1 equals even and 2 equals odds")
  print("Your guess is", str(guess))
  if bet > 100: 
  	print("bet is too large, place a smaller bet")
  elif bet <= 0:
    print("No bet has been placed")
  num1 = random.randint(1,6)
  print("die value is ", str(num1))
  num2 = random.randint(1,6)
  print("die value is ", str(num2))
  sum = (num1 + num2)
  print("Sum of the two dies are ", str(sum))
  if guess == 1  and sum % 2 == 0: 
    print("You have won $", str(bet))
    return bet
  if guess == 2 and sum % 2 == 1: 
    print("You have lost -$", str(bet))
    return -bet

def card_game(bet): 
  print("Lets play the a card game! WHo ever has the higher card wins.")
  if bet > 100: 
  	print("bet is too large, place a smaller bet")
  elif bet <= 0:
    print("No bet has been placed")
  card1 = random.randint(1,10)
  print("your card was", str(card1))
  card2 = random.randint(1,10)
  print("your card was", str(card2))
  if card1 == card2: 
    print("Tie!")
    return 0
  elif card1 > card2: 
    print("Player one wins $", str(bet))
    return bet
  elif card1 < card2: 
    print("Player two wins $", str(bet))
    return bet

def roulette(guess, bet):
  print("Lets play roulette!")
  print("Place a guess of either even, odd, or a specific number")
  print("Your guess is", guess)
  if bet > 100: 
  	print("bet is too large, place a smaller bet")
  elif bet <= 0:
    print("No bet has been placed")
  result = random.randint(0,37)
  if result == 37:
    print("Landed on 00")
  else: 
    print("Landed on ", str(result))
        
  if guess == "even".lower() and result % 2 == 0 and result != 0: 
    print("You win $ ", str(bet))
    return bet
  elif guess == "odd".lower() and result % 2 == 1 and result != 37: 
    print("You win $", str(bet))
    return bet
  elif guess == result: 
    print("You win $", str(bet * 35))
    return (bet * 35)
  else: 
    print("You lost $", str(bet))
    return -bet

money += coin_flip(1, 10)
money += card_game(15)
money += roulette("even", 10)
money += cho_han(2,4)







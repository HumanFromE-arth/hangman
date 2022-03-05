import random
import shapes
import time

print("                                                                      HANGMAN                                                                      ")

word = '''acting
action
active
actual
advice
advise
agency
almost
amount
answer
anyone
around
aspect
author
backed
barely
beauty
behalf
behind
belong
berlin
beyond
bishop
bought
branch
breath
bridge
bright
broken
budget
burden
carbon
castle
caught
charge
chosen
client
closed
closer
column
combat
coming
comply
costly
county
couple
course
covers
credit
custom
danger
deputy
design
detail
direct
double
driven
during
easily
eating
editor
employ
ending
enough
equity
ethnic
expand
export
fabric
facing
factor
failed
fairly
family
famous
father
figure
finger
fiscal
flight
flying
forced
forest
forget
formal
format
foster
fought
fourth
french
friend
garden
gather
german
golden
ground
growth
guilty
handle
hardly
health
height
holder
honest
impact
import
income
injury
intend
invest
island
itself
joseph
junior
labour
launch
lawyer
legacy
length
lights
likely
linked
listen
losing
lucent
mainly
making
margin
marine
marked
market
martin
master
mature
medium
mental
method
minute
mobile
modern
modest
module
mostly
mother
motion
moving
myself
nation
native
nature
nearby
nearly
nights
normal
notice
number
object
obtain
online
option
orange
parent
partly
patent
period
permit
person
phrase
picked
planet
player
plenty
pocket
police
policy
prince
prison
profit
proven
public
raised
random
rating
reason
region
remain
repair
replay
result
retail
retain
reward
robust
ruling
safety
sample
saving
saying
search
second
sector
senior
should
signal
signed
silent
silver
simple
simply
single
slight
social
sought
source
soviet
spoken
spread
spring
square
stable
steady
stolen
strain
stream
strike
string
strong
struck
studio
submit
surely
survey
switch
symbol
taking
tender
thanks
theory
thrown
timely
toward
travel
trying
unable
unique
united
unlike
update
useful
varied
vendor
versus
visual
volume
walker
wealth
weight
window
winter
wonder
wright
'''

time.sleep(1)
instructions = "Instructions: \n1.Do not enter repeated letters. \n2.Guess all the letters to make the word and save your man before he gets hung! \nBEST OF LUCK!"

print()

print(instructions)
time.sleep(1)
print()

choice = "y"

while choice == "y":
    words = word.split()
    h_word = words[random.randrange(len(words))]
    wrong = 1
    
    print("Here is your word: ")
    for i in h_word:
        print("_",end=" ")
    print()
    print()
    
    ans = ["_","_","_","_","_","_"]
    while wrong<=6 or ans == list(h_word):
        letter = input("Enter your guess in lowercase only: ")
        w_l = list(h_word)
        print()
        if letter in w_l:
            if w_l[0] == letter:
                ans[0] = letter
            else:
                ans[w_l.index(letter)] = letter

            print(" ".join(ans))
            print()
            time.sleep(1)
            print("Great")
        else:
            time.sleep(1)
            print("Oops!")
            wrong = wrong + 1
            time.sleep(1)
            if wrong == 2:
                shapes.hang_one()
            elif wrong == 3:
                shapes.hang_two()
            elif wrong == 4:
                shapes.hang_three()
            elif wrong == 5:
                shapes.hang_four()
            elif wrong == 6:
                shapes.hang_five()
            elif wrong == 7:
                shapes.hang_six()
                print()
                time.sleep(1)
                print("The answer was:",h_word)
                time.sleep(1)
    choice = input("Would you like to play again? y/n ")
    if choice == "n":
        break

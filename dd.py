from random import randint

print("nhập: kéo, búa, bao, súng ")

player = input()
bot = randint(0,2)

if bot == 0:
    bot = "búa"
if bot == 1:
    bot = "kéo"
if bot == 2:
    bot = "bao"
if bot == 3:
    bot = "súng"    

print("^_____^")
print("You choose : " + player)
print("bot choose:" + bot)
print("---")

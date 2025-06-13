import random

emotes = ["❤️","🥇","💵","⭐","7️⃣"]
betting = "yes"
debt = 0
winnings = 0
slot1 = ""
slot2 = ""
slot3 = ""

while betting == "yes":
    betting = input("$5 a spin. Play slots? (yes/no) ").lower()
    
    if betting != "yes":
        break

    debt += 5

    slot1 = random.choice(emotes)
    slot2 = random.choice(emotes)
    slot3 = random.choice(emotes)

    print(f"|  {slot1}  |  {slot2}  |  {slot3}  | ")
    if slot1 == slot2 and slot1 == slot3:
        winnings +=50
        print(f"You won! $50 added to winnings. Total winnings: {winnings}")
    else:
        print("You lost! Down another $5")

print(f"Total winnings: ${winnings}. Total loss: ${debt}. Net: ${winnings-debt}")    

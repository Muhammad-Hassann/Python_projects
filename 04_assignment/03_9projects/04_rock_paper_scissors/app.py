import random 

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n").lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return f"Both players selected ({user}). It's a tie!"

    # r > s, s > p, p > r
    if is_win(user, computer):
        return f"You chose ({user}) and the computer chose ({computer}). \nYou won!"

    return f"You chose {user} and the computer chose {computer}. \nYou lost!"

def is_win(player, opponent):
    # return true if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True    

print(play())        
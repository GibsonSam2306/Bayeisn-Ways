def play_game():
    player1_points = 0
    player2_points = 0

    for round in range(1, 11):
        player1 = input("Player1, enter r, p, or s: ")
        player2 = input("Player2, enter r, p, or s: ")

        if player1 == player2:
            print("Round", round, "Draw")
        elif (player1 == 'r' and player2 == 's'):
            print("Round", round, ": Player1 wins!")
            player1_points += 1
        elif (player1 == 's' and player2 == 'p'):
            print("Round", round, ": Player1 wins!")
            player1_points += 1
        elif (player1 == 'p' and player2 == 'r'):
            print("Round", round, ": Player1 wins!")
            player1_points += 1
        else:
            print("Round", round, ": Player2 wins!")
            player2_points += 1

    if player1_points > player2_points:
        print("Winner is Player1")
    elif player2_points > player1_points:
        print("Winner is Player2")
    else:
        print("Draw")

play_game()

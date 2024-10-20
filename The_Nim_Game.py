import random


def print_piles(piles):
    # pile_type = int(input("""
    #             Please select the preferred counter (1,2,3,4,5): 
    #                 1. Donuts: 🍩
    #                 2. Bitcoins: 🪙
    #                 3. Robux: ⏣
    #                 4. Soccer Balls: ⚽
    #                 5. Earth: 🌎
    #                 6. Maple Leaves: 🍁
    #                 7. Tony Tokens 🥚
    #                 8. Pranushan Points 🤓 
    #                 9. Kayden Kash 💷 
    #                 10. Ritvik Rupees 💰
    #                 11. Samuel 
                
    #                 """))
    for pile,counter in enumerate(piles):
        print(f"Pile {pile + 1}: {'lol ' * counter}")

def play_nim():
    # for i in range(3):
        
        # time.sleep(1)
    print("Welcome to the Nim Game!")
    
    print("\nRules:")
    print("""
        1. Start by placing counters into 3 piles.
        2. Player #1 picks a pile, then removes one or more counters from that pile. (It is okay to
        take the whole pile.)
        3. Player #2 picks a pile, then removes one or more counters from that pile.
        4. Player #1 plays again. (It is okay to choose a different pile this time.)
        5. Whichever player is forced to take the last counter is the LOSER.
          """)
    
    player1 = input("\nEnter Player 1's name: ")
    player2 = input("Enter Player 2's name: ")
    
    piles = [random.randint(5, 10), random.randint(5, 10), random.randint(5, 10)]
    
    current_turn = int(input("Which player would like to start? (1 or 2): "))
    if current_turn == 1:
         player_choose = player1
    elif current_turn == 2:
         player_choose = player2

    # player_choose = player1
    
    while True:
        print("\n")
        print(f"\n{player_choose}'s turn")
        
        while True:
            try:
                print_piles(piles)
                pile = int(input("Choose a pile (1, 2, or 3): ")) - 1
                if pile < 0 or pile > 2:
                    print("Invalid pile number. Please choose 1, 2, or 3.")
                    continue
                if piles[pile] == 0:
                    print("This pile is empty. Please choose another pile.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        
        while True:
            try:
                max_remove = min(3, piles[pile])
                remove = int(input(f"How many toothpicks to remove from pile {pile+1} ({max_remove}-1): "))
                if remove <= 0 or remove > max_remove:
                    print(f"Invalid number. You can remove 1 to {max_remove} toothpicks.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        
        piles[pile] -= remove
        
        if sum(piles) == 0:
            print(f"\nGame over! {player_choose} took the last toothpick and loses!")
            break
        
        player_choose = player2 if player_choose == player1 else player1

play_nim()

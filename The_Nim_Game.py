# Pranushan Piruthviraj
# 2024-10-25
# The Nim Game

import random
import time

piles = [random.randint(5, 10), random.randint(5, 10), random.randint(5, 10)]
pile_list = ["💲","🥚","𓍢ִ໋🍃","💷","💰","🪙","⏣ ","⚽","🌎","🍁",]

# AI win rates for different difficulties
ai_win_rates = {
    "Kayden": {"Easy": 0.3, "Medium": 0.4, "Hard": 0.5},
    "Ritvik": {"Easy": 0.4, "Medium": 0.5, "Hard": 0.6},
    "Samuel": {"Easy": 0.5, "Medium": 0.6, "Hard": 0.7}
}
COLOR_BLUE = "\033[94m"  
COLOR_PURPLE = "\033[95m" 
COLOR_GREEN = "\033[92m"  
COLOR_RESET = "\033[0m"   
# Personalized AI phrases with more variety
ai_phrases = {
    "Kayden": {
        "good_move": [
            f"{COLOR_PURPLE}Wait, that was so meta..{COLOR_RESET}",
            f"{COLOR_PURPLE}Wow, good job..{COLOR_RESET}",
            f"{COLOR_PURPLE}You ruined it, but i'll let it slide.{COLOR_RESET}",
            f"{COLOR_PURPLE}Oh my god bro, like that was so unecessary.{COLOR_RESET}"
        ],
        "bad_move": [
            f"{COLOR_PURPLE}Wait, do that again.{COLOR_RESET}",
            f"{COLOR_PURPLE}There's no way your iq is this low..{COLOR_RESET}",
            f"{COLOR_PURPLE}You're strange aren't you?{COLOR_RESET}",
            f"{COLOR_PURPLE}Wow, didn't see that coming... for a reason.{COLOR_RESET}"
        ],
        "player_wins": [
            f"{COLOR_PURPLE}Say thank you...for not slapping you.{COLOR_RESET}",
            f"{COLOR_PURPLE}Alright, calm down lil one.{COLOR_RESET}",
            f"{COLOR_PURPLE}Like, you aint all that, calm down now.{COLOR_RESET}",
            f"{COLOR_PURPLE}Wow, Congrats, want a cookie or something?{COLOR_RESET}"
        ],
        "player_loses": [
            f"{COLOR_PURPLE}Yea, you're so crazy bro.{COLOR_RESET}",
            f"{COLOR_PURPLE}Better luck next time... or not.{COLOR_RESET}",
            f"{COLOR_PURPLE}I'd say nice try, but we both know that's not true.{COLOR_RESET}",
            f"{COLOR_PURPLE}Lord I thank you for sunshine..thank you for rain...{COLOR_RESET}"
        ]
    },
    "Ritvik": {
        "good_move": [
            f"{COLOR_GREEN}Ooooh{COLOR_RESET}",
            f"{COLOR_GREEN}Okay, hold on.{COLOR_RESET}",
            f"{COLOR_GREEN}That's actually crazy how you saw that.{COLOR_RESET}",
            f"{COLOR_GREEN}Okay, okay, that was pretty good.{COLOR_RESET}"
        ],
        "bad_move": [
            f"{COLOR_GREEN}Yea, okay, nice one 💀{COLOR_RESET}",
            f"{COLOR_GREEN}Save our souls 🙏.{COLOR_RESET}",
            f"{COLOR_GREEN}You really thought that was it, huh?{COLOR_RESET}",
            f"{COLOR_GREEN}What was that 💀{COLOR_RESET}"
        ],
        "player_wins": [
            f"{COLOR_GREEN}Oh my gawd broo{COLOR_RESET}",
            f"{COLOR_GREEN}Grrrrr{COLOR_RESET}",
            f"{COLOR_GREEN}Luck carried smh 🙏.{COLOR_RESET}",
            f"{COLOR_GREEN}Just a warm up round, lets play again.{COLOR_RESET}"
        ],
        "player_loses": [
            f"{COLOR_GREEN}Pranushan level sell bro 💀{COLOR_RESET}",
            f"{COLOR_GREEN}Never touch this game again.{COLOR_RESET}",
            f"{COLOR_GREEN}Okay, Okay, that was a close game.{COLOR_RESET}",
            f"{COLOR_GREEN}Stay in your lane lil bro.{COLOR_RESET}"
        ]
    },
    "Samuel": {
        "good_move": [
            f"{COLOR_BLUE}Wow, you did something that's ACTUALLY productive.{COLOR_RESET}",
            f"{COLOR_BLUE}I'm mildly surprised by your competence.{COLOR_RESET}",
            f"{COLOR_BLUE}Not terrible, I guess.{COLOR_RESET}",
            f"{COLOR_BLUE}You might actually have a brain cell.{COLOR_RESET}"
        ],
        "bad_move": [
            f"{COLOR_BLUE}Bro, I'm losing braincells by watching this..{COLOR_RESET}",
            f"{COLOR_BLUE}Are you even trying at this point?{COLOR_RESET}",
            f"{COLOR_BLUE}That move was... interesting? i guess..{COLOR_RESET}",
            f"{COLOR_BLUE}Bro..I've seen better moves from Tony.{COLOR_RESET}"
        ],
        "player_wins": [
            f"{COLOR_BLUE}To be honest, I couldn't be bothered to actually try against you so..{COLOR_RESET}",
            f"{COLOR_BLUE}Congratulations, you've peaked in life.{COLOR_RESET}",
            f"{COLOR_BLUE}Almost 100 percent of the rounds you play against me have a guaranteed chance of you losing, which if you think about it, means that your win was complete luck.{COLOR_RESET}",
            f"{COLOR_BLUE}Great, now I have to pretend to be impressed.{COLOR_RESET}"
        ],
        "player_loses": [
            f"{COLOR_BLUE}You want to play again? Sure.{COLOR_RESET}",
            f"{COLOR_BLUE}You're shocking absolutely no one with that result.{COLOR_RESET}",
            f"{COLOR_BLUE}Maybe try something easier, like tic-tac-toe?{COLOR_RESET}",
            f"{COLOR_BLUE}Actually Crazy.{COLOR_RESET}"
        ]
    }
}

loading_quotes = ["If everyone is thinking alike, then somebody isnt thinking.\n - George S. Patton",
                  "What counts it not necessarily the size of the dog in the fight - it's the size of the fight in the dog. \n -  Dwight D. Eisenhower",
                  "We're in a giant car heading towards a brick wall and everyone's arguing over whree they're going to sit. \n - David Suzuki",
                  """We're rounding 'em up in a very humane way, in a very nice way. And they're going to be happy because they want to be legalized. 
                    And, by the way, I know it doesn't sound nice. But not everything is nice. \n - Donald Trump on domestic policy"""
                  ]

def delayed_text(text):
    for char in text:
        print(char, end='')
        time.sleep(0.04)
    print("\n")

def loading_screen():
    global loading_quotes
    delayed_text(loading_quotes[random.randint(0,3)])
                

def ai_comment(ai_name, situation):
    phrases = ai_phrases[ai_name][situation]
    return f"\n{ai_name}: {random.choice(phrases)}"


def ai_move(piles, ai_name, difficulty, game_version):
    if game_version == 1:  # Last to grab loses
        # Implement logic to avoid losing
        if is_forced_last_move(piles):
            return random_move(piles)  # Just make a random move
        else:
            return optimal_move(piles,game_version)  # Prefer optimal moves
    else:  # Last to grab wins
        if random.random() < ai_win_rates[ai_name][difficulty]:
            return optimal_move(piles)
        else:
            return random_move(piles)

def optimal_move(piles, game_version):
    nim_sum = 0
    for pile in piles:
        nim_sum ^= pile

    # In the losing version, check for forced moves
    if game_version == 1:
        # If nim_sum is 0, the player is in a losing position if they play optimally
        if nim_sum == 0:
            return random_move(piles)

        for i, pile in enumerate(piles):
            if pile > 0 and (pile - 1) ^ nim_sum < pile:
                # The AI can make a move that will force the player into a losing position
                return i, 1  # Prefer taking one to avoid losing in the next turn
            elif pile > 1 and (pile - 2) ^ nim_sum < pile:
                return i, 2
            elif pile > 2 and (pile - 3) ^ nim_sum < pile:
                return i, 3

    # Default behavior for winning version
    for i, pile in enumerate(piles):
        if pile > 0 and (pile ^ nim_sum) < pile:
            return i, min(3, pile - (pile ^ nim_sum))

    return random_move(piles)


def random_move(piles):
    non_empty_piles = [i for i, pile in enumerate(piles) if pile > 0]
    pile = random.choice(non_empty_piles)
    remove = random.randint(1, min(3, piles[pile]))  
    return pile, remove

def give_hint(piles):
    pile, remove = optimal_move(piles)
    return f"Consider removing {remove} from pile {pile + 1}."

def ai_comment(ai_name, situation):
    phrases = ai_phrases[ai_name][situation]
    return f"\n{ai_name}: {random.choice(phrases)}"
    
    return random_move(piles)

def give_hint(piles):
    pile, remove = optimal_move(piles)
    return f"Consider removing {remove} from pile {pile + 1}."

def ai_comment(ai_name, situation):
    phrases = ai_phrases[ai_name][situation]
    phrase = random.choice(phrases)
    print(f"\n{ai_name}: {phrase}")
    pause_for_player()

def is_forced_last_move(piles):
    return sum(piles) == 1

def pause_for_player():
    input("Press Enter to continue...")

def play_nim(piles):
    global pile_list
    loading_screen()
    pause_for_player()
    print("Welcome to the Nim Game!")

    while True:
        game_version = input("Choose game version:\n1. Last to grab a counter loses\n2. Last to grab a counter wins\nEnter 1 or 2: ")
        if game_version in ['1', '2']:
            game_version = int(game_version)
            break
        print("Invalid input. Please enter 1 or 2.")

    # Display rules based on game version
    print("\nRules:")
    if game_version == 1:
        print("""
        1. Start by placing counters into 3 piles.
        2. Players take turns removing one or more counters from a single pile.
        3. A player must remove at least one counter on their turn, and may remove up to 3 counters.
        4. The player forced to take the last counter LOSES the game.
        """)
    else:
        print("""
        1. Start by placing counters into 3 piles.
        2. Players take turns removing one or more counters from a single pile.
        3. A player must remove at least one counter on their turn, and may remove up to 3 counters.
        4. The player who takes the last counter WINS the game.
        """)
    
    
    game_mode = input("Choose game mode (PvP/PvAI): ").lower()
    assisted_mode = input("Do you want to play in assisted mode? (yes/no): ").lower() == "yes"
    
    if game_mode == "pvp":
        player1 = input("\nEnter Player 1's name: ")
        player2 = input("Enter Player 2's name: ")
        ai_name = "Samuel"  # Default AI for hints in PvP mode
        ai_difficulty = "Medium"
    else:
        player1 = input("\nEnter your name: ")
        ai_name = input("Choose AI opponent (Kayden/Ritvik/Samuel): ")
        ai_difficulty = input("Choose AI difficulty (Easy/Medium/Hard): ")
        player2 = ai_name
    
    pile_type = int(input("""
    Please select the preferred counter (1,2,3,4,5,6,7,8,9, or 10):
        1. Samuel Sols:💲        
        2. Tony Tokens: 🥚
        3. Pranushan Points: 𓍢ִ໋🍃 
        4. Kayden Kash: 💷 
        5. Ritvik Rupees: 💰                          
        6. Bitcoins: 🪙
        7. Robux: ⏣
        8. Soccer Balls: ⚽
        9. Earth: 🌎
        10. Maple Leaves: 🍁
        
        
                
                    """))
    for pile,counter in enumerate(piles):
        print(f"Pile {pile + 1}: {pile_list[pile_type-1] * counter}")

    current_turn = int(input("Which player would like to start? (1 or 2): "))
    player_choose = player1 if current_turn == 1 else player2

    hints_used = {player1: 0, player2: 0}

    while True:
        print("\n")
        print(f"\n{player_choose}'s turn")
        
        for pile, counter in enumerate(piles):
            print(f"Pile {pile + 1}: {pile_list[pile_type-1] * counter}")
        
        if is_forced_last_move(piles):
            next_player = player2 if player_choose == player1 else player1
            if game_version == 1:  # Last to grab loses
                print(f"\n{player_choose}, you must take the last remaining counter, so")
                print(f"you lose. {next_player} wins!")
            else:  # Last to grab wins
                print(f"\n{player_choose}, you must take the last remaining counter, so")
                print(f"you win. {next_player} loses!")
            
            if game_mode == "pvai":
                if (next_player == player1 and game_version == 2) or (player_choose == player1 and game_version == 1):
                    print(ai_comment(ai_name, "player_wins"))
                else:
                    print(ai_comment(ai_name, "player_loses"))
            break

        if player_choose == player2 and game_mode == "pvai":
            pile, remove = ai_move(piles, ai_name, ai_difficulty, game_version)
            print(f"{player_choose} removes {remove} from pile {pile + 1}")


        else:
            while True:
                if assisted_mode:
                    move = input("Choose a pile (1, 2, or 3) or type 'help' for a hint (max 2 hints): ")
                    if move.lower() == 'help':
                        if hints_used[player_choose] < 2:
                            print(give_hint(piles))
                            hints_used[player_choose] += 1
                        else:
                            print("You've used all your hints!")
                        continue
                else:
                    move = input("Choose a pile (1, 2, or 3): ")
                
                try:
                    pile = int(move) - 1
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
                    remove_input = input(f"How many counters to remove from pile {pile + 1} (1-{max_remove}) or type 'back' to choose again: ")
                    if remove_input.lower() == 'back':  
                        print("Going back to pile selection...")
                        break  
                    remove = int(remove_input)
                    if remove <= 0 or remove > max_remove:
                        print(f"Invalid number. You can remove 1 to {max_remove} counters.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number.")
            if remove_input.lower() == 'back':
                continue
            # AI comments on player's move (only in PvAI mode)
            if game_mode == "pvai" and not is_forced_last_move(piles): # Not the last move
                if (pile, remove) == optimal_move(piles,game_version):
                    print(ai_comment(ai_name, "good_move"))
                else:
                    print(ai_comment(ai_name, "bad_move"))
        
        piles[pile] -= remove
        
            # Check if the game is over after the current move
        if sum(piles) == 0:
            if game_version == 1:
                print(f"\nGame over! {player_choose} took the last counter and loses!")
                winner = player2 if player_choose == player1 else player1
            else:
                print(f"\nGame over! {player_choose} took the last counter and wins!")
                winner = player_choose
            
            if game_mode == "pvai":
                if winner == player1:
                    print(ai_comment(ai_name, "player_wins"))
                else:
                    print(ai_comment(ai_name, "player_loses"))
            break
        if sum(piles) == 1:
            next_player = player2 if player_choose == player1 else player1
            if game_version == 1:  # Last to grab loses
                print(f"\n{next_player}, you must take the last remaining counter, so")
                print(f"you lose. {player_choose} wins!")
            else:  # Last to grab wins
                print(f"\n{next_player}, you must take the last remaining counter, so")
                print(f"you win. {player_choose} loses!")
            break

        player_choose = player2 if player_choose == player1 else player1
    
play_nim(piles)

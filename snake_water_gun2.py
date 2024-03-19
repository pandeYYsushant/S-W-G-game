import random

class SnakeWaterGun:
    def __init__(self):
        self.user_score = 0
        self.comp_score = 0
        self.choices = ['snake', 'water', 'gun']
    
    @staticmethod
    def get_comp_choice():
        return random.choice(['snake', 'water', 'gun'])
    
    @classmethod
    def evaluate(cls, user_choice, comp_choice):
        if user_choice == comp_choice:
            return "It's a tie!"
        elif (user_choice, comp_choice) in [('snake', 'water'), ('water', 'gun'), ('gun', 'snake')]:
            return "You win!"
        else:
            return "Computer wins!"
    
    def play(self, rounds):
        print("Welcome to Snake Water Gun Game!")
        for _ in range(rounds):
            user_choice = input("Enter your choice (snake/water/gun): ").lower()
            if user_choice not in self.choices:
                print("Invalid choice. Try again.")
                continue
            
            comp_choice = self.get_comp_choice()
            print(f"Computer chose: {comp_choice}")
            
            result = self.evaluate(user_choice, comp_choice)
            print(result)
            
            if result == "You win!":
                self.user_score += 1
            elif result == "Computer wins!":
                self.comp_score += 1
        
        print("Game Over!")
        print("Final Scores:")
        print(f"You: {self.user_score}, Computer: {self.comp_score}")
        if self.user_score > self.comp_score:
            print("Congratulations! You win!")
        elif self.user_score < self.comp_score:
            print("Sorry! Computer wins!")
        else:
            print("It's a tie!")

if __name__ == "__main__":
    game = SnakeWaterGun()
    game.play(rounds=3)  # You can adjust the number of rounds here
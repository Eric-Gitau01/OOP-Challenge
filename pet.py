class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.hapiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, slef.hunger - 3)
        self.happiness = min(10, self.happines + 1)
        print(f"{self.name} is eating...🍫")
    
    def play(self):
        if self.energy >= 2:
            self.energy = max(0, self.energy -2)
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} is playing ....")
        else:
             print(f"{self.name} is too tired to play1 Need sleep.")

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = max(0, self.happiness - 1)

        print(f"{self.name} learned a new trick: {trick}!")

    def show_trick(self):
        if self.tricks:
            print(f"{self.name} Kmowa these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
    def get_status(self):
        print(f"\n{self.name}'s current status:")
        print(f"hunger: {self.hunnger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"happiness: {self.happiness}/10")
        if self.trick: 
            print(f"Tricks: {self}")
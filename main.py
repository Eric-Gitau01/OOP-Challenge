from pet import Pet

def main():
    print("creating a new pet named Max..")
    my_pet = Pet("Max")

    #Test basic action
    my_pet.eat()
    my_pet.play()
    my_pet.sleep()

    #Train some tricks
    my_pet.train('roll over')
    my_pet.train('play dead')

    # show status and ticks
    my_pet.get_status()
    my_pet.show_tricks()

    #Edge case testing
    print("\nTesting edge case:")
    my_pet.energy = 1
    my_pet.play()
    my_pet.my_hunger = 0
    my_pet.eat()

if __name__ == "__main__":
    main()


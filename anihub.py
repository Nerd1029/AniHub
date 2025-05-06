import os

#views animals based on animal type prompt

print("Welcome to AniHub!")

rodents = [
    # Living rodents
    "Mouse (living)",
    "Rat (living)",
    "Squirrel (living)",
    "Beaver (living)",
    "Porcupine (living)",
    "Guinea Pig (living)",
    "Capybara (living)",
    "Hamster (living)",
    "Chinchilla (living)",
    "Gerbil (living)",
    "Lemming (living)",
    "Vole (living)",
    "Agouti (living)",
    "Pacarana (living)",
    "Nutria (living)",
    "Dormouse (living)",
    "Marmot (living)",
    "Groundhog (living)",
    "Gopher (living)",
    "Prairie Dog (living)",
    "Kangaroo Rat (living)",
    "Kangaroo Mouse (living)",
    "Jerboa (living)",
    "Spiny Mouse (living)",
    "Multimammate Mouse (living)",
    "Acouchi (living)",
    "Tuco-tuco (living)",
    "Viscacha (living)",
    "Springhare (living)",
    "Zokor (living)",
    "Desert Rat (living)",
    "Tree Rat (living)",
    "Brush-tailed Rat (living)",
    "Deer Mouse (living)",
    "Cotton Rat (living)",
    "Harvest Mouse (living)",
    "Swamp Rat (living)",

    # Extinct rodents
    "Josephoartigasia monesi (giant extinct rodent, largest ever discovered)",
    "Neoepiblema acreensis (large extinct South American rodent)",
    "Ischyromys (one of the earliest known rodents)",
    "Reithroparamys (early rodent from the Eocene)",
    "Paramys (primitive rodent, ancestor of squirrels and beavers)"
]

arachnids = [
    # Living arachnids
    "Spider (living)",
    "Scorpion (living)",
    "Tick (living)",
    "Mite (living)",
    "Harvestman (living)",
    "Camel Spider (living)",
    "Whip Spider (living)",
    "Whip Scorpion (living)",
    "Pseudoscorpion (living)",
    "Tailless Whip Scorpion (living)",
    "Sun Spider (living)",
    "Daddy Longlegs (living)",
    "Trapdoor Spider (living)",
    "Wolf Spider (living)",
    "Jumping Spider (living)",
    "Orb-weaver (living)",
    "Tarantula (living)",
    "Brown Recluse (living)",
    "Black Widow (living)",
    "Funnel-web Spider (living)",
    "Huntsman Spider (living)",
    "Redback Spider (living)",
    "Mouse Spider (living)",
    "Goliath Birdeater (living)",
    "Peacock Spider (living)",
    "Banana Spider (living)",
    "Hobo Spider (living)",
    "Sac Spider (living)",
    "Tick Mite (living)",
    "Dust Mite (living)",
    "Chigger (living)",
    "Demodex Mite (living)",
    "Lone Star Tick (living)",
    "Deer Tick (living)",
    "Dog Tick (living)",

    # Extinct arachnids
    "Trigonotarbus (extinct spider-like arachnid from the Devonian)",
    "Palaeotarbus jerami (extinct Devonian arachnid)",
    "Permarachne novokshonovi (Permian fossil with scorpion-like traits)",
    "Idmonarachne brasieri (extinct close relative of spiders, from the Carboniferous)",
    "Attercopus fimbriunguis (extinct early spider with a tail-like spinneret)",
    "Chimerarachne yingi (transitional fossil between spiders and ancient relatives)"
]

mammals = [
    "Human (living)",
    "Lion (living)",
    "Elephant (living)",
    "Whale (living)",
    "Bat (living)",
    "Woolly Mammoth (extinct)",
    "Saber-toothed Cat (extinct)",
    "Diprotodon (extinct)"
]

birds = [
    "Pigeon (living)",
    "Ostrich (living)",
    "Penguin (living)",
    "Bald Eagle (living)",
    "Dodo (extinct)",
    "Passenger Pigeon (extinct)",
    "Great Auk (extinct)"
]

reptiles = [
    "Crocodile (living)",
    "Komodo Dragon (living)",
    "Green Iguana (living)",
    "Tuatara (living)",
    "Tyrannosaurus rex (extinct)",
    "Triceratops (extinct)",
    "Ichthyosaur (extinct)"
]

amphibians = [
    "Frog (living)",
    "Salamander (living)",
    "Caecilian (living)",
    "Beelzebufo (extinct)",
    "Gerobatrachus (extinct)"
]

fish = [
    "Shark (living)",
    "Salmon (living)",
    "Clownfish (living)",
    "Coelacanth (living)",
    "Dunkleosteus (extinct)",
    "Megalodon (extinct)",
    "Placoderm (extinct)"
]

insects = [
    "Ant (living)",
    "Bee (living)",
    "Butterfly (living)",
    "Dragonfly (living)",
    "Meganeura (extinct)",
    "Palaeodictyoptera (extinct)"
]

invertebrates = [
    "Octopus (living)",
    "Squid (living)",
    "Jellyfish (living)",
    "Trilobite (extinct)",
    "Ammonite (extinct)",
    "Hallucigenia (extinct)"
]

marine_mammals = [
    "Dolphin (living)",
    "Seal (living)",
    "Sea Otter (living)",
    "Basilosaurus (extinct)",
    "Desmostylus (extinct)"
]

while True:
    type = input("What type of animal would you like to see? (ie. rodents) (You can also type 'credits' to see where the animals are sourced from.)")

    if type == "rodent" or type == "rodents":
        print(rodents)
        print("Press enter to continue.")
        input("")
        os.system('clear')

    elif type == "arachnid" or type == "arachnids":
        print(arachnids)
        print("Press enter to continue.")
        input("")
        os.system('clear')

    elif type == "mammal" or type == "mammals":
        print(mammals)
        print("Press enter to continue.")
        input("")
        os.system('clear')

    elif type == "bird" or type == "birds":
        print(birds)
        print("Press enter to continue.")
        input("")
        os.system('clear')
    
    elif type == "reptile" or type == "reptiles":
        print(reptiles)
        print("Press enter to continue.")
        input("")
        os.system('clear')
    
    elif type == "amphibian" or type == "amphibians":
        print(amphibians)
        print("Press enter to continue.")
        input("")
        os.system('clear')
    
    elif type == "fish":
        print(fish)
        print("Press enter to continue.")
        input("")
        os.system('clear')
    
    elif type == "insect" or type == "insects":
        print(insects)
        print("Press enter to continue.")
        input("")
        os.system('clear')
    
    elif type == "invertebrate" or type == "invertebrates":
        print(invertebrates)
        print("Press enter to continue.")
        input("")
        os.system('clear')
    
    elif type == "marine mammal" or type == "marine mammals":
        print(marine_mammals)
        print("Press enter to continue.")
        input("")
        os.system('clear')
    
    elif type == "credits":
        print("Thanks to OpenAI's ChatGPT for providing the animals and their data!")
        print("Press enter to continue.")
        input("")
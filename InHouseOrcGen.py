from random import randrange
#auto generation for Total Warhammer Orcs & Goblins Army following the following rules
# no more than 25% of points on Lord, But atleast 1 lord
# no more than 25% of points on Hero
# atleast 25% points spent on Core
# no more than 50% points spent on Special, no more than 3 of the same unit
# no more than 25% points spend on Rare, no more than 2 of the same unit
Core = {"Orc Boyz": 450, "Orc Arrer Boyz": 500, "Savage Orc Boyz": 550, "Big 'Uns": 700, "Goblin Wolf Riders": 300, "Goblins": 300, "Night Goblins": 400, "Forest Goblin Spider Riders": 450, "Savage Orc Big 'Uns": 850, "Night Goblin Fanatics": 450, "Goblin Archers": 350, "Night Goblin Archers": 500, "Night Goblin Archer Fanatics": 550, "Savage Orc Arrer Boyz": 550, "Forest Goblin SPider Rider Archers": 500}
Special = {"Black Orcs": 1000, "Orc Boar Boyz": 750, "Goblin Wolf Chariot": 600, "Orc Boar Chariot": 750, "Trolls": 800, "Orc Boar Boy Big 'Uns": 900, "Savage Orc Boar Boyz": 850, "Savage Orc Boar Boy Big 'Uns": 1000}
Rare = {"Giant": 1600, "Rock Lobba": 600, "Doom Diver": 800, "Arachnarok": 2000}
Lord = {"Grimgor Ironhide": 1700, "Azhag the Slaughterer": 1400, "Azhag the Slaughterer with Wyvern": 1900, "Orc Warboss": 1200, "Orc Warboss with Boar": 1450, "Orc Warboss with Wyvern": 1850, "Great Goblin Shaman": 900, "Great Goblin Shaman with Wolf": 1100}
Hero = {"Goblin Boss": 500, "Goblin Boss with Wolf": 600, "Goblin Boss with Spider": 700, "Night Goblin Shaman": 700, "Orc Shaman": 850, "Orc Shaman with Boar": 1200}
Points = input("What is your starting gold?")
LordPoints = Points*0.25
SpecialPoints = Points*0.5
CorePoints = Points*0.25
RarePoints = Points*0.25
HeroPoints = Points*0.25

LC = randrange(0, 8, 1)
 for Lord[LC] >= LordPoints LC = randrange(0, 8, 1)
 LordChoice = Lord[LC]
 print LordChoice

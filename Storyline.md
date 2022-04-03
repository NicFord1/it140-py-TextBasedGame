You're the hero visiting the Dangerous Monarch's castle. The Dangerous Monarch is creating havoc in the castle and the hero must prevent the Dangerous Monarch from creating too much havoc upon the castle and it's visitors. Collect all items to win and save the castle.

Characters
    Villian (Boss) -- Dangerous Monarch
    Hero (Player) -- Incredible Geo

GAME_MAP = {
    "Throne Room": {"East": "Garderobe", "South": "Queen's Room", "Item": "Spores"},
    "Garderobe": {"West": "Throne Room", "Item": "Doubloons"},
    "Queen's Room": {"North": "Throne Room", "East": "Atrium", "Item": "Key"},
    "Refectory": {"East": "Passageway 1", "South": "Galley", "West": "Atrium", "Item": "Silver Knife"},
    "Atrium": {"East": "Refectory", "South": "Meditation Room", "West": "Queen's Room"},
    "Passageway 1": {"East": "Passageway 2", "South": "Peasant's Mess", "West": "Refectory"},
    "Passageway 2": {"North": "Stables", "East": "Depository", "South": "Passageway 3", "West": "Passageway 1"},
    "Passageway 3": {"North": "Passageway 2", "East": "Storage Room", "South": "Study"},
    "Meditation Room": {"North": "Atrium", "South": "Sunroom", "Item": "Ouija Board"},
    "Galley": {"North": "Refectory", "East": "Peasant's Mess", "Item": "Rancid Cheesecake"},
    "Peasant's Mess": {"North": "Passageway 1", "South": "Chapel", "West": "Galley", "Item": "Health Potion"},
    "Chapel": {"North": "Peasant's Mess", "West": "Sunroom", "Item": "Sweets"},
    "Sunroom": {"North": "Meditation Room", "East": "Chapel", "South": "Courtyard", "Item": "Swim Trunks"},
    "Stables": {"South": "Passageway 2", "Item": "Rat Poison"},
    "Depository": {"West": "Passageway 2", "Item": "Excrement"},
    "Storage Room": {"West": "Passageway 3", "Item": "Tacks"},
    "Study": {"North": "Passageway 3", "Item": "Manual"},
    "Courtyard": {"North": "Sunroom", "Item": VILLAIN}
}

def expand(d):
    return d


gem_10 = expand({
    1: "Azurite",
    2: "Banded Agate",
    3: "Blue Quartz",
    4: "Eye Agate",
    5: "Hematite",
    6: "Lapis Lazuli",
    7: "Malchite",
    8: "Moss Agate",
    9: "Obsidian",
    10: "Rhodochrosite",
    11: "Tiger Eye",
    12: "Turquoise"
})

gem_50 = expand({
    1: "Bloodstone",
    2: "Carnelian",
    3: "Chalcedony",
    4: "Chrysoprase",
    5: "Citrine",
    6: "Jasper",
    7: "Moonstone",
    8: "Onyx",
    9: "Quartz",
    10: "Sardonyx",
    11: "Star rose quartz",
    12: "Zircon"
})

gem_100 = expand({
    1: "Amber",
    2: "Amethyst",
    3: "Chrysoberyl",
    4: "Coral",
    5: "Garnet",
    6: "Jade",
    7: "Jet",
    8: "Pearl",
    9: "Spinel",
    10: "Tourmaline"
})

gem_500 = expand({
    1: "Alexandrite",
    2: "Aquamarine",
    3: "Black Pearl",
    4: "Blue Spinel",
    5: "Peridot",
    6: "Topaz"
})

gem_1000 = expand({
    1: "Black Opal",
    2: "Blue Sapphire",
    3: "Emerald",
    4: "Fire Opal",
    5: "Opal",
    6: "Star Ruby",
    7: "Star Sapphire",
    8: "Yellow Sapphire"
})

gem_5000 = expand({
    1: "Black Sapphire",
    2: "Diamond",
    3: "Jacinth",
    4: "Ruby"
})

art_25 = expand({
    1: "Silver ewer",
    2: "Carved bone statuette",
    3: "Small gold bracelet",
    4: "Cloth-of-gold vestments",
    5: "Black velvet mask stitched with silver thread",
    6: "Copper chalice with silver filigree",
    7: "Pair of engraved bone dice",
    8: "Small mirror set in a painted wooden frame",
    9: "Embroidered silk handkerchief",
    10: "gold locket with a painted portrait inside"
})

art_250 = expand({
    1: "Gold ring set with bloodstones",
    2: "Carved ivory statuette",
    3: "Large gold bracelet",
    4: "Silver necklace with gemstone pendant",
    5: "Bronze crown",
    6: "Silk robe with gold embroidery",
    7: "Large well-made tapestry",
    8: "Brass mug with jade inlay",
    9: "Box of turquoise animal figurines",
    10: "Gold bird cage with electrum filigree"
})

art_750 = expand({
    1: "Silver chalice with moonstones",
    2: "Sliver-plated steel longsword with jet set in hilt",
    3: "Carved hard of exotic wood with ivory inlay and zirconb gems",
    4: "Small gold idol",
    5: "Gold dragon comb set with red garnets as eyes",
    6: "Bottle stopper cork embossed with gold leaf and set with amethysts",
    7: "Ceremonial electrum dagger with a black pearl in the pommel",
    8: "Silver and gold brooch",
    9: "Obsidian statuette with gold fittings and inlay",
    10: "Painted gold war mask"
})

art_2500 = expand({
    1: "Fine gold chain set with a fire opal",
    2: "Old masterpiece painting",
    3: "Embroidered silk and velvet mantle set with numerous moonstones",
    4: "Platinum bracelet set with a sapphire",
    5: "Embroidered glove set with jewel chips",
    6: "Jeweled anklet",
    7: "Gold music box",
    8: "Gold circlet set with four aquamarines",
    9: "Eye patch with a mock eye set in blue sapphire and moonstone",
    10: "A necklace string of small pink pearls"
})

art_7500 = expand({
    1: "Jeweled gold crown",
    2: "Jeweled platinum ring",
    3: "Small gold statuette set with rubies",
    4: "Gold cup set with emeralds",
    5: "Gold jewlery box with platinum filigree",
    6: "Painted gold child sarcophagus",
    7: "Jade game board with solid gold playing pieces",
    8: "Bejeweled ivory drinking horn with gold filigree"
})

item_a = expand({
    range(1, 50): "Potion of healing",
    range(51, 60): "Spell scroll - cantrip",
    range(61, 70): "Potion of climbing",
    range(71, 90): "Spell scroll - 1st level",
    range(91, 94): "Spell scroll - 2nd level",
    range(95, 98): "Potion of greater healing",
    99: "Bag of holding",
    100: "Driftglobe"
})

item_b = expand({
    range(1, 15): "Potion of greater healing",
    range(16, 22): "Potrange of keys in dictionaryion of fire breath",
    range(23, 29): "Potion of resistance",
    range(30, 34): "Ammunition, +1",
    range(35, 39): "Potion of animal friendship",
    range(40, 44): "Potion of hill giant strength",
    range(45, 49): "Potion of growth",
    range(50, 54): "Potion of water breathing",
    range(55, 59): "Spell scroll - 2nd level",
    range(60, 64): "Spell scroll - 3rd level",
    range(65, 67): "Bag of holding",
    range(68, 70): "Keoghtom ointment",
    range(71, 72): "Oil of slipperiness",
    range(74, 75): "Dust of disappearance",
    range(76, 77): "Dust of dryness",
    range(78, 79): "Dust of sneezing and choking",
    range(80, 81): "Elemental gem",
    range(82, 83): "Philter of love",
    84: "Alchemy jug",
    85: "Cap of water breathing",
    86: "Cloak of the manta ray",
    87: "Driftglobe",
    88: "Goggles of night",
    89: "Helm of comprehending languages",
    90: "Immovable rod",
    91: "Lantern of revealing",
    92: "Mariner armor",
    93: "Mithral armor",
    94: "Potion of poison",
    95: "Ring of swimming",
    96: "Robe of useful items",
    97: "Rope of climbing",
    98: "Saddle of the cavalier",
    99: "Wand of magic detection",
    100: "Wand of secrets"
})

item_c = expand({
    range(1, 15): "Potion of superior healing",
    range(16, 22): "Spell scroll - 4th level",
    range(23, 27): "Ammunition, +2",
    range(28, 32): "Potion of clairvoyance",
    range(33, 37): "Potion of diminution",
    range(38, 42): "Potion of gaseous form",
    range(43, 47): "Potion of frost giant strength",
    range(48, 52): "Potion of stone giant strength",
    range(53, 57): "Potion of heroism",
    range(58, 62): "Potion of invulnerability",
    range(63, 67): "Potion of mind reading",
    range(68, 72): "Spell scroll - 5th level",
    range(73, 75): "Elixer of health",
    range(76, 78): "Oil of etherealness",
    range(79, 81): "Potion of fire giant strength",
    range(82, 84): "Quaal feather token",
    range(85, 87): "Scroll of protection",
    range(88, 89): "Bag of beans",
    range(90, 91): "Bead of force",
    92: "Chime of endless water",
    93: "Decanter of endless water",
    94: "Eyes of minute seeing",
    95: "Folding boat",
    96: "Heward handy haversack",
    97: "Horseshoes of speed",
    98: "Necklace of fireballs",
    99: "Periapt of health",
    100: "Sending stones"
})

item_d = expand({
    range(1, 20): "Potion of supreme healing",
    range(21, 30): "Potion of invisibility",
    range(31, 40): "Potion of speed",
    range(41, 50): "Spell scroll - 6th level",
    range(51, 57): "Spell scroll - 7th level",
    range(58, 62): "Ammunition, +3",
    range(63, 67): "Oil of sharpness",
    range(68, 72): "Potion of flying",
    range(73, 77): "Potion of cloud giant strength",
    range(78, 82): "Potion of longevity",
    range(83, 87): "Potion of vitality",
    range(88, 92): "Spell scroll - 8th level",
    range(93, 95): "Horseshoes of zephyr",
    range(96, 98): "Nolzur marvelous pigments",
    99: "Bag of devouring",
    100: "Portable hole"
})

item_e = expand({
    range(1, 30): "Spell scroll - 8th level",
    range(31, 55): "Potion of storm giant strength",
    range(56, 70): "Potion of supreme healing",
    range(71, 85): "Spell scroll - 9th level",
    range(86, 93): "Universal solvent",
    range(94, 98): "Arrow of slaying",
    range(99, 100): "Sovereign glue"
})

item_f = expand({
    range(1, 15): "Weapon, +1",
    range(16, 18): "Sheild, +1",
    range(19, 21): "Sentinel shield",
    range(24, 25): "Boots of elvenkind",
    range(26, 27): "Boots of striding and springing",
    range(28, 29): "Bracers of archery",
    range(30, 31): "Brooch of shielding",
    range(32, 33): "Broom of flying",
    range(34, 35): "Cloak of elvenkind",
    range(36, 37): "Cloak of protection",
    range(38, 39): "Gauntlets of ogre power",
    range(40, 41): "Hat of disguise",
    range(42, 43): "Javelin of lightning",
    range(44, 45): "Pearl of power",
    range(46, 47): "Rod of the pact keeper, +1",
    range(48, 49): "Slippers of spider climbing",
    range(50, 51): "staff of the adder",
    range(52, 53): "Staff of the python",
    range(54, 55): "Sword of vengeance",
    range(56, 57): "Trdient of fish command",
    range(58, 59): "Want of magic missiles",
    range(60, 61): "Wand of the war mage, +1",
    range(62, 63): "Wand of web",
    range(64, 65): "Weapon of warning",
    66: "Adamantine chain male",
    67: "Adamantine chain shirt",
    68: "Adamantine scale male",
    69: "Bag of tricks - gray",
    70: "Bag of tricks - rust",
    71: "Bag of tricks - tan",
    72: "Boots of the winterlands",
    73: "Circlet of blasting",
    74: "Deck of illusions",
    75: "Eversmoking bottle",
    76: "Eyes of charming",
    77: "Eyes of the eagle",
    78: "Figurine of wondrous power - silver raven",
    79: "Gem of brightness",
    80: "Gloves of missile snaring",
    81: "Gloves of swimming and climbing",
    82: "Glove of thievery",
    83: "Headband of intellect",
    84: "Helm of telepathy",
    85: "Doss lute of the bards",
    86: "Fochlucan bandor of the bards",
    87: "Mac-Fuimidh cittern of the bards",
    88: "Medallion of thoughts",
    89: "Necklace of adaptation",
    90: "Periapt of wound closure",
    91: "Pipes of haunting",
    92: "Pipes of sewers",
    93: "Ring of jumping",
    94: "Ring of mind shielding",
    95: "Ring of warmth",
    96: "Ring of water walking",
    97: "Quiver of Ehlonna",
    98: "Stone of good luck",
    99: "Wind fan",
    100: "Winged boots"
})

item_g = expand({
    range(1, 11): "Weapon, +2",
    15: "Adamantine breastplate",
    16: "Adamantine splint male",
    17: "Amulet of health",
    18: "Armor of vulnerability",
    19: "Arrow-catching shiled",
    20: "Belt of dwarvenkind",
    21: "Belt of hill giant strength",
    22: "Berserker axe",
    23: "Boots of levitation",
    24: "Boots of speed",
    25: "Bowl of commanding water elementals",
    26: "Bracers of defense",
    27: "Brazier of commanding fire elementals",
    28: "Cape of the mountebank",
    29: "Censer of controlling air elementals",
    30: "Armor, +1 chain male",
    31: "Chain male of resistance",
    32: "Armor, +1 chain shirt",
    33: "Chain shirt of resistance",
    34: "Cloak of displacement",
    35: "Cloak of the bat",
    36: "Cube of force",
    37: "Daern instant fortress",
    38: "Dagger of venom",
    39: "Dimensional shackles",
    40: "Dragon slayer",
    41: "Elven chain",
    42: "Flame tongue",
    43: "Gem of seeing",
    44: "Giant slayer",
    45: "Glamoured studded leather",
    46: "Helm of teleportation",
    47: "Horn of blasting",
    48: "Horn of Valhalla - silver or brass",
    49: "Canaith mandolin of the bards",
    50: "Cli lyre of the bards",
    51: "Ioun stone - awareness",
    52: "Ioun stone - protection",
    53: "Ioun stone - reserve",
    54: "Ioun stone - sustenance",
    55: "Iron bands of Bilarro",
    56: "Armor, +1 leather",
    57: "Armor of resistance (leather)",
    58: "Mace of disruption",
    60: "Mace of smiting",
    61: "Mantle of spell resistance",
    62: "Necklace of prayer beads",
    63: "Periapt of proof against poison",
    64: "Ring of animal influence",
    65: "Ring of evasion",
    66: "Ring of feather falling",
    67: "Ring of free action",
    68: "Ring of protection",
    69: "Ring of resistance",
    70: "Ring of spell storing",
    71: "Ring of the ram",
    72: "Ring of x-ray vision",
    73: "Robe of eyes",
    74: "Rod of ruleship",
    75: "Rod of the pact keeper, +2",
    76: "Rope of entanglement",
    77: "Armor, +1 scale mail",
    78: "Scale mail of resistance",
    79: "Shield, +2",
    80: "Shield of missile attraction",
    81: "Staff of charming",
    82: "Staff of healing",
    83: "Staff of swarming insects",
    84: "Staff of the woodlands",
    85: "Staff of withering",
    86: "Stone of controlling earth elementals",
    87: "Sun blade",
    88: "Sword of life stealing",
    89: "Sword of wounding",
    90: "Tentacle rod",
    91: "Vicious weapon",
    92: "Wand of blinding",
    93: "Wand of enemy detection",
    94: "Wand of fear",
    95: "Wand of fireballs",
    96: "Wand of lightning bolts",
    97: "Wand of paralysis",
    98: "Wand of the war mage, +2",
    99: "Wand of wonder",
    100: "Wings of flying"
})

item_g_12 = expand({
    1: "Figurine of wondrous power - bronze griffon",
    2: "Figurine of wondrous power - ebony fly",
    3: "Figurine of wondrous power - golden lions",
    4: "Figurine of wondrous power - ivory goats",
    5: "Figurine of wondrous power - marble elephant",
    range(6, 7): "Figurine of wondrous power - onyx dog",
    8: "Figurine of wondrous power - serpentine owl",
})

item_h = expand({
    range(1, 10): "Weapon, +3",
    range(11, 12): "Amulet of the planes",
    range(13, 14): "Carpet of flying",
    range(15, 16): "Crystal ball (very rare version)",
    range(17, 18): "Ring of regeneration",
    range(19, 20): "Ring of shooting stars",
    range(21, 22): "Ring of telekinesis",
    range(23, 24): "Robe of scintillating colors",
    range(25, 26): "Robe of stars",
    range(27, 28): "Rod of absorption",
    range(29, 30): "Rod of alertness",
    range(31, 32): "Rod of security",
    range(33, 34): "Rod of the pact keeper, +3",
    range(35, 36): "Scimitar of speed",
    range(37, 38): "Shield, +3",
    range(39, 40): "Staff of fire",
    range(41, 42): "Staff of frost",
    range(43, 44): "Staff of power",
    range(45, 46): "Staff of striking",
    range(47, 48): "Staff of thunder and lightning",
    range(49, 50): "Sword of sharpness",
    range(51, 52): "Wand of polymorph",
    range(53, 54): "Wand of the war mage, +3",
    55: "Adamantine half plate",
    56: "Adamantine full plate",
    57: "Animated shield",
    58: "Belt of fire giant strength",
    59: "Belt of frost (or stone) giant strength",
    60: "Breastplate, +1",
    61: "Candle of invocation",
    63: "Chainmail, +2",
    64: "Chain shirt, +2",
    65: "Cloak of arachnida",
    66: "Dancing sword",
    67: "Demon armor",
    68: "Dragon scale mail",
    69: "Dwarven plate",
    70: "Dwarven thrower",
    71: "Efreeti bottle",
    72: "Figurine of wondrous power (obsidian steed)",
    73: "Frost brand",
    74: "Helm of brilliance",
    75: "Horn of Valhalla (bronze)",
    76: "Anstruth harp of the bards",
    77: "Ioun stone - absorption",
    78: "Ioun stone - agility",
    79: "Ioun stone - fortitude",
    80: "Ioun stone - insight",
    81: "Ioun stone - intellect",
    82: "Ioun stone - leadership",
    83: "Ioun stone - strength",
    84: "Armor, +2 leather",
    85: "Manual of bodily health",
    86: "Manual of gainful exercise",
    87: "Manual of golems",
    88: "Manual of quickness of action",
    89: "Mirror of life trapping",
    90: "Nine lives stealer",
    91: "Oathbow",
    92: "Scale mail, +2",
    93: "Spellguard shield",
    94: "Armor, +1 splint",
    95: "Splint armor of resistance",
    96: "Studded leather armor, +1",
    97: "Studded leather armor of resistance",
    98: "tome of clear thought",
    99: "Tome of leadership and influence",
    100: "Tome of understanding"
})

item_i = expand({
    range(1, 5): "Defender",
    range(6, 10): "Hammer of thunderbolts",
    range(11, 15): "Luck blade",
    range(16, 20): "Sword of answering",
    range(21, 23): "Holy avenger",
    range(24, 26): "Ring of djinni summoning",
    range(27, 29): "Ring of invisibility",
    range(30, 32): "Ring of spell turning",
    range(33, 35): "Rod of lordly might",
    range(36, 38): "Staff of the magi",
    range(39, 41): "Vorpal sword",
    range(42, 43): "Belt of cloud giant strength",
    range(44, 45): "Breastplate, +2",
    range(46, 47): "Chain mail, +3",
    range(48, 49): "Chain shirt, +3",
    range(50, 51): "Cloak of invisibility",
    range(52, 53): "Crystal ball (legendary version)",
    range(54, 55): "Half plate, +1",
    range(56, 57): "Iron flask",
    range(58, 59): "Leather armor, +3",
    range(60, 61): "Plate armor, +1",
    range(62, 63): "Robe of the archmagi",
    range(64, 65): "Rod of ressurection",
    range(66, 67): "Scale mail, +1",
    range(68, 69): "Scarab of protection",
    range(70, 71): "Splint armor, +2",
    range(72, 73): "Studded leather armor, +2",
    range(74, 75): "Well of many worlds",
    77: "Apparatus of Kwalish",
    78: "Armor of invulnerability",
    79: "Belt of storm giant strength",
    80: "Cubic gate",
    81: "Deck of many things",
    82: "Efretti chain",
    83: "Half plate armor of resistance",
    84: "Horn of Valhalla (iron)",
    85: "Ollamh harp of the bards",
    86: "Ioun stone - greater absorption",
    87: "Ioun stone - mastery",
    88: "Ioun stone - regeneration",
    89: "Plate armor of etherealness",
    90: "Plate armor of resistance",
    91: "Ring of air elemental command",
    92: "Ring of earth elemental command",
    93: "Ring of fire elemental command",
    94: "Ring of three wishes",
    95: "Ring of water elemental command",
    96: "Sphere of annihilation",
    97: "Talisman of pure good",
    98: "Talisman of the sphere",
    99: "Talisman of ultimate evil",
    100: "Tome of the stilled tongue"
})

item_i_76 = expand({
    range(1, 2): "Half plate, +2",
    range(3, 4): "Plate armor, +2",
    range(5, 6): "Studded leather armor, +3",
    range(7, 8): "Breastplate, +3",
    range(9, 10): "Splint armor, +3",
    11: "Half plate armor, +3",
    12: "Full plate armor, +3"
})

cr_xp = expand({
    0: 10,
    1 / 8: 25,
    1 / 4: 50,
    1 / 2: 100,
    1: 200,
    2: 450,
    3: 700,
    4: 1100,
    5: 1800,
    6: 2300,
    7: 2900,
    8: 3900,
    9: 5000,
    10: 5900,
    11: 7200,
    12: 8400,
    13: 10000,
    14: 11500,
    15: 13000,
    16: 15000,
    17: 18000,
    18: 20000,
    19: 22000,
    20: 25000,
    21: 33000,
    22: 41000,
    23: 50000,
    24: 62000,
    25: 75000,
    26: 90000,
    27: 105000,
    28: 120000,
    29: 135000,
    30: 155000,
})

item_loot = []

card_deck = [
    "Hooded One (7)    ",
    "Enchanter (3)     ",
    "Shepherd (4)      ",
    "Tempter           ",
    "Raven             ",
    "Seer              ",
    "Swashbuckler (1)  ",
    "Executioner       ",
    "Ghost             ",
    "Warrior           ",
    "Tax Collector (8) ",
    "Anarchist (6)     ",
    "Marionette        ",
    "Miser (9)         ",
    "Torturer (9)      ",
    "Priest            ",
    "Traitor (9)       ",
    "Paladin (2)       ",
    "Thief (7)         ",
    "Beast             ",
    "Guild Member (5)  ",
    "Healer (3)        ",
    "Darklord          ",
    "Myrmidon (5)      ",
    "Elementalist (5)  ",
    "Diviner (2)       ",
    "Abjurer (4)       ",
    "Artifact          ",
    "Avenger (1)       ",
    "Beggar (6)        ",
    "Beserker (6)      ",
    "Bishop (8)        ",
    "Broken One        ",
    "Charlatan (7)     ",
    "Conjurer (9)      ",
    "Dictator (8)      ",
    "Donjon            ",
    "Druid (5)         ",
    "Evoker (6)        ",
    "Horseman          ",
    "Illusionist (7)   ",
    "Innocent          ",
    "Missionary (2)    ",
    "Mists             ",
    "Monk (1)          ",
    "Necromancer (8)   ",
    "Philanthropist (2)",
    "Rogue             ",
    "Soldier (3)       ",
    "Trader (3)        ",
    "Transmuter (1)    ",
    "Wizard            ",
    "Mercenary (4)     ",
    "Merchant (4)      "
]


all_tables = {
    "gem 10": gem_10,
    "gem 50": gem_50,
    "gem 100": gem_100,
    "gem 500": gem_500,
    "gem 1000": gem_1000,
    "gem 5000": gem_5000,
    "art 25": art_25,
    "art 250": art_250,
    "art 750": art_750,
    "art 2500": art_2500,
    "art 7500": art_7500,
    "item a": item_a,
    "item b": item_b,
    "item c":item_c,
    "item d": item_d,
    "item e": item_e,
    "item f": item_f,
    "item g": item_g,
    "item g 12": item_g_12,
    "item h": item_h,
    "item i": item_i,
    "item i 76": item_i_76,
    "item loot": item_loot,
}

weighted_table = {
    range(1, 10): gem_10,
    range(10, 15): gem_50,
    range(15, 20): gem_100,
    range(20, 24): gem_500,
    range(24, 28): gem_1000,
    range(28, 30): gem_5000,
    range(30, 40): art_25,
    range(40, 44): art_250,
    range(44, 46): art_750,
    46: art_2500,
    47: art_7500,
    range(48, 60): item_a,
    range(60, 70): item_b,
    range(70, 75): item_c,
    range(75, 80): item_d,
    range(80, 83): item_e,
    range(83, 86): item_f,
    range(86, 88): item_g,
    range(88, 90): item_h,
    91: item_i,
    range(92, 101): {}
}

import random

def get_table_max(table):
    if not table:
        return None
    mx = 0
    for k in table.keys():
        if isinstance(k, range) and list(k)[-1] > mx:
            mx = list(k)[-1]
        elif isinstance(k, int) and k > mx:
            mx = k
    return mx

def get_loot(table, roll):
    #print("table:", table)
    if not table:
        return None
    for k, v in table.items():
        if isinstance(k, list) and roll in k:
                return v
        elif isinstance(k, int) and roll == k:
            return v
    return None


def random_weighted_table():
    r = random.randint(0, 100)
    for k, v in weighted_table.items():
        if isinstance(k, range) and r in k:
            return v
        elif isinstance(k, int) and r == k:
            return v
    return None


def roll_random_loot(min_items, max_items, fail_chance=0.5):
    it = random.randint(min_items, max_items)
    loot = []
    for i in range(it):
        table = random_weighted_table()
        table_max = get_table_max(table)
        if not table_max:
            continue
        table_max /= fail_chance
        #print(table_max)

        rolled_loot = get_loot(table, random.randint(0, table_max))
        if rolled_loot:
            loot += [rolled_loot]
    return  loot

print(roll_random_loot(1, 5))

def loot_fn():
    print("generating loot ...")
    mi = int(input("enter minimum items"))
    mx = int(input("enter maximum items"))
    items = roll_random_loot(mi, mx)
    print("loot is: ")
    for i in items:
        print("\t", i)

    print("==== END ====\n")
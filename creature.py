import json
import constants

class Creature:

    def __init__(self, json_data):
        self.name = json_data["name"]
        self.str = json_data["strength"]
        self.dex = json_data["dexterity"]
        self.con = json_data["constitution"]
        self.int = json_data["intelligence"]
        self.wis = json_data["wisdom"]
        self.cha = json_data["charisma"]
        self.cr = json_data["challenge_rating"]
        self.senses = json_data["senses"]
        self.max_hp = json_data["hit_points"]
        self.current_hp = self.max_hp
        self.ac = json_data["armor_class"]
        self.speed = json_data["speed"]
        self.actions = json_data["actions"]
        self.type = json_data["type"]
        self.subtype = json_data["subtype"]
        self.current_initiative = 0
        self.is_turn = False
        self.complete_data = json_data

    @staticmethod
    def load_from_name(name):
        path = constants.CREATURE_DIR + "/" + name + ".json"
        with open(path) as f:
            return Creature(json.load(f))

    def clone(self):
        c = Creature(self.complete_data)
        c.current_hp = self.current_hp
        return c

    def pretty_format(self):
        # TODO: show special abillities too? see aboleth.json
        s = "{:<12} {}/{} {:>5}".format(self.name, self.max_hp, self.current_hp, "AC" + str(self.ac)) + "\n"
        s += "STR: {}".format(self.str) + "\n"
        s += "DEX: {}".format(self.dex) + "\n"
        s += "CON: {}".format(self.con) + "\n"
        s += "WIS: {}".format(self.wis) + "\n"
        s += "INT: {}".format(self.int) + "\n"
        s += "CHA: {}".format(self.cha) + "\n"
        s += "\n"
        s += self.format_actions()
        s += "\n"
        return s

    def format_actions(self):
        s = ""
        for action in self.actions:
            s += "\t" + action["name"] + "\n"
            s += " \t\t" + action["desc"] + "\n"
        return s

    def __getattr__(self, item):
        try:
            return self.complete_data.get(item)
        except KeyError as e:
            raise AttributeError(e)

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            c = self.clone()
            c.current_hp += other
            return c
        raise TypeError("other should be a numeric type")

    def __iadd__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.current_hp += other
        raise TypeError("other should be a numeric type")

    def __isub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.current_hp -= other
        raise TypeError("other should be a numeric type")

    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            c = self.clone()
            c.current_hp -= other
            return c
        raise TypeError("other should be a numeric type")

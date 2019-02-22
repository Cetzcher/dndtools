import json
import constants
from creature import Creature

def make_test_ecnoutner():
    import load
    encounter = Encounter.load("pitf")
    data = load.load_files()
    return PlayableEncouter.from_encounter(
        data,
        encounter
    )


class Encounter:

    def __init__(self, name, creatures=None):
        self.name = name
        self.creatures = creatures if creatures is not None else []

    @staticmethod
    def create_encounter(name, creatures):
        encounter = Encounter(name)
        encounter.creatures = creatures
        return encounter

    @staticmethod
    def load(name):
        with open(constants.ENCOUNTER_DIR + "/" + name + ".json", "r") as f:
            data = json.load(f)
            e = Encounter(data["name"], data["creatures"])
            return e

    def save_encoutner(self):
        with open(constants.ENCOUNTER_DIR + "/" + self.name + ".json", "w+") as f:
            json.dump(self.to_json_data(), f, indent=4)

    def to_json_data(self):
        return self.__dict__


class PlayableEncouter(Encounter):

    def __init__(self, creature_data_source, name, creatures=None):
        Encounter.__init__(self, name, creatures)
        self.creature_data_source = creature_data_source
        self.active_creatures = []
        self.__load_creatures()
        self.current_monster = 0

    @staticmethod
    def from_encounter(creature_data_source, encounter):
        return PlayableEncouter(creature_data_source, encounter.name, encounter.creatures)

    def __load_creatures(self):
        for cr in self.creatures:
            self.active_creatures += [Creature(self.creature_data_source[cr])]

    def sort_by_initiative(self):
        self.active_creatures.sort(key=lambda creature: creature.current_initiative, reverse=True)

    def next(self):
        self.active_creatures[self.current_monster % len(self.active_creatures)].is_turn = False
        self.current_monster += 1
        self.active_creatures[self.current_monster % len(self.active_creatures)].is_turn = True
        if self.active_creatures[self.current_monster % len(self.active_creatures)].current_hp <= 0:
            self.next()

    def start_encounter(self):
        self.active_creatures[0].is_turn = True


def generate_ecnounter_io():
    import load
    monsters = load.load_files()
    added_creatures = []
    e_name = input("enter an encounter name [do not include '/', '\\']: ")
    inp = ""
    while inp != "!":
        cur_encounter = Encounter(e_name, added_creatures)
        inp = input("enter the name of a creature that you want to search for\n"
                    "or type '!' to stop adding creatures\n"
                    "or type '?' to show the current encounter\nsearch:")

        if inp == "?":
            print(json.dumps(cur_encounter.to_json_data(), indent=4))
        elif inp == "!":
            cur_encounter.save_encoutner()
        else:
            try:
                found, key, _, certainty = monsters.search(inp)
                monster = monsters[key]
                print("found a monster with a probability of ", 100 * certainty, "%", key, ":")
                yesno = input("add monster ? [y/N]")
                if yesno.lower() == "y":
                    added_creatures += [key]
                    print("added monster to encounter")
            except KeyError:
                print("could not find creature :(")
        print("\n")

if __name__ == '__main__':
    generate_ecnounter_io()
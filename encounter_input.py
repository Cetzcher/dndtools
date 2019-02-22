import encounter_generator
import random
import json

help_msg = """
(s) show displays the encounter again
(d) damage <to> <amount> deals damage to the specified creature
(h) heal <to> <amount> heals the specified creature
(u) undo undoes the last action
(E) end ends the encounter with prompt
(R) roll <dice> should roll a dice in the format of <amnt>d<eyes>
(n) next continues to the next turn with a prompt
(more) <creature> shows details to creature
(help, ?) shows help dialog
"""

short_help = "(s)how, (d)amage, (h)eal, (u)ndo, (E)nd, (R)oll, (n)ext, more #, (?)"


def promptYN(msg="are you sure?[y/N] "):
    if "y" in input(msg).lower():
        return True
    return False


def read_unitl_int_greater0():
    try:
        x = input()
        x = int(x)
        if x < 0:
            read_unitl_int_greater0()
        return x
    except Exception as e:
        print("input must be a number > 0")
        read_unitl_int_greater0()


class EncounterInput:

    def __init__(self, playable_encounter, encounter_display):
        self.rnd = random.Random()
        self.ended = False
        self.__inital_done = False
        self.encounter = playable_encounter
        self.display = encounter_display

    def initial(self):
        if self.__inital_done:
            return
        # setup encounter
        print()
        print("Assign initiative ...")
        idx = 0
        initiative_arr = []
        for creature in self.encounter.active_creatures:
            idx += 1
            print("({}) {} initiative: ".format(idx, creature.name), end="")
            initiative = read_unitl_int_greater0()
            initiative_arr += [(creature, idx, initiative)]

        print("========================")
        for creature, idx, initiative in initiative_arr:
            print("({}) {} initiative: {}".format(idx, creature.name, initiative))

        if not promptYN("is this correct[y/N] "):
            print("\nOkay then doing it again ... ")
            self.initial()

        for creature, _, initiative in initiative_arr:
            creature.current_initiative = initiative

        self.encounter.sort_by_initiative()
        self.encounter.start_encounter()
        self.__inital_done = True
        print()


    def show(self, io):
        print("showing")
        # we do not need to do this since draw is called by display self.display.draw()

    def damage(self, io):
        if len(io) == 3:
            _, to, amnt = io
            to = int(to) - 1
            amnt = int(amnt)
            self.encounter.active_creatures[to] -= amnt
        else:
            print("damage needs 2 arguments in the form <to> <damage>")

    def heal(self, io):
        if len(io) == 3:
            _, to, amnt = io
            to = int(to) - 1
            amnt = int(amnt)
            self.encounter.active_creatures[to] += amnt
        else:
            print("damage needs 2 arguments in the form <to> <damage>")

    def undo(self, io):
        if promptYN():
            print("undoing")
        else:
            print("continue ..")

    def end(self, io):
        if promptYN():
            print("ending encounter")
            self.ended = True
        else:
            print("continue ...")

    def roll(self, io):
        print("rolling dice")
        times, dice = io[1].strip().split("d")
        sum = 0
        times = int(times)
        dice = int(dice)
        for t in range(times):
            roll = self.rnd.randint(1, dice)
            sum += roll
            print("roll #", t + 1, "=", roll)
        print("==============")
        print("sum = ", sum)

    def next(self, io):
        self.encounter.next()

    def more(self, io):
        if len(io) > 1:
            monster_num = int(io[1]) - 1
            m = self.encounter.active_creatures[monster_num]
            print(m.pretty_format())
        else:
            raise IndexError("invalid format should be 'more <ID>' of monster")

    def help(self, io):
        print(help_msg)

    def read(self):
        # read should build a command that will change will lead to the drawing of something:
        # (s) show should always display the encounter again
        # (d) damage <to> <amount> should subtract amount from to
        # (h) heal <to> <amount> should add amount to <to>
        # (u) undo should change heal to damage and damage to heal
        # (E) end should end the encounter
        # (R) roll <dice> should roll a dice in the format of <amnt>d<eyes>
        # (n) next should continue to the next turn
        # (more) <creature> shows details to creature
        # (help, ?) shows help dialog
        self.initial()
        print(short_help)
        print()
        io = input(":")
        actions = [
            ["s", "show", self.show],
            ["d", "damage", self.damage],
            ["h", "heal", self.heal],
            ["u", "undo", self.undo],
            ["E", "end", self.end],
            ["R", "roll", self.roll],
            ["n", "next", self.next],
            ["m", "more", self.more],
            ["help", "?", self.help]
        ]
        try:
            if len(io) > 0:
                splited = io.split(" ")
                first_item = splited[0]
                for action in actions:
                    short_desc, long_desc, func = action
                    if short_desc in first_item or long_desc in first_item:
                        return func(splited)
                print("Command not recognized :( type (help, ?, h) for available commands")
            else:
                print("empty command")
        except Exception as e:
            print("error while parsing command")
            print(e)

import encounter_generator
import load

class Display:

    def __init__(self, playable_encounter):
        self.playable_encounter = playable_encounter

    def draw(self):
        f = "{:<4}{:<30}{:<14}{:^5}{:>5}{:>12}"
        idx = 0
        print(f.format("#  ", "Creature Name", "initiative", "HP", "AC", "Type"))
        for cr in self.playable_encounter.active_creatures:
            idx += 1
            s = f.format("(" + str(idx) + ")", cr.name, cr.current_initiative, cr.current_hp, cr.ac, cr.type)
            frmt_start = ""
            frmt_end = ""
            if cr.is_turn:
                frmt_start = "\033[32m"
                frmt_end = "\033[0m"
            print(frmt_start + s + frmt_end)


if __name__ == '__main__':
    pe= encounter_generator.make_test_ecnoutner()
    d = Display(pe)
    d.draw()

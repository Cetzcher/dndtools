import encounter_display
import encounter_input
import encounter_generator

def main():
    import ecnounter_finder
    import load
    print("select the encounter you want to choose from below: ")
    enc = ecnounter_finder.main()
    enc_num = int(input("encounter number: "))
    playable_encounter = encounter_generator.PlayableEncouter.from_encounter(
        load.load_files(),
        encounter_generator.Encounter.load(enc[enc_num])
    )
    if len(playable_encounter.active_creatures) == 0:
        print("the encounter does not contain any monsters, exiting ... ")
        return

    display = encounter_display.Display(playable_encounter)
    inp = encounter_input.EncounterInput(playable_encounter, display)
    while not inp.ended:
        display.draw()
        inp.read()


if __name__ == '__main__':
    main()
import json
from constants import *


def main():
    with open("./data/srdMonsters.json") as f:
        data = json.load(f)
        print("splitting monsters into files")
        print("there are", len(data), "entries")
        for e in data:
            try:
                name = e["name"]
                name = name.replace("/", "_")
                name = name.replace('"', "")
                print("creating a new entry: ", name)
                outfile = CREATURE_DIR + "/" + name + ".json"
                with open(outfile, "w+") as out:
                    json.dump(e, out, indent=4)
                    print("wrote a file: ", outfile)
            except KeyError as ke:
                print("could not parse an entry: ", ke, "of", e)


if __name__ == '__main__':
    main()
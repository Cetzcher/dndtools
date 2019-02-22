import argparse
import load
import json

def main():
    data = load.load_files()
    parser = argparse.ArgumentParser()
    parser.add_argument("lookup", help="the lookup")
    args = parser.parse_args()
    print("looking for monster with lookup: ", args.lookup)
    res = data.search(args.lookup)
    found, key, _, certainty = res
    try:
        monster = data[key]
        print("found a monster with a probability of ", 100 * certainty, "%", key, ":")
        yesno = input("show monster details [Y/n]")
        if not yesno.lower() == "n":
            print(json.dumps(monster, indent=4))
    except KeyError:
        print("could not find monster :(")

if __name__ == '__main__':
    main()

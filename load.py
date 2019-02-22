import json
from constants import *
import glob
import errno
import fuzzysearch

def load_files():
    path = CREATURE_DIR + "/*.json"
    files = glob.glob(path)
    d = fuzzysearch.FuzzyDict()
    for name in files:
        try:
            with open(name) as f:
                data = json.load(f)
                n = data["name"]
                d[n] = data
        except IOError as exc:
            if exc.errno != errno.EISDIR:
                raise
    return d


if __name__ == '__main__':
    print(load_files())

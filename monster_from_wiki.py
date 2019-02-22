import requests
DEBUG = False

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("ERROR: Beautiful soup 4 not supported")
    exit()


def l_attr(attr):
    """
    creates the long name of an attribute i.e dex = dexterity
    :param attr: the attr name either, case insensitive
    :return: the long name of the attr string or None
    """
    return {"str": "strength",
            "dex": "dexterity",
            "con": "constitution",
            "int": "intelligence",
            "wis": "wisdom",
            "cha": "charisma"
            }.get(str(attr).lower(), None)


ATTRS = ["str", "dex", "con", "int", "wis", "cha"]
SKILLS = [
    "athletics",
    # TODO: add more skills
]


class Parser:

    @staticmethod
    def load_page(url):
        return requests.get(url).text

    def __init__(self, html=None, url=None):
        if html:
            self.soup = BeautifulSoup(html, "html.parser")
        elif url:
            self.soup = BeautifulSoup(Parser.load_page(url), "html.parser")
        else:
            raise ValueError("html must be html or url must be a valid url")

        self.creature_dict = dict()

    def extract_special(self):
        pass

    def extract_actions(self):
        pass

    def extract_name(self):
        pass

    def extract_hp(self):
        pass

    def extract_skills(self):
        pass

    def extract_senses(self):
        pass

    def extract_attrs(self):
        pass

    def extract_resistances(self):
        pass

    def extract_vulnerabilities(self):
        pass

    def extract_ac(self):
        pass

    def extract_speed(self):
        pass

    def extract_size(self):
        pass

    def extract_type(self):
        pass

    def extract_subtype(self):
        pass

    def extract_alignment(self):
        pass

    def extract_condition_imunities(self):
        pass

    def pre_parse(self):
        pass

    def post_parse(self):
        pass

    def extract_cr(self):
        pass

    def parse(self):
        self.pre_parse()
        self.extract_name()
        self.extract_ac()
        self.extract_hp()
        self.extract_speed()
        self.extract_size()
        self.extract_type()
        self.extract_subtype()
        self.extract_alignment()
        self.extract_attrs()
        self.extract_cr()
        self.extract_resistances()
        self.extract_vulnerabilities()
        self.extract_condition_imunities()
        self.extract_special()
        self.extract_skills()
        self.extract_senses()
        self.extract_actions()
        self.post_parse()
        return self.creature_dict


class ChisaipeteGithubParser(Parser):

    def pre_parse(self):
        """
        the general layout of the page contains header and footer and an article in the middle
        the article contains the relevant information regarding the creatures stats
        the stats itself follow a simple scheme of [<p><strong> DESCRIPTION </strong> text </p> ...]
        this array contains:
        [0] = size type, alignment
        [1] = ac
        [2] = hp (format: number (dice))
        [3] = speed (i.e: 30ft., fly 60 ft.)
        from there on out the stat block changes since some creatures do not have skills or saving throws
        there is also a table containing the attributes of the creature
        :return: None
        """
        self.soup2 = self.soup("article")[0]  # all stats are in first article of page
        self.attr_table = zip(self.soup2("tr")[0], self.soup2("tr")[1])  # attr to number
        self.rows = self.soup2("p")  # this contains all rows in the page.
        self.action_pos = next(i for i, v in enumerate(self.rows) if "Actions" in v.text) # finds the index of Actions in the rows array
        self.cr_pos = next(i for i, v in enumerate(self.rows) if "Challenge" in v.text) # the index of "Challange in the p tags"

    def extract_name(self):
        name = self.soup("h1", class_="post-title")[0].text  # name is in post title
        self.creature_dict["name"] = name

    def extract_attrs(self):
        for attr_name, attr_value in self.attr_table:
            if str(attr_name).strip():  # skip empty lines
                name_t = attr_name.text
                val_t = attr_value.text
                # value is number (mod)
                raw_val = val_t.strip().split("(")[0]
                self.creature_dict[l_attr(name_t)] = raw_val.strip()

    def extract_size(self):
        t = self.rows[0].text.split(" ")[0]  # first word of first row is the size
        self.creature_dict["size"] = t

    def extract_type(self):
        row = self.rows[0].text
        first_space = row.index(" ")
        first_comma = row.index(",")
        t = row[first_space:first_comma].strip()
        split = t.split(" ")
        if len(split) == 2:
            _type, subtype = split
            self.creature_dict["type"] = _type
            self.creature_dict["subtype"] = subtype[1:-1]  # subtype is in '(' so we remove them
        else:
            self.creature_dict["type"] = t
            self.creature_dict["subtype"] = ""
        # we parse type and subtype together in th this case

    def extract_alignment(self):
        row = self.rows[0].text
        # alignment is from the first comma to the end
        t = row[row.index(",") + 1:].strip()
        self.creature_dict["alignment"] = t

    def extract_ac(self):
        row = self.rows[1].text  # is the ac text node
        self.creature_dict["armor_class"] = row.split(" ")[2].strip()

    def extract_hp(self):
        row = self.rows[2].text
        self.creature_dict["hit_points"] = row.split(" ")[2].strip()

    def extract_speed(self):
        row = self.rows[3].text
        self.creature_dict["speed"] = row[len("speed"):].strip()    # just remove the word speed and use the format

    def extract_cr(self):
        row = self.rows[self.cr_pos].text
        self.creature_dict["challenge_rating"] = row[row.find(" "):row.find("(")].strip()

    def extract_special(self):
        """
        starting from challange pos to action pos
        :return: None
        """
        unparseable = []
        actions = []
        for idx in range(self.cr_pos + 1, self.action_pos):
            nodes = list(self.rows[idx].children)
            try:
                name = nodes[0].text
                desc = str(nodes[1])
                actions += [{"name": name, "desc": desc, "attack_bonus": 0}]
            except AttributeError:
                # when this happens name was a navigable string
                # most likely because it is in the format of 3/day each: alter self, command, detect magic
                # we just append them to unparseable and handle them later
                unparseable += [str(nodes[0])]
        if unparseable:
            actions += [{"name": "Spellcasting", "desc": str.join(" ; ", unparseable), "attack_bonus": 0}]
        self.creature_dict["special_actions"] = actions

    def extract_actions(self):
        actions = self.rows[self.action_pos + 1:]
        action_arr = []
        for action in actions:
            try:
                nodes = action.children
                name, desc = nodes
                action_arr += [{"name": name.text, "desc": desc, "attack_bonus": 0}]
            except ValueError:
                pass  # some monsters have fluff at the bottom like a deva, we just ignore that
        self.creature_dict["actions"] = action_arr

    def post_parse(self):
        """
        since the data format is NOT normalized we need to take special care of some stats
        from index [4] to [challnge_pos] are differing values
        from [challange_pos] to [action_pos] are the creatures special actions
        from [action_pos] onward are the creatures actions
        we will parse [4] to [challange_pos] here looking for keywords and parsing that all here.
        :return: None
        """
        for idx in range(4, self.cr_pos):
            txt = self.rows[idx].text
            if "Saving Throws" in txt:
                # i.e txt = Saving Throws Str +7, Con +6, Int +5, Cha +6
                st = txt[len("Saving Throws"):].strip()
                attrs = st.split(",")
                for a in attrs:
                    name, val = a.strip().split("+")    # there are no - saving throws (i think)
                    full_name = l_attr(name.strip()) + "_save"
                    self.creature_dict[full_name] = val
            elif "Skills" in txt:
                skill = txt[len("skills"):].strip().split(",")
                res = {k.strip(): v for k, v in map(lambda x: x.split("+"), skill)}
                for k, v in res.items():
                    self.creature_dict[k.lower()] = v
            elif "Damage Resistances" in txt:
                resitance = txt[len("Damage Resistances"):]
                self.creature_dict["damage_reistances"] = resitance.strip()
            elif "Senses" in txt:
                self.creature_dict["senses"] = txt[len("senses"):].strip()
            elif "Languages" in txt:
                self.creature_dict["languages"] = txt[len("languages"):].strip()


DEBUG = True
if __name__ == '__main__':
    import json
    import constants
    import encounter_input
    import creature
    if not DEBUG:
        inp = input("enter the url of a creature you want to create: ")
    else:
        inp = "http://chisaipete.github.io/bestiary/creatures/manes"

    p = ChisaipeteGithubParser(url=inp)
    parse_result = p.parse()
    c = creature.Creature(parse_result)
    print(c.pretty_format())
    if encounter_input.promptYN("show creature json? [y/N]"):
        print(json.dumps(c.__dict__, indent=4))
    path = constants.CREATURE_DIR + "/" + c.name + ".json"
    if encounter_input.promptYN("write to " + path + " [y/N]"):
        with open(path, "w+") as f:
            json.dump(parse_result, f, indent=4)



import random
import string
import os.path
import jsonpickle
import getopt
import sys
from generator.group import random_string
from model.contact import Contact

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_numbers(prefix, maxlen):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@" + "".join(
        [random.choice(symbols) for i in range(random.randrange(maxlen))]) + "a.com"


testdata = [Contact(firstname="", lastname="")] + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10),
            nickname=random_string("nickname", 10), title=random_string("title", 10),
            company=random_string("company", 15),
            address=random_string("address", 30),
            work_phone_number=random_numbers("+", 10), email=random_email("email", 5), bday="10",
            bmonth="March", byear="1990", notes=random_string("firstname", 30))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))

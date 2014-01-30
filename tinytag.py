import os
import sys
import random
import string

tagpath = "/home/shark/.tinytag/"


def listTags():
    return os.listdir(tagpath)


def randomSymbol():
    return random.choice(string.ascii_lowercase +
                         string.ascii_uppercase +
                         string.digits)


def randomTag():
    # this generates (26 + 26 + 10)^2 = 3844 different tags
    return randomSymbol() + randomSymbol()


def generateTag():
    # TODO ...
    existing = listTags()

    tag = randomTag()

    while tag in existing:
        tag = randomTag()

    return tag


def createLink(filename, tag):
    os.symlink(filename, os.path.join(tagpath, tag))


def main(argv):
    if len(argv) != 2:
        print("Usage: tinytag <filename>")
        sys.exit(-1)

    filename = argv[1]
    pathname = os.path.realpath(filename)
    if not os.path.exists(pathname):
        print("File '{}' does not exist.".format(filename))
        sys.exit(-1)
    tag = generateTag()

    createLink(pathname, tag)

    print("The tag for '{}' is: '{}'".format(filename, tag))

if __name__ == "__main__":
    main(sys.argv)

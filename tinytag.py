import os
import sys
import random
import string
import argparse


def tagPath():
    tagpath = os.path.join(os.path.expanduser("~"), ".tinytag")
    if not os.path.exists(tagpath):
        os.mkdir(tagpath)

    return tagpath


def listTags():
    return os.listdir(tagPath())


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


def getSymlinkPath(tag):
    return os.path.join(tagPath(), tag)


def createLink(filename, tag):
    os.symlink(filename, getSymlinkPath(tag))


def getFilename(tag):
    tagfile = getSymlinkPath(tag)
    return os.path.realpath(tagfile)


def main():
    parser = argparse.ArgumentParser(prog="tinytag")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("filename", nargs="?",
                       help="create a new tinytag for the given file",
                       action="store")
    group.add_argument("-l", "--list",
                       help="list all tinytags", action="store_true")
    group.add_argument("-r", "--remove", dest="tag",
                       help="remove a certain tinytag", action="store")
    args = parser.parse_args()

    if args.filename:
        fname = args.filename
        pname = os.path.realpath(fname)
        if not os.path.exists(pname):
            print("File '{}' does not exist.".format(fname))
            sys.exit(-1)
        tag = generateTag()

        createLink(pname, tag)

        print("Created tag \033[1m{}\033[0m for file '{}'".format(tag, fname))

    elif args.tag:
        tag = args.tag
        fname = getFilename(tag)
        os.unlink(getSymlinkPath(tag))
        print("Removed tag \033[1m{}\033[0m for file '{}'".format(tag, fname))

    else:
        tlist = listTags()
        if not tlist:
            print("No tiny tags available")
        else:
            print("List of tinytags:")
            print("")

            for tag in tlist:
                fname = getFilename(tag)
                print("\033[1m{}\033[0m:  {}".format(tag, fname))

    print("")


if __name__ == "__main__":
    main()

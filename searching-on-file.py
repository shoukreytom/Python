import re
def main():
    with open("file.log", "r+") as f:
        line = r"{}".format(f.read())
        s = re.findall("I'm", line)
        try:
            c = re.search("I'm", line)
            print(c.group())
        except AttributeError:
            return
        print(s)
        print(line)


if __name__ == "__main__":
    main()

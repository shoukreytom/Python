"""Important methods in re module
    1) sub(pattern, rep, source)
    2) findAll(pattern, source)
    3) search(pattern, source)
    4) match(pattern, source)
"""
import re


text = """Hi there I'm Shoukrey Tom, I'm software developer from
Sudan I code in mutilple programming langauges using Java, Python and
C++. but my favourit langauge is Java
"""


def main():
    pattern = r"Hi"
    if re.match(pattern, text): # matches the beginning of text
        print("Match found")
    else:
        print("No match found")

    if re.search("Java", text):
        print("found")
    else:
        print("not found")

    # this will replace C++ to C/C++ in text
    pattern = r"C\+\+"
    new = re.sub(pattern, "C/C++", text)
    print(new)
    
    print(re.findall("Java", text))


if __name__ == "__main__":
    main()

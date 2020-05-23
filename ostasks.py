import os


home = os.getenv('HOME')


def createFolders():
    os.makedirs(os.path.join(home, "test", "test1"))


def main():
    print(home)
    print(os.getcwd())
    os.chdir(home)
    print(os.getcwd())
    createFolders()



if __name__ == '__main__':
    main()

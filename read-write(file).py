import os


class Tasks:

    def __init__(self):
        self.testFolder = os.path.join(str(os.getcwd()), "test")

    def create_folder(self):
        os.mkdir(self.testFolder+"dir")

    def create_folders(self):
        os.makedirs(os.path.join(self.testFolder, "folder1", "folder2"))

    def write_file(self):
        names = ["name1", "name2", "name3", "name4"]

        """File flags:
        1- a: for append
        2- r: for read-only
        3- w: for write-only
        """

        file = open(self.testFolder+'/file.txt', "a+")
        for name in names:
            file.write(name+"\n")

    def read_file(self):
        try:
            file = open(self.testFolder+'/file.txt', "r+")
            print(file.read())
        except OSError:
            print('Something went wrong')


def main():
    tasks = Tasks()
    tasks.create_folders()
    tasks.write_file()


if __name__ == "__main__":
    main()

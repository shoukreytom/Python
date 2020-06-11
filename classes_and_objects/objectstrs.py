class About:

    def __init__(self):
        self.author = 'Shoukrey Tom'
        self.location = 'Sudan'
        self.job = 'Student'

    # this is for debugging
    def __repr__(self):
        return "<About - Class author: {0}, location: {1}, job: {2}".format(
            self.author, self.location, self.job
        )

    # this is for human readable
    def __str__(self):
        return "author: {0}, location: {1}, job:{2}".format(
            self.author, self.location, self.job
        )

    def __bytes__(self):
        val = "author: {0}, location: {1}, job: {2}".format(
            self.author, self.location, self.job
        )
        return bytes(val.encode('utf-8'))


def main():
    about = About()
    print(repr(about))
    print(str(about))
    print(bytes(about))


if __name__ == '__main__':
    main()

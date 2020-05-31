# script for throwing system notifications using notify2 lib
import notify2


def main():
    notify2.init("notify")
    n = notify2.Notification("Tip", "Don't watch porn videos, It'll damage your brain",
                             "")
    n.set_timeout(2000)
    n.show()


if __name__ == '__main__':
    main()

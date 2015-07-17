import sys

from py_grabber.application import Application

def run():
    if len(sys.argv) == 1:
        print("print pygrab [your url] to download page")
        exit()

    app = Application()
    app.run(sys.argv[1])

if __name__ == '__main__':
    run()




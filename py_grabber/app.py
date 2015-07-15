import sys

from py_grabber.application.Application import Application

def run():
    if len(sys.argv) < 1:
        print("Pass url as a command line parameter")
        exit()

    app = Application()
    app.run(sys.argv[1])

if __name__ == '__main__':
    run()




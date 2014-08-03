
import sys
from application.Application import Application

if len(sys.argv) < 1:
    print("Pass url as a command line parameter")
    exit()

try:
    app = Application()
    app.run(sys.argv[1])
except:
    print(sys.exc_info())




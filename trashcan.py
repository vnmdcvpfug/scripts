import sys
from send2trash import send2trash

target = sys.argv[1]

def dialogue():
    prompt = input("Move '" + str(target) + "' to trash? y/N ")
    if prompt in ['', 'y', 'yes', 'Y', 'Yes', 'YES']:
        try:
            send2trash(target)
            print("'" + target + "' was moved to trash.")
        except OSError:
            print("No such file or directory.")
    else:
        pass

dialogue()

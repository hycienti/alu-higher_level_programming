#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    arg_count = len(argv) - 1

    if arg_count == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(arg_count, "s" if arg_count > 1 else ""))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))

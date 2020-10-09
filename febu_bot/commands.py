from febu_bot import VERSION


def run_commands(argv):
    if len(argv) == 2:
        if argv[1] == '-v' or argv[1] == '--version':
            print(VERSION)
            quit()
        if argv[1] == 'run':
            from .drive import drive_bot
            drive_bot()
    if len(argv) == 3:
        if argv[1] == 'run':
            from .drive import drive_bot
            if argv[2] is not None:
                drive_bot(int(argv[2]))
            drive_bot()

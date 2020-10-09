import sys
from febu_bot.commands import run_commands
from febu_bot.exceptions import CommandNotFound
import os


def main(argv):
    os.environ.setdefault('FEBU_BOT_SETTINGS', 'FacebookAutomation.settings')
    try:
        run_commands(argv)
    except CommandNotFound as e:
        print("Command not found")


if __name__ == '__main__':
    main(sys.argv)

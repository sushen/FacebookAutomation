import dotenv
import time

import emoji

from febu_bot import VERSION


def start(name: str):
    print()
    print()
    print(f"************ Facebook bot \U0001F600 {VERSION} ************")
    dotenv.load_dotenv()

    time.sleep(2)
    print(">>>>>>>> STARTED!!! " + emoji.emojize(':winking_face_with_tongue:'))
    print(">>>>>>>> Now running " + name.title())
    time.sleep(1)

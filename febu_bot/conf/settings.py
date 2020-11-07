import os
import importlib

try:
    module_name = os.environ.get('FEBU_BOT_SETTINGS')
    mod = importlib.import_module(module_name)
except ModuleNotFoundError as e:
    print(e)
    print('******** Please specify your bot settings')


def __getattr__(name):
    return getattr(mod, name)

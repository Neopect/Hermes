# Processor.py - Handles system sub modules for processing requests

import importlib
import sys
import os
import requests
from decouple import config

import scheduler as shed
import inListener
import textProcess


current_loc = os.path.dirname(__file__)
sysPlug_dir = os.path.join(current_loc, "sysPlugs")
sys.path.append(sysPlug_dir)



TYPE_ENV = config('SYS_TYPE')


plugin_modules = []
pluginDir = os.listdir("./src/sysPlugs")
# print(pluginDir)

pluginDir = pluginDir[:-1]

for file in range(len(pluginDir)):
    if not pluginDir[file].__contains__('.py'):
        pluginDir.remove(pluginDir[file])
    else:
        pluginDir[file] = pluginDir[file].removesuffix('.py')
    # print(pluginDir)
    

for plugin in pluginDir:
    plugin_module = importlib.import_module("sysPlugs." + plugin, ".")
    # plugin_module = importlib.import_module("." + plugin, "__name__")
    plugin_modules.append(plugin_module)
    print(plugin_module)


# print(plugin_modules)


# plugin = plugin_modules[0].Plugin("hello", key=123)

# result = plugin.execute(5,3)
# print(result)




def cliBot():
    tp = textProcess.cliProcessor()

    tp.greet_user()
    while True:
            query = tp.take_user_input().lower()
            query_bd = inListener.breakdown(query)
            print(query_bd)




if __name__=='__main__':
    
    if TYPE_ENV == "CLI":
        cliBot()


        
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

import sys
import json
import commands

def miner():
  with open(file=sys.argv[1], mode='r') as file:
    try: 
      companies_data = json.load(file)
      # print(json.dumps(data, indent=4))
      getattr(commands, sys.argv[2])(companies_data, sys.argv[3])
    except IOError as e:
      print('IOError: ', e)
    except:
      print('Unexpected error: ', sys.exc_info()[0])
  
miner()
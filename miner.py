# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

import sys
import json
import commands

def miner():
  with open(file=sys.argv[1], mode='r') as file:
    try: 
      companies_data = json.load(file)
      result = getattr(commands, sys.argv[2])(companies_data, sys.argv[3])
      logResult(result)
    except IOError as e:
      print('IOError: ', e)
    except:
        print('Unexpected error: ', sys.exc_info()[0])

def logResult(result):
  company_names = ', '.join(result)
  company_numbers = len(result)
  print(f'Company names:\n{company_names}\n\nNumber of Companies: {company_numbers}')

miner()
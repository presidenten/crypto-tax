import datetime
import logging
import os
import sys

from credentials.credentials import initials

target_year = 2018
cutoff_year = datetime.datetime(target_year + 1,1,1)
derived_folder = './data/%s/%s/' % (initials, target_year)
final_file = '%s/transactions-final.json' % derived_folder
input_folder = './data/%s/input_data' % (initials)

# 1 day in seconds
one_day = 24 * 60 * 60
dollar_pct = .2

num_processes = 4
parallel = False
ignore_margins = True
reload_data = False
find_prices_network = False
likekind_threshold = 1000
likekind_cutoff_year = 2018


def maybe_open(path, encoding='utf-8'):
    maybe_print('Trying to open file %s' % path)
    if os.path.isfile(path) is False:
        maybe_print('Cannot find file %s' % path)
        return None
    return open(file=path, mode='r', encoding=encoding)


def maybe_print(s):
    if True:
        print(s)


logger = logging.getLogger()
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger.setLevel(logging.DEBUG)
logger.root.handlers.clear()
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)

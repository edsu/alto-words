#!/usr/bin/env python
"""
This script requieres a dump of the wiktionary for the language in question.
Check the README.md or run the following command.
    $ make dictionary.db
    
"""

import dbm
import gzip
import sys


def process_page_row(row, dictionary):
    """Write word into dictionary"""
    if row[1] == '0':
        word = row[2].lower().strip().replace('_', ' ').replace("'", "")
        dictionary[word] = '1'
        print(word)

def split_sql_insert(line):
    """Break a long sql insert into a list of lists of values"""
    value_list = line.split("),(")
    value_list[0] = value_list[0].replace("INSERT INTO `page` VALUES (", "")
    value_list[-1] = value_list[-1].replace(");\n", "")
    return value_list


def parse_sql(filename, dictionary):
    with gzip.open(filename, 'rt') as infile:
        data = infile.readlines()

    for line in data:
        if not line.startswith('INSERT'):
            continue
        else:
            rows = split_sql_insert(line)
        for row in rows:
            try:
                process_page_row(row.split(','), dictionary)
            except Exception as e:
                print(f"Exception {e}")

def main(filename):
    with dbm.open('dictionary.db', 'c') as dictionary:
        parse_sql(filename, dictionary)

if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)

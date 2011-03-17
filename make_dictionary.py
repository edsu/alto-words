#!/usr/bin/env python

"""
You'll need to download the latest enwiktionary dump before you run this:

    wget http://dumps.wikimedia.org/enwiktionary/latest/enwiktionary-latest-page.sql.gz

Once you have that, you should be able to run this and you'll end up with a
dbm dictionary to use.
"""

import re
import dbm
import gzip
import codecs


def main():
    dictionary = dbm.open('dictionary', 'c')
    parse_sql('enwiktionary-latest-page.sql.gz', dictionary)


def process_page_row(row, dictionary):
    if row[1] == '0':
        word = row[2].lower().strip().replace('_', ' ')
        dictionary[word] = '1'
        print word


def parse_sql(filename, dictionary):
    pattern = re.compile(r"\((\d+),(\d+),'(.+?)','.*?',\d+,\d+,\d+,\d\.\d+,'.+?',\d+,\d+,\d+\)")
    fh = codecs.EncodedFile(gzip.open(filename), data_encoding="utf-8")

    line = ""
    while True:
        buff = fh.read(1024)
        if not buff:
            break

        line += buff

        rows = list(re.finditer(pattern, line))
        for row in rows:
            try:
                process_page_row(row.groups(), dictionary)
            except Exception, e:
                print "uhoh: %s" % e

        if len(rows) > 0:
            line = line[rows[-1].end():]


if __name__ == "__main__":
    main()

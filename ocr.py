#!/usr/bin/env python

"""
ocr.py reads an Alto OCR XML file and prints out the ratio of dictionary words 
to all words for the document
"""

import re
import sys
import dbm

from xml.sax.handler import ContentHandler, feature_namespaces
from xml.sax import make_parser

def main(ocr_filename):
    handler = AltoHandler()
    parser = make_parser()
    parser.setContentHandler(handler)
    parser.setFeature(feature_namespaces, 0)
    parser.parse(ocr_filename)
    print handler.words


class AltoHandler(ContentHandler):

    def __init__(self):
        self.words = []
        #self.dictionary = dbm.open('dictionary')

    def startElement(self, tag, attrs):
        if tag == 'String':
            word = attrs.get("CONTENT").lower()
            self.words.append(word)

if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)

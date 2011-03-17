#!/usr/bin/env python

"""
alto_words.py reads an Alto OCR XML file and prints out the ratio of 
dictionary words to all words for the document. 

    alto-words.py example.xml

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
    print handler.ratio


class AltoHandler(ContentHandler):

    def __init__(self):
        self.dictionary = dbm.open('dictionary')
        self.dictionary_words = []
        self.words = []

    def startElement(self, tag, attrs):
        if tag == 'String':
            word = attrs.get("CONTENT").lower()
            if self.dictionary.has_key(word):
                self.dictionary_words.append(word)
            self.words.append(word)

    @property
    def ratio(self):
        return len(self.dictionary_words) / float(len(self.words))

if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)

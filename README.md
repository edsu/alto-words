# Alto words

This is a simplistic demonstration of how you can calculate the
ratio of dictionary words to all words in a METS Alto OCR XML file.

A dump of Wiktionary is used as source for the dictionary.

The latest dump of the English Wiktionary is used because its available
and somewhat sizable: ~2 million words.

```sh
    $ make dictionary.db
```

**Downloading the dump and creating the dictionary database will take a bit of time.**

Afterwarts the script `alto_words.py` can be used to compute the ratio of dictionary words.

```sh
    $ make install
    $ source ./.venv/bin/activate
    $ python alto_words.py example.xml
```

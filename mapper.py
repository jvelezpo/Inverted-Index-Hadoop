#!/usr/bin/env python

from sys import stdin
import re
import os

for line in stdin:

        # Get the file path
        doc_id = os.environ["map_input_file"]

        # Get the name of the file from the path
        doc_id = re.findall(r'\w+', doc_id)[-1]

        # Get an array of all the words inside the document
        words = re.findall(r'\w+', line.strip())

        # Map the words
        for word in words:
                print("%s\t%s:1" % (word.lower(), doc_id))
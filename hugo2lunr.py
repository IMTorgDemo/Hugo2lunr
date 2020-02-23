#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Jason Beach"
__version__ = "0.1.0"
__license__ = "MIT"



#imports
import os
import sys
import re, string
import argparse
import json

import numpy as np
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer







#config

path = './data/'
file = path + 'word_assocation_ref.json'
with open(file, 'r') as fp:
    word_association_ref = json.load(fp)

nlp = spacy.load("en_core_web_lg")
doc = nlp("This is a sentence.")

math = nlp( word_association_ref["math"] )
cs = nlp( word_association_ref["cs"] )
biz = nlp( word_association_ref["biz"] )

def general_logistic(cs, math):
    Beta = 25
    t = math - cs
    return (1/(1+np.exp(-Beta*t)))







def main(args):

    #load file
    FILE_PATH_IN = args.input_dir
    FILE_PATH_OUT = args.output_dir

    os.chdir(FILE_PATH_IN)
    files = os.listdir()


    for file in files:

        FILE_IN = os.path.abspath( file)
        with open(FILE_IN, 'r') as file:
            lines = file.readlines()

        metadata = lines[1:9]

        content = '  '.join(lines[9:])
        content = content.replace("\n","")
        pattern = re.compile(r'([^\s\w]|_)+')
        content = pattern.sub('', content)
        content = ' '.join(content.split())


        #add rankings
        tfidf = TfidfVectorizer(min_df=3, analyzer='word', stop_words = 'english', sublinear_tf=True)
        tfidf.fit(content.split(' '))
        feature_names = tfidf.get_feature_names()

        def get_ifidf_for_words(text):
            tfidf_matrix= tfidf.transform([text]).todense()
            feature_index = tfidf_matrix[0,:].nonzero()[1]
            tfidf_scores = zip([feature_names[i] for i in feature_index], [tfidf_matrix[0, x] for x in feature_index])
            return dict(tfidf_scores)

        scores = get_ifidf_for_words(content)
        sorted_scores = {k: v for k, v in sorted(scores.items(), key=lambda item: item[1], reverse=True)}

        words = ' '.join(list(sorted_scores.keys()))
        doc1 = nlp(words)
        BizPt = doc1.similarity(biz)
        CsPt = doc1.similarity(cs)
        MathPt = doc1.similarity(math)

        xPt = general_logistic(CsPt, MathPt)
        yPt = BizPt


        #combine file components

        metadata.insert(4, f"location = [{xPt}, {yPt}]\n")
        combined = ''.join(metadata) + content


        #export file

        FILE_OUT = "/Users/jason.beach/Desktop/Projects/Hugo_Site-site_support_prj/hugo-hugo2lunr/test/output/output.md"
        print(FILE_OUT)

        with open(FILE_OUT, 'w') as file:
            file.write(combined)






if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument("input_dir", help="Required input folder")

    # Required positional argument
    parser.add_argument("output_dir", help="Required output folder")

    args = parser.parse_args()
    main(args)

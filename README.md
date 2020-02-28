# Hugo2Lunr

This is a commandline utility that allows the user of a Hugo site to input markdown files and transform them into lunr-readable markdown files that can then be indexed by lunr.js, for use with a Hugo site.  It also implements spacy nlp functions to determin file-content similarity among three different datascience foundation fields: i)math, ii)computer science, iii)business.

Hugo2lunr makes the following transormations:

* removes leading-row (above metadata) whitespace
* cleans content of special characters and other un-searchable text
* compares content-text to field-specific text
* provides metadata xy-coordinate point for where the filename should appear on a background image

For more information concerning the implementation of nlp tools for visual-referencing, see the [blog post](?).


# Usage

Using script

```
pipenv install
pipenv shell
python hugo2lunr/hugo2lunr.py  ./test/input ./test/output
```

Installing as commandline utility

```
pip3 install spacy
python3 -m spacy download en_core_web_lg

pipenv install
pipenv shell
pip wheel -w dist --verbose .
exit

pip3 install -e .
hugo2lunr  -h
hugo2lunr -i ./test/input -o ./test/output
```


# Test and Develop

```
pipenv install
pipenv install --dev pipenv-setup
pipenv-setup sync
pipenv run python hugo2lunr.py  ./test/input ./test/output
```
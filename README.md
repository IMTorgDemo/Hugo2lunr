# Hugo2Lunr

This is a commandline utility that allows the user of a Hugo site to input markdown files and transform them into lunr-readable markdown files that can then be indexed by lunr.js, for use with a Hugo site.  It also implements spacy nlp functions to determin file-content similarity among three different datascience foundation fields: i)math, ii)computer science, iii)business.

Hugo2lunr makes the following transormations:

* removes leading-row (above metadata) whitespace
* cleans content of special characters and other un-searchable text
* compares content-text to field-specific text
* provides metadata xy-coordinate point for where the filename should appear on a background image

For more information concerning the implementation of nlp tools for visual-referencing, see the [blog post](?).



# Usage

Direct use of script.

```
pipenv install
pipenv shell
python3 hugo2lunr/hugo2lunr.py  ./test/input ./test/output
```

Build and install with egg.

```
#(MANIFEST.in)include hugo2lunr/data/word_association_ref.json
#(setup.py)package_data={'': ['hugo2lunr/data/word_association_ref.json']},
python3 setup.py install --force
pip3 install .
hugo2lunr ./test/input ./test/output    #input_dir and output_dir
```

Building a wheel (bdist_wheel) and installing as commandline utility.  If you are building a wheel (bdist_wheel), then include_package_data and MANIFEST.in are ignored and you must use package_data and data_files.

```
#(setup.py)data_files=[('',['hugo2lunr/data/word_association_ref.json'])],
pip3 install spacy
python3 -m spacy download en_core_web_lg

pipenv install
pipenv shell
rm -rf build *.egg-info
pip wheel -w dist --verbose .
exit

#pip3 install -e .    #<<<FAIL
pip3 install . --user
hugo2lunr  -h
hugo2lunr ./test/input ./test/output    #input_dir and output_dir
```



# Test and Develop

```
pipenv install
pipenv install --dev pipenv-setup
pipenv-setup sync
pipenv run python hugo2lunr.py  ./test/input ./test/output
```
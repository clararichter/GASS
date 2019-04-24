#! /bin/bash

# Make the updated changelog
python3 make_changelog.py

# Make the document twice with latex so that the labels are handled correctly
pdflatex main.tex
pdflatex main.tex
mv main.pdf business_req.pdf

# akordy - songbook typesetting
Python scripts to help typeset songbooks from Guitar Ultimate-like plaintext via the LaTeX songs package.

This is a collection of scripts to create chorded PDF songbooks in LaTeX from the common plaintext format.
For a working example, see the [zpevnik repository](https://github.com/simberaj/zpevnik).
The scripts are as follows:

-   `regen.py` converts a directory of chorded plaintext `.txt` files to individual `.tex` files ready
    for ingestion by the `songs` LaTeX package. Sometimes, manual edits might be necessary.
-   `maketoc.py` creates `songs`-based tables of contents for the songbook - both by song title and by
    author.
-   `merge.py` merges the individual song `.tex` files into a single songbook. The result can be compiled
    using `pdflatex` to produce a PDF songbook, which will automatically ingest the tables of contents
    as well.
    
    `merge.py` includes the `init.tex` file at the beginning of the songbook to declare necessary LaTeX
    macros and include a title page. You will probably want to modify the part after `\begin{document}`
    for your songbook.

Other scripts are mostly one-time utilities that have become obsolete over time.

## Dependencies

-   Python 3
-   LaTeX with the songs package (should be installed automatically at first compilation attempt)

## Pull requests welcome!

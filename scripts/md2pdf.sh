#!/bin/bash
# run from the content dir
TEXT=
TEMPL=scripts/
DIST=output/
SRC=book_eu/

# This wraps lines and adds line number...
#     --listings -H ${TEMPL}listings-setup.tex \

#FILES=${TEXT}prologue.md ${TEXT}level1.md ${TEXT}level7.md
pandoc --template=${TEMPL}plantilla-kdp.latex \
    -V language=spanish -V lang=spanish \
    -V author='Pello Xabier Altadill Izura' -V title='Programazioa Ikasi'\
    -V documentclass=book\
    -smart --latex-engine=xelatex  \
    -o ${DIST}mukiak.pdf  \
    ${SRC}00.md \
    ${SRC}01.md \
    ${SRC}02.md \
    ${SRC}03.md \
    ${SRC}04.md \
    ${SRC}05.md \
    ${SRC}06.md \
    ${SRC}07.md \
            --toc

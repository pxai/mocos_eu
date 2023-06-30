#!/bin/bash
# run from the content dir
TEXT=
TEMPL=scripts/
DIST=../dist/

# This wraps lines and adds line number...
#     --listings -H ${TEMPL}listings-setup.tex \

#FILES=${TEXT}prologue.md ${TEXT}level1.md ${TEXT}level7.md
pandoc --template=${TEMPL}plantilla-kdp.latex \
    -V language=spanish -V lang=spanish \
    -V author='Pello Xabier Altadill Izura' -V title='Programación para niños'\
    -V documentclass=book\
    -S --latex-engine=xelatex  \
    -o ${DIST}handbook.pdf  \
    00.md \
    01.md \
    02.md \
    03.md \
    04.md \
    05.md \
    06.md \
    07.md \
            --toc

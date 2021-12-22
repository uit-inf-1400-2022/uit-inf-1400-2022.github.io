LATEX=pdflatex
BIBTEX=bibtex

all: pdf

pdf: example_report.tex example.bib
	$(LATEX) example_report
	$(BIBTEX) example_report
	$(LATEX) example_report
	$(LATEX) example_report
	rm example_report.aux example_report.bbl example_report.blg example_report.log

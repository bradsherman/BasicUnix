all: homework06.pdf

homework06.pdf: demographics.png report.tex
	pdflatex -jobname homework06 report.tex
	pdflatex -jobname homework06 report.tex

demographics.png: histogram.plt 
	gnuplot histogram.plt

histogram.plt: demog.dat
	demo_stats.sh

clean:
	rm -f homework06.pdf demographics.png

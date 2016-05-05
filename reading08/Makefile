all: reading08.pdf

reading08.pdf: results.png report.tex 
	pdflatex -jobname reading08 report.tex 
results.png: histogram.plt 
	gnuplot> load 'histogram.plt'
clean:
	rm -f reading08.pdf results.png

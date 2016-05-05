all: project01.pdf

project01.pdf: latency.png throughput.png report.tex
	pdflatex -jobname project01 report.tex
	pdflatex -jobname project01 report.tex

latency.png: latency.plt
	gnuplot latency.plt

throughput.png: throughput.plt
	gnuplot throughput.plt

clean:
	rm -f project01.pdf latency.png throughput.png project01.aux project01.log project01.out

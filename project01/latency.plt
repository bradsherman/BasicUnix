set terminal png
set datafile separator "\t"
set output "latency.png"
set yrange [0:.1]
set ylabel "Time (s)"
set grid
set ytic auto
set style data histogram
set style histogram cluster gap 1
set boxwidth .9 relative
set style fill solid 1.0 border
set key left
plot "latency.txt" u 2:xtic(1) title "Static Files", "latency.txt" u 3 title "Directory Listing", "latency.txt" u 4 title "CGI Scripts", "latencyforked.txt" u 2 title "Static (Forked)", "latencyforked.txt" u 3 title "Directory (Forked)", "latencyforked.txt" u 4 title "CGI (Forked)"

set terminal png
set datafile separator "\t"
set output "throughput.png"
set yrange [0:40000000]
set ylabel "Rate (B/s)"
set grid
set ytic auto
set style data histogram
set style histogram cluster gap 1
set boxwidth .9 relative
set style fill solid 1.0 border
set key left
plot "throughput.txt" u 2:xtic(1) title "1KB", "throughput.txt" u 3 title "1MB", "throughput.txt" u 4 title "1GB", "throughputforked.txt" u 2 title "1KB (Forked)", "throughputforked.txt" u 3 title "1MB (Forked)", "throughputforked.txt" u 4 title "1GB (Forked)"

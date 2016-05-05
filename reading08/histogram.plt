#histogram.plt


set terminal x11 persist size 400,300 enhanced font "Arial,20"
set output 'results.png'
set grid
set title 'Results'
set yrange [0:300]
set xrange [0:7]
set xlabel 'Number rolled'
set ylabel 'Number of rolls'
set xtic auto
set ytic auto
set boxwidth .9 relative
set style fill solid
plot 'results.dat' with boxes lc rgb"blue"

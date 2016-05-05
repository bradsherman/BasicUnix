# Plot a histogram using collected demographic data
#set terminal x11 persist size 800,600 enhanced font "Arial,20"
set terminal png 
set datafile separator ","
set output 'demographics.png'
set key inside left top
set title 'Demographic Data in CSE at Notre Dame'
set xlabel 'Year'
set ylabel 'Number of Students'
set ytic auto
set style data histogram
set style histogram cluster gap 1
set boxwidth .9 relative
set style fill solid 1.0 border
set yrange[0:100]
plot 'demog.dat' using 2:xtic(1) t "Male", '' using 3 t "Female", '' using 4 t "Caucasian", '' using 5 t "Oriental", '' using 6 t "Hispanic", '' using 7 t "African American", '' using 8 t "Native American", '' using 9 t "Multiple", '' using 10 t "Undeclared"
 

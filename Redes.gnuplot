set datafile separator ","
set output 'imgs/Redes.png'
set terminal png
set key title inside bottom
plot 'data/A.csv'  using 1:2 title 'A' with line,\
	'data/B.csv'  using 1:2 title 'B' with line,\
	'data/C.csv'  using 1:2 title 'C' with line,\
	'data/D.csv'  using 1:2 title 'D' with line,\
	'data/E.csv'  using 1:2 title 'E' with line,\
	'data/F.csv'  using 1:2 title 'F' with line

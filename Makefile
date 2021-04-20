

PLOTTER=gnuplot
PLOTTER_FILE=Redes.gnuplot
PLOTTER_DATA=$(wildcard data/*.csv)
PLOTTER_OUT=imgs/Redes.png

TEX=pdflatex
TEX_FILE=RNA.tex
TEX_TARGET=$(TEX_FILE:.tex=.pdf)

.PHONY: all

all: $(TEX_TARGET)

$(TEX_TARGET): $(TEX_FILE) $(PLOTTER_OUT)
	$(TEX) $<

$(PLOTTER_OUT): $(PLOTTER_FILE) $(PLOTTER_DATA)
	$(PLOTTER) $<



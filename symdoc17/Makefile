all: t3d.html

clean:
	rm t3d.md t3d.html
	rm -rf __pycache__

t3d.html: t3d.py
	python t3d.py --symdoc
	pandoc -t html -o t3d.html --standalone --mathjax t3d.md

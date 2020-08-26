all: SKK-JISYO.jawiki

clean:
	rm -f jawiki-latest-pages-articles.xml.bz2 jawiki-latest-pages-articles.xml grepped.txt scanned.tsv filtered.tsv SKK-JISYO.jawiki skipped.tsv

test:
	python -m unittest tests/test_filter.py
	pytest tests/test_hojin_filter.py
	pytest tests/test_filter_entry.py
	pytest tests/test_scan_words.py

jawiki-latest-pages-articles.xml.bz2:
	wget -nc https://dumps.wikimedia.org/jawiki/latest/jawiki-latest-pages-articles.xml.bz2

jawiki-latest-pages-articles.xml: jawiki-latest-pages-articles.xml.bz2
	bunzip2 --keep jawiki-latest-pages-articles.xml.bz2

grepped.txt: jawiki-latest-pages-articles.xml
	grep -E "<title>.*</title>|'''[（(]" jawiki-latest-pages-articles.xml > grepped.txt

scanned.tsv: grepped.txt scanner.py jawiki/scanner.py
	python scanner.py grepped.txt

filtered.tsv: scanned.tsv filter.py jawiki/filter.py
	python filter.py scanned.tsv

SKK-JISYO.jawiki: filtered.tsv makedict.py /usr/share/skk/SKK-JISYO.L
	python makedict.py /usr/share/skk/SKK-JISYO.L

.PHONY: all test


TARGET=/usr/local/bin/pyob

install:
	cp -f pyob.py $(TARGET)

uninstall:
	rm -f  $(TARGET)


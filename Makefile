# Makefile for Tazcraft
#

PACKAGE=tazcraft
PREFIX?=/usr
DESTDIR?=

all:

# Installation (full or server only)

install:
	install -m 0755 -d $(DESTDIR)$(PREFIX)/bin
	install -m 0755 -d $(DESTDIR)$(PREFIX)/share/applications
	install -m 0755 -d $(DESTDIR)$(PREFIX)/share/pixmaps
	install -m 0755 -d $(DESTDIR)$(PREFIX)/share/doc/slitaz
	install -m 0755 $(PACKAGE) $(DESTDIR)$(PREFIX)/bin
	install data/minecraft.desktop $(DESTDIR)$(PREFIX)/share/applications
	install web/minecraft.png $(DESTDIR)$(PREFIX)/share/pixmaps
	install README $(DESTDIR)$(PREFIX)/share/doc/slitaz/tazcraft.txt

install-server:
	install -m 0755 -d $(DESTDIR)$(PREFIX)/bin
	install -m 0755 -d $(DESTDIR)$(PREFIX)/share/doc/slitaz
	install -m 0755 $(PACKAGE) $(DESTDIR)$(PREFIX)/bin
	install README $(DESTDIR)$(PREFIX)/share/doc/slitaz/tazcraft.txt
	
# Uninstallation

uninstall:
	rm -f $(DESTDIR)$(PREFIX)/bin/$(PACKAGE)


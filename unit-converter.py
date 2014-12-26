#!/usr/bin/python

from gi.repository import Gtk
from collections import OrderedDict

units=OrderedDict()
units[u"litre"]=1000
units[u"millilitre"]=1
units[u"cubic metre"]=1000000
units[u"barrel"]=15987
units[u"fluid ounce (oz)"]=29.5
units[u"gill"]=142
units[u"pint (pt)"]=568
units[u"quart (qt)"]=1137
units[u"gallon (gal)"]=4546

def getConvertedValue(unit1,unit2,value):
	return float(value)*units[unit1]/units[unit2]

def recalc(*args):
	inputtext=inp.get_text()
	if inputtext!="":
		x=getConvertedValue(combo1.get_active_text(),combo2.get_active_text(),inputtext)
		out.set_text(str(x))

handlers = {
    "onDeleteWindow": Gtk.main_quit,
    "recalc": recalc
}


builder = Gtk.Builder()
builder.add_from_file("layout.glade")

combo1 = builder.get_object("unit1")
combo2 = builder.get_object("unit2")

inp = builder.get_object("inputvalue")
out = builder.get_object("outputvalue")

for i in units.keys():
	combo1.append_text(i);
	combo2.append_text(i);

combo1.set_active(0)
combo2.set_active(1)
recalc()

window = builder.get_object("applicationwindow1")
window.show_all()
builder.connect_signals(handlers)

Gtk.main()

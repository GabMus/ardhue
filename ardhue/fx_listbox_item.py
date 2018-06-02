import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Gio, GdkPixbuf
# from . import threading_helper as ThreadingHelper
import os

class FXBox(Gtk.ListBoxRow):
    def __init__(self, fx, *args, **kwds):
        super().__init__(*args, **kwds)

        self.fx = fx

        self.set_halign(Gtk.Align.CENTER)
        self.set_valign(Gtk.Align.CENTER)

        self.container_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        self.fx_label = Gtk.Label()
        self.fx_label.set_text(self.fx.capitalize())
        # self.fx_label.set_ellipsize(3)
        self.fx_label.set_halign(Gtk.Align.START)

        self.container_box.pack_start(self.fx_label, True, True, 3)
        self.container_box.set_margin_left(12)
        self.container_box.set_margin_right(12)
        self.container_box.set_margin_top(12)
        self.container_box.set_margin_bottom(12)
        self.add(self.container_box)
        self.set_size_request(200, -1)

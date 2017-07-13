'''
TabbedPanel
============

Test of the widget TabbedPanel.
'''

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle

import threading

V24Power = False
V12Power = False
TrackerPower = False
SensorPower = True
FanPower = False
PlatePower = False
CincozePower = False
SpecPower = False

def PowerOff():
	global headSensorPower
	SensorPower = True
	threading.Timer(5.0, PowerOff).start()
	SensorPower = True
	
	print('code ran')

class V24Label(Label):
	def on_size(self, *args):
		global V24Power
		self.canvas.before.clear()
		with self.canvas.before:
			if V24Power:
				Color(0,1,0,.25)
			else:
				Color(1,.1,0,.5)
			Rectangle(pos=self.pos, size=self.size)

class V12Label(Label):
	def on_size(self, *args):
		global V12Power
		self.canvas.before.clear()
		with self.canvas.before:
			if V12Power:
				Color(0,1,0,.25)
			else:
				Color(1,.1,0,.5)
			Rectangle(pos=self.pos, size=self.size)		

class TrackerLabel(Label):
	def on_size(self, *args):
		global TrackerPower
		self.canvas.before.clear()
		with self.canvas.before:
			if TrackerPower:
				Color(0,1,0,.25)
			else:
				Color(1,.1,0,.5)
			Rectangle(pos=self.pos, size=self.size)

			
class SensorLabel(Label):
	def on_size(self, *args):
		global SensorPower
		self.canvas.before.clear()
		with self.canvas.before:
			if SensorPower:
				Color(0,1,0,.25)
			else:
				Color(1,.1,0,.5)
			Rectangle(pos=self.pos, size=self.size)

class FanLabel(Label):
	def on_size(self, *args):
		global FanPower
		self.canvas.before.clear()
		with self.canvas.before:
			if FanPower:
				Color(0,1,0,.25)
			else:
				Color(1,.1,0,.5)
			Rectangle(pos=self.pos, size=self.size)

class PlateLabel(Label):
	def on_size(self, *args):
		global PlatePower
		self.canvas.before.clear()
		with self.canvas.before:
			if PlatePower:
				Color(0,1,0,.25)
			else:
				Color(1,.1,0,.5)
			Rectangle(pos=self.pos, size=self.size)

class CincozeLabel(Label):
	def on_size(self, *args):
		global CincozePower
		self.canvas.before.clear()
		with self.canvas.before:
			if CincozePower:
				Color(0,1,0,.25)
			else:
				Color(1,.1,0,.5)
			Rectangle(pos=self.pos, size=self.size)

class SpectrometerLabel(Label):
	def on_size(self, *args):
		global SpecPower
		self.canvas.before.clear()
		with self.canvas.before:
			if SpecPower:
				Color(0,1,0,.25)
			else:
				Color(1,.1,0,.5)
			Rectangle(pos=self.pos, size=self.size)
			

Builder.load_string("""

<Test>:
    pos_hint: {'center_x': .5, 'center_y': .5}
    do_default_tab: False

    TabbedPanelItem:
        text: 'Power Flow'
        FloatLayout:
			V24Label:
				text: '24V Power'
				font_size: 25
				size_hint: .4, .1
				pos: 30, 450
				color: 0,0,0,1
			SensorLabel:
				text: 'Head Sensor'
				font_size: 25
				size_hint: .4, .1
				pos: 30, 350
				color: 0,0,0,1
			CincozeLabel:
				text: 'Cincoze'
				font_size: 25
				size_hint: .4, .1
				pos: 30, 250
				color: 0,0,0,1
			PlateLabel:
				text: 'Cold Plate'
				font_size: 25
				size_hint: .4, .1
				pos: 30, 150
				color: 0,0,0,1
			V12Label:
				text: '12V Power'
				font_size: 25
				size_hint: .4, .1
				pos: 450, 450
				color: 0,0,0,1
			TrackerLabel:
				text: 'Tracker'
				font_size: 25
				size_hint: .4, .1
				pos: 450, 350
				color: 0,0,0,1	
			FanLabel:
				text: 'Box Fan'
				font_size: 25
				size_hint: .4, .1
				pos: 450, 250
				color: 0,0,0,1
			SpectrometerLabel:
				text: 'Spectrometer'
				font_size: 25
				size_hint: .4, .1
				pos: 450, 150
				color: 0,0,0,1
    TabbedPanelItem:
        text: 'tab2'
        BoxLayout:
            Label:
                text: 'Second tab content area'
            Button:
                text: 'Button that does nothing'
    TabbedPanelItem:
        text: 'tab3'
        RstDocument:
            text:
                '\\n'.join(("Hello world", "-----------",
                "You are in the third tab."))

""")


class Test(TabbedPanel):
    pass


class TabbedPanelApp(App):
    def build(self):
        return Test()
		
		
if __name__ == '__main__':
	PowerOff()
	TabbedPanelApp().run()

import kivy
kivy.require('1.9.0')

# required kivy applications for gui
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.tabbedpanel import TabbedPanel

# for GPIO integration
#import RPi.GPIO as GPIO


import time

# changes background color to grey
Window.clearcolor = (.8, .8, .8, 1)

headSensorPower = True

class MyLabel(Label):
	def on_size(self, *args):
		global headSensorPower
		self.canvas.before.clear()
		with self.canvas.before:
			if headSensorPower:
				Color(0,1,0,.25)
			else:
				Color(1,0,0,0)
			Rectangle(pos=self.pos, size=self.size)

class DashboardApp(App):
	
	def build(self):
		layout = FloatLayout()

		V24PowerLabel = MyLabel(
			text='24V Power', 
			font_size=25,
			size_hint = (.33, .1),
			pos=(30,500),
			color=(0,0,0,1)
			)
		
		HeadSensorLabel = MyLabel(
			text='Head Sensor Power', 
			font_size=25,
			size_hint = (.33, .1),
			pos=(30,400),
			color=(0,0,0,1)
			)
		
		V12PowerLabel = MyLabel(
			text='12V Power', 
			font_size=25,
			size_hint = (.33, .1),
			pos=(450,500),
			color=(0,0,0,1)
			)
			
		TrackerLabel = MyLabel(
			text='Tracker Power', 
			font_size=25,
			size_hint = (.33, .1),
			pos=(450,400),
			color=(0,0,0,1)
			)
		
		layout.add_widget(V24PowerLabel)
		layout.add_widget(HeadSensorLabel)
		layout.add_widget(V12PowerLabel)
		layout.add_widget(TrackerLabel)
		
		return layout

if __name__ == '__main__':
	DashboardApp().run()

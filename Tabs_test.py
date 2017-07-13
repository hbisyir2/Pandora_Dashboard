
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button

import threading

V24Power = False
V12Power = False
TrackerPower = False
SensorPower = True
FanPower = False
PlatePower = False
CincozePower = False
SpecPower = False
ct = 0
	
# class V24Label(Label):
	# def on_size(self, *args):
		# global V24Power
		# self.canvas.before.clear()
		# with self.canvas.before:
			# if V24Power:
				# Color(0,1,0,.25)
			# else:
				# Color(1,.1,0,.5)
			# Rectangle(pos=self.pos, size=self.size)

# class V12Label(Label):
	# def on_size(self, *args):
		# global V12Power
		# self.canvas.before.clear()
		# with self.canvas.before:
			# if V12Power:
				# Color(0,1,0,.25)
			# else:
				# Color(1,.1,0,.5)
			# Rectangle(pos=self.pos, size=self.size)		

# class TrackerLabel(Label):
	# def on_size(self, *args):
		# global TrackerPower
		# self.canvas.before.clear()
		# with self.canvas.before:
			# if TrackerPower:
				# Color(0,1,0,.25)
			# else:
				# Color(1,.1,0,.5)
			# Rectangle(pos=self.pos, size=self.size)

			
# class SensorLabel(Label):
	# def on_size(self, *args):
		# global SensorPower
		# self.canvas.before.clear()
		# with self.canvas.before:
			# if SensorPower:
				# Color(0,1,0,.25)
			# else:
				# Color(1,.1,0,.5)
			# Rectangle(pos=self.pos, size=self.size)

# class FanLabel(Label):
	# def on_size(self, *args):
		# global FanPower
		# self.canvas.before.clear()
		# with self.canvas.before:
			# if FanPower:
				# Color(0,1,0,.25)
			# else:
				# Color(1,.1,0,.5)
			# Rectangle(pos=self.pos, size=self.size)

# class PlateLabel(Label):
	# def on_size(self, *args):
		# global PlatePower
		# self.canvas.before.clear()
		# with self.canvas.before:
			# if PlatePower:
				# Color(0,1,0,.25)
			# else:
				# Color(1,.1,0,.5)
			# Rectangle(pos=self.pos, size=self.size)

# class CincozeLabel(Label):
	# def on_size(self, *args):
		# global CincozePower
		# self.canvas.before.clear()
		# with self.canvas.before:
			# if CincozePower:
				# Color(0,1,0,.25)
			# else:
				# Color(1,.1,0,.5)
			# Rectangle(pos=self.pos, size=self.size)

# class SpectrometerLabel(Label):
	# def on_size(self, *args):
		# global SpecPower
		# self.canvas.before.clear()
		# with self.canvas.before:
			# if SpecPower:
				# Color(0,1,0,.25)
			# else:
				# Color(1,.1,0,.5)
			# Rectangle(pos=self.pos, size=self.size)
			
class MyLabel(Label):
	def on_size(self, *args):
		self.canvas.before.clear()
		with self.canvas.before:
			Color(0,1,0,.25)
			Rectangle(pos=self.pos, size=self.size)

class DashboardApp(App):
	
	def build(self):
		AllTabs = TabbedPanel(
			do_default_tab = False
			)
		
		PowerLayout = FloatLayout()
		
		V24Indicator = MyLabel(
				text='24V Power', 
				font_size=25,
				size_hint = (.33, .1),
				pos=(30,450),
				color=(0,0,0,1)
			)
			
		SensorIndicator = MyLabel(
				text='Head Sensor', 
				font_size=25,
				size_hint = (.33, .1),
				pos=(30,350),
				color=(0,0,0,1)
			)
			
		CincozeIndicator = MyLabel(
				text='Cincoze', 
				font_size=25,
				size_hint = (.33, .1),
				pos=(30,250),
				color=(0,0,0,1)
			)
			
		PlateIndicator = MyLabel(
				text='Cold Plate', 
				font_size=25,
				size_hint = (.33, .1),
				pos=(30,150),
				color=(0,0,0,1)
			)
			
		V12Indicator = MyLabel(
				text='12V Power', 
				font_size=25,
				size_hint = (.33, .1),
				pos=(450,450),
				color=(0,0,0,1)
			)
			
		TrackerIndicator = MyLabel(
				text='Tracker', 
				font_size=25,
				size_hint = (.33, .1),
				pos=(450,350),
				color=(0,0,0,1)
			)
			
		FanIndicator = MyLabel(
				text='Box Fan', 
				font_size=25,
				size_hint = (.33, .1),
				pos=(450,250),
				color=(0,0,0,1)
			)
			
		SpecIndicator = MyLabel(
				text='Tracker', 
				font_size=25,
				size_hint = (.33, .1),
				pos=(450,150),
				color=(0,0,0,1)
			)
			
		PowerLayout.add_widget(V24Indicator)
		PowerLayout.add_widget(SensorIndicator)
		PowerLayout.add_widget(CincozeIndicator)
		PowerLayout.add_widget(PlateIndicator)
		PowerLayout.add_widget(V12Indicator)
		PowerLayout.add_widget(TrackerIndicator)
		PowerLayout.add_widget(FanIndicator)
		PowerLayout.add_widget(SpecIndicator)
		
		
		PowerFlowTab = TabbedPanelHeader(text='Power Flow')
		PowerFlowTab.content = PowerLayout
		AllTabs.add_widget(PowerFlowTab)
		##############################################
		AtmosphereLayout = FloatLayout()
		
		SensorsLabel = Label(
			text='Information from Sensors', 
			font_size=25,
			size_hint = (.33, .1),
			pos=(450,150),
			color=(0,0,0,1)
		)
		
		AtmosphereLayout.add_widget(SensorsLabel)
		AtmosphereTab = TabbedPanelHeader(text='Atmosphere')
		AtmosphereTab.content = AtmosphereLayout
		AllTabs.add_widget(AtmosphereTab)
		
		def UpdateLabels():
			global V24Power, ct
			threading.Timer(5.0, UpdateLabels).start()
			if ct%2 == 0:
				V24Power = True
				print('Turn GREEN')
				V24Indicator.canvas.before.clear()
				with V24Indicator.canvas.before:
					Color(0,1,0,.25)
					Rectangle(pos=V24Indicator.pos, size=V24Indicator.size)
			else:
				V24Power = False
				print('Turn RED')
				V24Indicator.canvas.before.clear()
				with V24Indicator.canvas.before:
					Color(1,.1,0,.25)
					Rectangle(pos=V24Indicator.pos, size=V24Indicator.size)
			print('code ran')
			ct+=1
			print('\n')
		
		UpdateLabels()
		
		return AllTabs

if __name__ == '__main__':
	DashboardApp().run()

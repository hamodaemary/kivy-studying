from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
Window.size = (400,600)
Builder.load_file('baba.kv')
class Bob(Widget):
	def btn(self):
		show()
class Float(FloatLayout):
	pass
class Baba(App):
	def build(self):
		return Bob()
def show():
	c = Float()
	pop = Popup(title='hi',content=c,size_hint=(None,None),size=(500,500))
	pop.open()
Baba().run()
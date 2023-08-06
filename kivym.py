from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.app import runTouchApp
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
Window.size = (400,600)
class Baba(GridLayout):
	def __init__(self,**kwargs):
		super(Baba,self).__init__(**kwargs)
		self.cols=1
		self.inside = GridLayout()
		self.inside.cols=2
		self.cols =2
		self.inside.add_widget(Label(text='name'))
		self.name = TextInput()
		self.inside.add_widget(self.name)
		self.inside.add_widget(Label(text='email'))
		self.email = TextInput()
		self.inside.add_widget(self.email)
		self.inside.add_widget(Label(text='pass'))
		self.passq =  TextInput()
		self.inside.add_widget(self.passq)
		self.submit=Button(text='submit')
		self.add_widget(self.submit)
		self.add_widget(self.inside)
		self.submit.bind(on_press=self.press)
	def press(self,instance):
		name = self.name.text
		email = self.email.text
		pasw = self.passq.text
		print(f'name:{name},email:{email},password:{pasw}')
		self.add_widget(Label(text=f'name:{name},email:{email},password:{pasw}'))
		self.name.text = ''
		self.email.text = ''
		self.passq.text=''

class Bab(App):
	def build(self):
		return Baba()
if __name__ == '__main__':
	Bab().run()

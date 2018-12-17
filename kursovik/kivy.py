import kivy
kivy.require('1.10.1')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager 
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from functions import*


class MainScreen(Screen):
	def __init__(self, **kwargs):
		super(MainScreen, self).__init__(**kwargs)

		self.title = Label(text = "Choose one of the options:", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.80}, font_size='30sp')
		self.add_widget(self.title)

		self.convert1 = Button(text = "Get keys", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.70})
		self.convert1.bind(on_press = self.changer1)
		self.add_widget(self.convert1)

		self.convert2 = Button(text = "Cipher string", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.60})
		self.convert2.bind(on_press = self.changer2)
		self.add_widget(self.convert2)

		self.convert3 = Button(text = "Decipher string", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.50})
		self.convert3.bind(on_press = self.changer3)
		self.add_widget(self.convert3)

		self.convert4 = Button(text = "Cipher file to new file", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.40})
		self.convert4.bind(on_press = self.changer4)
		self.add_widget(self.convert4)

		self.convert5 = Button(text = "Decipher file to new file", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.30})
		self.convert5.bind(on_press = self.changer5)
		self.add_widget(self.convert5)


		self.quit = Button(text = "Quit", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.1}, background_color = [1,0,0,1], font_size='20sp')
		self.quit.bind(on_press = self.quit_press)

		self.add_widget(self.quit)

	def changer1(self,*args): 
		self.manager.current = 'keyScreen'

	def changer2(self,*args): 
		self.manager.current = 'cipherScreen'

	def changer3(self,*args): 
		self.manager.current = 'decipherScreen'

	def changer4(self,*args): 
		self.manager.current = 'cipherfromfileScreen'

	def changer5(self,*args): 
		self.manager.current = 'decipherfromfileScreen'

	def quit_press():
		sys.exit()


class KeysScreen(Screen):
	def __init__(self, **kwargs):
		super(KeysScreen, self).__init__(**kwargs)

		self.convert = Button(text = "Получить ключи", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.7}, background_color = [1,1,1,1], font_size='20sp')
		self.convert.bind(on_press = self.get_k)

		self.add_widget(self.convert)

		self.output1 = TextInput(multiline = False, text = "0", size_hint=(.3, .1), pos_hint={'x':.4, 'y':.5})
		self.add_widget(self.output1)

		self.output2 = TextInput(multiline = False,text = "0", size_hint=(.3, .1), pos_hint={'x':.4, 'y':.4})
		self.add_widget(self.output2)

		self.output3 = Label(text = "Open key: ", size_hint=(.6, .1), pos_hint={'x':.0, 'y':.5})
		self.add_widget(self.output3)

		self.output4 = Label(text = "Close key: ", size_hint=(.6, .1), pos_hint={'x':.0, 'y':.4})
		self.add_widget(self.output4)

		self.convert2 = Button(text = "Return to main screen", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.1}, font_size='30sp')
		self.convert2.bind(on_press = self.changer)
		self.add_widget(self.convert2)

	def changer(self,*args):
		self.manager.current = 'mainScreen'


	def get_k(self,*args):
		self.convert.background_color = [0,1,1,1]
		n = get_keys()
		self.output1.text = str(n[1])
		self.output2.text = str(n[0])

	def push(self,*args):
		self.convert.background_color = [1,0,0,1]
		self.get_k()

class CipherScreen(Screen):
	def __init__(self, **kwargs):
		super(CipherScreen, self).__init__(**kwargs)

		self.label1 = Label(text = "Input your text to cipher: ", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.9}, font_size='30sp')
		self.add_widget(self.label1)

		self.input = TextInput(multiline = True, size_hint=(.6, .1), pos_hint={'x':.2, 'y':.8})
		self.add_widget(self.input)

		self.label2 = Label(text = "Input your open key: ", size_hint=(.6, .1), pos_hint={'x':.0, 'y':.6})
		self.add_widget(self.label2)

		self.input_o = TextInput(multiline = False, text = "[]", size_hint=(.3, .1), pos_hint={'x':.5, 'y':.6})
		self.add_widget(self.input_o)

		self.convert = Button(text = "Make cipher", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.45})
		self.convert.bind(on_press = self.changer2)
		self.add_widget(self.convert)

		self.label3 = Label(text = "Your Cipher: ", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.35})
		self.add_widget(self.label3)

		self.output = TextInput(multiline = True,text = "", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.25})
		self.add_widget(self.output)

		self.convert = Button(text = "Return to main screen", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.1})
		self.convert.bind(on_press = self.changer1)
		self.add_widget(self.convert)

	def changer1(self,*args):
		self.manager.current = 'mainScreen'

	def changer2(self,*args):
		text = self.input.text
		#c = self.input_o.text
		open_key = str_open_key_2list(self.input_o.text)
		c = encrypt_text(text, open_key)
		self.output.text = str(c)

class DecipherScreen(Screen):
	def __init__(self, **kwargs):
		super(DecipherScreen, self).__init__(**kwargs)

		self.label1 = Label(text = "Input your cipher: ", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.9}, font_size='30sp')
		self.add_widget(self.label1)

		self.input = TextInput(multiline = True, size_hint=(.6, .1), pos_hint={'x':.2, 'y':.8})
		self.add_widget(self.input)

		self.label2 = Label(text = "Input your open key: ", size_hint=(.6, .1), pos_hint={'x':.0, 'y':.7})
		self.add_widget(self.label2)

		self.input_o = TextInput(multiline = False, text = "[]", size_hint=(.3, .1), pos_hint={'x':.5, 'y':.7})
		self.add_widget(self.input_o)

		self.label3 = Label(text = "Input your close key: ", size_hint=(.6, .1), pos_hint={'x':.0, 'y':.6})
		self.add_widget(self.label3)

		self.input_c = TextInput(multiline = False, size_hint=(.3, .1), pos_hint={'x':.5, 'y':.6})
		self.add_widget(self.input_c)

		self.convert = Button(text = "Decipher", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.45})
		self.convert.bind(on_press = self.changer2)
		self.add_widget(self.convert)

		self.label4 = Label(text = "Your Text is: ", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.35})
		self.add_widget(self.label4)

		self.output = TextInput(multiline = True,text = "", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.25})
		self.add_widget(self.output)

		self.convert = Button(text = "Return to main screen", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.1})
		self.convert.bind(on_press = self.changer1)
		self.add_widget(self.convert)

	def changer1(self,*args):
		self.manager.current = 'mainScreen'

	def changer2(self,*args):
		cipher = from_str2lst(self.input.text)
		open_key = str_open_key_2list(self.input_o.text)
		close_key = int(self.input_c.text)
		c = decipher_text(cipher,open_key,close_key)
		self.output.text = str(c)

class CipherFromFileScreen(Screen):
	def __init__(self, **kwargs):
		super(CipherFromFileScreen, self).__init__(**kwargs)

		self.label1 = Label(text = "Write filename you want to cipher in 'name.txt' format ", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.9})
		self.add_widget(self.label1)

		self.input1 = TextInput(multiline = True, size_hint=(.6, .1), pos_hint={'x':.2, 'y':.8})
		self.add_widget(self.input1)

		self.label2 = Label(text = "Input your open key: ", size_hint=(.6, .1), pos_hint={'x':.0, 'y':.6})
		self.add_widget(self.label2)

		self.input_o = TextInput(multiline = False, text = "[]", size_hint=(.3, .1), pos_hint={'x':.5, 'y':.6})
		self.add_widget(self.input_o)

		self.label3 = Label(text = "Write filename to cipher in 'new_name.txt' format ", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.5})
		self.add_widget(self.label3)

		self.input2 = TextInput(multiline = True,text = "", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.4})
		self.add_widget(self.input2)

		self.convert1 = Button(text = "Make cipher", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.3})
		self.convert1.bind(on_press = self.changer2)
		self.add_widget(self.convert1)

		self.label4 = Label(text = "", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.2})
		self.add_widget(self.label4)

		self.convert2 = Button(text = "Return to main screen", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.1})
		self.convert2.bind(on_press = self.changer1)
		self.add_widget(self.convert2)

	def changer1(self,*args):
		self.manager.current = 'mainScreen'

	def changer2(self,*args):
		filename = self.input1.text
		newfilename = self.input2.text
		open_key = str_open_key_2list(self.input_o.text)
		encrypt_text_from_file2newfile(filename,newfilename,open_key)
		self.label4.text = 'Cipher has been written in ' + newfilename

class DecipherFromFileScreen(Screen):
	def __init__(self, **kwargs):
		super(DecipherFromFileScreen, self).__init__(**kwargs)

		self.label1 = Label(text = "Write filename you want to decipher in 'name.txt' format ", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.9})
		self.add_widget(self.label1)

		self.input1 = TextInput(multiline = True, size_hint=(.6, .1), pos_hint={'x':.2, 'y':.8})
		self.add_widget(self.input1)

		self.label2 = Label(text = "Input your open key: ", size_hint=(.6, .1), pos_hint={'x':.0, 'y':.7})
		self.add_widget(self.label2)

		self.input_o = TextInput(multiline = False, text = "[]", size_hint=(.3, .1), pos_hint={'x':.5, 'y':.7})
		self.add_widget(self.input_o)

		self.label3 = Label(text = "Input your close key: ", size_hint=(.6, .1), pos_hint={'x':.0, 'y':.6})
		self.add_widget(self.label3)

		self.input_c = TextInput(multiline = False, size_hint=(.3, .1), pos_hint={'x':.5, 'y':.6})
		self.add_widget(self.input_c)

		self.label4 = Label(text = "Write filename to decipher in 'new_name.txt' format ", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.5})
		self.add_widget(self.label4)

		self.input2 = TextInput(multiline = True,text = "", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.4})
		self.add_widget(self.input2)

		self.convert1 = Button(text = "Decipher", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.3})
		self.convert1.bind(on_press = self.changer2)
		self.add_widget(self.convert1)

		self.label5 = Label(text = "", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.2})
		self.add_widget(self.label5)

		self.convert2 = Button(text = "Return to main screen", size_hint=(.6, .1), pos_hint={'x':.2, 'y':.1})
		self.convert2.bind(on_press = self.changer1)
		self.add_widget(self.convert2)

	def changer1(self,*args):
		self.manager.current = 'mainScreen'

	def changer2(self,*args):
		filename = self.input1.text
		newfilename = self.input2.text
		open_key = str_open_key_2list(self.input_o.text)
		close_key = int(self.input_c.text)
		decipher_from_file2newfile(filename,newfilename,open_key,close_key)
		self.label5.text = 'Decipher has been written in ' + newfilename

class ElGamalApp(App):
	def build(self):
		my_screenmanager = ScreenManager()
		mainScreen = MainScreen(name='mainScreen')
		keyScreen = KeysScreen(name='keyScreen')
		cipherScreen = CipherScreen(name='cipherScreen')
		decipherScreen = DecipherScreen(name='decipherScreen')
		cipherfromfileScreen = CipherFromFileScreen(name='cipherfromfileScreen')
		decipherfromfileScreen = DecipherFromFileScreen(name='decipherfromfileScreen')
		my_screenmanager.add_widget(mainScreen)
		my_screenmanager.add_widget(keyScreen)
		my_screenmanager.add_widget(cipherScreen)
		my_screenmanager.add_widget(decipherScreen)
		my_screenmanager.add_widget(cipherfromfileScreen)
		my_screenmanager.add_widget(decipherfromfileScreen)
		return my_screenmanager


if __name__ == '__main__':
	ElGamalApp().run()
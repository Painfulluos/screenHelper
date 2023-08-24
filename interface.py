from tkinter import Tk, Menu, Button, HORIZONTAL, Label, PhotoImage
from tkinter.ttk import Progressbar
from pynput import keyboard

from interface_functional import InterfaceFuncs
from logger import logger


class PyScreenHelper(Tk):
	
	def __init__(self):
		super().__init__()
		self.window_conf()

	def window_conf(self):
		self.title("ScreenHelper")
		self.geometry("400x300")
		self.iconphoto(True, PhotoImage(file='./icon.png'))
		self.focus_force()

	def run(self):
		self.draw_menu()
		self.widgets()

		self.start_key_listener()

		self.mainloop()

	def draw_menu(self):
		self.menu_bar = Menu(self)

		self.file_menu = Menu(self.menu_bar, tearoff=0)
		self.file_menu.add_separator()
		self.file_menu.add_command(label="Выход", command=lambda:InterfaceFuncs().close_program(self))
		
		self.menu_bar.add_cascade(label="Файл", menu=self.file_menu)

		self.configure(menu=self.menu_bar)

	def widgets(self):
		self.label_save_path_text = Label(self, text="Путь сохранения изображения:", font=("Arial Bold", 12))
		self.label_save_path_text.grid(row=0,column=0)

		self.label_save_path = Label(self, text="", font=("Arial Bold", 12))
		self.label_save_path.grid(row=1,column=0)
		InterfaceFuncs().change_save_path_label(self.label_save_path)

		self.button_change_save_path = Button(self, text="Изменить путь", command=lambda:InterfaceFuncs().change_save_path(self.label_save_path))
		self.button_change_save_path.grid(row=2, column=0)

		self.button_change_save_path = Button(self, text="Сделать скрин", command=lambda:InterfaceFuncs().make_screen(self))
		self.button_change_save_path.grid(row=3, column=0)

	def start_key_listener(self):
		self.listener = keyboard.Listener(on_press=self.on_keypress)
		self.listener.start()

	def on_keypress(self, key):
		if key == keyboard.Key.print_screen:

			try:
				logger.info("key pressed")

				InterfaceFuncs().make_screen(self)

			except Exception as e:
				logger.error(e)
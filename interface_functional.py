from tkinter import Tk, HORIZONTAL, Label
from tkinter import filedialog as fd
from tkinter.ttk import Progressbar

import time
import threading

from config import settings
from logger import logger
from screenshot import Screenshot


class InterfaceFuncs():
	def change_save_path(self,label):
		try:
			save_path = fd.askdirectory()
			settings.set_save_path(save_path)
			self.change_save_path_label(label)
			settings.save_settings_to_file()
			logger.info("Successfully change pass")
		except Exception as e:
			logger.error(e)

	def make_screen(self, root):

		try:

			save_path = settings.SAVE_PATH
			img_name = Screenshot().save_img(save_path)

			root.clipboard_clear()
			root.clipboard_append(img_name)

			self.show_progress()

		except Exception as e:
			logger.error(e)
				

	def show_progress(self):

		def close_window():
			progress_window.destroy()

		progress_window = Tk()
		
		width, height = progress_window.winfo_screenwidth(), progress_window.winfo_screenheight()
		progress_window.geometry(f"150x200+{width-150}+{height-100}")

		progress_window.after(500, close_window)
			# progressbar = Progressbar(progress_window, orient=HORIZONTAL, length=100, mode='indeterminate')
			# progressbar.pack()
			# progressbar.start()

			# time.sleep(1)

			# progressbar.stop()

		label = Label(progress_window, text="Screenshot saved", font=("Arial Bold", 12))
		label.pack()			

		# threading.Thread(target=real_show_progress).start()

		progress_window.mainloop()

	def change_save_path_label(self, label):
		label.configure(text=settings.SAVE_PATH)

	def close_program(self,root):
			root.quit()
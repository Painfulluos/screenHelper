import os
import json


class Settings():
	def __init__(self):
		self.SETTINGS_FILE = "settings.json"
		self.BASE_DIR = os.path.dirname(os.path.dirname(__file__))
		self.SAVE_PATH = ""
		self.set_save_path()
		self.load_settings_from_file()

	def set_save_path(self, path : str = ""):
		try:
			if not path:
				if not self.SAVE_PATH:
					path = self.BASE_DIR
				else:
					path = self.SAVE_PATH
					
			self.SAVE_PATH = path
		except Exception as e:
			print(e)
		# try:
		# 	if path != self.BASE_DIR:
		# 		self.SAVE_PATH = path + "\\screens"
		# 		self.__create_screens_dir(self.SAVE_PATH)
		# except Exception as e:
		# 	print(e)

	def get_save_path(self):

		return self.SAVE_PATH


	#  Сохранение настроек в файл
	def save_settings_to_file(self):
		info = {"save_path": self.SAVE_PATH}
		with open(self.SETTINGS_FILE, 'w') as f:
			json.dump(info, f, indent=4)

	#  Загрузка настроек из файла
	def load_settings_from_file(self):

		if not os.path.exists(self.SETTINGS_FILE):
				with open(self.SETTINGS_FILE, 'w') as f:
					json.dump({"save_path": ""}, f)
		else:
			with open(self.SETTINGS_FILE, "r") as f:
				config = json.load(f)
				if config["save_path"] == "":
					return
				self.SAVE_PATH = config["save_path"]


	# def __create_screens_dir(self, save_path):

	# 	if not os.path.isdir(save_path):
	# 		os.mkdir(save_path)


settings = Settings()

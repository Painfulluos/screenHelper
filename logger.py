import os
from datetime import datetime


class Logger:

	def error(self, text : str):
		self.log_to_file(f"[ERROR]:    {text}\n")

	def warning(self, text : str):
		self.log_to_file(f"[WARNING]:    {text}\n")

	def info(self, text : str):
		self.log_to_file(f"[INFO]:    {text}\n")


	def log_to_file(self, text : str = ""):
		self.check_log_dir()
		if not os.path.exists("log/log.txt"):
			with open("log/log.txt", 'w') as log_file:
				log_text = f"|{self.get_date()}|{text}"
				log_file.write(log_text)
		else:
			with open("log/log.txt", 'a') as log_file:
				log_text = f"|{self.get_date()}|{text}"
				log_file.write(log_text)


	def check_log_dir(self):
		if not os.path.exists("log"):
			os.makedirs('log')

	def get_date(self):
		now = datetime.now()
		date_str = now.strftime("%d-%m-%Y-%H%M%S")
		date_str = date_str.replace('-', '_')
		return date_str


logger = Logger()
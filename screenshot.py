import pyautogui
from datetime import datetime
from logger import logger


class Screenshot:

	def get_img_name(self):
		now = datetime.now()
		date_str = now.strftime("%d-%m-%Y-%H%M%S")
		date_str = date_str.replace('-', '_')

		img_name = "screenshot_" + date_str + ".png"
		logger.info(f"get image name: {img_name}")
		return img_name

	def save_img(self, save_path : str):
		logger.info("save image")

		try:
			img = pyautogui.screenshot()
			img_name = self.get_img_name()
			img.save(save_path + "/" + img_name)

			logger.info(f"Successfully saved to: {save_path}")

			return img_name

		except Exception as e:
			logger.error(e)
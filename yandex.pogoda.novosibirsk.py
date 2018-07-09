import sys
import requests
import bs4
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon

class Data:
	def __init__(self):
		self.temp = []
		self.cond = []
		self.get_data()
		
	def get_data(self):
		a = requests.get('https://yandex.ru/pogoda/novosibirsk/details')
		b = bs4.BeautifulSoup(a.text, 'html.parser')
		b1 = b.select('div.weather-table__temp')
		b2 = b.select('td.weather-table__body-cell.weather-table__body-cell_type_condition')
		for i in range(12):
			self.temp.append(b1[i].getText())
			self.cond.append(b2[i].getText())

class Example(QWidget):
	def __init__(self, data):
		super().__init__()
		self.data = data
		self.initUI()

	def initUI(self):
		times = ["Утро: ", "День: ", "Вечер: ", "Ночь: "]
		text1 = QLabel('Погода сегодня', self)
		text1.move(10, 10)
		for i in range(12):
			tod1  = QLabel(times[i%4]+data.temp[i]+'    '+data.cond[i], self)
			tod1.move(10+170*(i//4), 60+50*(i%4))
		self.setGeometry(300, 300, 650, 300)
		self.move(300, 300)
		self.setWindowTitle('Погода.Новосибирск')
		self.setWindowIcon(QIcon('sun.png'))
		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	data = Data()
	w1 = Example(data)
	sys.exit(app.exec_())

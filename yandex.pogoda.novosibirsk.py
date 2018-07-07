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
		text1 = QLabel('Погода сегодня', self)
		text1.move(10, 10)
		tod1  = QLabel("Утро: "+data.temp[0]+'    '+data.cond[0], self)
		tod1.move(10, 60)
		tod2  = QLabel("День: "+data.temp[1] + '    ' + data.cond[1], self)
		tod2.move(15, 110)
		tod3  = QLabel("Вечер: "+data.temp[2] + '    ' + data.cond[2], self)
		tod3.move(15, 160)
		tod4  = QLabel("Ночь: "+data.temp[3] + '    ' + data.cond[3], self)
		tod4.move(15, 210)
		text2 = QLabel('Погода завтра', self)
		text2.move(220, 10)
		tom1  = QLabel("Утро: "+data.temp[4] + '    ' + data.cond[4], self)
		tom1.move(220, 60)
		tom2  = QLabel("День: "+data.temp[5] + '    ' + data.cond[5], self)
		tom2.move(220, 110)
		tom3  = QLabel("Вечер: "+data.temp[6] + '    ' + data.cond[6], self)
		tom3.move(220, 160)
		tom4  = QLabel("Ночь: "+data.temp[7] + '    ' + data.cond[7], self)
		tom4.move(220, 210)
		text3 = QLabel('Погода послезавтра', self)
		text3.move(440, 10)
		at1  = QLabel("Утро: "+data.temp[8] + '    ' + data.cond[8], self)
		at1.move(440, 60)
		at2  = QLabel("День: "+data.temp[9] + '    ' + data.cond[9], self)
		at2.move(440, 110)
		at3  = QLabel("Вечер: "+data.temp[10] + '    ' + data.cond[10], self)
		at3.move(440, 160)
		at4  = QLabel("Ночь: "+data.temp[11] + '    ' + data.cond[11], self)
		at4.move(440, 210)
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

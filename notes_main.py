from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel, QButtonGroup, QListWidget,
        QTextEdit, QInputDialog, QMessageBox)
import json


notes = {}
'''
with open('info.json', 'w', encoding= 'utf-8') as file:
            json.dump(notes, file, sort_keys = True, ensure_ascii = False)'''

app = QApplication([])

window = QWidget()
window.setWindowTitle('Умные заметки')
window.resize(900,600)
line_g = QHBoxLayout()
line_1 = QVBoxLayout()
line_2 = QVBoxLayout()
list_name = QLabel('Список заметок')
list_main = QListWidget()
text_in_list = QTextEdit()
button_create = QPushButton('Добавить заметку')
button_delete = QPushButton('Удалить заметку')
button_save = QPushButton('Сохранить заметку')
line_2.addWidget(list_name)
line_2.addWidget(list_main)
line_1.addWidget(text_in_list)
line_2.addWidget(button_create)
line_2.addWidget(button_save)
line_2.addWidget(button_delete)
line_g.addLayout(line_1)
line_g.addLayout(line_2)
window.setLayout(line_g)

def show_note():
        name = list_main.selectedItems()[0].text()
        text_in_list.setText(notes[name])

list_main.itemClicked.connect(show_note)


def add_note():
    note_name, res = QInputDialog.getText(
        window, 'Добавить заметку', 'Название заметки:'
    )
    if note_name != '':
        notes[note_name] = ''
        list_main.addItem(note_name)    
button_create.clicked.connect(add_note)

def save_note():
    if list_main.selectedItems():
        key = list_main.selectedItems()[0].text()
        notes[key] = text_in_list.toPlainText()
        with open('info.json', 'w', encoding= 'utf-8') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
    else:    
        message = QMessageBox()
        message.setText('Заметка для сохранения не выбрана!')
        message.exec()

def del_note():
    if list_main.selectedItems():
        key = list_main.selectedItems()[0].text()
        del notes[key] 
        list_main.clear()
        text_in_list.clear()
        list_main.addItems(notes)
        with open('info.json', 'w', encoding= 'utf-8') as file:
            json.dump(notes, file, sort_keys = True, ensure_ascii = False)
    else:
        message = QMessageBox()
        message.setText('Заметка для удаления не выбрана!')
        message.exec()

button_save.clicked.connect(save_note)
button_delete.clicked.connect(del_note)

window.show()

with open('info.json', 'r', encoding= 'utf-8') as file:
    notes = json.load(file)
list_main.addItems(notes)
























app.exec()
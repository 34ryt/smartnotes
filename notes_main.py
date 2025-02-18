#начни тут создавать приложение с умными заметками
# импорт
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QButtonGroup, QMessageBox, QPushButton, QRadioButton, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox, QTextEdit, QListWidget, QLineEdit, QInputDialog
import json
# создание словаря
'''
notes = {
    'Privacy Policy':
    {
        'text' : 'Welcome to SmartNotes++! Here you can create, delete or save some notes with tags!',
        'tags' : ['welcome', 'tutorial', 'smartnotesplusplus']
    }
}
with open('notes_data.json', 'w', encoding = 'utf-8') as file:
    json.dump(notes, file, sort_keys = True)
'''
# генератор
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('SmartNotes++')
main_win.resize(900, 600)
# интерфейс
text_editor = QTextEdit()
notes_list_l = QLabel('Notes List')
notes_list = QListWidget()
button_create = QPushButton('Create Note')
button_delete = QPushButton('Delete Note')
button_save = QPushButton('Save Note')
tags_list_l = QLabel('Tags List')
tags_list = QListWidget()
tag_editor = QLineEdit()
tag_editor.setPlaceholderText('Please, input tag...')
button_tag_add = QPushButton('Add Tag')
button_tag_del = QPushButton('Delete Tag')
button_notes_search = QPushButton('Search Notes')
# отступы
main_Layout = QHBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutV1 = QVBoxLayout()
layoutV2 = QVBoxLayout()
# равновесие виджетов
layoutH1.addWidget(button_create)
layoutH1.addWidget(button_delete)
layoutH2.addWidget(button_tag_add)
layoutH2.addWidget(button_tag_del)
layoutV1.addWidget(text_editor)
layoutV2.addWidget(notes_list_l, alignment = Qt.AlignLeft)
layoutV2.addWidget(notes_list)
layoutV2.addLayout(layoutH1)
layoutV2.addWidget(button_save)
layoutV2.addWidget(tags_list_l, alignment = Qt.AlignLeft)
layoutV2.addWidget(tags_list)
layoutV2.addWidget(tag_editor)
layoutV2.addLayout(layoutH2)
layoutV2.addWidget(button_notes_search)
# равновесие виджетов со стретчами
main_Layout.addLayout(layoutV1, stretch = 2)
main_Layout.addLayout(layoutV2, stretch = 1) 
# установить главный отступ
main_win.setLayout(main_Layout)
# импорт словаря
def show_note():
    title = notes_list.selectedItems()[0].text()
    text_editor.setText(notes[title]['text'])
    tags_list.clear()
    tags_list.addItems(notes[title]['tags'])
notes_list.itemClicked.connect(show_note)
with open('notes_data.json', 'r', encoding = 'utf-8') as file:
    notes = json.load(file)
notes_list.addItems(notes)
# функции-манипуляторы
def add_note():
    note, result = QInputDialog.getText(main_win, 'Create note', 'Title?')
    if note != '' and result == True:
        notes[note] = {'text' : '', 'tags' : []}
        notes_list.addItem(note)
button_create.clicked.connect(add_note)
def del_note():
    if notes_list.selectedItems():
        title = notes_list.selectedItems()[0].text()
        del notes[title]
        with open('notes_data.json', 'w', encoding = 'utf-8') as file:
            json.dump(notes, file, sort_keys = True)
        text_editor.clear()
        tags_list.clear()
        notes_list.clear()
        notes_list.addItems(notes)
button_delete.clicked.connect(del_note)
def save_note():
    if notes_list.selectedItems():
        title = notes_list.selectedItems()[0].text()
        text = text_editor.toPlainText()
        notes[title]['text'] = text
        with open('notes_data.json', 'w', encoding = 'utf-8') as file:
            json.dump(notes, file, sort_keys = True)
button_save.clicked.connect(save_note)
def add_tag():
    if notes_list.selectedItems():
        tag = tag_editor.text()
        title = notes_list.selectedItems()[0].text()
        if not(tag in notes[title]['tags']):
            notes[title]['tags'].append(tag)
            tags_list.addItem(tag)
            tag_editor.clear()
            with open('notes_data.json', 'w', encoding = 'utf-8') as file:
                json.dump(notes, file, sort_keys = True)
button_tag_add.clicked.connect(add_tag)
def del_tag():
    if notes_list.selectedItems():
        title = notes_list.selectedItems()[0].text()
        tag = tags_list.selectedItems()[0].text()
        notes[title]['tags'].remove(tag)
        tags_list.clear()
        tags_list.addItems(notes[title]['tags'])
        with open('notes_data.json', 'w', encoding = 'utf-8') as file:
                json.dump(notes, file, sort_keys = True)
button_tag_del.clicked.connect(del_tag)
def search_tag():
    tag = tag_editor.text()
    if button_notes_search.text() == 'Search Notes' and tag:
        notes_filtered = {}
        for note in notes:
            if tag in notes[note]['tags']:
                notes_filtered[note]=notes[note]
        button_notes_search.setText('Reset Search')
        notes_list.clear()
        tags_list.clear()
        notes_list.addItems(notes_filtered)
    elif button_notes_search.text() == 'Reset Search':
        tag_editor.clear()
        notes_list.clear()
        tags_list.clear()
        notes_list.addItems(notes)
        button_notes_search.setText('Search Notes')
    else:
        pass
button_notes_search.clicked.connect(search_tag)
# запуск
main_win.show()
app.exec_()
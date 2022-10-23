from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import json

notes = {
    'Добро пожаловать!':

    {'Текст': 'кто ты',
    'Теги':  ['зачем зашёл'],
    }
}

def search_tag():
    tag = lg.text()
    if ta3.text() == 'Искать заметки по тегу' and tag:
        notes_filtered = {}
        for note in notes:
            if tag in notes[note]['Теги']:
                notes_filtered[note]=notes[note]
        ta3.setText('Сбросить поиск')
        l.clear()
        l_t.clear()
        l.addItems(notes_filtered)
    elif ta3.text() == 'Сбросить поиск':
        lg.clear()
        l.clear()
        l_t.clear()
        l.addItems(notes)
        ta3.setText('Искать заметки по тегу')
    else:
        pass


def add_tag():
    if l.selectedItems():
        key = l.selectedItems()[0].text()
        tag = lg.text()
        if not tag in notes[key]['Теги']:
            notes[key]['Теги'].append(tag)
            l_t.addItem(tag)
            t_e.clear()
        with open('a.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print('Заметка для добавления тега не выбрана!')

def save_note():
    key = list_notes.selectedItems()[0].text()
    i = 0
    for note in notes:
        if note[0] == key:
            note[1] = field_text.toPlainText()
            filename = str(i)+'.txt'
            with open (filename, 'w') as file:
                file.write(note[0]+'\n')
                file.write(note[1]+'\n')
                for tag in note[2]:
                    file.write(tag+'')
                file.write('\n')
        i += 1

def del_note():
    if l.selectedItems():
        key = l.selectedItems()[0].text()
        del notes[key]
        l.clear()
        l_t.clear()
        t_e.clear()
        l.addItems(notes)
        with open('a.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print('Заметка для удаления не выбрана')

def show_note():
    name = l.selectedItems()[0].text()
    t_e.setText(notes[name]['Текст'])
    l_t.clear()
    l_t.addItems(notes[name]['Теги'])

def add_note():
    note_name, ok = QInputDialog.getText(notes_win, 'Добавить заметку', 'Название заметки: ')
    if ok and note_name != '':
        note = list()
        note = [note_name, '', []]
        notes.append(note)
        list_notes.addItem(note[0])
        filename = str(len(notes)-1)+'.txt'
        with open (filename, 'w') as file:
            file.write(note[0]+ '\n')

a = QApplication([])
w = QWidget()

w.setWindowTitle('Умные заметки')
m_layout = QHBoxLayout()
r_layout = QVBoxLayout()
l_layout = QVBoxLayout()

t = QLabel('Список заметок')
r_layout.addWidget(t)

t_e = QTextEdit(t)
l_layout.addWidget(t_e)

l = QListWidget()
r_layout.addWidget(l)

b1 = QPushButton('Создать заметку')
r_layout.addWidget(b1)

b2 = QPushButton('Удалить заметку')
r_layout.addWidget(b2)

b3 = QPushButton('Сохранить заметку')
r_layout.addWidget(b3)

t2 = QLabel('Список тегов')
r_layout.addWidget(t)

l_t = QListWidget()
r_layout.addWidget(l_t)

lg = QLineEdit()
r_layout.addWidget(lg)

ta1 = QPushButton('Добавить к заметке')
r_layout.addWidget(ta1)

ta2 = QPushButton('Открепить от заметки')
r_layout.addWidget(ta2)

ta3 = QPushButton('Искать заметки по тегу')
r_layout.addWidget(ta3)

w.setLayout(m_layout)
m_layout.addLayout(l_layout)
m_layout.addLayout(r_layout)

with open('a.json', 'w') as file:
    json.dump(notes, file)

with open('a.json', 'r') as file:
    notes = json.load(file)

l.addItems(notes)





























































































l.itemClicked.connect(show_note)
ta1.clicked.connect(add_tag)
b1.clicked.connect(add_note)
b2.clicked.connect(del_note)
b3.clicked.connect(save_note)
ta3.clicked.connect(search_tag)

w.show()
a.exec_()

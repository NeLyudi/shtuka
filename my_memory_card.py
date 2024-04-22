from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox, QRadioButton, QButtonGroup

app=QApplication([])
mw = QWidget()
mw.resize(400,250)
main_line = QVBoxLayout()
button = QPushButton('Ответить')
main_text = QLabel('Какой национальности не существует?')
mw.cur = -1
mw.procent = 0
mw.que = 0

line = QHBoxLayout()
line2 = QVBoxLayout()
line3 = QVBoxLayout()
box = QGroupBox()
ans1 = QRadioButton('Энцы')
ans2 = QRadioButton('Смурфы')
ans3 = QRadioButton('Чулымцы')
ans4 = QRadioButton('Алеуты')

box.setLayout(line)
line.addLayout(line2)
line.addLayout(line3)
line2.addWidget(ans1, alignment = Qt.AlignCenter)
line2.addWidget(ans2, alignment = Qt.AlignCenter)
line3.addWidget(ans3, alignment = Qt.AlignCenter)
line3.addWidget(ans4, alignment = Qt.AlignCenter)

main_line.addWidget(main_text, alignment = Qt.AlignCenter)
main_line.addWidget(box)


result = QGroupBox()
text_result1 = QLabel('d')
text_result2 = QLabel('Энцы')
result_line = QVBoxLayout()
result_line.addWidget(text_result1, alignment = (Qt.AlignLeft | Qt.AlignTop))
result_line.addWidget(text_result2, alignment = Qt.AlignCenter, stretch = 2)
result.setLayout(result_line)
main_line.addWidget(result)

main_line.addWidget(button, alignment = Qt.AlignCenter)

box.show()
result.hide()

group = QButtonGroup()
group.addButton(ans1)
group.addButton(ans2)
group.addButton(ans3)
group.addButton(ans4)

def show_result():
    box.hide()
    result.show()
    button.setText('Следующий вопрос')

def show_question():
    result.hide()
    box.show()
    button.setText('Ответить')
    group.setExclusive(False)
    ans1.setChecked(False)
    ans2.setChecked(False)
    ans3.setChecked(False)
    ans4.setChecked(False)
    group.setExclusive(True)

from random import shuffle

answer = [ans1, ans2, ans3, ans4]

class Question():
    def __init__(self, quest, right, wrong1, wrong2, wrong3):
        self.quest=quest
        self.right=right
        self.wrong1=wrong1
        self.wrong2=wrong2
        self.wrong3=wrong3

def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    main_text.setText(q.quest)
    text_result2.setText(q.right)
    show_question()
def correct(res):
    text_result1.setText(res)
    show_result()
def check_answer():
    if answer[0].isChecked():
        correct('Правильно!')
        mw.procent +=10
        mw.que +=1
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            correct('Неверно!')
    print(mw.procent,'% верно')
    print('Отвеченно на', mw.que, 'из 10')

def next_q():
    mw.cur = mw.cur + 1
    if mw.cur >= len(card):
        mw.cur = 0
        mw.procent = 0
        mw.que = 0
    q = card[mw.cur]
    ask(q)

def click_OK():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_q()

card = []
card.append(Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'))
card.append(Question('Как переводится слово "Карма" с санскрита ?', 'действие', 'возмездие', 'следствие', 'бездействие'))
card.append(Question('Как назывался особый головной убор, который носили фараоны в Древнем Египте?','Немес','Картуз','Корона','Убрус'))
card.append(Question('У какого животного самые большие глаза относительно тела?','У долгопята','У лемура','У летучей мыши','У тупайи'))
card.append(Question('Детинцем на Руси называли...','Кремль','Школу','Княжеский терем','Монастырь'))
card.append(Question('Как называли строителя в старину?','Зодчий','Бондарь','Бортник','Кормчий'))
card.append(Question('Продолжите пословицу: «Знает кошка…»','«Чье мясо съела»','«Да мыши не знают»','«Почем фунт лиха»','«Где собака зарыта»'))
card.append(Question('Какое из этих растений — плотоядное?','Росянка','Володушка','Мытник','Астрагал'))
card.append(Question('Как называется человек, покоряющий крыши многоэтажных домов?','Руфер','Диггер','Сталкер','Байкер'))

next_q
mw.setLayout(main_line)

button.clicked.connect(click_OK)


mw.show()
app.exec_()
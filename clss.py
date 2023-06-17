# НЕ СОВЕТУЮ РЕДАКТИРОВАТЬ, ЕСЛИ НЕ ЗНАЕТЕ, ЧТО ДЕЛАЕТЕ! РЕДАКТИРУЙТЕ НА СВОЙ СТРАХ И РИСК!
class Locations:
    # Класс локаций, Содержит 17 параметров!

    def __init__(self, id, name, desc1, desc2, desc3, desc4, desc5, desc6, desc7, desc8, desc9, desc10, desc11, desc12, answer1, answer2, answer3) -> None:
        self.id = id # id локации
        self.name = name # Название локации
        self.desc1 = desc1 # 1 Описание локации
        self.desc2 = desc2 # 2 Описание локации
        self.desc3 = desc3 # 3 Описание локации
        self.desc4 = desc4 # 4 Описание локации
        self.desc5 = desc5 # 5 Описание локации
        self.desc6 = desc6 # 6 Описание локации
        self.desc7 = desc7 # 7 Описание локации
        self.desc8 = desc8 # 8 Описание локации
        self.desc9 = desc9 # 9 Описание локации
        self.desc10 = desc10 # 10 Описание локации
        self.desc11 = desc11 # 11 Описание локации
        self.desc12 = desc12 # 12 Описание локации
        self.answer1 = answer1 # id ответа 1
        self.answer2 = answer2 # id ответа 2
        self.answer3 = answer3 # id ответа 3
        return

class Answers:
    # Класс ответов, Содержит 3 параметра!

    def __init__(self, id, text, location_id):
        self.id = id # id ответа
        self.text = text # Текст ответа
        self.location_id = location_id # id локации, на которую попадет игрок при выборе этого ответа
        return

locations = []
location = {}

answers = []
answer = {}
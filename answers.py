import pgzrun
from cfg import *
from clss import *


''' 
answers.append(Answers("id этой кнопки", "текст этой кнопки", "id локации на которую перенесет игрока"))

answers.append(Answers("", "", ""))
'''


# Для конца
answers.append(Answers("end", "Конец", "break"))
answers.append(Answers("replay", "Заново", "start"))



# start
answers.append(Answers("a.start.door.locked", "Открыть дверь", "l.start.door.locked"))
answers.append(Answers("a.start.closet", "Заглянуть в шкаф", "l.start.closet.open"))
answers.append(Answers("a.start.button", "Нажать на кнопку", "l.start.button.press"))

# l.start.button.press
answers.append(Answers("a.start.button.press.none", "", "l.start.button.press"))

# l.start.closet.open
answers.append(Answers("a.start.door.open", "Открыть дверь", "l.room2"))
answers.append(Answers("a.start.closet.open.none", "", "l.start.closet.open"))



# l.room2
answers.append(Answers("a.room2.b1", "Кнопка 1", "l.room2.b1"))
answers.append(Answers("a.room2.b2", "Кнопка 2", "l.room2.b2"))
answers.append(Answers("a.room2.b3", "Кнопка 3", "l.room2.b3"))

# l.room2.b1
answers.append(Answers("a.room2.b1.none", "", "l.room2.b1"))

# l.room2.b3
answers.append(Answers("a.room2.b3.door1", "В 1 дверь", "l.room2.b3.door1"))
answers.append(Answers("a.room2.b3.door2", "Во 2 дверь", "l.corridor"))
answers.append(Answers("a.room2.b3.stand", "Остаться", "l.room2.b3.stand"))

# l.room2.b3.stand
answers.append(Answers("a.room2.b3.stand.none", "", "l.room2.b3.stand"))

# l.room2.b3.door1
answers.append(Answers("a.room2.b3.door1.none", "", "l.room2.b3.door1"))


# l.corridor
answers.append(Answers("a.corridor.torch", "Взять факел", "l.corridor.torch"))
answers.append(Answers("a.corridor.go", "Пойти дальше", "l.corridor.exit"))
answers.append(Answers("a.corridor.none", "", "l.corridor"))

# l.corridor.torch
answers.append(Answers("a.corridor.torch.none", "", "l.corridor.torch"))

# l.corridor.exit
answers.append(Answers("a.corridor.exit.run", "Побежать", "l.corridor.exit.run"))
answers.append(Answers("a.corridor.exit.walk", "Идти шагом", "l.forest"))
answers.append(Answers("a.corridor.exit.slow", "Пойти медленнее", "l.corridor.exit.slow"))

# l.corridor.exit.slow
answers.append(Answers("a.corridor.exit.slow.none", "", "l.corridor.exit.slow"))

# l.corridor.exit.run
answers.append(Answers("a.corridor.exit.run.none", "", "l.corridor.exit.run"))

# l.forest
answers.append(Answers("a.forest", "Конец?", "break"))
answers.append(Answers("a.forest.none", "", "l.forest"))
answers.append(Answers("a.forest.none", "", "l.forest"))

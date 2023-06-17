# Настройки ----------------------------------------
TITLE = 'Demo Game' # Название окна программы
WIDTH = 1200 # Ширина экрана
HEIGHT = 800 # Высота экрана

l_id = "start" # id локации в которой находится игрок (выбранное значение - начальная локация)

location_block_color = "black" # Цвет блока локации
bg_collor = "#565656" # Цвет заднего фона
frame_color = "white" # Цвет обводки окон

button_color = "black" # Основной цвет кнопки
button_select_color = "#292929" # Цвет кнопки при наведении
button_press_color = "#1f1f1f" # Цвет кнопки при нажатии

name_text_color = "white" # Цвет названия локации
desc_text_color = "white" # Цвет описания локации
button_text_color = "white" # Цвет текста кнопок

bg_name = None # Цвет фона текста названия локации
bg_desc = None # Цвет фона текста описания локации
bg_button = None # Цвет фона текста кнопок

name_size = 33 # Размер шрифта названия локации
desc_size = 28 # Размер шрифта описания
button_text_size = 28 # Размер шрифта кнопок

font_name = None # Шрифт названия локации (None - стандартный)
font_desc = None # Шрифт описания локации (None - стандартный)
font_button = None # Шрифт текста кнопок выбора (None - стандартный)

antialias_name = True # Шрифт названия локации - сглаженый
antialias_desc = True # Шрифт описания локации - сглаженый
antialias_button = True # Шрифт текста кнопок - сглаженый

italic_name = False # Шрифт названия локации - курсив
italic_desc = False # Шрифт описания локации - курсив
italic_button = False # Шрифт текста кнопок - курсив

bold_name = False # Шрифт названия локации - жирный
bold_desc = False # Шрифт описания локации - жирный
bold_button = True # Шрифт текста кнопок - жирный

underline_name = False # Шрифт названия локации - подчеркнутый
underline_desc = False # Шрифт описания локации - подчеркнутый
underline_button = False # Шрифт текста кнопок - подчеркнутый

time_to_animation = 0.0005 # Время в секундах, которое должно пройти что бы пошла анимация вывода текста локации на экран
text_animation_speed = 13 # Скорость вывода текста локации на экран (0 что бы отключить анимацию)
name_animation = True # Включить анимацию для названия локации (False - только описание)



# Прочие настройки ----------------------------------------
button1_color = button_color # Цвет 1 кнопки
button2_color = button_color # Цвет 2 кнопки
button3_color = button_color # Цвет 3 кнопки

debug = False # Режим отладки (Показывает id локации и ответов)
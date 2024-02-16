# НЕ СОВЕТУЮ РЕДАКТИРОВАТЬ, ЕСЛИ НЕ ЗНАЕТЕ, ЧТО ДЕЛАЕТЕ! РЕДАКТИРУЙТЕ НА СВОЙ СТРАХ И РИСК!
# DO NOT EDIT UNLESS YOU KNOW WHAT YOU ARE DOING! EDIT AT YOUR OWN RISK!
import pgzrun
import sys
from cfg import *
from scene import *



# Переменные для работы программы (Не советую трогать!) ----------------------------------------
button1_pressed = False
button2_pressed = False
button3_pressed = False
button1_unpressed = False
button2_unpressed = False
button3_unpressed = False

mouse_pos = (0, 0)
mouse_x = 0
mouse_y = 0

def text_animation():
    global desc_blocking_coord, desc_blocking_wh
    if text_animation_speed != 0:
        if name_animation == True:
            desc_blocking_coord = [69, 52]
        else:
            desc_blocking_coord = [69, 85]
        desc_blocking_wh = [WIDTH-140, HEIGHT-360]
    else:
        desc_blocking_coord = [0, 0]
        desc_blocking_wh = [0, 0]
text_animation()

time = 0

# Загрузка частей интерфейса -------------------------------------------------------------------------
bg = Rect((0, 0), (WIDTH, HEIGHT))
location_block = Rect((63, 45), (WIDTH-127, 485))
answer_button1 = Rect((location_block.x, location_block.y + 510), (WIDTH-127, 51))
answer_button2 = Rect((location_block.x, answer_button1.y + 76), (WIDTH-127, 51))
answer_button3 = Rect((location_block.x, answer_button2.y + 76), (WIDTH-127, 51))


# Отрисовка текста взависимости от локации -------------------------------------------------------
def locate_draw():
    global locate_name, locate_desc1, locate_desc2, locate_desc3, locate_desc4, locate_desc5, locate_desc6, locate_desc7, locate_desc8, locate_desc9, locate_desc10, locate_desc11, locate_desc12, answ1, answ2, answ3
    global locate_id, answer1_id, answer2_id, answer3_id

    locate_name = screen.draw.text(location.get(l_id).name,
                 midleft=(80, 70),     
                 color=name_text_color,
                 fontname = font_name,
                 background = bg_name,
                 italic = italic_name,
                 underline = underline_name,
                 bold = bold_name,
                 antialias = antialias_name,
                 fontsize = name_size)
    locate_desc1 = screen.draw.text(location.get(l_id).desc1, 
                 midleft=(80, 110),     
                 color=desc_text_color,
                 fontname = font_desc,
                 background = bg_desc,
                 italic = italic_desc,
                 underline = underline_desc,
                 bold = bold_desc,
                 antialias = antialias_desc,
                 fontsize = desc_size)
    locate_desc2 = screen.draw.text(location.get(l_id).desc2, 
                 midleft=(80, 145),     
                 color=desc_text_color,
                 fontname = font_desc,
                 background = bg_desc,
                 italic = italic_desc,
                 underline = underline_desc,
                 bold = bold_desc,
                 antialias = antialias_desc,
                 fontsize = desc_size)
    locate_desc3 = screen.draw.text(location.get(l_id).desc3, 
                 midleft=(80, 180),     
                 color=desc_text_color,
                 fontname = font_desc,
                 background = bg_desc,
                 italic = italic_desc,
                 underline = underline_desc,
                 bold = bold_desc,
                 antialias = antialias_desc,
                 fontsize = desc_size)
    locate_desc4 = screen.draw.text(location.get(l_id).desc4, 
                 midleft=(80, 215),     
                 color=desc_text_color,
                 fontname = font_desc,
                 background = bg_desc,
                 italic = italic_desc,
                 underline = underline_desc,
                 bold = bold_desc,
                 antialias = antialias_desc,
                 fontsize = desc_size)
    locate_desc5 = screen.draw.text(location.get(l_id).desc5, 
                 midleft=(80, 250),     
                 color=desc_text_color,
                 fontname = font_desc,
                 background = bg_desc,
                 italic = italic_desc,
                 underline = underline_desc,
                 bold = bold_desc,
                 antialias = antialias_desc,
                 fontsize = desc_size)
    locate_desc6 = screen.draw.text(location.get(l_id).desc6, 
                 midleft=(80, 285),     
                 color=desc_text_color,
                 fontname = font_desc,
                 background = bg_desc,
                 italic = italic_desc,
                 underline = underline_desc,
                 bold = bold_desc,
                 antialias = antialias_desc,
                 fontsize = desc_size)
    locate_desc7 = screen.draw.text(location.get(l_id).desc7, 
                 midleft=(80, 320),     
                 color=desc_text_color,
                 fontname = font_desc,
                 background = bg_desc,
                 italic = italic_desc,
                 underline = underline_desc,
                 bold = bold_desc,
                 antialias = antialias_desc,
                 fontsize = desc_size)
    locate_desc8 = screen.draw.text(location.get(l_id).desc8, 
                 midleft=(80, 355),     
                 color=desc_text_color,
                 fontname = font_desc,
                 background = bg_desc,
                 italic = italic_desc,
                 underline = underline_desc,
                 bold = bold_desc,
                 antialias = antialias_desc,
                 fontsize = desc_size)
    locate_desc9 = screen.draw.text(location.get(l_id).desc9, 
                 midleft=(80, 390),     
                 color=desc_text_color,
                 fontname = font_desc,
                 background = bg_desc,
                 italic = italic_desc,
                 underline = underline_desc,
                 bold = bold_desc,
                 antialias = antialias_desc,
                 fontsize = desc_size)
    locate_desc10 = screen.draw.text(location.get(l_id).desc10, 
                 midleft=(80, 425),     
                 color=desc_text_color,
                 fontname = font_desc,
                 background = bg_desc,
                 italic = italic_desc,
                 underline = underline_desc,
                 bold = bold_desc,
                 antialias = antialias_desc,
                 fontsize = desc_size)
    locate_desc11 = screen.draw.text(location.get(l_id).desc11, 
                 midleft=(80, 460),     
                 color=desc_text_color,
                 fontname = font_desc,
                 background = bg_desc,
                 italic = italic_desc,
                 underline = underline_desc,
                 bold = bold_desc,
                 antialias = antialias_desc,
                 fontsize = desc_size)
    locate_desc12 = screen.draw.text(location.get(l_id).desc12, 
                 midleft=(80, 495),     
                 color=desc_text_color,
                 fontname = font_desc,
                 background = bg_desc,
                 italic = italic_desc,
                 underline = underline_desc,
                 bold = bold_desc,
                 antialias = antialias_desc,
                 fontsize = desc_size)
    
    answ1 = screen.draw.text(location.get(l_id).answer1.text, 
                 midleft=(80, 582),     
                 color=button_text_color,
                 fontname = font_button,
                 background = bg_button,
                 italic = italic_button,
                 underline = underline_button,
                 bold = bold_button,
                 antialias = antialias_button,
                 fontsize = button_text_size)
    answ2 = screen.draw.text(location.get(l_id).answer2.text, 
                 midleft=(80, 658),     
                 color=button_text_color,
                 fontname = font_button,
                 background = bg_button,
                 italic = italic_button,
                 underline = underline_button,
                 bold = bold_button,
                 antialias = antialias_button,
                 fontsize = button_text_size)
    answ3 = screen.draw.text(location.get(l_id).answer3.text, 
                 midleft=(80, 734),     
                 color=button_text_color,
                 fontname = font_button,
                 background = bg_button,
                 italic = italic_button,
                 underline = underline_button,
                 bold = bold_button,
                 antialias = antialias_button,
                 fontsize = button_text_size)

    return


# Отрисовка объектов на экране -----------------------------------------------
def draw():
    global WIDTH, HEIGHT

    screen.draw.filled_rect(bg, bg_collor)

    screen.draw.filled_rect(location_block, location_block_color)
    screen.draw.filled_rect(answer_button1, button1_color)
    screen.draw.filled_rect(answer_button2, button2_color)
    screen.draw.filled_rect(answer_button3, button3_color)

    screen.draw.rect(location_block, frame_color)
    screen.draw.rect(answer_button1, frame_color)
    screen.draw.rect(answer_button2, frame_color)
    screen.draw.rect(answer_button3, frame_color)

    locate_draw()

    desc_blocking = Rect(desc_blocking_coord, desc_blocking_wh)
    screen.draw.filled_rect(desc_blocking, location_block_color)

    if debug == True:
        locate_id = screen.draw.text(location.get(l_id).id,
                 midright=(WIDTH-89, 67),     
                 color="white",
                 fontsize = 25)
        answer1_id = screen.draw.text(f"{location.get(l_id).answer1.id} | {location.get(l_id).answer1.location_id}",
                 midright=(WIDTH-89, 582),     
                 color="white",
                 fontsize = 25)
        answer2_id = screen.draw.text(f"{location.get(l_id).answer2.id} | {location.get(l_id).answer2.location_id}",
                 midright=(WIDTH-89, 658),     
                 color="white",
                 fontsize = 25)
        answer3_id = screen.draw.text(f"{location.get(l_id).answer3.id} | {location.get(l_id).answer3.location_id}",
                 midright=(WIDTH-89, 734),     
                 color="white",
                 fontsize = 25)

# Програмный цикл ----------------------------------------------
def update(dt):
    global mouse_x, mouse_y, button1_color, button2_color, button3_color, button1_pressed, button2_pressed, button3_pressed, button1_unpressed, button2_unpressed, button3_unpressed, l_id, time, desc_blocking_coord, desc_blocking_wh
    
    if l_id == "break":
        sys.exit()
    
    if text_animation_speed != 0:
        time += dt
        if time >= time_to_animation:
            time = 0
            desc_blocking_coord[0] += text_animation_speed
            desc_blocking_wh[0] -= text_animation_speed

    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]
    
    if button1_pressed == True:
        button1_color = button_press_color
    elif ((mouse_x in range(63, WIDTH-64)) and (mouse_y in range(556, 607))) and button1_pressed == False:
        button1_color = button_select_color
    else:
        button1_color = button_color

    if button2_pressed == True:
        button2_color = button_press_color
    elif ((mouse_x in range(63, WIDTH-64)) and (mouse_y in range(632, 683))) and button2_pressed == False:
        button2_color = button_select_color
    else:
        button2_color = button_color

    if button3_pressed == True:
        button3_color = button_press_color
    elif ((mouse_x in range(63, WIDTH-64)) and (mouse_y in range(708, 759))) and button3_pressed == False:
        button3_color = button_select_color
    else:
        button3_color = button_color
    

    if button1_unpressed == True:
        button1_unpressed = False
        l_id = location.get(l_id).answer1.location_id
        text_animation()

    if button2_unpressed == True:
        button2_unpressed = False
        l_id = location.get(l_id).answer2.location_id
        text_animation()

    if button3_unpressed == True:
        button3_unpressed = False
        l_id = location.get(l_id).answer3.location_id
        text_animation()
    



# При нажатии на мышь -------------------------------------------
def on_mouse_down(button, pos):
    global button1_color, button2_color, button3_color, button1_pressed, button2_pressed, button3_pressed
    
    if button == mouse.LEFT:

        if (mouse_x in range(63, WIDTH-64)) and (mouse_y in range(556, 607)):
            button1_pressed = True

        if (mouse_x in range(63, WIDTH-64)) and (mouse_y in range(630, 683)):
            button2_pressed = True

        if (mouse_x in range(63, WIDTH-64)) and (mouse_y in range(708, 759)):
            button3_pressed = True


# При отжатии кнопки мыши -------------------------------------------
def on_mouse_up(button, pos):
    global button1_color, button2_color, button3_color, button1_pressed, button2_pressed, button3_pressed, button1_unpressed, button2_unpressed, button3_unpressed

    if button == mouse.LEFT:

        if button1_pressed == True:
            button1_pressed = False
            if (mouse_x in range(63, WIDTH-64)) and (mouse_y in range(556, 607)):
                button1_unpressed = True

        if button2_pressed == True:
            button2_pressed = False
            if (mouse_x in range(63, WIDTH-64)) and (mouse_y in range(630, 683)):
                button2_unpressed = True

        if button3_pressed == True:
            button3_pressed = False
            if (mouse_x in range(63, WIDTH-64)) and (mouse_y in range(708, 759)):
                button3_unpressed = True


# При передвижении мыши -------------------------------------------
def on_mouse_move(pos):
    global mouse_pos
    mouse_pos = pos


# При нажатии на клавишу -------------------------------------------
def on_key_down(key):
    pass


# При отжатии клавиши -------------------------------------------
def on_key_up(key):
    pass


# Запуск цикла программы
pgzrun.go()

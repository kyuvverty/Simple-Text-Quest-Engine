---------------------------------------------------------------------------------------------------------------------------------------------------
------- ENG ---------------------------------------------------------------------------------------------------------------------------------------

This program is a simple engine for creating text quests.
This version is outdated and will not be supported!

There are 6 main files here:

    main.py
    the main file to run.

    clss.py
    a file containing information about the classes of the program.
    There are only 2 classes in the program - Answers and Locations.
    There are 3 parameters in the Answers class, these are the answer id, the answer text and the location id, to which you will be sent when you click on the answer.
    There are 17 parameters in the Locations class, these are location id, location name, 12 descriptions and 3 response ids.

    cfg.py
    A file that stores settings that you can change for yourself.

    answers.py
    A file with your code that stores information about responses.

    locations.py
    File with your code storing location information.

    scene.py
    File that handles answers.py and locatons.py files

The program workflow is as follows:
    Run "main.py"
    1: "answers.py" and "locations.py" process the files "cfg.py" and "clss.py" and are executed
    2: The file "scene.py" processes "answers.py" first, then "locations.py".
    3: The file "main.py" executes "scene.py" and then executes itself.
    4: The program starts and runs.

Program written with PyGame Zero.

Then I will add here other information about working with the engine.
I also plan to add the ability to create scripts that can work in the game.

---------------------------------------------------------------------------------------------------------------------------------------------------
------- RUS ---------------------------------------------------------------------------------------------------------------------------------------

Данная программа - простой движок для создания текстовых квестов.
Эта версия устарела и не будет поддерживаться!

Здесь 6 основных файлов:

    main.py
    основной файл, который и нужно запускать.

    clss.py
    файл, содержащий информацию о классах программы.
    В программе всего 2 класса - Answers и Locations.
    В классе Answers 3 параметра, это id ответа, текст ответа и id локации, в которую вас отправит при нажатии на ответ.
    В классе Locations 17 параметров, - это id локации, название локации, 12 описаний и 3 id ответов.

    cfg.py
    Файл хранящий настройки, которые можно изменить под себя.

    answers.py
    Файл с вашим кодом, хранящий информацию о ответах.

    locatons.py
    Файл с вашим кодом, хранящий информацию о локациях.

    scene.py
    Файл, который обрабатывает файлы answers.py и locatons.py

Порядок работы программы такой:
    Запуск "main.py"
    1: "answers.py" и "locations.py" обрабатывают файлы "cfg.py" и "clss.py" и исполняются
    2: Файл "scene.py" обрабатывает сначала "answers.py", потом "locations.py".
    3: Файл "main.py" исполняет "scene.py" и после исполняется и сам.
    4: Программа запускается и работает.

Программа написана с помощью PyGame Zero.

Потом добавлю сюда прочую информацию о работе с движком.
Так же планирую добавить возможность создавать скрипты, которые смогут работать в игре.

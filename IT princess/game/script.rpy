﻿# Инициализация персонажей
define teacher = Character('Учитель', color = '#FF0000')
define Henry = Character('Генри', color = '#1F618D')
define Maks = Character('Макс', color = '#797D7F')
define Izabella = Character('Изабелла')
define dragon = Character('Спайнкндс', color = '#2471A3')
define troll = Character('Тролль')
define gnoms = Character('Гаети')
define mag = Character('Алистер')
define koldun = Character('Алистер')
define autor = Character('Автор')
define general = Character('Главнокомандующий')
define non = Character('???', color = '#E74C3C')

# Объявление переменных
$ has_dragon = False

# Растягивание персонажа
transform leap(z=1.05, t=.5):
    easeout t/2 yzoom z
    easein t/2 yzoom 1

# Подпрыгивание персонажа
transform jump_tr(dist=15, t=0.5):
    linear t/2 yoffset - dist
    linear t/2 yoffset 0
#1080*1920
#Вы указали: 500x1000 (c соблюдением пропорций)
#Получилось: 284x1000, 172.39 Кб

# Начало игры
label start:
    call scene1_school from _call_scene1_school # Диалог в школе (сцена 1)
    call scene2_class from _call_scene2_class # Сцена с учителем и засыпание Генри
    call scene3_sleep from _call_scene3_sleep # Генри летит спать
    call scene4_new_country from _call_scene4_new_country # Генри впервые в новом мире
    call scene5_forest from _call_scene5_forest # Встреча с дракончиком
    call scene6_wizard_forest # Разговор с дракончиком об оружии
    return

label scene1_school:
    scene scene1 with dissolve
    show henry at left with moveinbottom
    show maks at right with moveinbottom
    show maks at right, leap
    Maks 'Слушай, а чем бы ты хотел заниматься всю жизнь?'
    show henry at left, leap
    Henry 'Если честно, я еще не решил, чем хочу заниматься'
    show maks at right, leap
    Maks 'Я бы хотел связать свою жизнь с информационными технологиями'
    show henry at left, leap
    Henry 'А это интересно, но в этой сфере столько направлений и специальностей...'
    show maks at right, leap
    Maks 'Ладно, что-то мы заболтались, пошли на урок'
    return

label scene2_class:
    scene scene2 with dissolve
    show teacher at center with moveinbottom
    teacher '"Отец мой Андрей Петрович Гринёв в молодости своей..." - монотонно начал читать учитель'
    scene bg black with Fade(2,0,0)
    scene scene2_blur with Dissolve(1) # блюр 10
    scene bg black with Fade(2,0,0)
    scene scene2_blur with Dissolve(1)
    'Генри не выспавшись уже начал засыпать на задней парте'
    return

label scene3_sleep:
    scene scene3 with dissolve
    hide textbox
    show henry at right with moveinleft
    hide henry with easeinright
    Henry 'ААААААААААААААААА'
    return

label scene4_new_country:
    scene scene4 with dissolve
    show henry at center with moveinbottom
    Henry 'Куда я попал? Где я очутился?'
    Henry 'Что мне делать?'
    return

label scene5_forest:
    scene scene5 with dissolve
    show henry at center with moveinbottom
    show henry at center, leap
    Henry 'Хммммм...'
    Henry 'Что это за синий свет в лесу?'
    menu meet_dragon:
        Henry 'Что мне сделать?'
        'Пойти проверить':
            $ has_dragon = True
            show henry at left with easeinleft
            show dragon_in_chains at topright with moveinbottom
            Henry 'Это же дракон, он попал в ловушку, нужно ему помочь'
            show henry at center with easeinright
            'Генри бросается к дракону и распутывает цепи'
            show henry at left with easeinleft
            hide dragon_in_chains with easeinbottom
            show dragon at right with moveinbottom
            show henry at left, leap
            Henry 'Кто ты такой?'
            show dragon at right, leap
            non 'Спасибо за помощь. Меня зовут Спайндикс'
            dragon 'Я помогу тебе разобраться в этом мире'
        'Не обратить внимание':
            $ has_dragon = False
    return

label scene6_wizard_forest:
    scene scene6 with dissolve
    show henry at left with moveinbottom
    show dragon at right with moveinbottom
    show dragon at right, leap
    dragon 'Чтобы выжить в этой стране, необходимо найти оружие'
    show henry at left, leap
    Henry 'Ты знаешь, где его можно достать?'
    show dragon at right, leap
    dragon 'К счастью, здесь недалеко есть пещера, в которой может быть что-нибудь полезное'

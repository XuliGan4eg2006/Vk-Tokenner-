# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
import time
import vk
import requests
import random
import sys
from colorama import init
import colorama
from os import system, name
import os
init(autoreset=True)



class color:
    Red = '\033[91m'
    Green = '\033[1;32m'
    Yellow = '\033[93m'
    Blue = '\033[94m'
    Magenta = '\033[95m'
    Cyan = '\033[96m'
    White = '\033[97m'
    Grey = '\033[90m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


    
# define our clear function
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


#vars
color.Cyan

color.END
infinite = 3
token_passed = 0
menu = str(color.Green + '[' + color.Yellow + '1' + color.Green + '] Поиск пользователя по ID [' + color.Yellow + '2' + color.Green + '] Информация о текущем пользователе\n['+ color.Yellow + '3' + color.Green + '] Скачать диалоги [' + color.Yellow + '4' + color.Green + '] Скачать вложения из диалога\n[' + color.Yellow + '5' + color.Green + '] Оставить комментарий [' + color.Yellow + '6' + color.Green + '] Спам комментариями\n[' + color.Yellow + '7' + color.Green + '] Отправить сообщение [' + color.Yellow + '8' + color.Green + '] Поиск сообщения по фразе\n[' + color.Yellow + '0' + color.Green + '] Выход' + color.END)

while token_passed == 0:
    token = input('Введите токен: ')
    color.END
    session = vk.Session(access_token=token)
    api = vk.API(session ,v='5.92', lang='ru')
    try:
        api.users.get()
        token_passed = 1
    except vk.exceptions.VkAPIError:
        print(color.Green + 'Токен недействителен!' + color.END)
        token_passed = 0
        pass

token_dir = os.path.join(f"{token}")

if not os.path.exists(token_dir):
    os.mkdir(token_dir)
os.chdir(token_dir)

#Сделать коммент
def do_comment():
    clear()
    post_comment = input(color.Yellow + 'ID пользователя(прим: 11111111) >>> ' + color.Green)
    color.END
    postid = input(color.Yellow + 'ID записи(в ссылке после wall******_) >>> ' + color.Green)
    color.END
    mess = input(color.Yellow + 'Текст комментария >>> ' + color.Green)
    color.END
    try:
        api.wall.createComment(owner_id=post_comment,post_id=postid,message=mess)
    except vk.exceptions.VkAPIError:
        print(color.Green + 'У этого пользователя для вас закрыты комментарии.\n' + color.END)
        return
    print(color.Green + 'Комментарий отправлен!\n\n' + color.END)

#Инфа по айди
def info_by_id():
    clear()
    user_id = input(color.Yellow + 'ID пользователя >>> ' + color.Cyan)
    color.END

    user_info = api.users.get(user_ids=user_id, fields='relation, activity, can_write_private_message, online, sex')
    info = user_info[0]
    full_name = str(info.get('first_name') + ' ' + info.get('last_name'))
    link = 'https://vk.com/id' + str(info.get('id'))
    status = info.get('activity')
    check_pm = info.get('can_write_private_message')
    relation = info.get('relation')
    in_friends_check = info.get('can_access_closed')
    is_closed_check = info.get('is_closed')
    relation_list = ['не указано', 'не женат', 'не замужем', 'есть друг', 'есть подруга', 'помолвлен', 'помолвлена', 'женат', 'замужем', 'всё сложно', 'в активном поиске', 'влюблён', 'влюблена', 'в гражданском браке',]
    male = int(info.get('sex'))

    if male == 2: sex = 'Мужской'
    else: sex = 'Женский'

    if is_closed_check == True:
        is_closed = 'закрыта'
    else: 
        is_closed = 'открыта'
    if in_friends_check == True:
        in_friends = 'есть'
    else:
        in_friends = 'нет'
    if check_pm == 0:
        pm = 'закрыты'
    elif check_pm == 1:
        pm = 'открыты'
    if relation == 0 or str(relation) == 'None':
        show_r = str(relation_list[0])
        sp = str('Половинка: нет')
    if relation == 1:
        if male == 2:
            show_r = str(relation_list[1])
        else: show_r = str(relation_list[2])
        sp = str('Половинка: нет')
    elif relation == 2:
        if male == 2:
            show_r = str(relation_list[3])
        else: show_r = str(relation_list[4])
        try:
            rp = dict(info.get('relation_partner'))
            passed = 1
        except TypeError:
            sp = str('Половинка: нет')
            passed = 0
            pass
        if passed != 0:
            show_partner = str(rp.get('first_name') + rp.get('last_name'))
            partner_id = str(rp.get('id'))
            sp = str('Половинка: vk.com/id' + partner_id + '\n' + 'Имя половинки: ' + show_partner)

    elif relation == 3:
        if male == 2:
            show_r = str(relation_list[5])
        else: show_r = str(relation_list[6])
        try:
            rp = dict(info.get('relation_partner'))
            passed = 1
        except TypeError:
            sp = str('Половинка: нет')
            passed = 0
            pass
        if passed != 0:
            show_partner = str(rp.get('first_name') + ' ' + rp.get('last_name'))
            partner_id = str(rp.get('id'))
            sp = str('Половинка: vk.com/id' + partner_id + '\n' + 'Имя половинки: ' + show_partner)
    elif relation == 4:
        if male == 2:
            show_r = str(relation_list[7])
        else: show_r = str(relation_list[8])
        try:
            rp = dict(info.get('relation_partner'))
            passed = 1
        except TypeError:
            sp = str('Половинка: нет')
            passed = 0
            pass
        if passed != 0:
            show_partner = str(rp.get('first_name') + ' ' + rp.get('last_name'))
            partner_id = str(rp.get('id'))
            sp = str('Половинка: vk.com/id' + partner_id + '\n' + 'Имя половинки: ' + show_partner)
    elif relation == 5:
        show_r = str(relation_list[9])
        try:
            rp = dict(info.get('relation_partner'))
            passed = 1
        except TypeError:
            sp = str('Половинка: нет')
            passed = 0
            pass
        if passed != 0:
            show_partner = str(rp.get('first_name') + ' ' + rp.get('last_name'))
            partner_id = str(rp.get('id'))
            sp = str('Половинка: vk.com/id' + partner_id + '\n' + 'Имя половинки: ' + show_partner)
    elif relation == 6:
        show_r = str(relation_list[10])
        sp = str('Половинка: нет')
    elif relation == 7:
        if male == 2: show_r = str(relation_list[11])
        else: show_r = str(relation_list[12])
        try:
            rp = dict(info.get('relation_partner'))
            passed = 1
        except TypeError:
            sp = str('Половинка: нет')
            passed = 0
            pass
        if passed != 0:
            show_partner = str(rp.get('first_name') + ' ' + rp.get('last_name'))
            partner_id = str(rp.get('id'))
            sp = str('Половинка: vk.com/id' + partner_id + '\n' + 'Имя половинки: ' + show_partner)
    elif relation == 8:
        show_r = str(relation_list[13])
        try:
            rp = dict(info.get('relation_partner'))
            passed = 1
        except TypeError:
            sp = str('Половинка: нет')
            passed = 0
            pass
        if passed != 0:
            show_partner = str(rp.get('first_name') + ' ' + rp.get('last_name'))
            partner_id = str(rp.get('id'))
            sp = str('Половинка: vk.com/' + partner_id + '\n' + 'Имя половинки: ' + show_partner)

    print(color.Cyan + "===========================\n" + f"Имя: {full_name}\n" + f"Ссылка: {link}\n" + f"Статус: {status}\n" + f'Семейное положение: {show_r}\n' + f"Личные сообщения: {pm}\n" + f'Страница {is_closed}\n' + f'Возможность просмотра страницы: {in_friends}\n\n' + f'{sp}\n' + '===========================' + color.END)

#Скачать истории диалогов
def dl_history():
    clear()
    print(color.Cyan + "Данная функция доступна в нашем Телеграм боте! : @Vk_Tokenner_bot ! Для выхода в главное меню нажмите Q"  + color.END)
    choice = input('>>> ')
    if choice == 'Q' or choice == 'q':
        return
    
#Получение инфы о странице
def page_info():
    clear()
    print(color.Yellow + '[' + color.Cyan + '1' + color.Yellow + '] Записать в profile_info.txt [' + color.Cyan + '0' + color.Yellow + '] Вывести в командную строку\n' + color.END)
    to_txt = int(input(color.Yellow + '>>> '))

    info = api.account.getInfo()

    info1 = api.account.getProfileInfo()

    male = int(info1.get('sex'))

    if male == 2: sex = 'Мужской'
    else: sex = 'Женский'

    pro = ['не указано', 'не женат', 'не замужем', 'есть друг', 'есть подруга', 'помолвлен', 'помолвлена', 'женат', 'замужем', 'всё сложно', 'в активном поиске', 'влюблён', 'влюблена', 'в гражданском браке',]
    relation = int(info1.get('relation'))
    if relation == 1:
        if male == 2:
            show_r = str(pro[1])
        else: show_r = str(pro[2])
        sp = str('Половинка: нет')
    elif relation == 2:
        if male == 2:
            show_r = str(pro[3])
        else: show_r = str(pro[4])
        try:
            rp = dict(info1.get('relation_partner'))
            passed = 1
        except TypeError:
            sp = str('Половинка: нет')
            passed = 0
            pass
        if passed != 0:
            show_partner = str(rp.get('first_name') + rp.get('last_name'))
            partner_id = str(rp.get('id'))
            sp = str('Половинка: vk.com/id' + partner_id + '\n' + 'Имя половинки: ' + show_partner)

    elif relation == 3:
        if male == 2:
            show_r = str(pro[5])
        else: show_r = str(pro[6])
        try:
            rp = dict(info1.get('relation_partner'))
            passed = 1
        except TypeError:
            sp = str('Половинка: нет')
            passed = 0
            pass
        if passed != 0:
            show_partner = str(rp.get('first_name') + ' ' + rp.get('last_name'))
            partner_id = str(rp.get('id'))
            sp = str('Половинка: vk.com/id' + partner_id + '\n' + 'Имя половинки: ' + show_partner)
    elif relation == 4:
        if male == 2:
            show_r = str(pro[7])
        else: show_r = str(pro[8])
        try:
            rp = dict(info1.get('relation_partner'))
            passed = 1
        except TypeError:
            sp = str('Половинка: нет')
            passed = 0
            pass
        if passed != 0:
            show_partner = str(rp.get('first_name') + ' ' + rp.get('last_name'))
            partner_id = str(rp.get('id'))
            sp = str('Половинка: vk.com/id' + partner_id + '\n' + 'Имя половинки: ' + show_partner)
    elif relation == 5:
        show_r = str(pro[9])
        try:
            rp = dict(info1.get('relation_partner'))
            passed = 1
        except TypeError:
            sp = str('Половинка: нет')
            passed = 0
            pass
        if passed != 0:
            show_partner = str(rp.get('first_name') + ' ' + rp.get('last_name'))
            partner_id = str(rp.get('id'))
            sp = str('Половинка: vk.com/id' + partner_id + '\n' + 'Имя половинки: ' + show_partner)
    elif relation == 6:
        show_r = str(pro[10])
        sp = str('Половинка: нет')
    elif relation == 7:
        if male == 2: show_r = str(pro[11])
        else: show_r = str(pro[12])
        try:
            rp = dict(info1.get('relation_partner'))
            passed = 1
        except TypeError:
            sp = str('Половинка: нет')
            passed = 0
            pass
        if passed != 0:
            show_partner = str(rp.get('first_name') + ' ' + rp.get('last_name'))
            partner_id = str(rp.get('id'))
            sp = str('Половинка: vk.com/id' + partner_id + '\n' + 'Имя половинки: ' + show_partner)
    elif relation == 8:
        show_r = str(pro[13])
        try:
            rp = dict(info1.get('relation_partner'))
            passed = 1
        except TypeError:
            sp = str('Половинка: нет')
            passed = 0
            pass
        if passed != 0:
            show_partner = str(rp.get('first_name') + ' ' + rp.get('last_name'))
            partner_id = str(rp.get('id'))
            sp = str('Половинка: vk.com/' + partner_id + '\n' + 'Имя половинки: ' + show_partner)

    else: 
        show_r = str(pro[0])
        sp = str('Половинка: нет')
    name = str(info1.get('first_name') + ' ' + info1.get('last_name'))


    twofactor = int(info.get('2fa_required'))
    if twofactor == 1: tf = 'Включена'
    else: tf = 'Не включена'

    country = str(info.get('country'))
    ids1 = api.users.get()
    ids = str(ids1[0]['id'])
    link = str('vk.com/id' + ids)
    birthday = str(info1.get('bdate'))
    status = str(info1.get('status'))
        
    

    end = str('====================' + '\n' + 'Имя и фамилия: ' + name + '\n' + 'Пол: ' + sex + '\n' + 'Страна: ' + country + '\n' + 'Статус:' + status + '\n' + 'Дата рождения: ' + birthday + '\n' + 'Ссылка: ' + link + '\n' + 'Двухфакторная аутентификация: ' + tf + '\n' + 'Семейное положение: ' + show_r + '\n' + '\n' + sp + '\n' + '====================')
        
    if to_txt == 1:
        with open('profile_info.txt', 'tw', encoding='utf-8') as f:
            f.write(end)
            f.close()
        print(color.Green + f'Информация о профиле записана в {token}\\profile_info.txt !\n\n' + color.END)
    elif to_txt == 0:
        print(color.Cyan + end + '\n\n')

#Отправка сообщений
def send_message():
    clear()
    print(color.Cyan + "Данная функция доступна в нашем Телеграм боте! : @Vk_Tokenner_bot ! Для выхода в главное меню нажмите Q"  + color.END)
    choice = input('>>> ')
    if choice == 'Q' or choice == 'q':
        return

#Дамп вложений из диалога
def dl_attachments_from_dialog():
    clear()
    print(color.Cyan + "Данная функция доступна в нашем Телеграм боте! : @Vk_Tokenner_bot ! Для выхода в главное меню нажмите Q"  + color.END)
    choice = input('>>> ')
    if choice == 'Q' or choice == 'q':
        return
        

#Поиск в диалоге по сообщению
def search_by_word():
    peer_Id = int(input(color.Yellow + 'ID пользователя >>> ' + color.Green))
    color.END
    query = str(input(color.Yellow + 'Фраза, по которой будем искать >>> ' + color.Green))
    color.END
    search = api.messages.search(q=query, peer_id=peer_Id)
    print(search)

#Спам комментариями
def spam_comments():
    clear()
    while True:
        user_ids = input(color.Cyan + 'ID пользователя >> ')
        user_info_get = api.users.get(user_ids=user_ids, fields="wall_comments, uid")
        user_id = user_info_get[0]['id']
        comment_allowed = user_info_get[0].get("wall_comments")
        if comment_allowed == 0:
            print(color.Green + 'У этого пользователя закрыты комментарии.\n')
            return
        else:
            break
    wall_id_list = []
    try:
        wall = api.wall.get(owner_id=user_id, count=200)
    except vk.exceptions.VkAPIError:
        print(color.Green + 'У этого пользователя закрыт профиль.\n')
        return  

    for z in wall['items']:
        wall_id_list.append(z.get('id'))
    print(color.Cyan + 'Какими комментариями будем спамить? (В конце каждого комментария должен быть символ ; )')
    comments = input(color.Cyan + '>>> ')
    comment_list = comments.split(';')
    try:
        print(color.Yellow + 'Нажмите CTRL+C чтобы остановить работу спама.')
        while True:
            for wall_ in wall_id_list:
                for comment in comment_list:
                    try:
                        api.wall.createComment(owner_id=user_id, post_id=wall_, message=comment)
                        time.sleep(.6)
                    except vk.exceptions.VkAPIError:
                        time.sleep(10.0)
                        pass
    except KeyboardInterrupt:
        print(color.Green + 'Спам прерван пользователем.\n')
        pass

#Скачать фото с страницы
def photo_flood():
    clear()
    

#menu
while infinite < 5:
    init()
    print(menu)
    color.Yellow
    cmd = str(input('>>> '))
    color.END
    if cmd == '0': break
    elif cmd == '1': info_by_id()
    elif cmd == '2': page_info()
    elif cmd == '3': dl_history()
    elif cmd == '4': dl_attachments_from_dialog()
    elif cmd == '5': do_comment()
    elif cmd == '6': spam_comments()
    elif cmd == '7': send_message()
    elif cmd == '8': search_by_word()
    elif cmd == '9': photo_flood()
    elif cmd == '':
        clear()
        continue
    else: print(color.Green + 'Некорректный ввод!' + color.END)

    print(color.Green + 'Вы хотите продолжить? [0, N, no, нет] Нет [1, Y, yes, да] Да\n' + color.END)
    color.Yellow
    y = input('>>> ')
    color.END
    if y == "0" or y == 'no' or y == 'N' or y == 'нет': 
        clear()
        break
    if y == "1" or y == 'yes' or y == 'Y' or y == 'да': 
        clear()
        continue

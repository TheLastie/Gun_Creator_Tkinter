from tkinter import *
import random
def o(stihiya):
    def characteristic(type, level, stihiya):
        def types(type):
            t = {1: 'pystol', 2: 'automat', 3: 'pp', 4: 'shotgun', 5: 'sniper'}
            types = {'pystol': 1, 'automat': 0.7, 'pp': 0.4, 'shotgun': 3, 'sniper': 1.7}
            return types[t[type]]
        type = types(type)
        morf = random.randint(0, 1)
        dmg = int(((level/2) * random.randint(100, 150) / 10) * type)
        speed = round(((random.randint(5, 20) + 5) / type) / 10, 1)
        accuracy = int(random.randint(40, 58) * type)
        ammo = int(random.randint(5, 20) / type + 10)
        stdamage = speed * (level * random.randint(10, 15) / 10) * type
        if type == 3:
            if speed == 0:
                speed = 0.2

            i = random.randint(2, 15)
            dmg = str(int((((level/2) * random.randint(100, 150) / 10) * type) / i)) + 'x' + str(i)
            accuracy = int((random.randint(30, 100) / int(type)) + 10)
            stdamage = speed * (level * random.randint(10, 15) / 10)
        elif type == 1.7:
            speed = round(((random.randint(5, 20) + 10) / 2) / 10, 1)
            ammo = int(random.randint(5, 20) / type)
            stdamage = speed * (level * random.randint(10, 15) / 10)
        o = random.randint(1, 100)

        stih = stihiya - 1
        if stih != 5:
            stihiy = ['огня', 'холода', 'электричества', 'токсинов', 'радиации']
            stih = stihiy[stih]
        st = {1: 'fire', 2: 'cold', 3: 'elctr', 4: 'tox', 5: 'rad', 6: 'обычный'}
        stihiya = st[stihiya]
        if o < 20:
            speed = int(speed * 1.1)
            bonus = 'speed'
        else:
            bonus = 'n'
        if o > 20 and o < 40:
            if type == 3:
                final_damage = str(int((int(dmg.split('x')[0])*int(dmg.split('x')[1]) * (6 / 5)) / i))+'x'+str(i)
            else:
                final_damage = int(int(dmg) * (6 / 5))
            bonus = 'strength'
        else:
            final_damage = dmg
            bonus = 'n'
        if o > 80:
            if accuracy * 1.4 < 100:
                accuracy = accuracy * 1.3
                bonus = 'accuracy'
            else:
                bonus = 'n'

        if bonus != 'n':
            file = open('adjective/' + str(bonus) + '_namep.txt', encoding='UTF8')
            file = file.read()
            file = file.split()
            bon_name = file[random.randint(0, len(file) - 1)]
            if morf == 0:
                bon_name = bon_name[:-2] + 'ая'
        else:
            bon_name = ''
        if morf == 1:
            nam = open('adjective/3rd_namepm.txt', encoding='UTF8')
            nam = nam.read()
            nam = nam.split()
            name = nam[random.randint(0, len(nam) - 1)]
        else:
            nam = open('adjective/3rd_namepfem.txt', encoding='UTF8')
            nam = nam.read()
            nam = nam.split()
            name = nam[random.randint(0, len(nam) - 1)]
        if stihiya != 'обычный':
            stihiya = open('adjective/2st_' + stihiya + 'namep.txt', encoding='UTF8')
            stihiya = stihiya.read()
            stihiya = stihiya.split(' ')
            p = random.randint(0, len(stihiya) - 1)
            stihiya = stihiya[p]
            if morf == 0:
                stihiya = stihiya[:-2] + 'ая'
            name = bon_name.title() + ' ' + stihiya.title() + ' ' + name.title()
        else:
            name = bon_name.title() + ' ' + name.title()
            stdamage = 0
        return name, final_damage, speed, round(accuracy, 0), ammo, stdamage, stih
    type = random.randint(1, 5)
    t = {1: pystol, 2: auto, 3: pp, 4: shotgun, 5: snip}
    p = characteristic(type, 10, stihiya)
    l_1.config(text=p[0], font=('Bodoni MT Black', 13))
    l_2.config(text="Урон: " + str(p[1]), font=('Bodoni MT Black', 13))
    l_3.config(text='Скорость: ' + str(p[2]), font=('Bodoni MT Black', 13))
    l_4.config(text='Меткость: ' + str(p[3]), font=('Bodoni MT Black', 13))
    l_6.config(text='Количество патронов: ' + str(p[4]), font=('Bodoni MT Black', 13))
    if p[5] != 0:
        stihiy = {'огня': 'red', 'холода': 'blue', 'электричества': 'purple', 'токсинов': 'green', 'радиации': 'orange'}
        st = stihiy[p[6]]
        l_7.config(text='Урон от ' + p[6] + ' в секунду: ' + str(int(p[5])), font=('Bodoni MT Black', 10), fg=st)
    else:
        l_7.config(text='', font=('Bodoni MT Black', 10))

    l_5.config(image=t[type])
def t0():
    o(6)
def t1():
    o(1)
def t2():
    o(2)
def t3():
    o(3)
def t4():
    o(5)
def t5():
    o(4)

window = Tk()
window.title('Gun generator')
window.geometry('1000x900')
snip = PhotoImage(file='sniper.png')
auto = PhotoImage(file='automat.png')
pp = PhotoImage(file='pp.png')
shotgun = PhotoImage(file='shotgun.png')
pystol = PhotoImage(file='pystol.png')
images = {1.7: snip, 3: shotgun, 1: pystol, 0.4: pp, 0.7: auto}
b_1 = Button(window, text='Обычный', command=t0)
b_2 = Button(window, text='Огненный', command=t1, fg='red')
b_3 = Button(window, text='Ледяной', command=t2, fg='blue')
b_4 = Button(window, text='Электрический', command=t3, fg='purple')
b_5 = Button(window, text='Радиоактивный', command=t4, fg='orange')
b_6 = Button(window, text='Токсичный', command=t5, fg='green')
b_1.grid(column=1, row=0)
b_2.grid(column=1, row=1)
b_3.grid(column=1, row=2)
b_4.grid(column=1, row=3)
b_5.grid(column=1, row=4)
b_6.grid(column=1, row=5)
l_1 = Label(window)
l_2 = Label(window)
l_3 = Label(window)
l_4 = Label(window)
l_5 = Label(window)
l_6 = Label(window)
l_7 = Label(window)
l_1.grid(column=2, row=0)
l_2.grid(column=2, row=1)
l_3.grid(column=2, row=2)
l_4.grid(column=2, row=4)
l_6.grid(column=2, row=3)
l_7.grid(column=4, row=1)
l_5.grid(column=2, row=40)
window.mainloop()







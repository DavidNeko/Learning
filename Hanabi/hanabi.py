#!/usr/bin/env python
# coding=utf-8

import Tkinter as tk
from PIL import Image, ImageTk
from time import time, sleep
from random import choice, uniform, randint
from math import sin, cos, radians

# 设置重力参数
GRAVITY = 0.09
# 设置随机的颜色列表
colors = ['red', 'blue', 'yellow', 'white', 'green', 'orange', 'purple', 'seagreen', 'cornflowerblue',
          'honeydew', 'lavender', 'turquoise', 'aquamarine', 'lawn green', 'gold', 'magenta',
          'orchid1', 'plum1', 'MediumPurple1', 'purple1', 'firebrick1', 'IndianRed1']

class part:
    def __init__(self, cv, idx, total, explosion_speed, x=0., y=0., vx=0., vy=0., size=4., color='red', lifespan=3,
                 **kwargs):
        self.id = idx
        self.x = x
        self.y = y
        self.initial_speed = explosion_speed
        self.vx = vx
        self.vy = vy
        self.total = total
        self.age = 0
        self.color = color
        self.cv = cv
        self.cid = self.cv.create_oval(
            x - size, y - size, x + size,
            y + size, fill=self.color)
        self.lifespan = lifespan

    def update(self, dt):
        self.age += dt

        # 颗粒爆炸
        if self.alive() and self.expand():
            move_x = cos(radians(self.id * 360 / self.total)) * self.initial_speed
            move_y = sin(radians(self.id * 360 / self.total)) * self.initial_speed
            self.cv.move(self.cid, move_x, move_y)
            self.vx = move_x / (float(dt) * 1000)

        # 颗粒降落
        elif self.alive():
            move_x = cos(radians(self.id * 360 / self.total))

            self.cv.move(self.cid, self.vx + move_x, self.vy + GRAVITY * dt)
            self.vy += GRAVITY * dt

        # 如果颗超过最长持续时间，颗粒消失
        elif self.cid is not None:
            cv.delete(self.cid)
            self.cid = None

    # 定义爆炸的时间
    def expand(self):
        return self.age <= 2.0

    # 检查颗粒在生命周内是否还存在
    def alive(self):
        return self.age <= self.lifespan

def simulate(cv):
    t = time()
    explode_points = []
    wait_time = randint(10, 100)
    numb_explode = randint(3,20)
    # 循环创建所有的烟花颗粒
    for point in range(numb_explode):
        objects = []
        x_cordi = randint(50, 550)
        y_cordi = randint(50, 150)
        speed = uniform(0.3, 1.0)
        size = uniform(0.5, 5)
        color = choice(colors)
        explosion_speed = uniform(0.2, 1)
        total_particles = randint(10, 50)
        for i in range(1, total_particles):
            r = part(cv, idx=i, total=total_particles, explosion_speed=explosion_speed, x=x_cordi, y=y_cordi,
                     vx=speed, vy=speed, color=color, size=size, lifespan=uniform(0.6, 1.75))
            objects.append(r)
        explode_points.append(objects)

    total_time = .0
    # 保持在1.8秒内进行更新
    while total_time < 1.8:
        sleep(0.01)
        tnew = time()
        t, dt = tnew, tnew - t
        for point in explode_points:
            for item in point:
                item.update(dt)
        cv.update()
        total_time += dt
    # 通过递归持续不断的在背景中添加新烟花
    root.after(wait_time, simulate, cv)

def close(*ignore):
    """停止模拟循环，关闭窗口"""
    global root
    root.quit()


if __name__ == '__main__':
    root = tk.Tk()
    cv = tk.Canvas(root, height=600, width=600)
    # 自己选择一个好的图像背景填充画布
    image = Image.open("tknv.jpg")
    photo = ImageTk.PhotoImage(image)
    cv.create_image(0, 0, image=photo, anchor='nw')

    cv.pack()
    root.protocol("WM_DELETE_WINDOW", close)

    root.after(100, simulate, cv)

    root.mainloop()

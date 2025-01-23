# -*- coding = utf-8 -*-
# @Time: 2024/9/24 12:27
# @Author: Zhihang Yi
# @File: app.py
# @Software: PyCharm

from flask import Flask, render_template
import sqlite3
import random


app = Flask(__name__)


@app.route('/')
def homepage():
    conn = sqlite3.connect('/Users/yzhbradoodrrpurp/Desktop/douban_films_top250.db')
    c = conn.cursor()
    sql = "select * from douban_films_top250"
    films = c.execute(sql).fetchall()
    random_picks = []
    selected_films = []

    conn.close()

    for i in range(2):
        random_num = random.randint(0, 249)
        random_picks.append(films[random_num])

    for i in range(15):
        selected_films.append(films[i])

    return render_template("index.html", films=selected_films, random_picks=random_picks)


@app.route('/index')
def index():
    conn = sqlite3.connect('/Users/yzhbradoodrrpurp/Desktop/douban_films_top250.db')
    c = conn.cursor()
    sql = "select * from douban_films_top250"
    films = c.execute(sql).fetchall()
    random_picks = []
    selected_films = []

    conn.close()

    for i in range(2):
        random_num = random.randint(0, 249)
        random_picks.append(films[random_num])

    for i in range(15):
        selected_films.append(films[i])

    return render_template("index.html", films=selected_films, random_picks=random_picks)


@app.route('/randompicks')
def random_picks():
    conn = sqlite3.connect('/Users/yzhbradoodrrpurp/Desktop/douban_films_top250.db')
    c = conn.cursor()
    sql = "select * from douban_films_top250"
    films = c.execute(sql).fetchall()
    random_picks = []

    conn.close()

    for i in range(18):
        random_num = random.randint(0, 249)
        random_picks.append(films[random_num])

    return render_template("randompicks.html", random_picks=random_picks)


@app.route('/toprated')
def top_rated():
    conn = sqlite3.connect('/Users/yzhbradoodrrpurp/Desktop/douban_films_top250.db')
    c = conn.cursor()
    sql = "select * from douban_films_top250"

    films = c.execute(sql).fetchall()
    conn.close()

    return render_template("toprated.html", films=films)


if __name__ == "__main__":
    app.run()

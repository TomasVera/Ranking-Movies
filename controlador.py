# -*- coding: utf-8 -*-

import sqlite3

def conectar():
    con = sqlite3.connect('movies.db')
    con.row_factory = sqlite3.Row
    return con


def get_movies():
    '''Metodo para obtener las peliculas listadas en la tabla "movies"'''
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM movies ORDER BY ranking ASC"
    resultado = c.execute(query)
    movies = resultado.fetchall()
    return movies


def get_id(pk):
    con = conectar()
    c = con.cursor()
    query = "SELET * FROM movies WHERE id = ?"
    resultado = c.execute(query, [pk])
    movie = resultado.fetchall()
    return movie


def get_rank(rank):
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM movies WHERE ranking = ?"
    resultado = c.execute(query, [rank])
    movie = resultado.fetchall()
    return movie


def update(nombre, rank):
    con = conectar()
    c = con.cursor()
    query = "UPDATE movies SET ranking = ? WHERE title = ?"
    c.execute(query, [rank, nombre])
    con.commit()


def get_max():
    con = conectar()
    c = con.cursor()
    query = "SELECT COUNT(*) FROM movies"
    num = c.execute(query)
    return num


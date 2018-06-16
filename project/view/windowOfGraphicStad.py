#!/usr/bin/python3
# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt


def graphicCake(dictDatas):
    """
    :param dictDatas: dict that contains the datas to graphic the type cake
    """
    names, datas = list(dictDatas.keys()), list(dictDatas.values())

    fig, ax = plt.subplots(figsize=(9, 6), subplot_kw=dict(aspect="equal"))


    def func(pct, allvals):

        absolute = int(pct / 100. * np.sum(allvals))
        return "{:.1f}%({:d})".format(pct, absolute)

    wedges, texts, autotexts = ax.pie(datas,  autopct=lambda pct: func(pct, datas), textprops=dict(color="w"))


    ax.legend(wedges, names,
              title="Movimientos",
              loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=8, weight="bold")

    ax.set_title("Grafica de tipo pastel")

    plt.show()


def graphicBar(dictDatas):
    """
    :param dictDatas: dict that contains the datas to graphic the type Bar
    """

    names,datas = list(dictDatas.keys()), list(dictDatas.values())

    fig = plt.figure(u'Gráfica de barras')  # Figure
    fig.set_size_inches((9,6))
    ax = fig.add_subplot(111)  # Axes
    xx = range(len(datas))
    valor = [(i / np.sum(datas))*100 for i in datas ]
    ax.bar(xx, valor, width=0.8, align='center')
    ax.set_xticks(xx)
    ax.set_xticklabels(names)
    ax.set_title("Grafica de tipo barra")
    plt.show()

#dic = {"up":12.5, "down": 34.2,"left": 0, "right":5, "open":12, "close":7 }
#graphicCake(dic)
#graphicBar(dic)



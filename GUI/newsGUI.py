'''
title: GUI for Newsfeed
author: Palaash Kolhe
date created: 2020-06-12
'''

from webscraping import webScrapeURL, getNewsStock
from tkinter import *
import webbrowser

class NewsfeedGUI:
    def __init__(self, window, ticker):
        self.url = "https://finviz.com/quote.ashx?t={0}".format(ticker)
        self.page = webScrapeURL(self.url)
        self.news = getNewsStock(self.page)

        self.backgroundColor = 'gray12'
        self.foregroundColor = 'white'

        self.newsFrame = Frame(window, height=374, width=425, bg=self.backgroundColor)
        self.newsFrame.grid(row=3, column=8, rowspan=3, sticky='s')

        self.titleLabel = Label(self.newsFrame, text="LATEST NEWS", font=('Helvetica', '12', 'bold'), bg=self.backgroundColor, fg=self.foregroundColor, padx=10, pady=10.5)
        self.titleLabel.grid(row=0, columnspan=3, sticky='news')

        self.row = 1

        for i in range(8):
            self.publisherLabel = Label(self.newsFrame, text=self.news[i][1], font=('Helvetica', '7', 'bold'), bg=self.backgroundColor, fg=self.foregroundColor, padx=3, pady=2, wraplength=100, justify=LEFT)
            self.newsLabel = Label(self.newsFrame, text=self.news[i][0], font=('Helvetica', '9'), bg=self.backgroundColor, fg=self.foregroundColor, padx=2, pady=2, wraplength=325, justify=LEFT, cursor='hand1')

            self.newsLabel.bind("<Button-1>", lambda e: self.callback(self.news[i][2]))

            self.publisherLabel.grid(row=self.row, column=1, sticky=W)
            self.newsLabel.grid(row=self.row, column=2, sticky=W)

            self.row+=1

        self.newsFrame.grid_propagate(0)

    def callback(self, url):
        webbrowser.open_new(url)


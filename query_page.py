from tkinter import Tk, Frame, Canvas, Button, Entry, Label, NW, W
import requests
from urllib import parse
from utils import captcha_url, save_image, mul_thread
from constants import STATION_CODE, TICKET_FROM, TICKET_TO, TICKET_DATE, TICKET_PURPOSE, ADULT, URL_UNKNOW


class QueryPage:
    def __init__(self, root, session):
        self.window = root
        self.frame = Frame(self.window)
        self.session = session
        # setup input box
        self.label_name = Label(self.frame, text="出发地")
        self.label_name.grid(row=0, column=0, sticky=W)
        self.from_station = Entry(self.frame)
        self.from_station.grid(row=0, column=1)
        self.label_name = Label(self.frame, text="目的地")
        self.label_name.grid(row=1, column=0, sticky=W)
        self.to_station = Entry(self.frame)
        self.to_station.grid(row=1, column=1)
        self.label_name = Label(self.frame, text="出发时间")
        self.label_name.grid(row=2, column=0, sticky=W)
        self.train_date = Entry(self.frame)
        self.train_date.grid(row=2, column=1)
        # setup button
        self.button_login = Button(self.frame, text="查询", width=10, height=5)
        self.button_login.grid(row=3, column=1, padx=1, pady=1)
        self.button_login.bind("<ButtonRelease-1>", self.query)
        self.frame.pack()
        # self.frame.mainloop()

    def my_request(self, url, params=None, data=None):
        if data:
            response = self.session.post(url, data=data)
        elif not params:
            response = self.session.get(url)
        else:
            response = self.session.get(url, params=params)
        return response

    def log(self):
        pass

    def query(self, event):
        params = self.ticket_data()
        with open("url.py", "r") as f:
            url = f.read().strip(' ') + params
        print(url)
        response = self.my_request(url)
        print(response.json())

    def ticket_data(self):
        encoded_params = ''
        f = self.from_station.get()
        t = self.to_station.get()
        ticket_from = STATION_CODE[f]
        ticket_to = STATION_CODE[t]
        adult = ADULT
        date = self.train_date.get()
        k_list = [TICKET_DATE, TICKET_FROM, TICKET_TO, TICKET_PURPOSE]
        v_list = [date, ticket_from, ticket_to, adult]
        for i, e in enumerate(k_list):
            v = v_list[i]
            encoded_params += parse.urlencode({e: v}) + '&'
        return encoded_params.strip('&')






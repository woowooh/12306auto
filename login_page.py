from tkinter import Tk, Frame, Canvas, Button, Entry, Label, NW, W, PhotoImage
import requests
from utils import captcha_url, save_image, mul_thread
from constants import INIT_PAGE, CAPTCHA_NAME, CAPTCHA_CHECK_PATH, ANSWER, RAND, SJRAND, LOGIN_SITE_E,\
    LOGIN_SITE, LOGIN_PATH, UAUTH_PATH, UA_CLIENT_PATH, USER_LOGIN_PATH, INIT_MY12306
from query_page import QueryPage
from werkzeug.contrib.cache import SimpleCache


class LoginPage:
    def __init__(self, root):
        self.window = root
        self.frame = Frame(self.window)
        self.image = ""
        self.captcha_position = ""
        self.session = requests.Session()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0",
            "Referer": "https://kyfw.12306.cn/otn/login/init",
        }
        self.canvas = Canvas(self.window, width=300, height=200, bg="#86bff0")
        self.setup_captcha()
        # setup input box
        self.label_name = Label(self.frame, text="账号")
        self.label_name.grid(row=0, column=0, sticky=W)
        self.username_input = Entry(self.frame)
        self.username_input.grid(row=0, column=1)
        self.label_name = Label(self.frame, text="密码")
        self.label_name.grid(row=1, column=0, sticky=W)
        self.password_input = Entry(self.frame, show="*")
        self.password_input.grid(row=1, column=1)
        # setup button
        self.button_login = Button(self.frame, text="登陆", width=10, height=5)
        self.button_login.grid(row=2, column=1, padx=1, pady=1)
        self.button_login.bind("<ButtonRelease-1>", self.login)
        self.button_refresh = Button(self.frame, text="刷新", width=3, height=3)
        self.button_refresh.grid(row=0, column=3, padx=1, pady=1)
        self.button_refresh.bind("<ButtonRelease-1>", self.refresh_captcha)
        self.frame.pack()

    def setup_captcha(self):
        self.my_request(INIT_PAGE)
        self.my_request(UAUTH_PATH)
        image = self.download_captcha()
        self.image = PhotoImage(file=image)
        self.draw_captcha()

    def my_request(self, url, data=None):
        if data:
            response = self.session.post(url, data=data, headers=self.headers)
        else:
            response = self.session.get(url)
        return response

    def download_captcha(self):
        url = captcha_url()
        response = self.my_request(url)
        image = save_image(CAPTCHA_NAME, response.content)
        return image

    @mul_thread
    def draw_point(self, event):
        self.paint(event)
        self.save_position(event)

    def paint(self, event):
        x1, y1 = (event.x - 5), (event.y - 5)
        x2, y2 = (event.x + 5), (event.y + 5)
        self.canvas.create_oval(x1, y1, x2, y2, fill="red")

    def save_position(self, event):
        self.captcha_position += str(event.x) + ',' + str(int(event.y) - 20) + ','

    def captcha_data(self):
        data = dict()
        data[ANSWER] = self.captcha_position.strip(',')
        data[LOGIN_SITE] = LOGIN_SITE_E
        data[RAND] = SJRAND
        return data

    def user_data(self):
        params = dict()
        params['username'] = self.username_input.get()
        params['password'] = self.password_input.get()
        params['appid'] = 'otn'
        return params

    def draw_captcha(self):
        self.canvas.create_image(0, 0, anchor=NW, image=self.image)
        self.canvas.bind("<Button-1>", self.draw_point)
        self.canvas.pack()

    def reset_position(self):
        self.captcha_position = ''

    @mul_thread
    def refresh_captcha(self, event):
        self.reset_position()
        self.setup_captcha()

    def login(self, event):
        form_data = self.captcha_data()
        capt_json = self.my_request(CAPTCHA_CHECK_PATH, data=form_data).json() # 4
        user_data = self.user_data()
        uauth_json = self.my_request(LOGIN_PATH, data=user_data).json() # 0
        response = self.my_request(UAUTH_PATH, data={"appid": "otn"}).json()
        new_tk = response["newapptk"]
        self.my_request(UA_CLIENT_PATH, data={"tk": new_tk}).json() # 0
        self.my_request(INIT_MY12306)
        self.frame.destroy()
        self.canvas.destroy()
        QueryPage(self.window, self.session)


if __name__ == '__main__':
    root = Tk()
    LoginPage(root)
    root.mainloop()

# to dos

# 2. 搜索列车筛选
# 3. 选定乘坐车次
# 4. 占座





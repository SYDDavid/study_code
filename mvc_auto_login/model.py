import pyautogui
from configparser import ConfigParser
import os


class Model():
    def __init__(self):
        self.conf = ConfigParser()
        self.conf_path = os.path.join(os.getcwd(), 'conf.ini')
        self._creat_conf()

    # 键入R来重连ssh
    def press_R(self):
        pyautogui.typewrite('R')

    # 键入用户与密码
    def auth(self, str_name, str_pwd):
        pyautogui.typewrite(str_name)
        pyautogui.press('enter')
        pyautogui.typewrite(str_pwd)
        pyautogui.press('enter')

    # 切换进程
    def alterProgress(self):
        pyautogui.hotkey('alt', 'tab')

    # 写入配置文件
    def write_config(self, str_name, str_pwd):
        self.conf.read(self.conf_path, encoding='utf-8')
        self.conf.set('login_info', 'name', str_name)
        self.conf.set('login_info', 'pwd', str_pwd)
        self.conf.write(open(self.conf_path, 'w', encoding='utf-8'))

    # 读取配置文件
    def read_config(self):
        self.conf.read(self.conf_path, encoding='utf-8')
        return {
            'name': self.conf.get('login_info', 'name'),
            'pwd': self.conf.get('login_info', 'pwd')
        }

    # 判断文件是否存在，若不存在创建配置文件并赋予默认值
    def _creat_conf(self):
        if os.path.exists(self.conf_path) != True:
            with open(self.conf_path, 'w') as f:
                f.writelines(['[login_info]\r', 'name = root\r', 'pwd = Engine-147+'])

            # self.conf.read(self.conf_path, encoding='utf-8')
            # self.conf.set('login_info', 'name', '')
            # self.conf.set('login_info', 'pwd', '')
            # self.conf.write(open(self.conf_path, 'w', encoding='utf-8'))


if __name__ == '__main__':
    m = Model()
    # m.creat_conf()

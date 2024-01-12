from model import Model
from view import View


class Controller():
    def __init__(self, view, model):
        self._view = view
        self._model = model

        login_info_dict = self._model.read_config()
        self._view.name.setText(login_info_dict['name'])
        self._view.pwd.setText(login_info_dict['pwd'])

        self._view.button.clicked.connect(self.r_conn)

    # 重连函数
    def r_conn(self):
        name = self._view.get_name()
        pwd = self._view.get_pwd()

        self._model.alterProgress()
        self._model.press_R()

        self._model.auth(name, pwd)
        self._model.write_config(name, pwd)

from .view import View
from .model import Model
from .controller import Controller

view = View()
model = Model()
controller = Controller(view, model)
view.window_show()

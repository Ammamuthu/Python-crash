import kivy
from kivy.app import App
from kivy.core import text
from kivy.core.text import markup
from kivy.uix.label import Label
class God(App):
    def build(self):
        l=Label(text="[color=][i][b]Hello [/b][/color]World[/i]",markup=True,font_size="50px")

        return l
a=God()
a.run()
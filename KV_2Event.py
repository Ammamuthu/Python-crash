import kivy
from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label

class HelloWorld(App):
    def clicl(selfinstancevalue):
        print("hhhhooooooooo")
    def build(self):
    
        l=Label(text="A[ref=Rebel] Rebel[/ref] WITh An Stroy")

        l.bind(on_ref_press=self.clicl)
        return l
a=HelloWorld()

a.run()
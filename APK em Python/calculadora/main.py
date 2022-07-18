from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Window.size(500,700)
Builder.load("main.kv")

class MyLayout(Widget):
    #funções
    def clear(self):
        valor = ""
        self.ids.calc_input.text = valor
    def delete(self):
        valor = self.ids.calc_iput.text
        self.ids.calc_input.text = valor[:-1]
        
    def recebeCar(self, car):
        valor = car
        self.ids.calc_input.text += valor
        
    def calcular(self):
        valor = eval(self.ids.calc_input.text)
        self.ids.calc_input.text = str(valor)
    
    #def inverteSinal():

class calculadora(App):
    #montável com o kivy
    def build(self):
        return MyLayout()
    
calculadora.run()

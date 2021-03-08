
#importa los archivos carga.py,corriente.py,voltaje.py
import carga
import corriente
import voltaje
#importa las librerias de kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

#este es el builder de kivy donde se hace la interfaz del programa
Builder.load_string("""
<test_screen>:
    Label:
        id:label
        text:"Graficadora del Comportamiento de la Carga de un Capacitor"
        font_size: 28
        size_hint: 1, .35
        pos_hint:{'center_x':.5,'y':.6}
        color: 1,.5,0,1
    Label:
        id:v
        text:"Voltaje (Volt)"
        font_size: 18
        size_hint: None, None
        pos_hint:{'center_x':.37,'y':.49}
        color: 1,.5,0,1
    TextInput:
        id:textE
        hint_text:"Volt"
        size_hint: None, None
        width:100
        height:28
        pos_hint:{'center_x':.5,'y':.55}
    Label:
        id:r
        text:"Resistencia (Ohm)"
        font_size: 18
        size_hint: None, None
        pos_hint:{'center_x':.34,'y':.39}
        color: 1,.5,0,1
    TextInput:
        id:textR
        hint_text:"Ohm"
        size_hint: None, None
        width:100
        height:28
        pos_hint:{'center_x':.5,'y':.45}
    Label:
        id:C
        text:"Capacitancia (F)"
        font_size: 18
        size_hint: None, None
        pos_hint:{'center_x':.35,'y':.29}
        color: 1,.5,0,1
    TextInput:
        id:textC
        hint_text:"Faradio"
        size_hint: None, None
        width:100
        height:28
        pos_hint:{'center_x':.5,'y':.35}
    Label:
        id:t
        text:"Tiempo (Seg)"
        font_size: 18
        size_hint: None, None
        pos_hint:{'center_x':.36,'y':.19}
        color: 1,.5,0,1
    TextInput:
        id:textT
        hint_text:"Segundos"
        size_hint: None, None
        width:100
        height:28
        pos_hint:{'center_x':.5,'y':.25}
    Button:
        text:"Graficar la Carga"
        size_hint:None, None
        width:125
        height:48
        pos_hint:{'center_x':.5,'y':.05}
        on_press:root.graficarQ()
    Button:
        text:"Graficar la Corriente"
        size_hint:None, None
        width:150
        height:48
        pos_hint:{'center_x':.72,'y':.05}
        on_press:root.graficarI()
    
    Button:
        text:"Graficar el Voltaje"
        size_hint:None, None
        width:135
        height:48
        pos_hint:{'center_x':.28,'y':.05}
        on_press:root.graficarV()
        
    
    
""")
class test_screen(FloatLayout):
    #funcion del boton de Graficar la Carga
    def graficarQ(self):
        #llama los datos introducidos en el textinput 
        #dato del Voltaje
        textE = self.ids.textE.text
        #dato de la resistencia
        textR = self.ids.textR.text
        #dato de la capasitancia
        textC = self.ids.textC.text
        #dato del tiempo
        textT = self.ids.textT.text
        if textE=="" or textR=="" or textC=="" or textT=="":
            #condicion si no a introducido todos los datos
            print("digite los parametros")
        else:
            #llama al archivo carga.py y manda los datos y ala funcion graficar 
            carga.datos(textE,textR,textC,textT)
            carga.grafic()
              
   #funcion del boton de Graficar el Voltaje         
    def graficarV(self):
         #llama los datos introducidos en el textinput 
        #dato del Voltaje
        textE = self.ids.textE.text
        #dato de la resistencia
        textR = self.ids.textR.text
        #dato de la capasitancia
        textC = self.ids.textC.text
        #dato del tiempo
        textT = self.ids.textT.text
        if textE=="" or textR=="" or textC=="" or textT=="":
            #condicion si no a introducido todos los datos
            print("digite los parametros")
        else:
             #llama al archivo voltaje.py y manda los datos y ala funcion graficar 
            voltaje.datos(textE,textR,textC,textT)
            voltaje.grafic()
    #funcion del boton de Graficar la Corriente
    def graficarI(self):
         #llama los datos introducidos en el textinput 
        #dato del Voltaje
        textE = self.ids.textE.text
        #dato de la resistencia
        textR = self.ids.textR.text
        #dato de la capasitancia
        textC = self.ids.textC.text
        #dato del tiempo
        textT = self.ids.textT.text
        if textE=="" or textR=="" or textC=="" or textT=="":
            #condicion si no a introducido todos los datos
            print("digite los parametros")
        else:
            #llama al archivo corriente.py y manda los datos y ala funcion graficar 
            corriente.datos(textE,textR,textC,textT)
            corriente.grafic()     

        
    
       
class GraficadoraApp(App):
    def build(self):
        Window.clearcolor= 1,1,1,1
        return test_screen()
if __name__ == '__main__':
    GraficadoraApp().run()


from kivymd.app import MDApp
from kivymd.uix.button import MDFloatingActionButton, MDFlatButton
from kivymd.uix.screen import Screen



class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.primary_hue = "100"
        
       
        btn1 = MDFlatButton(text='Show Chord', pos_hint={'center_x': 0.5, 'center_y': 0.05})
        btn = MDFloatingActionButton(icon="android",
                                     pos_hint={'center_x': 0.5, 'center_y': 0.05},
                                     )
        btn2 = MDFlatButton(text='SelectChord', pos_hint={'center_x': 0.05, 'center_y': 0.95})
        btn = MDFloatingActionButton(icon="android",
                                     pos_hint={'center_x': 0.05, 'center_y': 0.95},
                                     )
        screen.add_widget(btn1)
        screen.add_widget(btn2)
        return screen


DemoApp().run()
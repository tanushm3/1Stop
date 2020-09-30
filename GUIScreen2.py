# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 20:58:13 2020

@author: NECROMANCER
"""



from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivy.uix.scrollview import ScrollView


chordList = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
variation = ['Major','Minor']

class DemoApp(MDApp):

    def build(self):
        screen = Screen()

        # Creating a Simple List
        scroll = ScrollView()

        list_view = MDList()
        for i in chordList:

            # items = ThreeLineListItem(text=str(i) + ' item',
            #                          secondary_text='This is ' + str(i) + 'th item',
            #                          tertiary_text='hello')
            for j in variation:
                # icons = IconLeftWidget(icon="android")
                items = OneLineIconListItem(text= i + ' ' + j)
                # items.add_widget(icons)
                list_view.add_widget(items)

        scroll.add_widget(list_view)
        # End List

        screen.add_widget(scroll)
        return screen


DemoApp().run()
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.image import Image
from kivymd.app import MDApp
from kivymd.uix.list import IRightBodyTouch, ILeftBody
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget


chordList = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
variation = ['Major','Minor']
Builder.load_string(
    """
<ListItemWithCheckbox@OneLineAvatarIconListItem>:
    MyAvatar:
        source: "data/logo/kivy-icon-128.png"
    MyCheckbox:


<Lists@BoxLayout>
    name: "lists"
    orientation: "vertical"

    MDToolbar:
        title:"List item with Checkbox"
        md_bg_color: app.theme_cls.primary_color
        elevation: 10

    ScrollView:

        MDList:
            id: scroll
"""
)
    


class MyCheckbox(IRightBodyTouch, MDCheckbox):
    pass


class MyAvatar(ILeftBody, Image):
    pass


class MainApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "Kivymd Examples - MDList with Checkboxes"
        
        super().__init__(**kwargs)

    def build(self):
        list = Factory.Lists()
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

                list.ids.scroll.add_widget(Factory.ListItemWithCheckbox(text= i+" "+j))
        self.root = list


if __name__ == "__main__":
    MainApp().run()
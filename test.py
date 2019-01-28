import cocos
import pyglet
from cocos.actions import *

cDirector = cocos.director.director
cScene = cocos.scene
cText = cocos.text
cLayer = cocos.layer
cSprite = cocos.sprite

class HelloWorld(cLayer.Layer):
    is_event_handler = True

    def __init__(self):
        super(HelloWorld, self).__init__()

        self.txtKey = cText.Label(
            '',
            font_name='Times New Roman',
            font_size=32,
            anchor_x='center',
            anchor_y='center'
        )

        self.txtKey.position = 300, 240

        self.keys_pressed = set()
        self.update_text()
        self.add(self.txtKey)


    def on_key_press(self, key, modifiers):
        self.keys_pressed.add(key)
        self.update_text()


    def on_key_release(self, key, modifiers):
        self.keys_pressed.remove(key)
        self.update_text()


    def update_text(self):
        key_names = [pyglet.window.key.symbol_string(k) for k in self.keys_pressed]
        self.txtKey.element.text = ','.join(key_names)


cDirector.init()
hello_layer = HelloWorld()

main_scene = cScene.Scene(hello_layer)

cDirector.run(main_scene)

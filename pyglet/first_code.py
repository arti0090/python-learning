import pyglet
from pyglet.window import key, mouse

window = pyglet.window.Window()
# importing images
# image = pyglet.resource.image('kitten.jpg')
# or out of app dir
# image = pyglet.image.load(path)

# importing music (in app directory) | use streaming=False for short sounds 
# music = pyglet.resource.media('music.mp3')
# 
# importing music (rel or abs path)
# music = pyglet.media.load(path)
# 
# music.play()

label = pyglet.text.Label('Hello World',
                          font_name='Times New Roman',
                          font_size=36,
                          x = window.width // 2, y = window.height // 2,
                          anchor_x='center', anchor_y='center'
                          )

@window.event
def on_draw():
    window.clear()
    label.draw()
    # image.blit(0, 0)

@window.event
def on_key_press(symbol, modifiers):
    print(f'A {chr(symbol)} was pressed')
    if symbol == key.ESCAPE:
        pyglet.app.exit()

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print("the left mouse was pressed")

# Shows events in console
event_logger = pyglet.window.event.WindowEventLogger()
window.push_handlers(event_logger)

pyglet.app.run()

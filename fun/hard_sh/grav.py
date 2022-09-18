from tkinter import *
import time
window = Tk()
canvas = Canvas(window, width=400, height=400)
canvas.pack()

def move_rect(event):
  key = event.keysym
  if key == 'Up':
    for x in range(20, 0, -1):
      canvas.move(rect, 0, -x)
      window.update()
      time.sleep(0.15)
    for y in range(20):
      canvas.move(rect, 0, y)
      window.update()
      time.sleep(0.15)
    canvas.move(rect, 0, 20)

rect = canvas.create_rectangle(150, 400, 250, 300, fill = 'blue')


canvas.bind_all('<Key>', move_rect)
window.mainloop()
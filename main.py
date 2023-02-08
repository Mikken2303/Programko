import tkinter as tk

root = tk.Tk()
root.configure(bg='black')
root.title("Blue Face")
root.geometry("200x200")

canvas = tk.Canvas(root, bg='black', height=200, width=200)

# Draw the head
head_coords = [50, 50, 150, 150]
canvas.create_polygon(head_coords, outline='blue', width=2, fill='black')

# Draw the eyes
eye_left_coords = [70, 80, 90, 90, 80, 100]
canvas.create_polygon(eye_left_coords, outline='blue', width=2, fill='black')

eye_right_coords = [110, 80, 130, 90, 120, 100]
canvas.create_polygon(eye_right_coords, outline='blue', width=2, fill='black')

# Draw the mouth
mouth_coords = [70, 140, 140, 140, 105, 160]
canvas.create_polygon(mouth_coords, outline='blue', width=2, fill='black')

canvas.pack()

root.mainloop()
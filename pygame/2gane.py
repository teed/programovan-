import tkinter as tk

# okno
W, H = 600, 200
root = tk.Tk()
root.title("Kolečko jezdí tam a zpět")

c = tk.Canvas(root, width=W, height=H, bg="white")
c.pack()

# čára
y = H // 2
x1, x2 = 80, W - 80
c.create_line(x1, y, x2, y, width=4)

# kolečko
r = 15
x = x1
dx = 4  # rychlost (kladně doprava, záporně doleva)

ball = c.create_oval(x - r, y - r, x + r, y + r, fill="dodgerblue", outline="")

def animate():
    global x, dx
    x += dx

    # odraz na koncích čáry
    if x >= x2 - r:
        x = x2 - r
        dx = -dx
    elif x <= x1 + r:
        x = x1 + r
        dx = -dx

    c.coords(ball, x - r, y - r, x + r, y + r)
    root.after(16, animate)  # ~60 FPS

animate()
root.mainloop()

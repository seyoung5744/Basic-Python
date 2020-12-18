import tkinter as tk
import day04.mini_project.Map as map
def main():
    root = tk.Tk()
    app = map.Map(root, '700x700+600+150') # 600, 150, 700, 700
    app.mainloop()

main()
import tkinter as tk
    
def open_new_window():

    root.destroy()

    new_window = tk.Tk()
    new_window.title("PC Hacked!")
    new_window.geometry("300x200")
    new_label = tk.Label(new_window, text="Hahaha, I knew it!", font=("Helvetica", 16))
    new_label.pack(pady=20)

    new_window.mainloop()    

root = tk.Tk()
root.title("PC Hacked!")
root.geometry("300x200")

frame = tk.Frame(root)
frame.pack(pady=20, expand=True)

label = tk.Label(frame, text="Are You an Idiot?", font=("Helvetica", 16))
label.pack()

button_frame = tk.Frame(frame)
button_frame.pack(pady=10)

button = tk.Button(button_frame, text="No", font=("Helvetica", 16), padx=10, pady=5, bg="green", fg="white")
button.pack(side=tk.RIGHT, padx=10)
button = tk.Button(button_frame, text="Yes", command=open_new_window, font=("Helvetica", 12), padx=20, pady=10, bg="red", fg="white")
button.pack(side=tk.LEFT, padx=10)

label = tk.Label(frame, text="Did You Leave your PC Unlocked?", font=("Helvetica", 12))
label.pack()

root.mainloop()
import tkinter as tk

#window = tk.Tk()

#greet = tk.Label(text='hello')

#label = tk.Label(
 #   text="Hello, Tkinter",
  #  foreground="white",  # Set the text color to white
   # background="black"  # Set the background color to black
#)

#label.pack

#greet.pack

#tk.mainloop

window = tk.Tk()
text_box = tk.Text()
text_box.insert(1.0,'hello')
  
    
text_box.pack()
tk.mainloop()
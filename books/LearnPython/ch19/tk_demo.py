import sys
from tkinter import Button, mainloop  # Tkinter in 2.6

x = Button(
    text='Press me',
    command=(lambda: sys.stdout.write('Spam\n'))
)
print(dir(Button))
x.pack()
mainloop()

import tkinter as tk
from PIL.ImageTk import PhotoImage
from PIL import ImageTk
from PIL.ImageTk import Image
from random import choice
colors = [ '1', '2', '3', '4', '5', '6', '7', '8', '9',
            'A', 'B', 'C', 'D', 'E', 'F' ] 
root = tk.Tk()
def change_color():
    color = "#"+"".join([ choice(colors) for _ in range(6) ])
    label.config(bg=color)
    label.after(1000, change_color)
label = tk.Label(root, text="Qoutes of the Day ", font=('Times', 30, 'bold'),fg='white')

label.pack(fill=tk.BOTH, expand=tk.YES)

label.after(1000, change_color)

image_list = ['images/apj.png','images/modi.png','images/tata.png','images/sachin.png']
text_list = ['''Don’t take rest 
after your first victory
 because if you fail in second, 
 more lips are waiting 
 to say that your first
  victory was just luck.
   - A.P.J Abdul Kalam''',
                '''Our vision and commitment
                 is towards the country's progress, 
                 its place in the world 
                 and the happiness of its people.  
                    -Narendra Modi''',
                '''The day I am not able to fly will be a sad day for me.
                     -Ratan Tata''',
                '''I always had a dream to play for India
                 but I never let it put pressure on me. 
                    -Sachin Tendulkar''']
move=0
def slide(d):
    global image_list,text_list,move
    # if not (0 <= move + d < len(image_list)):
    #     tkMessageBox.showinfo('End', 'No more image.')
    #     return
    move+=d
    image = Image.open(image_list[move])
    photo = PhotoImage(image)
    w['text'] = text_list[move]
    w['image']= photo
    w.photo = photo

w = tk.Label(root, compound=tk.RIGHT,fg='white', bg='black', font=('monospace', 20, 'bold', 'italic'))
w.pack(fill=tk.BOTH, expand=tk.YES)

# tk.Button(root, text='Previous', command=lambda: slide(-1)).pack(side=tk.LEFT)
# tk.Button(root, text='Next', command=lambda: slide(+1)).pack(side=tk.LEFT)
# tk.Button(root, text='Quit', command=root.quit).pack(side=tk.LEFT)

prev = tk.Button(root, text='Previous', font=10, width=20, height=2)
prev.config(command= lambda: slide(-1), justify='left')
prev.pack(fill= tk.BOTH, side=tk.LEFT)



nextf = tk.Button(root, text='Next', font=10, width=20, height=2)
nextf.config(command= lambda: slide(1), justify='left')
nextf.pack(fill=tk.BOTH, side=tk.LEFT)

exit_button = tk.Button(root)
exit_button.config(text='Exit', bg='white', fg='#123456', font=('monospace', 20, 'bold', 'italic'))
exit_button.config(command= lambda: root.quit(), height=2)
exit_button.pack(fill=tk.X, expand=tk.YES)



slide(0)

root.mainloop()
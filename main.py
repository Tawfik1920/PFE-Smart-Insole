from tkinter import * 
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from PIL import ImageTk,Image  
import csv
import matplotlib.pyplot as plt


Tab=[]
T=[]
C1=[]
C2=[]
C3=[]
C4=[]
C5=[]
C6=[]
C7=[]
C8=[]
LMFI=[]
Zone2=[]
Zone3=[]
def Traiter():
    nomF=str(entryNom.get())
    with open (nomF,'r') as file: #ouvrir le fichier csv 
        obj = csv.reader(file, delimiter=';') #créer un objet csv à partir du fichier
        for ligne in obj:
            if ligne != []:
                Tab.append(ligne)
        for i in range(0,len(Tab)):
            T.append(int(Tab[i][0]))
            C1.append(int(Tab[i][1]))
            C2.append(int(Tab[i][2]))
            C3.append(int(Tab[i][3]))
            C4.append(int(Tab[i][4]))
            C5.append(int(Tab[i][5]))
            C6.append(int(Tab[i][6]))
            C7.append(int(Tab[i][7]))
            C8.append(int(Tab[i][8])) 
            LMFI.append((int(Tab[i][1])+int(Tab[i][2])+int(Tab[i][8])+int(Tab[i][7]))/(int(Tab[i][4])+int(Tab[i][5])+int(Tab[i][6])+int(Tab[i][7])))
            Zone3.append(int(Tab[i][2])+int(Tab[i][3])+int(Tab[i][4]))
            Zone2.append(int(Tab[i][5])+int(Tab[i][6]))
    return None
import tkinter as tk

def convert_kohm_to_newton(resistance):
    # Relation linéaire entre résistance et force
    # Remplacez les valeurs de pente et d'ordonnée à l'origine par les valeurs appropriées
    slope = 0.5
    intercept = 10
    
    force = slope * resistance + intercept
    return force

def convert_button_click():
    # Obtenir les valeurs de force converties
    force_values = [convert_kohm_to_newton(resistance) for resistance in C1]
    
    # Afficher les valeurs de force converties
    for force in force_values:
        print(force)

# Créer une fenêtre tkinter


# Créer un bouton "Convertir" qui appelle la fonction convert_button_click lorsque cliqué

# Afficher la fenêtre




def Tracer1(): 
    Traiter()
    window = Tk() 
    window.title('La courbe du SENSOR 1') 
    window.geometry("750x750") 
    
    fig = Figure(figsize=(10, 6), dpi=100)
    plot1 = fig.add_subplot(111)
    plot1.plot(T, C1)
    
    plot1.set_xlabel('Time (ms)')
    plot1.set_ylabel('Resistance value (K OHM)')
    plot1.set_title('Force vs. Time')

    canvas = FigureCanvasTkAgg(fig, master=window)   
    canvas.draw() 
    canvas.get_tk_widget().pack() 
    toolbar = NavigationToolbar2Tk(canvas, window) 
    toolbar.update() 
    canvas.get_tk_widget().pack() 
  
    window.mainloop() 
    return None
    
def Tracer2(): 
    Traiter()
    window = Tk() 
    window.title('La courbe du SENSOR 2') 
    window.geometry("750x750") 
    
    fig = Figure(figsize=(10, 6), dpi=100)
    plot1 = fig.add_subplot(111)
    plot1.plot(T, C2)
    
    plot1.set_xlabel('Time (ms)')
    plot1.set_ylabel('Resistance value (K OHM)')
    plot1.set_title('Force vs. Time')

    canvas = FigureCanvasTkAgg(fig, master=window)   
    canvas.draw() 
    canvas.get_tk_widget().pack() 
    toolbar = NavigationToolbar2Tk(canvas, window) 
    toolbar.update() 
    canvas.get_tk_widget().pack() 
  
    window.mainloop() 
    return None
    
def Tracer3(): 
    Traiter()
    window = Tk() 
    window.title('La courbe du SENSOR 3') 
    window.geometry("750x750") 
    
    fig = Figure(figsize=(10, 6), dpi=100)
    plot1 = fig.add_subplot(111)
    plot1.plot(T, C3)
    
    plot1.set_xlabel('Time (ms)')
    plot1.set_ylabel('Resistance value (K OHM)')
    plot1.set_title('Force vs. Time')

    canvas = FigureCanvasTkAgg(fig, master=window)   
    canvas.draw() 
    canvas.get_tk_widget().pack() 
    toolbar = NavigationToolbar2Tk(canvas, window) 
    toolbar.update() 
    canvas.get_tk_widget().pack() 
  
    window.mainloop() 
    return None
    
def Tracer4(): 
    Traiter()
    window = Tk() 
    window.title('La courbe du SENSOR 4') 
    window.geometry("750x750") 
    
    fig = Figure(figsize=(10, 6), dpi=100)
    plot1 = fig.add_subplot(111)
    plot1.plot(T, C4)
    
    plot1.set_xlabel('Time (ms)')
    plot1.set_ylabel('Resistance value (K OHM)')
    plot1.set_title('Force vs. Time')

    canvas = FigureCanvasTkAgg(fig, master=window)   
    canvas.draw() 
    canvas.get_tk_widget().pack() 
    toolbar = NavigationToolbar2Tk(canvas, window) 
    toolbar.update() 
    canvas.get_tk_widget().pack() 
  
    window.mainloop() 
    return None
    
def Tracer5():
    Traiter()
    window = Tk() 
    window.title('La courbe du SENSOR 5') 
    window.geometry("750x750") 
    
    fig = Figure(figsize=(10, 6), dpi=100)
    plot1 = fig.add_subplot(111)
    plot1.plot(T, C5)
    
    plot1.set_xlabel('Time (ms)')
    plot1.set_ylabel('Resistance value (K OHM)')
    plot1.set_title('Force vs. Time')

    canvas = FigureCanvasTkAgg(fig, master=window)   
    canvas.draw() 
    canvas.get_tk_widget().pack() 
    toolbar = NavigationToolbar2Tk(canvas, window) 
    toolbar.update() 
    canvas.get_tk_widget().pack() 
  
    window.mainloop() 
    return None
    
def Tracer6():
    Traiter()
    window = Tk() 
    window.title('La courbe du SENSOR 6') 
    window.geometry("750x750") 
    
    fig = Figure(figsize=(10, 6), dpi=100)
    plot1 = fig.add_subplot(111)
    plot1.plot(T, C6)
    
    plot1.set_xlabel('Time (ms)')
    plot1.set_ylabel('Resistance value (K OHM)')
    plot1.set_title('Force vs. Time')

    canvas = FigureCanvasTkAgg(fig, master=window)   
    canvas.draw() 
    canvas.get_tk_widget().pack() 
    toolbar = NavigationToolbar2Tk(canvas, window) 
    toolbar.update() 
    canvas.get_tk_widget().pack() 
  
    window.mainloop() 
    return None
    
def Tracer7(): 
    Traiter()
    window = Tk() 
    window.title('La courbe du SENSOR 7') 
    window.geometry("750x750") 
    
    fig = Figure(figsize=(10, 6), dpi=100)
    plot1 = fig.add_subplot(111)
    plot1.plot(T, C7)
    
    plot1.set_xlabel('Time (ms)')
    plot1.set_ylabel('Resistance value (K OHM)')
    plot1.set_title('Force vs. Time')

    canvas = FigureCanvasTkAgg(fig, master=window)   
    canvas.draw() 
    canvas.get_tk_widget().pack() 
    toolbar = NavigationToolbar2Tk(canvas, window) 
    toolbar.update() 
    canvas.get_tk_widget().pack() 
  
    window.mainloop() 
    return None
    
def Tracer8(): 
    Traiter()
    window = Tk() 
    window.title('La courbe du SENSOR 8') 
    window.geometry("750x750") 
    
    fig = Figure(figsize=(10, 6), dpi=100)
    plot1 = fig.add_subplot(111)
    plot1.plot(T, C8)
    
    plot1.set_xlabel('Time (ms)')
    plot1.set_ylabel('Resistance value (K OHM)')
    plot1.set_title('Force vs. Time')

    canvas = FigureCanvasTkAgg(fig, master=window)   
    canvas.draw() 
    canvas.get_tk_widget().pack() 
    toolbar = NavigationToolbar2Tk(canvas, window) 
    toolbar.update() 
    canvas.get_tk_widget().pack() 
  
    window.mainloop() 
    return None

def Tracer9(): 
    Traiter()
    window = Tk() 
    window.title('La courbe dse la zone articulations métatarso-phalangiennes') 
    window.geometry("500x500") 
    
    fig = Figure(figsize = (5, 5), dpi = 100)
    plot1 = fig.add_subplot(111)
    plot1.plot(T,Zone2)
    plot1.set_title('Force vs. Time')
    
    
    canvas = FigureCanvasTkAgg(fig,master = window)   
    canvas.draw() 
    canvas.get_tk_widget().pack() 
    toolbar = NavigationToolbar2Tk(canvas, window) 
    toolbar.update() 
    canvas.get_tk_widget().pack() 
  
    window.mainloop() 
    return None

def Tracer10(): 
    Traiter()
    window = Tk() 
    window.title('La courbe  de la base du 5eme métatarsien') 
    window.geometry("500x500") 
    
    fig = Figure(figsize = (5, 5), dpi = 100)
    plot1 = fig.add_subplot(111)
    plot1.plot(T,Zone3)
    plot1.set_title('Force vs. Time')
    
    canvas = FigureCanvasTkAgg(fig,master = window)   
    canvas.draw() 
    canvas.get_tk_widget().pack() 
    toolbar = NavigationToolbar2Tk(canvas, window) 
    toolbar.update() 
    canvas.get_tk_widget().pack() 
  
    window.mainloop() 
    return None
    
def Tracer11():
    Traiter()
    window = Tk()
    window.title('La courbe du LMFI')
    window.geometry("500x500")

    fig = Figure(figsize=(5, 5), dpi=100)
    plot1 = fig.add_subplot(111)
    plot1.plot(T, LMFI)

    plot1.set_xlabel('Time (ms)')
    plot1.set_ylabel('LMFI')
    plot1.set_title('Force vs. Time')

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    canvas.get_tk_widget().pack()

    window.mainloop()
    return None

    
def Tracer_Tous():
    Traiter()
    window = Tk()
    window.title('Toutes Les courbes')
    window.geometry("500x500")

    fig = Figure(figsize=(5, 5), dpi=100)
    plot1 = fig.add_subplot(111)
    plot1.plot(T, C1, label='SENSOR 1')
    plot1.plot(T, C2, label='SENSOR 2')
    plot1.plot(T, C3, label='SENSOR 3')
    plot1.plot(T, C4, label='SENSOR 4')
    plot1.plot(T, C5, label='SENSOR 5')
    plot1.plot(T, C6, label='SENSOR 6')
    plot1.plot(T, C7, label='SENSOR 7')
    plot1.plot(T, C8, label='SENSOR 8')
    plot1.set_title('Force vs. Time')
    plot1.legend()

    plot1.set_xlabel('Time (ms)')
    plot1.set_ylabel('Resistance value (K OHM)')

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    canvas.get_tk_widget().pack()

    window.mainloop()
    return None


        
    
main = Tk()
main.geometry("600x500+450+500")
main.title("SMART INSOLE")


# Chemin vers votre image
image_path = r"c:\Users\tawfik aj\Downloads\immagine-copertina5.jpeg"


# Chargement de l'image
image = Image.open(image_path)
# Récupération des dimensions de l'écran
screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()

# Redimensionnement de l'image pour couvrir l'écran tout en conservant les proportions
image_width, image_height = image.size
aspect_ratio = image_width / image_height

# Calcul de la taille de l'image pour couvrir l'écran
if screen_width / screen_height > aspect_ratio:
    # L'écran est plus large que l'image
    new_width = int(screen_height * aspect_ratio)
    new_height = screen_height
else:
    # L'écran est plus haut que l'image
    new_width = screen_width
    new_height = int(screen_width / aspect_ratio)
# Redimensionnement de l'image pour s'adapter à la fenêtre principale
resized_image = image.resize((600, 500), Image.ANTIALIAS)
# Conversion de l'image en format compatible avec Tkinter
tk_image = ImageTk.PhotoImage(resized_image)

# Création d'un widget Label pour afficher l'image de fond
background_label = Label(main, image=tk_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Vous pouvez ajouter d'autres widgets et éléments à votre fenêtre ici

#main['bg']='Grey'

lblnom=Label(main,text="Enter the file name :")
lblnom.place(x=200,y=70)
entryNom=Entry(main)
entryNom.place(x=350,y=70)

can=Canvas(main, width=90,height=90,bg="white")
can.pack()
img = ImageTk.PhotoImage(Image.open(r"c:\Users\tawfik aj\Desktop\Smart Car Logo.png").resize((100,100),Image.ANTIALIAS))  

can.create_image(5,5,anchor=NW,image=img)
can.place(x=22,y=22)

black_rgba = (0, 0, 0, 0.5)
black_hex= main.cget('bg')

button1 = Button(master = main,  command =Tracer2, height = 2,  width = 10, text = "FSR1",bg=
black_hex, fg="black")
button1.place(x=115, y=200) 
button1.configure(fg="black", bd=6, highlightthickness=0, highlightbackground=
black_hex, highlightcolor=
black_hex)

button2 = Button(master = main,  command =Tracer2, height = 2,  width = 10, text = "FSR2",bg=
black_hex, fg="black") 
button2.configure(fg="black", bd=6, highlightthickness=0, highlightbackground=
black_hex, highlightcolor=
black_hex)
button2.place(x=215, y=200) 

button3 = Button(master = main,  command =Tracer3, height = 2,  width = 10, text = "FSR3",bg=
black_hex, fg="black") 
button3.configure(fg="black", bd=6, highlightthickness=0, highlightbackground=
black_hex, highlightcolor=
black_hex)
button3.place(x=315, y=200) 

button4 = Button(master = main,  command =Tracer4, height = 2,  width = 10, text = "FSR4",bg=
black_hex, fg="black") 
button4.configure(fg="black", bd=6, highlightthickness=0, highlightbackground=
black_hex, highlightcolor=
black_hex)
button4.place(x=415, y=200) 

button5 = Button(master = main,  command =Tracer5, height = 2,  width = 10, text = "FSR5",bg=
black_hex, fg="black") 
button5.configure(fg="black", bd=6, highlightthickness=0, highlightbackground=
black_hex, highlightcolor=
black_hex)
button5.place(x=115, y=250) 

button6 = Button(master = main,  command =Tracer6, height = 2,  width = 10, text = "FSR6",bg=
black_hex, fg="black") 
button6.configure(fg="black", bd=6, highlightthickness=0, highlightbackground=
black_hex, highlightcolor=
black_hex)
button6.place(x=215, y=250) 

button7 = Button(master = main,  command =Tracer7, height = 2,  width = 10, text = "FSR7",bg=
black_hex, fg="black") 
button7.configure(fg="black", bd=6, highlightthickness=0, highlightbackground=
black_hex, highlightcolor=
black_hex)
button7.place(x=315, y=250) 

button8 = Button(master = main,  command =Tracer8, height = 2,  width = 10, text = "FSR8",bg=
black_hex, fg="black") 
button8.configure(fg="black", bd=6, highlightthickness=0, highlightbackground=
black_hex, highlightcolor=
black_hex)
button8.place(x=415, y=250) 

button9 = Button(master=main, command=Tracer_Tous, height=2, width=20, text="Draw all the curves", bg=
black_hex, fg="black")
button9.configure(fg="black", bd=6, highlightthickness=20, highlightbackground=
black_hex, highlightcolor=
black_hex)
button9.place(x=200, y=200)

button9.place(x=220, y=350) 

button10 = Button(master = main,  command =Tracer9, height = 2,  width = 10, text = "Zone1",bg=
black_hex, fg="black")
button10.configure(fg="black", bd=6, highlightthickness=0, highlightbackground="black", highlightcolor="black")
button10.place(x=150, y=300) 

button11 = Button(master = main,  command =Tracer10, height = 2,  width = 10, text = "Zone2",bg=
black_hex, fg="black")
button11.configure(fg="black", bd=6, highlightthickness=0, highlightbackground="black", highlightcolor="black")
button11.place(x=250, y=300)

button12 = Button(master = main,  command =Tracer11, height = 2,  width = 10, text = "LMFI",bg=
black_hex, fg="black")
button12.configure(fg="black", bd=2, highlightthickness=0, highlightbackground="black", highlightcolor="black")
button12.place(x=350, y=300) 


main.mainloop()
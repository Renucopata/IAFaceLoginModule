from tkinter import *
import os
import cv2
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
import numpy as np


    
    
def registro_facial():
  
    cap = cv2.VideoCapture(0)
    while(True):
        ret,frame = cap.read()             
        cv2.imshow('Registro Facial',frame)
        if cv2.waitKey(1) == 32: 
            break
    usuario_img = usuario.get()
    cv2.imwrite(usuario_img+".jpg",frame) 
    cap.release()                               
    cv2.destroyAllWindows()

    usuario_entrada.delete(0, END)

    Label(pantalla1, text = "Registro Facial Exitoso", fg = "green", font = ("Calibri",11)).pack()


    
    def reg_rostro(img, lista_resultados):
        data = pyplot.imread(img)
        for i in range(len(lista_resultados)):
            x1,y1,ancho, alto = lista_resultados[i]['box']
            x2,y2 = x1 + ancho, y1 + alto
            pyplot.subplot(1, len(lista_resultados), i+1)
            pyplot.axis('off')
            cara_reg = data[y1:y2, x1:x2]
            cara_reg = cv2.resize(cara_reg,(150,200), interpolation = cv2.INTER_CUBIC)
            cv2.imwrite(usuario_img+".jpg",cara_reg)
            pyplot.imshow(data[y1:y2, x1:x2])
        pyplot.show()

    img = usuario_img+".jpg"
    pixeles = pyplot.imread(img)
    detector = MTCNN()
    caras = detector.detect_faces(pixeles)
    reg_rostro(img, caras)   
    

def registro():
    global usuario

    global usuario_entrada

    global pantalla1
    pantalla1 = Toplevel(pantalla)
    pantalla1.title("Registro")
    pantalla1.geometry("800x500")
    
 
    
    usuario = StringVar()

    
    Label(pantalla1, text = "Debe asignar un nombre usuario:").pack()
    

    Label(pantalla1, text = "").pack()  
    Label(pantalla1, text = "Nombre de Usuario").pack()  
    usuario_entrada = Entry(pantalla1, textvariable = usuario)
    usuario_entrada.pack()
  
    Label(pantalla1, text = "").pack() 

    Label(pantalla1, text = "").pack()
    Button(pantalla1, text = "Registro Facial", width = 15, height = 1, command = registro_facial).pack()


    

    

def login_facial():

    cap = cv2.VideoCapture(0)
    while(True):
        ret,frame = cap.read() 
        cv2.imshow('Login Facial',frame) 
        if cv2.waitKey(1) == 32:
            break
    usuario_login = verificacion_usuario.get() 
    cv2.imwrite(usuario_login+"LOG.jpg",frame)   
    cap.release()                               
    cv2.destroyAllWindows()

    usuario_entrada2.delete(0, END)
 

  
    
    def log_rostro(img, lista_resultados):
        data = pyplot.imread(img)
        for i in range(len(lista_resultados)):
            x1,y1,ancho, alto = lista_resultados[i]['box']
            x2,y2 = x1 + ancho, y1 + alto
            pyplot.subplot(1, len(lista_resultados), i+1)
            pyplot.axis('off')
            cara_reg = data[y1:y2, x1:x2]
            cara_reg = cv2.resize(cara_reg,(150,200), interpolation = cv2.INTER_CUBIC) #Guardamos la imagen 150x200
            cv2.imwrite(usuario_login+"LOG.jpg",cara_reg)
            return pyplot.imshow(data[y1:y2, x1:x2])
        pyplot.show()

 
    
    img = usuario_login+"LOG.jpg"
    pixeles = pyplot.imread(img)
    detector = MTCNN()
    caras = detector.detect_faces(pixeles)
    log_rostro(img, caras)


    def orb_sim(img1,img2):
        orb = cv2.ORB_create()
 
        kpa, descr_a = orb.detectAndCompute(img1, None) 
        kpb, descr_b = orb.detectAndCompute(img2, None)  

        comp = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True) 

        matches = comp.match(descr_a, descr_b)  

        regiones_similares = [i for i in matches if i.distance < 70] 
        if len(matches) == 0:
            return 0
        return len(regiones_similares)/len(matches)  
        

    
    im_archivos = os.listdir()  
    if usuario_login+".jpg" in im_archivos:  
        rostro_reg = cv2.imread(usuario_login+".jpg",0)   
        rostro_log = cv2.imread(usuario_login+"LOG.jpg",0)  
        similitud = orb_sim(rostro_reg, rostro_log)
        if similitud >= 0.90:   #tolerancia de similitud
            Label(pantalla2, text = "Inicio de Sesion Exitoso", fg = "green", font = ("Calibri",11)).pack()
            print("Bienvenido al sistema: ",usuario_login)
            print("Compatibilidad con la foto del registro: ",similitud)
        else:
            print("Rostro incorrecto, vuelva a intentarlo")
            print("Compatibilidad con la foto del registro: ",similitud)
            Label(pantalla2, text = "Incompatibilidad de rostros", fg = "red", font = ("Calibri",11)).pack()
    else:
        print("Usuario no encontrado")
        Label(pantalla2, text = "Usuario no encontrado", fg = "red", font = ("Calibri",11)).pack()
            


        
def login():
    global pantalla2
    global verificacion_usuario
    
    global usuario_entrada2
  
    
    pantalla2 = Toplevel(pantalla)
    pantalla2.title("Login")
    pantalla2.geometry("500x500")
    Label(pantalla2, text = "Ingrese su usuario:").pack()

    Label(pantalla2, text = "").pack()
    
    verificacion_usuario = StringVar()

    
 
    Label(pantalla2, text = "Nombre de usuario").pack()
    usuario_entrada2 = Entry(pantalla2, textvariable = verificacion_usuario)
    usuario_entrada2.pack()
    
    Label(pantalla2, text = "").pack()
   


    Label(pantalla2, text = "").pack()
    Button(pantalla2, text = "Inicio de Sesion Facial", width = 20, height = 1, command = login_facial).pack()
        

    
def pantalla_principal():
    global pantalla
    pantalla = Tk()
    pantalla.geometry("600x600")
    pantalla.title("Modulo de autenticacion facial")
    Label(text = "Login Page", bg = "gray", width = "300", height = "2", font = ("Verdana", 13)).pack()
    

    
    Label(text = "").pack()
    Button(text = "Iniciar Sesion", height = "2", width = "30", command = login).pack()
    Label(text = "").pack()
    Button(text = "Registro", height = "2", width = "30", command = registro).pack()

    pantalla.mainloop()

pantalla_principal()
from math import sin, cos, sqrt
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import numpy 
from PIL import Image
global esqdir
global cimabaixo
global aux1
global aux2
global b_colision
global angulo
global liga_ventilador
global bol1
global bol2
global luz_acesa
luz_acesa = False
b_colision = False
esqdir = 0
cimabaixo = 0
aux1 = 0
aux2 = 0
bol1 = 0
bol2 = 0
bolscale=1
angulo = 30
liga_ventilador = 0
camera_mode = 0  # 0 para a câmera padrão, 1 para a câmera parede, 2 para a câmera bola

def eixos():
    glColor3f(.9, .1, .1)
    glPushMatrix()
    glRotatef(90, 0.0, 1.0, 0.0)
    glTranslate(0.0, 0.0, -2.0)
    glutSolidCylinder(0.01, 4.0, 4, 10)
    glPopMatrix()

    glColor3f(.1, .1, .9)
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)
    glTranslate(0.0, 0.0, -2.0)
    glutSolidCylinder(0.01, 4.0, 4, 10)
    glPopMatrix()

    glColor3f(.1, .9, .1)
    glPushMatrix()
    glTranslate(0.0, 0.0, -2.0)
    glutSolidCylinder(0.01, 4.0, 4, 10)
    glPopMatrix()

def pisotextura():
    #glColor3f(0.7, 0.7, 0.7) # cor RGB
    glPushMatrix()
    glTranslate( 0.0, 0.0, 0.0)  #Transtacao do objeto
    # Textured 
    #tex = load_texture('xadrez.jpg')  
   # glEnable(GL_TEXTURE_2D)
    #glBindTexture(GL_TEXTURE_2D, tex)
    
    glBegin(GL_POLYGON)
    #gluCylinder(textura, largura da base, largura do topo, altura, resolucao , resolucao)
    glTexCoord2f (0.0, 0.0);
    glVertex3f(4.0, 0.0, -4.0)

    glTexCoord2f (3.0, 0.0);
    glVertex3f(4.0, 0.0, 4.0)

    glTexCoord2f (3.0, 3.0);
    glVertex3f(-4.0, 0.0, 4.0)

    glTexCoord2f (0.0, 3.0);
    glVertex3f(-4.0, 0.0, -4.0)
    glEnd()


    glDisable(GL_TEXTURE_2D)   
    glPopMatrix()
def mao():

    #Base dda mão
    glColor3f(1.0, 1.0, 0.0)  # Cor branco
    glPushMatrix()
    glTranslate(0, 3, -0.4)
    glScale(1.5,0.5,2.5)
    glutSolidCube(0.5)
    glPopMatrix()

    #Dedo 1
    glColor3f(1.0, 0.0, 0.0)  # Cor branco
    glPushMatrix()
    glTranslate(-0.55, 3, -0.0)
    glScale(3.5,1,1)
    glutSolidCube(0.2)
    glPopMatrix()

    #Dedo 2
    glColor3f(1.0, 0.5, 0.0)  # Cor branco
    glPushMatrix()
    glTranslate(-0.55, 3, -0.3)
    glScale(4.5,1,1)
    glutSolidCube(0.2)
    glPopMatrix()

    
    #Dedo 3
    glColor3f(0.5, 0.0, 0.0)  # Cor branco
    glPushMatrix()
    glTranslate(-0.55, 3, -0.6)
    glScale(4,1,1)
    glutSolidCube(0.2)
    glPopMatrix()

    #Dedo 4
    glColor3f(0.5, 0.0, 0.0)  # Cor branco
    glPushMatrix()
    glTranslate(-0.55, 3, -0.9)
    glScale(1.5,1,1)
    glutSolidCube(0.2)
    glPopMatrix()

    #Dedo 5
    glColor3f(1.0, 0.0, 0.0)  # Cor branco
    glPushMatrix()
    glTranslate(-0.55, 3, -0.0)
    glScale(3.5,1,1)
    glRotate(90,0,1,0)
    glutSolidCube(0.2)
    glPopMatrix()


def desenho():
    #eixos()
    
    
    pisotextura()
    mao()
    # OBJ BOLA
    glColor3f(0.5, 0.5, 0.5)  # Cor cinza
    glPushMatrix()
    # Variaveis globais que vão estar movimentando a bola
    glTranslate(bol2, bol1, -0.4)
    glScale(bolscale,1,bolscale)
    glutSolidSphere(0.2, 20, 20)
    glPopMatrix()

def load_texture(filename):
    img = Image.open(filename)
    img_data = numpy.array(list(img.getdata()), numpy.int8)
    textID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textID)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)    #  Opcao para Truncar a figura
    #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)      
   # glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)   #  Opcao para repetir a figura
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    #glTexEnvf(GL_TEXTURE_ENV,GL_TEXTURE_ENV_MODE,GL_REPLACE)
    #glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    #glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_SPOT_DIRECTIONAL)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
    return textID


def luz_fixa():
    luzAmbiente = [0.2, 0.2, 0.2, 1.0]
    luzDifusa = [0.7, 0.7, 0.7, 1.0]
    luzEspecular = [1.0, 1.0, 1.0, 1.0]
    posicaoLuz = [0.0, 50.0, 50.0, 1.0]
    especularidade = [1.0, 1.0, 1.0, 1.0]
    especMaterial = 60

    glShadeModel(GL_SMOOTH)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, especularidade)
    glMateriali(GL_FRONT, GL_SHININESS, especMaterial)

    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luzAmbiente)
    glLightfv(GL_LIGHT1, GL_AMBIENT, luzAmbiente)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, luzDifusa)
    glLightfv(GL_LIGHT1, GL_SPECULAR, luzEspecular)
    glLightfv(GL_LIGHT1, GL_POSITION, posicaoLuz)

def luz_acionavel():
    
    global aux1
    global luz_acesa

    luzAmbiente = [0.2, 0.2, 0.2, 1.0]
    luzDifusa = [1.0, 1.0, 0.0, 1.0] 
    luzEspecular = [1.0, 1.0, 1.0, 1.0]
    posicaoLuz = [aux1, 50.0, 50.0, 1.0]
    especularidade = [1.0, 1.0, 1.0, 1.0]
    especMaterial = 60

    glShadeModel(GL_SMOOTH)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, especularidade)
    glMateriali(GL_FRONT, GL_SHININESS, especMaterial)

    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luzAmbiente)
    glLightfv(GL_LIGHT0, GL_AMBIENT, luzAmbiente)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luzDifusa)
    glLightfv(GL_LIGHT0, GL_SPECULAR, luzEspecular)

    if luz_acesa:
        glEnable(GL_LIGHT0)
    else:
        glDisable(GL_LIGHT0)

    glLightfv(GL_LIGHT0, GL_POSITION, posicaoLuz)
    glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, 30.0)  # Ângulo de corte
    glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, [0.0, -1.0, 0.0])  # Direção do holofote
    glLightf(GL_LIGHT0, GL_SPOT_EXPONENT, 2.0) 

def iluminacao_da_cena():
    luz_fixa()
    luz_acionavel()
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT1)
    glEnable(GL_DEPTH_TEST)


def troca_camera():
    global camera_mode
    if camera_mode == 0:
        gluLookAt(sin(esqdir) * 10, 0 + cimabaixo, cos(esqdir) * 10, aux1, aux2, 0, 0, 1, 0)
       # gluLookAt(0, 8, 8, aux1, aux2, 0, 0, 1, 0)
    elif camera_mode == 1:
        gluLookAt(0, 3, 3, bol2, bol1, -0.4, 0, 1, 0)
    elif camera_mode == 2:
        gluLookAt(bol2, bol1, 2, bol2, bol1, -0.4, 0, 1, 0)


def tela():
    global angulo

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(angulo, 1, 0.1, 500)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    troca_camera()
    iluminacao_da_cena()
    glEnable(GL_DEPTH_TEST)

    desenho()
    glFlush()
    glutSwapBuffers()

# Aqui vai acontecer a mudanção (quando chegar nas coordenadas predefinidas, ou quando colidir
def update(value):
    global bol1
    global bol2
    global b_colision
    global bolscale

    if b_colision == False and bol1 > 0:
        
        
        if bol1 <=2.0:
            bol1 -=0.05
        else:
            bol1 -=0.04 

         #   Colocar a escala, para achatar a bola
       
        
        if bol1 <=0.55:
            bolscale = 1.0
        if bol1 <=0.5:
            bolscale = 1.25
        if bol1 <=0.4:
            bolscale = 1.50
        if bol1 <=0.3:
            bolscale = 1.75
        if bol1 <=0.2:
            bolscale = 2.0

        if bol1 <= 0:
            b_colision = True
            
   
        

    else:
        
       

        
        if bol1 < 1.0:       
            bol1 += 0.09
        if bol1 <=2.0:  
            bol1 +=0.05
        else:
            bol1 +=0.04

    
        if bol1 <=0.55:
            bol1 += 0.09
            bolscale = 1.0
        if bol1 <=0.5:
            bol1 += 0.09
            bolscale = 1.25
        if bol1 <=0.4:
            bol1 += 0.02
            bolscale = 1.50
        if bol1 <=0.3:
            bol1 += 0.01
            bolscale = 1.75
        if bol1 <=0.2:
            bol1 += 0.01
            bolscale = 2.0

        if bol1 >= 2.5:
            b_colision = False

        

    glutPostRedisplay()
    glutTimerFunc(16, update, 0)


def Teclado(tecla, x, y):
    global aux1
    global aux2
    global liga_ventilador
    global camera_mode
    global luz_acesa

    print("*** Tratamento de teclas comuns")
    print(">>> Tecla: ", tecla)

    if tecla == chr(27):
        sys.exit(0)

    if tecla == b'a':
        aux1 = aux1 - 0.1
        print("aux1 = ", aux1)

    if tecla == b'd':
        aux1 = aux1 + 0.1
        print("aux1 = ", aux1)

    if tecla == b'w':
        aux2 = aux2 + 0.1
        print("aux2 = ", aux2)

    if tecla == b's':
        aux2 = aux2 - 0.1
        print("aux2 = ", aux2)

    if tecla == b'z':
        luz_acesa = not luz_acesa
        print("Pressionou o interruptor do ventilador")

    if tecla == b'1':
        camera_mode = 0
        print("Modo de câmera padrão")

    if tecla == b'2':
        camera_mode = 1
        print("Modo de câmera parede")

    if tecla == b'3':
        camera_mode = 2
        print("Modo de câmera bola")

    tela()
    glutPostRedisplay()


def TeclasEspeciais(tecla, x, y):
    global esqdir
    global cimabaixo

    if tecla == GLUT_KEY_LEFT:
        esqdir = esqdir - 0.1
    elif tecla == GLUT_KEY_RIGHT:
        esqdir = esqdir + 0.1
    elif tecla == GLUT_KEY_UP:
        cimabaixo = cimabaixo + 0.1
    elif tecla == GLUT_KEY_DOWN:
        cimabaixo = cimabaixo - 0.1

    tela()
    glutPostRedisplay()


def ControleMouse(button, state, x, y):
    global angulo
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if angulo >= 10:
            angulo -= 2

    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        if angulo <= 130:
            angulo += 2
    tela()
    glutPostRedisplay()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(800, 600)
glutCreateWindow(b"Ambiente Virtual")

glutDisplayFunc(tela)
glutMouseFunc(ControleMouse)
glutKeyboardFunc(Teclado)
glutSpecialFunc(TeclasEspeciais)
glutTimerFunc(25, update, 0)

glutMainLoop()

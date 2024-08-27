import pyautogui as bt
import time

def localization():
          time.sleep(6)
          coordenadas = bt.position()
          time.sleep(5)
          return print(coordenadas)
#Point(x=1351, y=382) coordenadas da barra de pesquisa , Point(x=627, y=421)
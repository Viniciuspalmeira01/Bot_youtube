import time 
import pyautogui as bt

#acessar o google , e ir até um canal e assistir o seu vídeo várias vezes
#Como realizar? Por meio de funções

class Bot_Youtube:
      def __init__(self,link,minutagem, contagem, titulo) -> None:
                  self.link = link #nome do canal , ou link para acessá-lo
                  self.minutagem = int(minutagem) #Quantos minutos tem o seu video.
                  self.contador = int(contagem) #quantas vezes será executado a função reiniciar
                  self.titulo = str(titulo) #título do vídeo a ser assistido
                  pass
      def abrir_navegador(self): 
              bt.press('win')
              time.sleep(3)
              bt.write('brave', interval=3.0)
              bt.press('enter',interval=2.5)
              pass
      def pesquisar_youtube(self):#Após abrir o google
              bt.moveTo(x=595, y=55)#mover em direção a barra de pesquisa
              bt.click(x=595, y=55, interval=3.0)#clica na barra
              bt.write(self.link, interval=0.75)#escreve o que é pra ser pesquisado
              time.sleep(3)
              bt.press('enter')#enter na pesquisa
              pass
      def acessar_canal(self):
              bt.click( x=688, y=110)
              bt.write(self.titulo, interval=1.25)
              bt.press('enter')
              bt.scroll(clicks=1.0 , x=1351, y=382 )


      def reiniciar(self, n =int()):
              #botão de reiniciar : Point(x=82, y=56)
              for x in range(n):
                    bt.click(x = 82 , y = 56 )
        
      def main(self):
              bt.alert("O código vai começar. Não utilize nada do computador até o código finalizar!")
              self.abrir_navegador()
              time.sleep(4)
              self.pesquisar_youtube()
              time.sleep(3)
              self.acessar_canal()
              time.sleep(self.minutagem)
              self.reiniciar(n = self.contador)
              pass
bot = Bot_Youtube(link = 'Youtube',minutagem=194, contagem=5,titulo='Por que Echic')
bot.main()

#bt.moveTo(x=688, y=110) #reais coordenadas x=688, y=110 para a barra do yt ,x=595, y=55 para a do navegador 
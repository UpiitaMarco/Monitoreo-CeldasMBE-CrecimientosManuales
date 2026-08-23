# Función que imprime la portada del programa.

# Librería necesaria:
import os

# Códigos de color ANSI para la terminal
class Color:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def Portada():
    # La terminal se tiene que limpiar para que los caracteres aparezcan con colores:
    os.system('cls' if os.name == 'nt' else 'clear')
    # Logo del CINVESTAV usando una imagen PNG y la herramienta "Image to ASCII Art" de https://www.asciiart.eu/image-to-ascii
    # Texto en ASCII usando la fuente "Future"
    # de https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type+Something+&x=none&v=4&h=4&w=80&we=false
    # Texto en ASCII usando la fuente "Short" y el filtro "Sleek"
    # de https://patorjk.com/software/taag/#p=display&f=Short&t=para%20Crecimientos%20Manuales%20en%20el%20Laboratorio%20MBE&x=sleek
    print(Color.CYAN + Color.BOLD + "")
    print("""
                                        ---++++=++++===---                               
                                       :@+%@@@@@@@@@@@@#=*-                                  
                                        @%:            :=@                                   
                                         ::=%@@    @@@*:..                                   
                               =+##@# :=#%@%: -.   :  #@@%+- -%#++=:                         
                              ==+#@ -++*@  @%=##@@@*=#%  .@*+-.#@+-=-                        
                             *==%= #*-@@:    ::+. #+:    :*@@=*  @+-=.                       
                            *==+#   @@=.-%.-#@@=   *@@+-@+..%@#  =#==*                       
                           .#-=#      ++@@@@          #@#@*=      @+-=+                      
                           #==+#     =-+                  %-+      #-=*                      
                           @:--  @%@+%:@@-:             %-@--+@%%+ @--+                      
                           @+:::.-=--@@#%*=             *-@@@+===: ::+@                      
                            @@@@@@-=.    @=            -=@    +=*@@@@@                       
                                 =#--  : -@@.         #@@ :. .=+#                            
                                  #-+*@@%::  :=-. .-=  :-=@@@+=+                             
                                 ---@@@-:+@@@*::#%@@@@=:-%@@@-:=@@#--                          
                              #%-::  @@    *@@#%  %#@@@.   -@# ::=*%                         
                               @%--:.     *-. .:   :  .+      :==+@                          
                                -@*==-:   +@@@***#**#@@@   .-=*+@@                           
                                  -@%=---.   :%*+%*@+    -=+**@@                             
                                     @@@*==-:-*    .*:-==+%@@.                               
                                        %@@@@@      @@@@@@

                                        
=====================================================================================================
                      ┏┳┓┏━┓┏┓╻╻╺┳╸┏━┓┏━┓┏━╸┏━┓   ╺┳┓┏━╸   ┏━╸┏━╸╻  ╺┳┓┏━┓┏━┓
                      ┃┃┃┃ ┃┃┗┫┃ ┃ ┃ ┃┣┳┛┣╸ ┃ ┃    ┃┃┣╸    ┃  ┣╸ ┃   ┃┃┣━┫┗━┓
                      ╹ ╹┗━┛╹ ╹╹ ╹ ┗━┛╹┗╸┗━╸┗━┛   ╺┻┛┗━╸   ┗━╸┗━╸┗━╸╺┻┛╹ ╹┗━┛

          ╱`   _  _.,_ . _ ,_│─   _  │╲╱│  ,_    │ _  _   _ ,_   _ │  │   │       │─    .    │╲╱││)[~
│)(││`(│  ╲,│`(╱_(_│││││(╱_│││_()_╲  │  │(│││L│(││(╱__╲  (╱_││  (╱_│  │_(││)()│`(││_()│`│()  │  ││)[_
│                                                                                                    
=====================================================================================================
    """)
    print("" + Color.RESET)

# Entorno de pruebas con la función:    
if __name__ == '__main__':
    Portada()
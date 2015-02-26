# ACAGAM

V 1.0

Edison Javier Herran Cortes - ejherran.c@ŋmail.com

Implementación académica del algoritmo ElGamal sobre lenguaje Python 2.x


== Descripción ==

Esta pieza de código permite emular el conocido algoritmo de cifrado ElGamal (http://es.wikipedia.org/wiki/Cifrado_ElGamal); cifrando byte a byte un fichero mediante espacios de claves definidos por números primos de cuatro dígitos.

Su propósito es meramente académico, ya que el cifrado byte a byte y el uso de cálculos exponenciales uno a uno de números de cuatro dígitos genera una ralentización desmedida del algoritmo, esto sumado al hecho de que la presente implementación solo puede operar sobre ficheros de texto plano, hacen de la misma una solución por completo inútil en casos de aplicación real.


== Contenido ==

+> acagam.py: Punto de inicio de la ejecución, lee y escribe los ficheros objetivos.


+> basico: Modulo de funciones básicas para la implementación.

+----> primos.py: Contiene una lista iterable con todos los números primos de cuatro dígitos.

+----> tipos.py: Modulo de funciones útiles para convertir a formato hexadecimal y decimal.

+----> barra.py: Modulo que permite dibujar una barra de progreso (meramente cosmético).


+> algoritmo: Modulo general del algoritmo ElGamal.

+----> elgamal.py: Modulo que realiza las funciones matemáticas necesarias para generar la claves, cifrar y descifrar mediante el algoritmo ElGamal.

== Uso ==

Use los siguientes comandos:

        python acagam.py -genkey                                #Generar una clave
        python acagam.py -key [PUBLIC_KEY] -enc [ARCHIVO].txt   #Cifrar un archivo txt.
        python acagam.py -key [PRIVATE_KEY] -des [ARCHIVO].hex  #Descifrar un archivo hex.

ACAGAM cifra archivos de texto plano (txt) y genera archivos hexadecimales (hex). Descifra en sentido contrario (hex -> txt).

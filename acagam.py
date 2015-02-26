#!/usr/bin/env python
# -*- coding: utf-8 -*-

from basico.tipos import toHex
from basico.tipos import toInt
from basico.primos import PRIMOS
from basico.barra import BarraProgreso
import algoritmo.elgamal as eg

import random
import sys

def genKeys():
    
    p = PRIMOS[ random.randint( 0, len(PRIMOS)-1 ) ]
    key = eg.genKeys(p)
    
    return key

def descomponeKeys(k):
    q = []
    
    while len(k) > 0:
        q.append( k[0:4] )
        k = k[4:]
    
    i = 0
    while i < len(q):
        q[i] = int(q[i], 16)
        i += 1
    
    return q

def cifrar(path, key):
    
    barra = BarraProgreso('Cifrando', 50, '#', '-')
    
    fichero = open(path, 'r')
    original = fichero.read()
    fichero.close()
    
    key = descomponeKeys(key)
    
    p = key[0]
    g = key[1]
    b = eg.getSal(p)
    A = key[2:]
    
    base = eg.getBase(p, g, b)
    cifrado = eg.toHex(base, 4)
    
    e = 0
    lim = len(original)
    
    i = 0
    for c in original:
        
        m = ord(c)
        cifrado += eg.toHex( eg.getDeterminante(p, g, b, A[i], m), 4 )
        
        i += 1
        if i == 16:
            i = 0
        
        e += 1
        barra.actualizarBarra( ((1.0 * e) / lim)*100 )
    
    fichero = open(path+'.hex', 'w')
    fichero.write(cifrado)
    fichero.close()
    
    print "\tOK... Fichero cifrado: "+path+".hex\n"

def descifrar(path, key):
    
    barra = BarraProgreso('Descifrando', 50, '#', '-')
    
    fichero = open(path, 'r')
    cifrado = fichero.read()
    fichero.close()
    
    key = descomponeKeys(key)
    
    p = key[0]
    a = key[1:]
    
    base = toInt(cifrado[0:4])
    cifrado = cifrado[4:]
    
    original = ''
    
    lim = len(cifrado)
    
    i = 0
    while len(cifrado) > 0:
        determinante = toInt(cifrado[0:4])
        cifrado = cifrado[4:]
        original += chr( eg.getOrigen(p, base, determinante, a[i]) )
        
        i += 1
        if i == 16:
            i = 0
        
        barra.actualizarBarra( 100 - (1.0 * len(cifrado) / lim) * 100 )
        
    fichero = open(path+'.txt', 'w')
    fichero.write(original)
    fichero.close()
    
    print "\tOK... Fichero descifrado: "+path+".txt\n"

def msgUsage():
    
    msg =  "\nUse los siguientes comandos:\n\n"
    msg += "\tpython acagam.py -genkey\t\t\t\t#Generar una clave\n"
    msg += "\tpython acagam.py -key [PUBLIC_KEY] -enc [ARCHIVO].txt\t#Cifrar un archivo txt.\n"
    msg += "\tpython acagam.py -key [PRIVATE_KEY] -des [ARCHIVO].hex\t#Descifrar un archivo hex.\n"
    msg += "\nACAGAM cifra archivos de texto plano (txt) y genera archivos hexadecimales (hex). Descifra en sentido contrario (hex -> txt).\n"
    print msg


def main():
    
    argv = sys.argv
    argc = len(argv)
    
    if(argc == 1):
        msgUsage()
    
    elif argv[1] == '-genkey':
        PAP = genKeys()
        print '\n\tPRIVATE KEY:\t' + PAP[0]
        print '\tPUBLIC  KEY:\t' + PAP[1] + '\n'
    
    elif argc == 5 and argv[3] == '-enc':
        cifrar(argv[4], argv[2])
        pass
    
    elif argc == 5 and argv[3] == '-des':
        descifrar(argv[4], argv[2])
        pass
    
    else:
        print "\n\tACAGAM: Comando incorrecto!\n", argc, argv
    
    return 0

if __name__ == '__main__':
	main()

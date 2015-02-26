#!/usr/bin/env python
# -*- coding: utf-8 -*-

from basico.tipos import toHex
import random

def genKeys(p):
    
    g = random.randint(2, p-1)
    
    ak = []
    Ak = []
    
    for i in range(16): 
        
        a = random.randint(2, p-1)
        A = int ( (g ** a) % p )
        
        ak.append( toHex(a, 4) )
        Ak.append( toHex(A, 4) )
        
    q = toHex(p, 4) + ''.join(ak)
    Q = toHex(p, 4) + toHex(g, 4) + ''.join(Ak)
    
    return (q, Q)

def getSal(p):
    return int( random.randint(2, p-1) )

def getBase(p, g, b):
    return  int( (g ** b) % p )

def getDeterminante(p, g, b, A, m):
    return int( ( (A**b)*m ) % p )

def getOrigen(p, base, determinante, a):
    return int( ( ( base ** (p-1-a) ) * determinante ) % p )

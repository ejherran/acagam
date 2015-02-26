#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time

class BarraProgreso:
        
    def __init__ (self, titulo, longitud, completado, vacio):
        
        self.titulo = titulo
        self.longitud = longitud
        self.completado = completado
        self.vacio = vacio
        self.progreso = 0
       
        sys.stdout.write("\n\t" + self.titulo + ": [" + self.vacio * self.longitud + "]" + chr(8) * (self.longitud + 1) )
        sys.stdout.flush()
               
    def actualizarBarra(self, x):
        
        bloques = int(x) * self.longitud / 100
        sys.stdout.write( self.completado * (bloques - self.progreso) )
        
        if x == 100:
            sys.stdout.write("\n\n")
        
        sys.stdout.flush()
        self.progreso = bloques

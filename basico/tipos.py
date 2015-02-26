#!/usr/bin/env python
# -*- coding: utf-8 -*-

def toInt(h):
    return int(h, 16)

def toHex(dec, zc):
    bh = hex(dec).split('x')[1].upper()
    bh = bh.replace('L', '')
    return ( '0' * ( zc - len(bh) ) ) + bh 

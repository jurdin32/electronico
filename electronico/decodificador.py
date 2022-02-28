#!/usr/bin/python
#-*- coding: utf-8 -*-

import os, sys

archivo=open('/mnt/07EBF45679F193CD/var/www/electronico/media/firmado/2802202201070388669700110010010000001890000000013.xml','r')
lineas=''
for l in archivo.readlines():
    lineas+=str(l)
print(lineas)
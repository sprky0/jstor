#!/usr/bin/python
import subprocess, urllib, random
class NoBlocks(Exception): pass
def getblocks():
r = urllib.urlopen("http://{?REDACTED?}/grab").read()
if '<html' in r.lower(): raise NoBlocks
return r.split()

import sys
if len(sys.argv) > 1:
  prefix = ['--socks5', sys.argv[1]]
else
  prefix = ['']

line = lambda x: ['curl'] + prefix + ['-H', "Cookie: TENACIOUS=" + str(random.random())[3:], '-o', 'pdfs/' + str(x) + '.pdf', "http://www.jstor.org/stable/pdfplus/" + str(x) + ".pdf?acceptTC=true"]

while 1:
blocks = getblocks()
for block in blocks:
  print block
  subprocess.Popen(line(block)).wait()
  
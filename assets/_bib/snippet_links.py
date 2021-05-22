#-*- coding: utf-8 -*-

import sys

refs = dict()

htmlname = sys.argv[1]
mdname = sys.argv[2]

with open('{}'.format(htmlname), 'r') as f:
  RAW = f.read()

with open('{}'.format(mdname), 'r') as f:
  for l in f:
    line = l.strip()
    if '<a name=' in line:
      cod = line.split('"')[1]
      num = line.split('</a>')[0].split('>')[-1]
      refs[cod] = num

with open('{}'.format(mdname.replace('.md', '.html')), 'w') as g:
  for key in refs:
    RAW = RAW.replace('@{}'.format(key), "<a href='#{}'>{}</a>".format(key, refs[key]))
  g.write(RAW)

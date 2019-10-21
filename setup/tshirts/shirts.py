#!/usr/bin/env python3


"""
mens	large	heather purple
mens	small	heather seafoam
womens	medium	Heather Purple
womens	medium	berry
mens 	medium 	heather coral silk
womens	Small	Kiwi
mens	large	Graphite Heather
mens	large	sport grey
"""

shirts = {}
with open("shirts.txt","r") as file_object: 
  for line in file_object:
    line = line.rstrip()
    [style, size, color] = line.split("\t")
    style = style.lower()
    size = size.lower()
    color = color.lower()
    if style not in shirts:
        shirts[style] = {}
    if size not in shirts[style]:
        shirts[style][size] = {}
    if color not in shirts[style][size]:
        shirts[style][size][color] = 0

    shirts[style][size][color] += 1

for style in shirts:
  for size in shirts[style]:
    for color in shirts[style][size]:
      count = shirts[style][size][color]
      print(style,size,color,count,sep="\t")


print(shirts)

#!/usr/bin/python
from os import listdir, makedirs
from os.path import isfile, join, splitext, exists
from shutil import copy2

# parse arguments

# open mapping file

actions_map={}
animation_map={}
application_map={}
category_map={}
device_map={}
emblem_map={}
international_map={}
mime_map={}
place_map={}
status_map={}

with open('mapping.csv', 'r') as f:
  for line in f:
    data = line.split('\t')
    if data[1] != '' :
        if data[2] == 'action':
            actions_map[data[0]]=data[1]
        elif data[2] == 'animation':
            animation_map[data[0]]=data[1]
        elif data[2] == 'application':
            application_map[data[0]]=data[1]
        elif data[2] == 'category':
            category_map[data[0]]=data[1]
        elif data[2] == 'device':
            device_map[data[0]]=data[1]
        elif data[2] == 'emblem':
            emblem_map[data[0]]=data[1]
        elif data[2] == 'international':
            international_map[data[0]]=data[1]
        elif data[2] == 'mime':
            mime_map[data[0]]=data[1]
        elif data[2] == 'place':
            place_map[data[0]]=data[1]
        elif data[2] == 'status':
            status_map[data[0]]=data[1]

# generate theme file

if not exists('icons/QtFontAwsome'):
  makedirs('icons/QtFontAwsome')


theme_file = qrc = open('icons/QtFontAwsome/index.theme', 'w')
theme_file.write("""[Icon Theme]
Name=QtFontAwsome
Comment=Qt Bindings for Font Awsome v5.0.8

Directories=actions

[actions]
Context=Actions
Type=Scalable
""")
theme_file.close()

# generate Qt resource file

qrc = open('fa-resources.qrc', 'w')
qrc.write("<!DOCTYPE RCC>\n")
qrc.write("<RCC version=\"1.0\">\n")

qrc.write("<qresource prefix=\"icons/QtFontAwsome\">\n")
qrc.write('    <file>icons/QtFontAwsome/index.theme</file>\n')
# iterate over map, find FA file, set alias, write to file
# this piece of code, preferes regular icons to solid ones.

for directory in ["regular","solid","brands"]:
    for i in actions_map.keys():
        for filename in listdir(directory):
            if splitext(filename)[0] == actions_map[i] :
                if not exists('icons/QtFontAwsome/actions'):
                    makedirs('icons/QtFontAwsome/actions')
                # copy actual file to corresponding directory
                newFileName = 'icons/QtFontAwsome/actions/{}.svg'.format(i);
                copy2(join(directory, filename), newFileName)
                qrc.write('    <file alias="{}">{}</file>\n'.format(i,join('icons/QtFontAwsome/actions', filename)))
                # delete key from map to prevent duplicated icons between solid and regular
                del actions_map[i]
                break;

qrc.write("</qresource>\n")
qrc.write("</RCC>\n")
qrc.close()

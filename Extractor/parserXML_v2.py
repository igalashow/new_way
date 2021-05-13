import os
import zipfile
import glob
import xml.etree.ElementTree as ET
import shutil
from re import *

# Распаковали вложенные архивы, получили доступ к XML
for it in [1, 2]:
	for name in glob.glob('*.zip'):
		zip1 = zipfile.ZipFile(name)
		zip1.extractall()

# список файлов в папке
directory = os.listdir(path=".")  
# удаляем лишние файлы
for name in directory:
	if name.startswith('out_docs') or name.endswith('sig'):
		os.remove(name)

# берём XMLки из папки
for name in glob.glob('*.xml'):
	# парсим XML
	vypiska = ET.parse(name) 
	root = vypiska.getroot()

	for child in root[0]:
		# выявляем кадастровый номер
		kadnumber = (child.attrib['CadastralNumber'])
		# заменяем двоеточие
		new_kad = sub(":", "_", kadnumber)
		# переименовываем XMl по кад номеру
		os.rename(name, new_kad+".xml")


Давайте попробуем сэмулировать работу HEX-браузера – программы, которая показывает содержание любого файла в шестнадцатиричном удобном виде.

Ваша программа должна открывать в бинарном режиме файл data.txt и предоставлять удобный просмотр содержимого этого файла 

Формат ввода
Bill Gates: Sorry about Control-Alt-Delete  

Формат вывода
Если значение байта является символом, который имеет смысл при печати, то он должен выводиться в блоке справа как есть, в противном случае вместо него должен быть выведен символ «.»

Коды символов являются шестнадцатиричными числами.

Отступы сделаны пробелами по горизонтали и новой строкой по вертикали. Размер отступов должен быть как в образце, так что будьте внимательны. Линейки вверху и слева позволяют узнать позицию байта в файле.

          00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f  
 
000000    42 69 6c 6c 20 47 61 74 65 73 3a 20 53 6f 72 72     Bill Gates: Sorr  
000010    79 20 61 62 6f 75 74 20 43 6f 6e 74 72 6f 6c 2d     y about Control-  
000020    41 6c 74 2d 44 65 6c 65 74 65 0d 0a                 Alt-Delete..

Примечания
Ваша программа должна получать данные в бинарном формате из указанного в условии источника, выводить данные в указанный в условии приемник в текстовом формате.
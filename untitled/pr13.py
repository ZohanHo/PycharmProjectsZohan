fw = open('saple.txt', 'w') #используем файловый обьект fw, используем функцию open, назовем его saple.txt, w - говорит что в файле можно что то написать
fw.write('pizdec nachalnik\n') #используем файловый обьект и функцию write (запись) и в кавычках текст который хотим написать, и перенос на нову строку
fw.write('OMG') #дописуем еще текс
fw.close() #необходимо закрыть обьект



fr = open('saple.txt', 'r') #хомим прочиталь фаил
text = fr.read () #Еужно сохранить гдето инфу так как в питоне нельзя работать напрямую с файлом или папкой, нам нужна переменная
print (text) #выводим текст файла
fr.close #необходимо закрыть обьект
import re

pattern = r"zohan"

if re.match(pattern, "zohanIslifeforzohanboy" ):  #Ищит совпадения вначале
    print("Math")
else:
    print("noMath")


if re.search(pattern, "Islifeforzohanboy" ): #Ищит совпадения везде
    print("Math")
else:
    print("noMath")

print(re.findall(pattern, "zohanIslifeforzohanboyzohan" ))  #Возвращает все совпадения найденые в строке в список


import this
 
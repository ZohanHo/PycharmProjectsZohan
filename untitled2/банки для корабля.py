#def speceship_building(nedelya):
#    total_cans = 0
#    for week in range(1, 53):
#        total_cans = total_cans + nedelya
#        print ("Неделя", week, "банок:", total_cans)

#speceship_building(2)




def moon_weight(start_weight, pribavka_vesa, b):


    for week in int(b):
        start_weight += 1
        suma = start_weight * pribavka_vesa
        print("мой лунный вес", suma)

moon_weight(72, 0.25, 5)




#def
#moon_weight(ves):

#    for week in range(1, 15):
#    ves += 1
#    suma = ves * 0.0165
#    print("мой лунный вес", suma)

#moon_weight(72)

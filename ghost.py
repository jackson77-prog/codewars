one="_____"
two="_____"
three ="_____"
four = "_____"
five = "_____"
six = "_____"
seven = "_____"
eigth = "_____"
nine = "_____"
ten = "_____"
eleven = "_____"
twelve = "_____"

position = [one,two,three,four,five,six,seven,eigth,nine,ten,eleven,twelve]

Earthenware_1 = "QUTHCRDMZ"
Waterfall_4 ="WEVOXING"
Fireplace_7 ="JFABKPLY"
Windowsill_10 = "SSSSSSSSS"

the_deads = ['Yojne', 'Xenna', 'Verap', 'Ebyam', 'Teseb', 'Ycuag', 'Onets', 'Skcaw', 'Yrovi', 'Tpets', 'Lizuf', 'Girnu']

first_order = [0,11,1,10,2,9,3,8,4,7,5,6]
second_order = [3,2,4,1,5,0,6,11,7,10,8,9]
third_order = [6,5,7,4,8,3,9,2,10,1,11,0]
fourth_order = [9,8,10,7,11,6,0,5,1,4,2,3]

def order(position,the_dead):
    
    for i in Earthenware_1:
        for dead in the_deads:
            if(dead[0] == i):
                order_1(first_order,dead)

    for i in Waterfall_4:
        for dead in the_deads:
            if(dead[0] == i):
                order_2(second_order,dead)

    for i in Fireplace_7:
        for dead in the_deads:
            if(dead[0] == i):
                order_3(third_order,dead)

    for i in Windowsill_10:
        for dead in the_deads:
            if(dead[0] == i):
                order_4(fourth_order,dead)

def order_1(first_order,dead):
    for order in fourth_order:
        if(position[order] == "_____"):
            position[order] = dead
            break

def order_2(second_order,dead):
    for order in second_order:
        if(position[order] == "_____"):
            position[order] = dead
            break

def order_3(third_order,dead):
    for order in third_order:
        if(position[order] == "_____"):
            position[order] = dead
            break

def order_4(fourth_order,dead):
    for order in fourth_order:
        if(position[order] == "_____"):
            position[order] = dead
            break

order(position, the_deads)
print(position)
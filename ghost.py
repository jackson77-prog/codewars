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

def order(position,the_dead):
    
    for i in Earthenware_1:
        for dead in the_deads:
            if(dead[0] == i):
                if(position[0] == "_____"):
                    position[0] = dead
                elif(position[11] == "_____"):
                    position[11] = dead
                elif(position[1] == "_____"):
                    position[1] = dead

    for i in Waterfall_4:
        for dead in the_deads:
            if(dead[0] == i):
                if(position[3] == "_____"):
                    position[3] = dead
                elif(position[2] == "_____"):
                    position[2] = dead
                elif(position[4] == "_____"):
                    position[4] = dead

    for i in Fireplace_7:
        for dead in the_deads:
            if(dead[0] == i):
                if(position[6] == "_____"):
                    position[6] = dead
                elif(position[5] == "_____"):
                    position[5] = dead
                elif(position[7] == "_____"):
                    position[7] = dead

    for i in Windowsill_10:
        for dead in the_deads:
            if(dead[0] == i):
                if(position[9] == "_____"):
                    position[9] = dead
                elif(position[11] == "_____"):
                    position[11] = dead
                elif(position[8] == "_____"):
                    position[8] = dead

       

order(position, the_deads)
print(position)
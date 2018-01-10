def left_join(mas):
    #return ','.join([i.replace('right', 'left') for i in mas])
    return ','.join(mas).replace('right', 'left')
            
print(left_join(("left", "right", "left", "stop"))) # == "left,left,left,stop"
print(left_join(("bright aright", "ok"))) # == "bleft aleft,ok"
print(left_join(("brightness wright",))) # == "bleftness wleft"
print(left_join(("enough", "jokes"))) # == "enough,jokes"
    
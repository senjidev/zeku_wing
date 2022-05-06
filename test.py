run = True
speed = .2
def ramp(var):
    i = .0002
    while run:
        i += speed
        print(i)
        if i >= 4.8: #cap at 4.8 (this way its not more than 5 as it will always add the .2 while run is true) so players cant zoom too fast
            i = 4.8
            

ramp(speed)
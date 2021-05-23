# #This is a basic feedbackless bldc driver code
# #
import machine
import utime

AH = machine.Pin(4, machine.Pin.OUT)
AL = machine.Pin(12, machine.Pin.OUT)
BH = machine.Pin(13, machine.Pin.OUT)
BL = machine.Pin(22, machine.Pin.OUT)
CH = machine.Pin(21, machine.Pin.OUT)
CL = machine.Pin(20, machine.Pin.OUT)
led = machine.Pin(25, machine.Pin.OUT)
# These are the first pins that worked on my pico, but it has had a
# rough life, so I expect I killed those earlier pins
# 
decrease = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_DOWN)
increase = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_DOWN)
# enable = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)
# 
#The switch states for the 6 step positions
lst0 = [0, 0, 0, 1, 1, 0]
lst1 = [1, 0, 0, 1, 0, 0]
lst2 = [1, 0, 0, 0, 0, 1] 
lst3 = [0, 0, 1, 0, 0, 1]
lst4 = [0, 1, 1, 0, 0, 0]
lst5 = [0, 1, 0, 0, 1, 0]

lstzero = [0, 0, 0, 0, 0, 0]
lol = [lst0, lst1, lst2, lst3, lst4, lst5] #list of lists
lop = [AH, AL, BH, BL, CH, CL]
#Initally setting all pins to Zero
i = 0
for pin in lop:
    pin.value(0)
    i += 1
phase = 0
speed = 0.1 #initial speed

while True:
    #while enable == True: #An interupt would make more sense here, but this is easier to read
    while True:
        led.toggle()
        print("entered primary loop{0}".format(1))
        #set pins
        i = 0
        for pin in lop:
            pin.value(lol[phase][i])
            i += 1
        #increment phases    
        if phase < 5:
            phase = phase + 1
        else:
            phase = 0
            #at the end of every 6 steps check and see if we should
            #increase or decrease the delay between motor pulses
            ###increase in delay is decrease in speed###
            if increase.value() == 1:
                speed = speed * 1.1
            elif decrease.value() == 1:
                speed = speed*0.91
         
        utime.sleep(speed)
#         


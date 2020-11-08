from movement import *
import brickpi3 

straight=1 or 2 or 5 or 7 or 12 or 15 or 16 or 19
right=3 or 6 or 10 or 14 or 18 or 22 or 23 
left=4 or 8 or 11 or 13 or 20 or 21 or 24 or 
back=9 or 17 or 25 or 26 or 27
gapStart=28
gapFininsh=29
pid=30 or 31 or 32 or 33 


def learningmovement(num):
    if num==staright:
        straight(2,30)
    elif num==right:
        r90cor()
    elif num==left:
        l90cor()
    elif num==back:
        # 180度回転する
        back()
    elif num==gapStart:
        
    elif num==gapFinish:
        
    elif num==pid:
        
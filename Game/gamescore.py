'''It contains the functions to calculate batting score or bowling score of a player'''

# Contains Functions Here

def batscore(run,balls,four,six,field):
    score = 0
    
    strikerate=(run/balls)*100
    
    if strikerate>=80 and strikerate<=100 :
        score = score + 2
        
    elif strikerate>100 :
        score = score + 4

    score=score + run/2
    
    if run>=100:         # Additional 10 points for century
        score=score+10
    if run>=50:        # Additional 5 points for half century
        score=score+5
   
    score = score + four + (six*2) + (field*10)  
     
    return int(score)

def bowlscore(bowled,runs,wkts,field):
    score = 0
    score = score + (wkts*10) #10 points for every wkts
    
    if wkts>=5:           # Additional 10 points for 5 or more wkts
        score = score+15  
    if wkts==3:         # Additional 5 points for 3 wkts
        score = score+5
    
    overs = bowled/6    
    ecorate=runs/overs
    if ecorate>3.5 and ecorate<=4.5:
        score = score+4
    elif ecorate>2 and ecorate<=3.5:
        score = score+7
    elif ecorate<=2:
        score = score+10
        
    score = score + (field*10)  #10 points each for fielding
    
    return int(score)

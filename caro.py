mapslot= [' ',' ',' ',' ',' ',' ',' ',' ',' ','5']

turn = 0
last_turn = ''
while turn > -1:
    while turn > -1:
        for x in range(3):
            print(mapslot[x*3] + "|" + mapslot[x*3+1] + "|" + mapslot[x*3+2])
        location = input()  
        if(mapslot[int(location)-1] == ' '):
            if(turn % 2 == 0):
                mapslot[int(location)-1] = 'x'
                turn += 1
                last_turn = mapslot[int(location)-1]
                break
            
            else:
                mapslot[int(location)-1] = 'o'    
                turn += 1
                last_turn = mapslot[int(location)-1]
                break
    if(mapslot[0] != ' ' and mapslot[0] == mapslot[1] and mapslot[0] == mapslot[2] or mapslot[3] != ' ' and mapslot[3] == mapslot[4] and mapslot[3] == mapslot[5] or mapslot[6] != ' ' and mapslot[6] == mapslot[7] and mapslot[6] == mapslot[8] or mapslot[0] != ' ' and mapslot[0] == mapslot[3] and mapslot[0] == mapslot[6] or mapslot[1] != ' ' and mapslot[1] == mapslot[4] and mapslot[1] == mapslot[7] or mapslot[2] != ' ' and mapslot[2] == mapslot[5] and mapslot[2] == mapslot[8] or mapslot[0] != ' ' and mapslot[0] == mapslot[4] and mapslot[0] == mapslot[8] or mapslot[2] != ' ' and mapslot[2] == mapslot[4] and mapslot[2] == mapslot[6]):
      for x in range(3):
             print(mapslot[x*3] + "|" + mapslot[x*3+1] + "|" + mapslot[x*3+2])
      print("the winner is: " + last_turn)  
      break
    elif(mapslot[0] != ' ' and mapslot[1] != ' ' and mapslot[2] != ' ' and mapslot[3] != ' ' and mapslot[4] != ' ' and mapslot[5] != ' ' and mapslot[6] != ' ' and mapslot[7] != ' ' and mapslot[8] != ' '):
    	 for x in range(3):
             print(mapslot[x*3] + "|" + mapslot[x*3+1] + "|" + mapslot[x*3+2])
    	 print("match tie")
    	 break

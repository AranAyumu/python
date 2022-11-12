map_slot= [' ',' ',' ',' ',' ',' ',' ',' ',' ']

turn = 0
last_turn = ''
while turn > -1:
    while turn > -1:
        for x in range(3):
            print(map_slot[x*3] + "|" + map_slot[x*3+1] + "|" + map_slot[x*3+2])
        location = input()  
        if(map_slot[int(location)-1] == ' '):
            if(turn % 2 == 0):
                map_slot[int(location)-1] = 'x'
                turn += 1
                last_turn = map_slot[int(location)-1]
                break
            
            else:
                map_slot[int(location)-1] = 'o'    
                turn += 1
                last_turn = map_slot[int(location)-1]
                break
    if(map_slot[0] != ' ' and map_slot[0] == map_slot[1] and map_slot[0] == map_slot[2] or map_slot[3] != ' ' and map_slot[3] == map_slot[4] and map_slot[3] == map_slot[5] or map_slot[6] != ' ' and map_slot[6] == map_slot[7] and map_slot[6] == map_slot[8] or map_slot[0] != ' ' and map_slot[0] == map_slot[3] and map_slot[0] == map_slot[6] or map_slot[1] != ' ' and map_slot[1] == map_slot[4] and map_slot[1] == map_slot[7] or map_slot[2] != ' ' and map_slot[2] == map_slot[5] and map_slot[2] == map_slot[8] or map_slot[0] != ' ' and map_slot[0] == map_slot[4] and map_slot[0] == map_slot[8] or map_slot[2] != ' ' and map_slot[2] == map_slot[4] and map_slot[2] == map_slot[6]):
      for x in range(3):
             print(map_slot[x*3] + "|" + map_slot[x*3+1] + "|" + map_slot[x*3+2])
      print("the winner is: " + last_turn)  
      break
    elif(map_slot[0] != ' ' and map_slot[1] != ' ' and map_slot[2] != ' ' and map_slot[3] != ' ' and map_slot[4] != ' ' and map_slot[5] != ' ' and map_slot[6] != ' ' and map_slot[7] != ' ' and map_slot[8] != ' '):
    	 for x in range(3):
             print(map_slot[x*3] + "|" + map_slot[x*3+1] + "|" + map_slot[x*3+2])
    	 print("match tie")
    	 break

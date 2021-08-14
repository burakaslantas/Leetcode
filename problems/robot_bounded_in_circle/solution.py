class Solution:
    def isRobotBounded(self, instructions: str) -> bool:    
        """
        Solution #1
        directions = [ [0,1], [-1,0], [0,-1], [1,0] ] #[+y, -x, -y, +x]
        direction = 0
        location = [0,0]
        
        for instruction in instructions:
            print(direction)
            if(instruction == 'G'):
                for i in range(2):
                    location[i] += directions[direction % 4][i]
            elif(instruction == 'L'):
                direction += 1
            elif(instruction == 'R'):
                direction -= 1
                
        if(location == [0,0] or direction % 4 != 0):
            return True
        return False
        """
        

        #Solution #2
        moveX, moveY = 0, 1
        x, y = 0, 0
        for instruction in instructions:
            if(instruction == 'R'):
                moveX, moveY = moveY, -1 * moveX
            elif(instruction == 'L'):
                moveX, moveY = -1 * moveY, moveX
            else:
                x, y = x + moveX, y + moveY
                
        if( (x, y) == (0, 0) or (moveX, moveY) != (0, 1) ):
            return True
        return False
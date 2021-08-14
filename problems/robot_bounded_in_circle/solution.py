class Solution:
    def isRobotBounded(self, instructions: str) -> bool:    
        directions = [ [0,1], [-1,0], [0,-1], [1,0] ] #[+y, -x, -y, +x]
        direction = 0
        location = [0,0]
        circle = 0
        
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
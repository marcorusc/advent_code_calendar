
class Drive_sub():
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.aim = 0

    def get_pos(self):
        position = [self.x, self.y]
        return position

    def forward(self, pos):
        self.x = self.x + pos
        self.y = self.y + (self.aim * pos)

    def down(self, pos):
        self.aim = self.aim + pos
        
    def up(self, pos):
        self.aim = self.aim - pos
    
def main():

    sub = Drive_sub()
    sub2 = Drive_sub()
    with open("test", "r") as f:
            data_list = []
            for line in f.readlines():
                    line = line.rstrip(" ")
                    lines = line.split()
                    #print(lines)
                    if lines[0] == "forward":
                        sub2.forward(int(lines[1]))
                    if lines[0] == "up":
                        sub2.up(int(lines[1]))
                    if lines[0] == "down":
                        sub2.down(int(lines[1]))
    print(sub.get_pos())
    
    with open("day2_data", "r") as f:
            data_list = []
            for line in f.readlines():
                    line = line.rstrip(" ")
                    lines = line.split()
                    #print(lines)
                    if lines[0] == "forward":
                        sub.forward(int(lines[1]))
                    if lines[0] == "up":
                        sub.up(int(lines[1]))
                    if lines[0] == "down":
                        sub.down(int(lines[1]))
    print(sub2.get_pos())
    print(sub.get_pos())
    print(sub.get_pos()[0] * sub.get_pos()[1])
    
    return

if __name__ == "__main__":
    main()
		
	

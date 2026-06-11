class Fan:
    def __init__(self):
        self.speed = 0      # speed level from 0 to 3
        self.status = False # False for off, True for on
        self.swing = False   # False for no swing, True for swing
        self.MAX_SPEED = 5
    
    def turn_on(self):
        self.status = True
        self.swing = False
        self.speed = 1

        self.show()
    
    def turn_off(self):
        self.status = False
        self.swing = False
        self.speed = 0

        self.show()

    def speed_up(self):
        if self.status == False:
            print('Fan is off. Please turn it on first.')
            return
        if self.speed == self.MAX_SPEED:
            print('Fan is at maximum speed.')
            return
        
        self.speed += 1
        self.show()

    def speed_down(self):
        if self.status == False:
            print('Fan is off. Please turn it on first.')
            return
        if self.speed == 0:
            print('Fan is at minimum speed.')
            return
        
        self.speed -= 1
        self.show()

    def swing_toggle(self):
        if self.status == False:
            print('Fan is off. Please turn it on first.')
            return
        
        self.swing = not self.swing
        self.show()
    
    def show(self):
        swinging = 'swinging' if self.swing else 'stood still'
        
        print(f'Fan is {"on" if self.status else "off"}, speed: {self.speed}, {swinging}')
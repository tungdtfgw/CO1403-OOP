class Television:
    def __init__(self):
        self.channels = ["CNN", "BBC", "Fox News", "HBO", "ESPN", "VTV1", "VTV2", "VTV3"]
        self.current = 0    # current channel index
        self.volume = 5     # volume level from 0 to 10
        self.status = False # False for off, True for on
        self.MAX_VOLUME = 10

    
    def turn_on(self):
        self.status = True
        self.playing()
    
    def turn_off(self):
        self.status = False
        print('TV is turned off')

    def change_channel(self, n):
        # Check if TV is on
        if self.status == False:
            print('TV is off. Please turn it on first.')
            return
        # Check if channel number is valid
        if n < 0 or n >= len(self.channels):
            print('Invalid channel number. Please choose a number between 0 and', len(self.channels)-1)
            return
        
        # Validation passed, change channel
        self.current = n
        self.playing()

    def volume_up(self):
        # Check if TV is on
        if self.status == False:
            print('TV is off. Please turn it on first.')
            return
        # Check if volume is at max
        if self.volume == self.MAX_VOLUME:
            print('Volume is at maximum level.')
            return
        
        # Validation passed, increase volume
        self.volume += 1
        self.playing()

    def playing(self):
        print(f'TV is playing {self.channels[self.current]} at volume {self.volume}')

    def volume_down(self):
        # Check if TV is on
        if self.status == False:
            print('TV is off. Please turn it on first.')
            return
        # Check if volume is at minimum
        if self.volume == 0:
            print('Volume is at minimum level.')
            return
        
        # Validation passed, decrease volume
        self.volume -= 1
        self.playing()

    def mute(self):
        # Check if TV is on
        if self.status == False:
            print('TV is off. Please turn it on first.')
            return
        
        # Validation passed, mute volume
        self.volume = 0
        self.playing()

# Test the Television class
if __name__ == "__main__":
    tv = Television()
    tv.turn_on()
    tv.change_channel(2)
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    tv.mute()

    tv.turn_off()
    tv.change_channel(1)  # Should prompt to turn on TV first
    tv.mute()            # Should prompt to turn on TV first

    tv.turn_on()
    tv.change_channel(10) # Should prompt invalid channel number
    tv.volume_down()      # Should prompt volume is at minimum level if volume is already at 0
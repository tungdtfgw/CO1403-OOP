from television import Television
from fan import Fan

class Remote:
    def __init__(self, ctrl_obj):
        self.ctrl_obj = ctrl_obj

    def on(self):
        self.ctrl_obj.turn_on()

    def off(self):
        self.ctrl_obj.turn_off()
    
    def number(self, n):
        if type(self.ctrl_obj) == Television:
            self.ctrl_obj.change_channel(n)

    def up(self):
        if type(self.ctrl_obj) == Television:
            self.ctrl_obj.volume_up()
        elif type(self.ctrl_obj) == Fan:
            self.ctrl_obj.speed_up()

    def down(self):
        if type(self.ctrl_obj) == Television:
            self.ctrl_obj.volume_down()
        elif type(self.ctrl_obj) == Fan:
            self.ctrl_obj.speed_down()

    def mute(self):
        if type(self.ctrl_obj) == Television:
            self.ctrl_obj.mute()
        elif type(self.ctrl_obj) == Fan:
            self.ctrl_obj.swing_toggle()
    

# Test the Remote class
if __name__ == "__main__":
    tv = Television()
    remote = Remote(tv)
    remote.on()
    remote.number(2)
    remote.up()
    remote.mute()
    remote.down()
    remote.off()

    # Test the Remote class with Fan
    fan = Fan()
    remote.ctrl_obj = fan
    remote.on()
    remote.up()
    remote.up()
    remote.mute()
    remote.down()
    remote.off()
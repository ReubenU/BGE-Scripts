#   By Reuben Unicruz
#   License: MIT/BSD
#
#

from bge import *

class Input:
    def __init__(self, mouse_sens):
        self.mouse = logic.mouse
        
        self.mouse_sens = mouse_sens
        
        self.joysticks = logic.joysticks
        
        self.keyboard = logic.keyboard
        
        self.bound_axes = {
            "X" : [events.AKEY, events.DKEY],
            "Y" : [events.SKEY, events.WKEY],
            "Z" : [events.LEFTSHIFTKEY, events.SPACEKEY]
            }
        
    def mouse_movement(self):
        mouse_x, mouse_y = self.mouse.position
        
        width = render.getWindowWidth()
        height = render.getWindowHeight()
        
        move_x = ( (width//2) - (mouse_x * width) ) * self.mouse_sens
        move_y = ( (height//2) - (mouse_y * height) ) * self.mouse_sens
        
        render.setMousePosition(width//2, height//2)
        return (move_x, move_y)
        
    def axis_active(self, axis, status):
        active_keys = self.keyboard.events
        
        if ( active_keys[self.bound_axes[axis][0]] == status):
            return -1
        elif ( active_keys[self.bound_axes[axis][1]] == status):
            return 1
        else:
            return 0
    

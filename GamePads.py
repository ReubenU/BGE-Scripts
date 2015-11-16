#   By Reuben Unicruz
#   License: MIT/BSD
#
#   This script is WIP

from bge import logic
import ctypes


#### Special thanks to HG1
class XINPUT_VIBRATION(ctypes.Structure):
    _fields_ = [
        ("wLeftMotorSpeed", ctypes.c_ushort),
        ("wRightMotorSpeed", ctypes.c_ushort)
    ]

class GamePad:
    
    def __init__(self, gamepadNum, threshold):
        self.gamepad = logic.joysticks[gamepadNum]
        self.name = self.gamepad.name
        self.numAxis = self.gamepad.numAxis
        self.numButtons = self.gamepad.numButtons
        self.numHats = self.gamepad.numHats
        self.threshold = threshold
        
        self.xbox360_config = {
            'A' : 10,
            'B' : 11,
            'X' : 12,
            'Y' : 13,
            'Start' : 4,
            'Back' : 5,
            'LS' : 6,
            'RS' : 7,
            'LB' : 8,
            'RB' : 9,
            'Guide' : 14
        }
        
        self.dualshock2_config = {
            'X' : 2,
            'Square' : 3,
            'Triangle' : 0,
            'Circle' : 1,
            'L1' : 6,
            'L2' : 4,
            'R1' : 7,
            'R2' : 5
        }

    def axisValue(self, axis):
        value = self.gamepad.axisValues[axis]
        
        if (value >= self.threshold):
            return value
        elif (value <= -self.threshold):
            return value
        else:
            return 0.0
    
    def isButtonActive(self, button, mapPreset):
        if (mapPreset[button] in self.gamepad.activeButtons):
            return 1.0
        else:
            return 0.0
    
    def hatDirection(self):
        return self.gamepad.hatValues
    
    def vibrate(self, left, right):
        xinput = ctypes.windll.xinput1_1

        XInputSetState = xinput.XInputSetState
        XInputSetState.argtypes = [ctypes.c_uint, ctypes.POINTER(XINPUT_VIBRATION)]
        XInputSetState.restype = ctypes.c_uint
        
        vib = XINPUT_VIBRATION(left, right)
        XInputSetState(0, ctypes.byref(vib))
        

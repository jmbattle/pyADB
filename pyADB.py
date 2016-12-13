# -*- coding: utf-8 -*-
"""pyADB.py: Helper class for interacting with Android devices over ADB 

__author__ = "Jason M. Battle"
"""

####IMPORTS####################################################################

import re
import os
import time
import subprocess

####CONSTANTS##################################################################

KEYCODE_UNKNOWN = 0
KEYCODE_SOFT_LEFT = 1
KEYCODE_SOFT_RIGHT = 2
KEYCODE_HOME = 3
KEYCODE_BACK = 4
KEYCODE_CALL = 5
KEYCODE_ENDCALL = 6
KEYCODE_0 = 7
KEYCODE_1 = 8
KEYCODE_2 = 9
KEYCODE_3 = 10
KEYCODE_4 = 11
KEYCODE_5 = 12
KEYCODE_6 = 13
KEYCODE_7 = 14
KEYCODE_8 = 15
KEYCODE_9 = 16
KEYCODE_STAR = 17
KEYCODE_POUND = 18
KEYCODE_DPAD_UP = 19
KEYCODE_DPAD_DOWN = 20
KEYCODE_DPAD_LEFT = 21
KEYCODE_DPAD_RIGHT = 22
KEYCODE_DPAD_CENTER = 23
KEYCODE_DPAD_VOLUME_UP = 24
KEYCODE_DPAD_VOLUME_DOWN = 25
KEYCODE_POWER = 26 
KEYCODE_CAMERA = 27 
KEYCODE_CLEAR = 28
KEYCODE_A = 29 
KEYCODE_B = 30
KEYCODE_C = 31
KEYCODE_D = 32
KEYCODE_E = 33 
KEYCODE_F = 34 
KEYCODE_G = 35 
KEYCODE_H = 36 
KEYCODE_I = 37 
KEYCODE_J = 38 
KEYCODE_K = 39 
KEYCODE_L = 40
KEYCODE_M = 41
KEYCODE_N = 42
KEYCODE_O = 43
KEYCODE_P = 44
KEYCODE_Q = 45
KEYCODE_R = 46
KEYCODE_S = 47
KEYCODE_T = 48
KEYCODE_U = 49
KEYCODE_V = 50
KEYCODE_W = 51
KEYCODE_X = 52
KEYCODE_Y = 53
KEYCODE_Z = 54
KEYCODE_COMMA = 55
KEYCODE_PERIOD = 56
KEYCODE_ALT_LEFT = 57
KEYCODE_ALT_RIGHT = 58
KEYCODE_SHIFT_LEFT = 59
KEYCODE_SHIFT_RIGHT = 60
KEYCODE_TAB = 61
KEYCODE_SPACE = 62
KEYCODE_SYM = 63
KEYCODE_EXPLORER = 64
KEYCODE_ENVELOPE = 65
KEYCODE_ENTER = 66
KEYCODE_DEL = 67
KEYCODE_GRAVE = 68
KEYCODE_MINUS = 69
KEYCODE_EQUALS = 70
KEYCODE_LEFT_BRACKET = 71
KEYCODE_RIGHT_BRACKET = 72
KEYCODE_BACKSLASH = 73
KEYCODE_SEMICOLON = 74
KEYCODE_APOSTROPHE = 75
KEYCODE_SLASH = 76
KEYCODE_AT = 77
KEYCODE_NUM = 78
KEYCODE_HEADSETHOOK = 79
KEYCODE_FOCUS = 80
KEYCODE_PLUS = 81
KEYCODE_MENU = 82
KEYCODE_NOTIFICATION = 83
KEYCODE_SEARCH = 84
KEYCODE_MEDIA_PLAY_PAUSE = 85
KEYCODE_MEDIA_STOP = 86
KEYCODE_MEDIA_NEXT = 87
KEYCODE_MEDIA_PREVIOUS = 88
KEYCODE_MEDIA_REWIND = 89
KEYCODE_MEDIA_FAST_FORWARD = 90
KEYCODE_MUTE = 91
KEYCODE_PAGE_UP = 92
KEYCODE_PAGE_DOWN = 93
KEYCODE_PICTSYMBOLS = 94
KEYCODE_SWITCH_CHARSET = 95
KEYCODE_BUTTON_A = 96
KEYCODE_BUTTON_B = 97
KEYCODE_BUTTON_C = 98
KEYCODE_BUTTON_X = 99
KEYCODE_BUTTON_Y = 100
KEYCODE_BUTTON_Z = 101
KEYCODE_BUTTON_L1 = 102
KEYCODE_BUTTON_R1 = 103
KEYCODE_BUTTON_L2 = 104
KEYCODE_BUTTON_R2 = 105
KEYCODE_BUTTON_THUMBL = 106
KEYCODE_BUTTON_THUMBR = 107
KEYCODE_BUTTON_START = 108
KEYCODE_BUTTON_SELECT = 109
KEYCODE_BUTTON_MODE = 110
KEYCODE_ESCAPE = 111
KEYCODE_FORWARD_DEL = 112
KEYCODE_CTRL_LEFT = 113
KEYCODE_CTRL_RIGHT = 114
KEYCODE_BUTTON_CAPS_LOCK = 115
KEYCODE_BUTTON_SCROLL_LOCK = 116
KEYCODE_META_LEFT = 117
KEYCODE_META_RIGHT = 118
KEYCODE_FUNCTION = 119
KEYCODE_SYSRQ = 120
KEYCODE_BREAK = 121
KEYCODE_MOVE_HOME = 122
KEYCODE_MOVE_END = 123
KEYCODE_INSERT = 124
KEYCODE_FORWARD = 125
KEYCODE_MEDIA_PLAY = 126
KEYCODE_MEDIA_PAUSE = 127
KEYCODE_META_SHIFT_RIGHT_ON = 128
KEYCODE_MEDIA_EJECT = 129
KEYCODE_MEDIA_RECORD = 130
KEYCODE_F1 = 131
KEYCODE_F2 = 132
KEYCODE_F3 = 133
KEYCODE_F4 = 134
KEYCODE_F5 = 135
KEYCODE_F6 = 136
KEYCODE_F7 = 137
KEYCODE_F8 = 139
KEYCODE_F9 = 140
KEYCODE_F10 = 141
KEYCODE_F11 = 142
KEYCODE_F12 = 143
KEYCODE_NUM_LOCK = 144
KEYCODE_NUMPAD_0 = 145
KEYCODE_NUMPAD_1 = 146
KEYCODE_NUMPAD_2 = 147
KEYCODE_NUMPAD_3 = 148
KEYCODE_NUMPAD_4 = 149
KEYCODE_NUMPAD_5 = 150
KEYCODE_NUMPAD_6 = 151
KEYCODE_NUMPAD_7 = 152
KEYCODE_NUMPAD_8 = 153
KEYCODE_NUMPAD_9 = 154
KEYCODE_NUMPAD_DIVIDE = 155
KEYCODE_NUMPAD_MULTIPLY = 156
KEYCODE_NUMPAD_SUBTRACT = 157
KEYCODE_NUMPAD_ADD = 158
KEYCODE_NUMPAD_DOT = 159
KEYCODE_NUMPAD_ENTER = 160
KEYCODE_NUMPAD_EQUALS = 161
KEYCODE_NUMPAD_LEFT_PAREN = 162
KEYCODE_NUMPAD_RIGHT_PAREN = 163
KEYCODE_VOLUME_MUTE = 164
KEYCODE_INFO = 165
KEYCODE_CHANNEL_UP = 166
KEYCODE_CHANNEL_DOWN = 167
KEYCODE_ZOOM_IN = 168
KEYCODE_ZOOM_OUT = 169
KEYCODE_WAKEUP = 224

###############################################################################

class Client():
                             
    def __init__(self, path, device):
        if os.path.isdir(path):
            if 'adb.exe' in os.listdir(path):
                os.chdir(path)
                self.start()
                if device == re.findall(r'^.*\r\n(\w+)\s+.*model:(\w+).*', self.devices())[0][1]:
                    self.__id = re.findall(r'^.*\r\n(\w+)\s+.*model:(\w+).*', self.devices())[0][0]
                    print '%s device connection detected. Storing id %s for subsequent ADB communication.' % (device, self.__id)
                else:
                    raise DeviceError('Specified device not connected. Please try again.')
                    pass
            else:
                raise FileError('Unable to locate executable for Android Debug Bridge. Please try again.') 
                pass
        else:
            raise FilePathError('Passed string syntax is incorrect. Please try again.')
            pass

####ADB-GENERAL COMMANDS#######################################################
        
    def devices(self):
        return filter(None, subprocess.check_output('adb devices -l', shell=True).strip('\r\n\n'))    

    def start(self):
        subprocess.check_output('adb start-server', shell=True)

    def kill(self):
        subprocess.check_output('adb kill-server', shell=True)

    def push(self, src, dest):
        subprocess.check_output('adb -s %s push %s %s' % (self.__id, src, dest), shell=True)

    def pull(self, src, dest):
        subprocess.check_output('adb -s %s pull %s %s' % (self.__id, src, dest), shell=True)

####ADB-SHELL COMMANDS#########################################################

    def ls(self, path=None, show_all=False, show_size=False, show_recursive=False):
        if path == None:
            if show_all == False and show_size == False and show_recursive == False:
                return filter(None, subprocess.check_output('adb -s %s shell ls' % self.__id, shell=True).split('\r\r\n'))
            elif show_all == False and show_size == False and show_recursive == True:
                return filter(None, subprocess.check_output('adb -s %s shell ls -R' % self.__id, shell=True).split('\r\r\n'))
            elif show_all == False and show_size == True and show_recursive == False:
                return filter(None, subprocess.check_output('adb -s %s shell ls -s' % self.__id, shell=True).split('\r\r\n'))
            elif show_all == False and show_size == True and show_recursive == True:
                return filter(None, subprocess.check_output('adb -s %s shell ls -sR' % self.__id, shell=True).split('\r\r\n'))                
            elif show_all == True and show_size == False and show_recursive == False:
                return filter(None, subprocess.check_output('adb -s %s shell ls -a' % self.__id, shell=True).split('\r\r\n'))
            elif show_all == True and show_size == False and show_recursive == True:
                return filter(None, subprocess.check_output('adb -s %s shell ls -aR' % self.__id, shell=True).split('\r\r\n'))
            elif show_all == True and show_size == True and show_recursive == False:
                return filter(None, subprocess.check_output('adb -s %s shell ls -as' % self.__id, shell=True).split('\r\r\n'))                
            elif show_all == True and show_size == True and show_recursive == True:
                return filter(None, subprocess.check_output('adb -s %s shell ls -asR' % self.__id, shell=True).split('\r\r\n'))                
            else:
                raise ArgumentError('One or more arguments were passed unsupported values.')
                pass                
        else:
            if show_all == False and show_size == False and show_recursive == False:
                return filter(None, subprocess.check_output('adb -s %s shell ls %s' % (self.__id, path), shell=True).split('\r\r\n'))
            elif show_all == False and show_size == False and show_recursive == True:
                return filter(None, subprocess.check_output('adb -s %s shell ls -R %s' % (self.__id, path), shell=True).split('\r\r\n'))
            elif show_all == False and show_size == True and show_recursive == False:
                return filter(None, subprocess.check_output('adb -s %s shell ls -s %s' % (self.__id, path), shell=True).split('\r\r\n'))
            elif show_all == False and show_size == True and show_recursive == True:
                return filter(None, subprocess.check_output('adb -s %s shell ls -sR %s' % (self.__id, path), shell=True).split('\r\r\n'))                
            elif show_all == True and show_size == False and show_recursive == False:
                return filter(None, subprocess.check_output('adb -s %s shell ls -a %s' % (self.__id, path), shell=True).split('\r\r\n'))
            elif show_all == True and show_size == False and show_recursive == True:
                return filter(None, subprocess.check_output('adb -s %s shell ls -aR %s' % (self.__id, path), shell=True).split('\r\r\n'))
            elif show_all == True and show_size == True and show_recursive == False:
                return filter(None, subprocess.check_output('adb -s %s shell ls -as %s' % (self.__id, path), shell=True).split('\r\r\n'))                
            elif show_all == True and show_size == True and show_recursive == True:
                return filter(None, subprocess.check_output('adb -s %s shell ls -asR %s' % (self.__id, path), shell=True).split('\r\r\n'))                
            else:
                raise ArgumentError('One or more arguments were passed unsupported values.')
                pass                

    def pwd(self):
        return subprocess.check_output('adb -s %s shell pwd' % self.__id, shell=True).strip('\r\r\n')

    def cat(self, path):
        return subprocess.check_output('adb -s %s shell cat %s' % (self.__id, path), shell=True).strip('\r\r\n')

    def cd(self, path=None):
        if path == None:
            pass
        else:
            subprocess.check_output('adb -s %s shell cd %s' % (self.__id, path), shell=True)

    def mkdir(self, path=None, mode=None, recursive=False):
        if path == None:
            pass
        else:
            if mode == None:
                if recursive == False:
                    subprocess.check_output('adb -s %s shell mkdir -p %s' % (self.__id, path), shell=True)
                elif recursive == True:
                    subprocess.check_output('adb -s %s shell mkdir %s' % (self.__id, path), shell=True)                    
            elif mode.isdigit():
                if recursive == False:
                    subprocess.check_output('adb -s %s shell mkdir -m %s %s' % (self.__id, mode, path), shell=True)
                elif recursive == True:
                    subprocess.check_output('adb -s %s shell mkdir -mp %s %s' % (self.__id, mode, path), shell=True)         

    def rmdir(self, path=None):
        if path == None:
            pass
        else:
            subprocess.check_output('adb -s %s shell rm -d %s' % (self.__id, path), shell=True)

    def rm(self, path=None, prompt=False, recursive=False):
        if path == None:
            pass
        else:
            if prompt ==  False and recursive == False:
                subprocess.check_output('adb -s %s shell rm %s' % (self.__id, path), shell=True)
            elif prompt ==  False and recursive == True:
                subprocess.check_output('adb -s %s shell rm -r %s' % (self.__id, path), shell=True)
            elif prompt ==  True and recursive == False:
                subprocess.check_output('adb -s %s shell rm -i %s' % (self.__id, path), shell=True)
            elif prompt ==  True and recursive == True:
                subprocess.check_output('adb -s %s shell rm -ir %s' % (self.__id, path), shell=True)                
            else:
                raise ArgumentError('One or more arguments were passed unsupported values.')
                pass

    def cp(self, src, dest): # Not yet tested
        subprocess.check_output('adb -s %s shell cp %s %s' % (self.__id, src, dest), shell=True)

    def mv(self, src, dest): # Not yet tested
        subprocess.check_output('adb -s %s shell mv %s %s' % (self.__id, src, dest), shell=True)
            
    def touch(self, path): # Not yet tested
        subprocess.check_output('adb -s %s shell touch %s' % (self.__id, path), shell=True)

    def echo(self, text, fname): # Not yet tested
        subprocess.check_output('adb -s %s shell echo %s > %s' % (self.__id, text, fname), shell=True)

    def screencap(self):
        subprocess.check_output('adb -s %s shell screencap /storage/sdcard0/DCIM/Screenshots/screen.png' % self.__id, shell=True)

    def screenrecord(self, duration=None):
        if duration != None:
            subprocess.check_output('adb -s %s shell screenrecord --time-limit %i /storage/sdcard0/DCIM/Screenshots/screen.mp4' % (self.__id, duration), shell=True)
        else:
            subprocess.check_output('adb -s %s shell screenrecord /storage/sdcard0/DCIM/Screenshots/screen.mp4' % self.__id, shell=True)

    def dumpsys(self):
        self.__tmp = filter(None, subprocess.check_output('adb -s %s shell dumpsys battery' % self.__id, shell=True).split('\r\r\n'))
        self.__tmp = filter(lambda x : re.match(r'.+:.+', x), map(lambda x: x.replace(' ', ''), self.__tmp))        
        self.__dat = {}
        [self.__dat.update({line.split(':')[0]:line.split(':')[1]}) for line in self.__tmp]
        del self.__tmp
        return self.__dat        
 
    def listpackages(self, pattern=None):
        if pattern != None:
            return map(lambda x: x.replace('package:', ''), reduce(lambda x,y: x+y, filter(None, map(lambda x: re.findall(r'.*%s.*' % pattern, x), subprocess.check_output('adb -s %s shell pm list packages' % self.__id, shell=True).split('\r\r\n')))))
        else:            
            return map(lambda x: x.replace('package:', ''), filter(None, subprocess.check_output('adb -s %s shell pm list packages' % self.__id, shell=True).split('\r\r\n')))

    def monkey(self, eventcount, package=None):
        if package != None:
            subprocess.check_output('adb -s %s shell monkey -p %s %i' % (self.__id, package, eventcount), shell=True)                
        else:
            subprocess.check_output('adb -s %s shell monkey %i' % (self.__id, eventcount), shell=True)                

###EXPERIMENTAL COMMANDS######################################################## 

    def GetVoltage(self):
        return int(self.dumpsys()['voltage'])
        
    def GetCurrent(self):
        return int(self.dumpsys()['currentnow'])

    def GetTemperature(self):
        return int(self.dumpsys()['temperature'])

    def GetSOC(self):
        return int(self.dumpsys()['level'])

    def GetBatteryType(self):
        return self.dumpsys()['technology']
    
    def GetChargeSource(self):
        if self.dumpsys()['ACpowered'] == 'true':
            return 'AC Adapter Charging'
        elif self.dumpsys()['USBpowered'] == 'true':
            return 'USB Port Charging'
        elif self.dumpsys()['Wirelesspowered'] == 'true':
            return 'Wireless Charging'
        else:
            return 'Not Charging'

    def LaunchImage(self, fpath):
        self.Wake()
        subprocess.check_output('adb -s %s shell am start -a android.intent.action.VIEW -t image/* -d file:///%s' % (self.__id, fpath), shell=True)   
        self.TapEvent(280, 1670)

    def LaunchAudio(self, fpath):
        self.Wake()
        subprocess.check_output('adb -s %s shell am start -a android.intent.action.VIEW -t audio/* -d file:///%s' % (self.__id, fpath), shell=True) 
        self.TapEvent(280, 1670)

    def LaunchVideo(self, fpath):
        self.Wake()
        subprocess.check_output('adb -s %s shell am start -a android.intent.action.VIEW -t video/* -d file:///%s' % (self.__id, fpath), shell=True) 
        self.TapEvent(800, 1670)

    def LaunchDocument(self, fpath):
        self.Wake()
        subprocess.check_output('adb -s %s shell am start -a android.intent.action.VIEW -t text/* -d file:///%s' % (self.__id, fpath), shell=True) 
        self.TapEvent(280, 1670)

    def LaunchBrowser(self, url):
        self.Wake()
        subprocess.check_output('adb -s %s shell am start -a android.intent.action.VIEW -d %s' % (self.__id, url), shell=True)   
        self.TapEvent(280, 1670)

    def LaunchCamera(self):
        self.Wake()
        subprocess.check_output('adb -s %s shell am start -a android.media.action.IMAGE_CAPTURE' % (self.__id), shell=True)  
        self.KeyEvent(KEYCODE_FOCUS)         
        self.KeyEvent(KEYCODE_CAMERA)
        self.Wait(2)
        self.TapEvent(810, 85)

    def LaunchGmail(self, address, subject, body):
        self.Wake()
        subprocess.check_output('adb -s %s shell am start -n com.google.android.gm/.ComposeActivityGmail -d email:%s --es subject %s --es body %s' % (self.__id, address, subject, body), shell=True)
        self.TapEvent(880, 160)

    def LaunchYouTube(self, ID):
        self.Wake()
        subprocess.check_output('adb -s %s shell am start -n com.google.android.youtube/.UrlActivity -d %s' % (self.__id, ID), shell=True)  
        self.Play()

    def KeyEvent(self, eventcode):
        subprocess.check_output('adb -s %s shell input keyevent %i' % (self.__id, eventcode), shell=True) 

    def SwipeEvent(self, x1, x2, y1, y2):
        subprocess.check_output('adb -s %s shell input swipe %i %i %i %i' % (self.__id, x1, x2, y1, y2), shell=True) 

    def TapEvent(self, x, y):
        subprocess.check_output('adb -s %s shell input tap %i %i' % (self.__id, x , y), shell=True)

    def Play(self):
        self.KeyEvent(KEYCODE_MEDIA_PLAY)

    def Pause(self):
        self.KeyEvent(KEYCODE_MEDIA_PAUSE)
        
    def Stop(self):
        self.KeyEvent(KEYCODE_MEDIA_STOP)

    def Rewind(self):
        self.KeyEvent(KEYCODE_MEDIA_REWIND)

    def Fastforward(self):
        self.KeyEvent(KEYCODE_MEDIA_FAST_FORWARD)    

    def Next(self):
        self.KeyEvent(KEYCODE_MEDIA_NEXT)            
    
    def Previous(self):
        self.KeyEvent(KEYCODE_MEDIA_PREVIOUS)

    def VolumeUp(self):
        self.KeyEvent(KEYCODE_DPAD_VOLUME_UP)

    def VolumeDown(self):
        self.KeyEvent(KEYCODE_DPAD_VOLUME_DOWN)        

    def VolumeMute(self):
        self.KeyEvent(KEYCODE_VOLUME_MUTE)        

    def Wake(self):
        self.KeyEvent(KEYCODE_WAKEUP)
        self.SwipeEvent(0, 1000, 1000, 1000)        

    def Wait(self, duration):
        time.sleep(duration)          

    def Reboot(self):
        subprocess.check_output('adb -s %s shell reboot' % self.__id, shell=True)

    def KillAll(self):
        subprocess.check_output('adb -s %s shell am kill-all' % self.__id, shell=True) 

####EXCEPTIONS#################################################################

class ArgumentError(Exception):
    pass

class FilePathError(Exception):
    pass

class FileError(Exception):
    pass
        
class DeviceError(Exception):
    pass

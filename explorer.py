#! /usr/bin/env python3

import os
import sys
import time
import termios
import subprocess
import json

import libevdev


# list of keys from the kernel at keyboard driver
keys_list = [
    libevdev.EV_KEY.KEY_ESC,
    libevdev.EV_KEY.KEY_1,
    libevdev.EV_KEY.KEY_2,
    libevdev.EV_KEY.KEY_3,
    libevdev.EV_KEY.KEY_4,
    libevdev.EV_KEY.KEY_5,
    libevdev.EV_KEY.KEY_6,
    libevdev.EV_KEY.KEY_7,
    libevdev.EV_KEY.KEY_8,
    libevdev.EV_KEY.KEY_9,
    libevdev.EV_KEY.KEY_0,
    libevdev.EV_KEY.KEY_MINUS,
    libevdev.EV_KEY.KEY_EQUAL,
    libevdev.EV_KEY.KEY_BACKSPACE,
    libevdev.EV_KEY.KEY_TAB,
    libevdev.EV_KEY.KEY_Q,
    libevdev.EV_KEY.KEY_W,
    libevdev.EV_KEY.KEY_E,
    libevdev.EV_KEY.KEY_R,
    libevdev.EV_KEY.KEY_T,
    libevdev.EV_KEY.KEY_Y,
    libevdev.EV_KEY.KEY_U,
    libevdev.EV_KEY.KEY_I,
    libevdev.EV_KEY.KEY_O,
    libevdev.EV_KEY.KEY_P,
    libevdev.EV_KEY.KEY_LEFTBRACE,
    libevdev.EV_KEY.KEY_RIGHTBRACE,
    libevdev.EV_KEY.KEY_ENTER,
    libevdev.EV_KEY.KEY_LEFTCTRL,
    libevdev.EV_KEY.KEY_A,
    libevdev.EV_KEY.KEY_S,
    libevdev.EV_KEY.KEY_D,
    libevdev.EV_KEY.KEY_F,
    libevdev.EV_KEY.KEY_G,
    libevdev.EV_KEY.KEY_H,
    libevdev.EV_KEY.KEY_J,
    libevdev.EV_KEY.KEY_K,
    libevdev.EV_KEY.KEY_L,
    libevdev.EV_KEY.KEY_SEMICOLON,
    libevdev.EV_KEY.KEY_APOSTROPHE,
    libevdev.EV_KEY.KEY_GRAVE,
    libevdev.EV_KEY.KEY_LEFTSHIFT,
    libevdev.EV_KEY.KEY_BACKSLASH,
    libevdev.EV_KEY.KEY_Z,
    libevdev.EV_KEY.KEY_X,
    libevdev.EV_KEY.KEY_C,
    libevdev.EV_KEY.KEY_V,
    libevdev.EV_KEY.KEY_B,
    libevdev.EV_KEY.KEY_N,
    libevdev.EV_KEY.KEY_M,
    libevdev.EV_KEY.KEY_COMMA,
    libevdev.EV_KEY.KEY_DOT,
    libevdev.EV_KEY.KEY_SLASH,
    libevdev.EV_KEY.KEY_RIGHTSHIFT,
    libevdev.EV_KEY.KEY_KPASTERISK,
    libevdev.EV_KEY.KEY_LEFTALT,
    libevdev.EV_KEY.KEY_SPACE,
    libevdev.EV_KEY.KEY_CAPSLOCK,
    libevdev.EV_KEY.KEY_F1,
    libevdev.EV_KEY.KEY_F2,
    libevdev.EV_KEY.KEY_F3,
    libevdev.EV_KEY.KEY_F4,
    libevdev.EV_KEY.KEY_F5,
    libevdev.EV_KEY.KEY_F6,
    libevdev.EV_KEY.KEY_F7,
    libevdev.EV_KEY.KEY_F8,
    libevdev.EV_KEY.KEY_F9,
    libevdev.EV_KEY.KEY_F10,
    libevdev.EV_KEY.KEY_NUMLOCK,
    libevdev.EV_KEY.KEY_SCROLLLOCK,
    libevdev.EV_KEY.KEY_KP7,
    libevdev.EV_KEY.KEY_KP8,
    libevdev.EV_KEY.KEY_KP9,
    libevdev.EV_KEY.KEY_KPMINUS,
    libevdev.EV_KEY.KEY_KP4,
    libevdev.EV_KEY.KEY_KP5,
    libevdev.EV_KEY.KEY_KP6,
    libevdev.EV_KEY.KEY_KPPLUS,
    libevdev.EV_KEY.KEY_KP1,
    libevdev.EV_KEY.KEY_KP2,
    libevdev.EV_KEY.KEY_KP3,
    libevdev.EV_KEY.KEY_KP0,
    libevdev.EV_KEY.KEY_KPDOT,
    libevdev.EV_KEY.KEY_ZENKAKUHANKAKU,
    libevdev.EV_KEY.KEY_102ND,
    libevdev.EV_KEY.KEY_F11,
    libevdev.EV_KEY.KEY_F12,
    libevdev.EV_KEY.KEY_RO,
    libevdev.EV_KEY.KEY_KATAKANA,
    libevdev.EV_KEY.KEY_HIRAGANA,
    libevdev.EV_KEY.KEY_HENKAN,
    libevdev.EV_KEY.KEY_KATAKANAHIRAGANA,
    libevdev.EV_KEY.KEY_MUHENKAN,
    libevdev.EV_KEY.KEY_KPJPCOMMA,
    libevdev.EV_KEY.KEY_KPENTER,
    libevdev.EV_KEY.KEY_RIGHTCTRL,
    libevdev.EV_KEY.KEY_KPSLASH,
    libevdev.EV_KEY.KEY_SYSRQ,
    libevdev.EV_KEY.KEY_RIGHTALT,
    libevdev.EV_KEY.KEY_HOME,
    libevdev.EV_KEY.KEY_UP,
    libevdev.EV_KEY.KEY_PAGEUP,
    libevdev.EV_KEY.KEY_LEFT,
    libevdev.EV_KEY.KEY_RIGHT,
    libevdev.EV_KEY.KEY_END,
    libevdev.EV_KEY.KEY_DOWN,
    libevdev.EV_KEY.KEY_PAGEDOWN,
    libevdev.EV_KEY.KEY_INSERT,
    libevdev.EV_KEY.KEY_DELETE,
    libevdev.EV_KEY.KEY_MACRO,
    libevdev.EV_KEY.KEY_MUTE,
    libevdev.EV_KEY.KEY_VOLUMEDOWN,
    libevdev.EV_KEY.KEY_VOLUMEUP,
    libevdev.EV_KEY.KEY_POWER,
    libevdev.EV_KEY.KEY_KPEQUAL,
    libevdev.EV_KEY.KEY_KPPLUSMINUS,
    libevdev.EV_KEY.KEY_PAUSE,
    libevdev.EV_KEY.KEY_KPCOMMA,
    libevdev.EV_KEY.KEY_HANGEUL,
    libevdev.EV_KEY.KEY_HANJA,
    libevdev.EV_KEY.KEY_YEN,
    libevdev.EV_KEY.KEY_LEFTMETA,
    libevdev.EV_KEY.KEY_RIGHTMETA,
    libevdev.EV_KEY.KEY_COMPOSE,
    libevdev.EV_KEY.KEY_STOP,
    libevdev.EV_KEY.KEY_CALC,
    libevdev.EV_KEY.KEY_SLEEP,
    libevdev.EV_KEY.KEY_WAKEUP,
    libevdev.EV_KEY.KEY_WWW,
    libevdev.EV_KEY.KEY_BOOKMARKS,
    libevdev.EV_KEY.KEY_COMPUTER,
    libevdev.EV_KEY.KEY_BACK,
    libevdev.EV_KEY.KEY_FORWARD,
    libevdev.EV_KEY.KEY_EJECTCD,
    libevdev.EV_KEY.KEY_NEXTSONG,
    libevdev.EV_KEY.KEY_PLAYPAUSE,
    libevdev.EV_KEY.KEY_PREVIOUSSONG,
    libevdev.EV_KEY.KEY_STOPCD,
    libevdev.EV_KEY.KEY_REFRESH,
    libevdev.EV_KEY.KEY_F13,
    libevdev.EV_KEY.KEY_F14,
    libevdev.EV_KEY.KEY_F15,
    libevdev.EV_KEY.KEY_F21,
    libevdev.EV_KEY.KEY_CAMERA,
    libevdev.EV_KEY.KEY_EMAIL,
    libevdev.EV_KEY.KEY_SEARCH,
    libevdev.EV_KEY.KEY_BRIGHTNESSDOWN,
    libevdev.EV_KEY.KEY_BRIGHTNESSUP,
    libevdev.EV_KEY.KEY_MEDIA,
    libevdev.EV_KEY.KEY_BLUETOOTH,
    libevdev.EV_KEY.KEY_WLAN,
]


keyb_union = [ # all printable keys from 101, modified 101, 102, 103 and 104 layouts
# row E
    libevdev.EV_KEY.KEY_GRAVE,
    libevdev.EV_KEY.KEY_1,
    libevdev.EV_KEY.KEY_2,
    libevdev.EV_KEY.KEY_3,
    libevdev.EV_KEY.KEY_4,
    libevdev.EV_KEY.KEY_5,
    libevdev.EV_KEY.KEY_6,
    libevdev.EV_KEY.KEY_7,
    libevdev.EV_KEY.KEY_8,
    libevdev.EV_KEY.KEY_9,
    libevdev.EV_KEY.KEY_0,
    libevdev.EV_KEY.KEY_MINUS,
    libevdev.EV_KEY.KEY_EQUAL,
    libevdev.EV_KEY.KEY_YEN,    
    libevdev.EV_KEY.KEY_BACKSPACE,
    
# row D
    libevdev.EV_KEY.KEY_TAB,
    libevdev.EV_KEY.KEY_Q,
    libevdev.EV_KEY.KEY_W,
    libevdev.EV_KEY.KEY_E,
    libevdev.EV_KEY.KEY_R,
    libevdev.EV_KEY.KEY_T,
    libevdev.EV_KEY.KEY_Y,
    libevdev.EV_KEY.KEY_U,
    libevdev.EV_KEY.KEY_I,
    libevdev.EV_KEY.KEY_O,
    libevdev.EV_KEY.KEY_P,
    libevdev.EV_KEY.KEY_LEFTBRACE,
    libevdev.EV_KEY.KEY_RIGHTBRACE,
    libevdev.EV_KEY.KEY_ENTER,

# row C
    libevdev.EV_KEY.KEY_A,
    libevdev.EV_KEY.KEY_S,
    libevdev.EV_KEY.KEY_D,
    libevdev.EV_KEY.KEY_F,
    libevdev.EV_KEY.KEY_G,
    libevdev.EV_KEY.KEY_H,
    libevdev.EV_KEY.KEY_J,
    libevdev.EV_KEY.KEY_K,
    libevdev.EV_KEY.KEY_L,
    libevdev.EV_KEY.KEY_SEMICOLON,
    libevdev.EV_KEY.KEY_APOSTROPHE,
    libevdev.EV_KEY.KEY_BACKSLASH,

# row B
    libevdev.EV_KEY.KEY_102ND,
    libevdev.EV_KEY.KEY_Z,
    libevdev.EV_KEY.KEY_X,
    libevdev.EV_KEY.KEY_C,
    libevdev.EV_KEY.KEY_V,
    libevdev.EV_KEY.KEY_B,
    libevdev.EV_KEY.KEY_N,
    libevdev.EV_KEY.KEY_M,
    libevdev.EV_KEY.KEY_COMMA,
    libevdev.EV_KEY.KEY_DOT,
    libevdev.EV_KEY.KEY_SLASH,
    libevdev.EV_KEY.KEY_RO,

# row A
    libevdev.EV_KEY.KEY_SPACE,
]


keyb_102 = [
# row E 00 - 13
    libevdev.EV_KEY.KEY_GRAVE,
    libevdev.EV_KEY.KEY_1,
    libevdev.EV_KEY.KEY_2,
    libevdev.EV_KEY.KEY_3,
    libevdev.EV_KEY.KEY_4,
    libevdev.EV_KEY.KEY_5,
    libevdev.EV_KEY.KEY_6,
    libevdev.EV_KEY.KEY_7,
    libevdev.EV_KEY.KEY_8,
    libevdev.EV_KEY.KEY_9,
    libevdev.EV_KEY.KEY_0,
    libevdev.EV_KEY.KEY_MINUS,
    libevdev.EV_KEY.KEY_EQUAL,
    libevdev.EV_KEY.KEY_BACKSPACE,
    
# row D 00 - 13
    libevdev.EV_KEY.KEY_TAB,
    libevdev.EV_KEY.KEY_Q,
    libevdev.EV_KEY.KEY_W,
    libevdev.EV_KEY.KEY_E,
    libevdev.EV_KEY.KEY_R,
    libevdev.EV_KEY.KEY_T,
    libevdev.EV_KEY.KEY_Y,
    libevdev.EV_KEY.KEY_U,
    libevdev.EV_KEY.KEY_I,
    libevdev.EV_KEY.KEY_O,
    libevdev.EV_KEY.KEY_P,
    libevdev.EV_KEY.KEY_LEFTBRACE,
    libevdev.EV_KEY.KEY_RIGHTBRACE,
    libevdev.EV_KEY.KEY_ENTER,

# row C 01 - 12
    libevdev.EV_KEY.KEY_A,
    libevdev.EV_KEY.KEY_S,
    libevdev.EV_KEY.KEY_D,
    libevdev.EV_KEY.KEY_F,
    libevdev.EV_KEY.KEY_G,
    libevdev.EV_KEY.KEY_H,
    libevdev.EV_KEY.KEY_J,
    libevdev.EV_KEY.KEY_K,
    libevdev.EV_KEY.KEY_L,
    libevdev.EV_KEY.KEY_SEMICOLON,
    libevdev.EV_KEY.KEY_APOSTROPHE,
    libevdev.EV_KEY.KEY_BACKSLASH,


# row B 00 - 10
    libevdev.EV_KEY.KEY_102ND,
    libevdev.EV_KEY.KEY_Z,
    libevdev.EV_KEY.KEY_X,
    libevdev.EV_KEY.KEY_C,
    libevdev.EV_KEY.KEY_V,
    libevdev.EV_KEY.KEY_B,
    libevdev.EV_KEY.KEY_N,
    libevdev.EV_KEY.KEY_M,
    libevdev.EV_KEY.KEY_COMMA,
    libevdev.EV_KEY.KEY_DOT,
    libevdev.EV_KEY.KEY_SLASH,

# row A
    libevdev.EV_KEY.KEY_SPACE,
]

layouts = []

r = subprocess.run(['localectl', 'list-x11-keymap-layouts'], capture_output=True, check=True, encoding='utf8')
for locale in r.stdout.split('\n'):
    r = subprocess.run(['localectl', 'list-x11-keymap-variants', locale], capture_output=True, check=False, encoding='utf8')
    layouts.append((locale, ''))
    if r.returncode == 0:
        for variant in r.stdout.split('\n'):
            if variant in ['tam_TAB', 'tam_TSCII']:
                # these are non unicode encodings. Hopefully the unicode
                # variants cover all keys
                continue
            layouts.append((locale, variant))

#layouts = [('us', ''), ('de', 'nodeadkeys'), ('de', '')]
#layouts = [('pk', 'ara')]

device = libevdev.Device()
device.name = 'explorer'
for k in keys_list:
    device.enable(k)
    
uinput = device.create_uinput_device()

time.sleep(1)

fd = sys.stdin.fileno()

old = termios.tcgetattr(fd)

new = termios.tcgetattr(fd)
# iflag
new[0] = new[0] | termios.IGNBRK | termios.IGNPAR
new[0] = new[0] & ~(termios.BRKINT | termios.PARMRK | termios.ISTRIP | termios.INLCR | termios.ICRNL | termios.IXON | termios.IXOFF)

# lflag
new[3] = new[3] & ~(termios.ICANON | termios.IEXTEN | termios.ECHO | termios.ISIG)

# cc
new[6][termios.VMIN] = 0
new[6][termios.VTIME] = 0

def press(key):
    press = [libevdev.InputEvent(key, value=1),
             libevdev.InputEvent(libevdev.EV_SYN.SYN_REPORT, value=0)]
    uinput.send_events(press)             
             
    press = [libevdev.InputEvent(key, value=0),
             libevdev.InputEvent(libevdev.EV_SYN.SYN_REPORT, value=0)]
    uinput.send_events(press)


responses = {}
oopses = []

try:
    termios.tcsetattr(fd, termios.TCSAFLUSH, new)
    
    for layout in layouts:
        print('=== {} ==='.format(layout))
        r = subprocess.run(['setxkbmap', *layout], check=True)
        for key in keyb_union:
            press(libevdev.EV_KEY.KEY_F1) # defeat dead keys part 1
            press(key)
            time.sleep(.01)
            response = os.read(fd, 100)
            if not response.startswith(b'\033OP'):
                print("oops")
                oopses.append((layout, key))
            else:
                response = response[3:]
            if not response:
                # dead key or unmapped key. Flush out with spaces
                for i in range(3):
                    press(libevdev.EV_KEY.KEY_SPACE)
                    time.sleep(.01)
                    os.read(fd, 100) # discard buffer
            print(key, repr(response))
            if response not in responses:
                responses[response] = set()
            responses[response].add(layout)
finally:
    termios.tcsetattr(fd, termios.TCSAFLUSH, old)

print(responses.keys())

with open('responses.txt', 'w') as f:
    for response, layouts in responses.items():
        decoded = '!!!' + repr(response)
        try:
            decoded = response.decode()
        except:
            pass
        print('{} {} {}'.format(repr(response), decoded, layouts), file=f)

j = []

for response, layouts in responses.items():
    decoded = '!!!' + repr(response)
    try:
        decoded = response.decode()
    except:
        pass
    j.append({ 'text': decoded, 'layouts': list(layouts)})

with open('responses.json', 'w') as f:
    json.dump(j, f)


print(oopses)

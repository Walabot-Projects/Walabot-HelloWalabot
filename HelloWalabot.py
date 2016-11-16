from __future__ import print_function
from sys import platform
from os import system
import WalabotAPI as wlbt

wlbt.Init()
wlbt.SetSettingsFolder()
wlbt.ConnectAny()

wlbt.SetProfile(wlbt.PROF_SENSOR)
wlbt.SetDynamicImageFilter(wlbt.FILTER_TYPE_MTI)

wlbt.Start()

while True:
    wlbt.Trigger()
    targets = wlbt.GetSensorTargets()
    system('cls' if platform == 'win32' else 'clear')  # clear the terminal
    for i, t in enumerate(targets):
        print('Target #{}\nx = {}\ny = {}\nz = {}\n'.format(
            i+1, t.xPosCm, t.yPosCm, t.zPosCm))

wlbt.Stop()
wlbt.Disconnect()

from __future__ import print_function
from sys import platform
from os import system
import WalabotAPI as wlbt

wlbt.Init()
wlbt.SetSettingsFolder()
wlbt.ConnectAny()
wlbt.SetProfile(wlbt.PROF_SENSOR)
wlbt.SetArenaR(10, 50, 5)
wlbt.SetArenaTheta(-15, 15, 10)
wlbt.SetArenaPhi(-30, 30, 5)
wlbt.SetThreshold(15)
wlbt.SetDynamicImageFilter(wlbt.FILTER_TYPE_MTI)
wlbt.Start()
while True:
    wlbt.Trigger()
    targets = wlbt.GetSensorTargets()
    system('cls' if platform == 'win32' else 'clear') $clear the terminal screen
    for i, t in enumerate(targets):
        print('Target #{}\nx = {}\ny = {}\nz = {}\n'.format(i+1, t.xPosCm, t.yPosCm, t.zPosCm))
wlbt.Stop()
wlbt.Disconnect()

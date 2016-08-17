from __future__ import print_function
from imp import load_source
from os.path import join
from sys import platform

if platform == 'win32': # for windows
    path = join('C:/', 'Program Files', 'Walabot', 'WalabotSDK', 'python')
else: # for linux, raspberry pi, etc.
    path = join('/usr', 'share', 'walabot', 'python')
wlbt = load_source('WalabotAPI', join(path, 'WalabotAPI.py'))
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
    print(chr(27) + "[2J") # clear the terminal screen
    for i, t in enumerate(targets):
        print('Target #{}\nx = {}\ny = {}\nz = {}\n'.format(i+1, t.xPosCm, t.yPosCm, t.zPosCm))
wlbt.Stop()
wlbt.Disconnect()

# Installing WalabotAPI Library Using pip
Simply write one of these two lines into the terminal or cmd depends on your operation system.
## Windows
```
python -m pip install "C:\Program Files\Walabot\WalabotSDK\python\WalabotAPI-1.0.21.zip"
```

## Linux
```
python -m pip install "/usr/share/walabot/python/WalabotAPI-1.0.21.tar.gz"
```

# First Walabot App

Here displays the simplest, shortest Walabot application available, written in Python.  
The app simply prints the cartesian coordinates of every found target.

## Full code

```
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
    system('cls' if platform == 'win32' else 'clear') #clear the terminal screen
    for i, t in enumerate(targets):
        print('Target #{}\nx = {}\ny = {}\nz = {}\n'.format(i+1, t.xPosCm, t.yPosCm, t.zPosCm))

wlbt.Stop()
wlbt.Disconnect()

```

## A line-by-line explanation

```
from __future__ import print_function
```
For cross python2-python3 code. Makes the `print()` function available in python2.


```
from imp import load_source
```
The `imp` module will allow us to load the `WalabotAPI.py` wrapper from specific path.

```
from os.path import join
```
The `join()` function is used here to create a cross-platform path easily.

```
path = join('/usr', 'share', 'walabot', 'python')
```
The path to 'WalabotAPI.py' wrapper is assigned to `path` variable.

```
wlbt = load_source('WalabotAPI', join(path, 'WalabotAPI.py'))
```
The `WalabotAPI.py` wrapper is loaded to the `wlbt` variable.

```
wlbt.Init()
```
The `WalabotAPI.py` wrapper uses the Walabot SDK (written in C).
The `Init()` function loads that SDK to the wrapper.
This line is a must-have after loading the wrapper.

```
wlbt.SetSettingsFolder()
```
The Walabot SDK uses certain database files. This function loads the path to those files.  
If no path is specified, the SDK will use the default path and internal databases.

```
wlbt.ConnectAny()
```
Establishes communication with the Walabot.  
Connection is required before `Start()`.
If multiple Walabots are present, a single available Walabot is selected.  
To specify one, use `Connect()`.

```
wlbt.SetProfile(wlbt.PROF_SENSOR)
```
Sets scan profile.  
For an explanation of other profiles, see [Imaging Features](http://api.walabot.com/_features.html).
###### Parameters
* `profile` - The scan profile to use.

```
wlbt.SetArenaR(10, 50, 5)
```
Sets radial (r) range and resolution of arena.  
For coordinate directions, see [Coordinate Systems](http://api.walabot.com/_features.html#_coordination).  
To check the current value, use `GetArenaR()`.  
Spherical (r-Θ-Φ) coordinates should be used only to get image data from a triggered scan that used one of the Sensor profiles. Otherwise use the `SetArena` functions for cartesian (X-Y-Z) coordinates.  
###### Parameters
* `start` - Beginning of radial distance range (cm).
* `end` - End of radial distance range (cm).
* `res` - Distance between pixels along radius (cm).

```
wlbt.SetArenaTheta(-15, 15, 10)
```
Sets polar (Θ) range and resolution of arena.  
For coordinate directions, see [Coordinate Systems](http://api.walabot.com/_features.html#_coordination).  
To check the current value, use `GetArenaTheta()`.  
Spherical (r-Θ-Φ) coordinates should be used only to get image data from a triggered scan that used one of the Sensor profiles. Otherwise use the `SetArena` functions for cartesian (X-Y-Z) coordinates.
###### Parameters
* `min` - Beginning of polar angular range (degrees).
* `max` - End of polar angular range (degrees).
* `res` - Angle between pixels across polar angle (degrees).

```
wlbt.SetArenaPhi(-30, 30, 5)
```
Sets azimuth (Φ) range and resolution of arena.
For coordinate directions, see [Coordinate Systems](http://api.walabot.com/_features.html#_coordination).  
To check the current value, use `GetArenaPhi()`.  
Spherical (r-Θ-Φ) coordinates should be used only to get image data from a triggered scan that used one of the Sensor profiles. Otherwise use the `SetArena` functions for cartesian (X-Y-Z) coordinates.
###### Parameters
* `min` - Beginning of azimuth angular range (degrees).
* `max` - End of azimuth angular range (degrees).
* `res` - Angle between pixels across polar angle (degrees).

```
wlbt.SetThreshold(15)
```
Changes the sensitivity threshold.  
For raw images (3-D and Slice), Walabot removes very weak signals, below this threshold. If the threshold is not set, a default value is used.  
To check the current value, use `GetThreshold()`.
###### Parameters
* `value` - The threshold to set.

```
wlbt.SetDynamicImageFilter(wlbt.FILTER_TYPE_MTI)
```
Dynamic-imaging filter removes static signals, leaving only changing signals.  
Specify filter algorithm to use. Filters are explained in [Imaging Features](http://api.walabot.com/_features.html).  
Filter is not applied to `GetImageEnergy()`.  
To check the current value, use `GetDynamicImageFilter()`.  
###### Parameters
* `type` - Filter algorithm to use.

```
wlbt.Start()
```
Starts Walabot in preparation for scanning.  
Requires previous Connect (`ConnectAny()` or `Connect()`) and `SetProfile()`.  
Required before `Trigger()` and GET actions.

```
while True:
```
Runs the indented block over and over - forever.

```
    wlbt.Trigger()
```
Initiates a scan and records signals.   
Initiates a scan according to profile and records signals to be available for processing and retrieval.  
Should be performed before every GET action.

```
    targets = wlbt.GetSensorTargets()
```
Provides a list of and the number of identified targets.  
Available only if one of the Sensor scan profiles was used.  
Requires previous `Trigger()`; provides data based on last completed triggered image.  
Provided image data is dependent on current configured arena and on current configuration from `SetDynamicImageFilter()` and `SetThreshold()`.
###### Returns
* `targets` - List of identified targets.

```
    print(chr(27) + "[2J")
```
 Clears the terminal screen.

```
    for i, t in enumerate(targets):
```
Iterates over the `targets` list while keeping the index of the corresponding target.  
See the [Python documentation](https://docs.python.org/3/library/functions.html#enumerate) in the topic.

```
        print('Target #{}\nx = {}\ny = {}\nz = {}\n'.format(i+1, t.xPosCm, t.yPosCm, t.zPosCm))
```
Prints the x, y, and z values of a target (of type `SensorTarget`).

```
wlbt.Stop()
```
Stops Walabot when finished scanning.


```
wlbt.Disconnect()
```
Stops communication with Walabot.

# First Walabot App

Here displays the simplest, shortest Walabot application available, written in Python.  
The app simply prints the cartesian coordinates of every found target.

## Installing the WalabotAPI Python Library Using pip

After [installing the WalabotSDK](http://walabot.com/getting-started) on your machine:  
Simply write one of these two lines into the terminal or cmd depends on your operation system.

### Windows
```
python -m pip install "C:\Program Files\Walabot\WalabotSDK\python\WalabotAPI-1.0.21.zip"
```

### Linux / Raspberry PI
```
python -m pip install "/usr/share/walabot/python/WalabotAPI-1.0.21.zip"
```

## Full code

```python
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
from sys import platform
```
Retrieve the type of operation system.

```
from os import system
```
Execute terminal commands (used to clear the terminal screen)

```
import WalabotAPI as wlbt
```
The `WalabotAPI` wrapper is loaded to the `wlbt` alias.

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
    system('cls' if platform == 'win32' else 'clear') # clear the terminal screen
```
 Clears the terminal screen (send command according to the user OS).

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

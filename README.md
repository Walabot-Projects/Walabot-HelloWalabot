# Hello Walabot App

[![Create your first app in under 2 minutes with Walabot!](http://img.youtube.com/vi/JBSL8tojM8Q/0.jpg)](http://www.youtube.com/watch?v=JBSL8tojM8Q)

Here displays the simplest, shortest Walabot application available, written in Python.  
* Prints the cartesian coordinates of every target found by the Walabot.
* Works on both Python 2 and Python 3.

## How to use

1. Install the [Walabot SDK](http://walabot.com/getting-started) and the WalabotAPI Python library using pip.
6. Run `HelloWalabot.py`.


####  Installing the WalabotAPI Python Library

After [installing the WalabotSDK](http://walabot.com/getting-started) on your machine:  
Simply write one of these two lines into the terminal or cmd depends on your operation system.

##### Windows
```
pip install WalabotAPI --no-index --find-links="%PROGRAMFILES%\Walabot\WalabotSDK\python\\"
```

##### Linux / Raspberry PI
```
pip install WalabotAPI --no-index --find-links="/usr/share/walabot/python/"
```

## Full code

```python
from __future__ import print_function
from sys import platform
from os import system
import WalabotAPI as wlbt


wlbt.Init()  # load the WalabotSDK to the Python wrapper
wlbt.Initialize()  # set the path to the essetial database files
wlbt.ConnectAny()  # establishes communication with the Walabot

wlbt.SetProfile(wlbt.PROF_TRACKER)  # set scan profile out of the possibilities
wlbt.SetDynamicImageFilter(wlbt.FILTER_TYPE_MTI)  # specify filter to use

wlbt.Start()  # starts Walabot in preparation for scanning

while True:
    wlbt.Trigger()  # initiates a scan and records signals
    targets = wlbt.wlbt.GetTrackerTargets()  # provides a list of identified targets
    system('cls' if platform == 'win32' else 'clear')  # clear the terminal
    for i, t in enumerate(targets):
        print('Target #{}\nx = {}\ny = {}\nz = {}\n'.format(
            i+1, t.xPosCm, t.yPosCm, t.zPosCm))

wlbt.Stop()  # stops Walabot when finished scanning
wlbt.Disconnect()  # stops communication with Walabot
```

## A line-by-line explanation

```python
import WalabotAPI as wlbt
```
The `WalabotAPI` wrapper is loaded to the `wlbt` alias.

```python
wlbt.Init()
```
The `WalabotAPI.py` wrapper uses the Walabot SDK (written in C).
The `Init()` function loads that SDK to the wrapper.
This line is a must-have after loading the wrapper.

```python
wlbt.wlbt.Initialize()
```
The Walabot SDK uses certain database files. This function loads the path to those files.  
If no path is specified, the SDK will use the default path and internal databases.

```python
wlbt.ConnectAny()
```
Establishes communication with the Walabot.  
Connection is required before `Start()`.
If multiple Walabots are present, a single available Walabot is selected.  
To specify one, use `Connect()`.

```python
wlbt.SetProfile(wlbt.PROF_TRACKER)
```
Sets scan profile.  
For an explanation of other profiles, see [Imaging Features](http://api.walabot.com/_features.html).
###### Parameters
* `profile` - The scan profile to use.

```python
wlbt.SetDynamicImageFilter(wlbt.FILTER_TYPE_MTI)
```
Dynamic-imaging filter removes static signals, leaving only changing signals.  
Specify filter algorithm to use. Filters are explained in [Imaging Features](http://api.walabot.com/_features.html).  
Filter is not applied to `GetImageEnergy()`.  
To check the current value, use `GetDynamicImageFilter()`.  
###### Parameters
* `type` - Filter algorithm to use.

```python
wlbt.Start()
```
Starts Walabot in preparation for scanning.  
Requires previous Connect (`ConnectAny()` or `Connect()`) and `SetProfile()`.  
Required before `Trigger()` and GET actions.

```python
    wlbt.Trigger()
```
Initiates a scan and records signals.   
Initiates a scan according to profile and records signals to be available for processing and retrieval.  
Should be performed before every GET action.

```python
    targets = wlbt.GetTrackerTargets()
```
Provides a list of and the number of identified targets.  
Available only if one of the Tracker scan profiles was used.  
Requires previous `Trigger()`; provides data based on last completed triggered image.  
Provided image data is dependent on current configured arena and on current configuration from `SetDynamicImageFilter()` and `SetThreshold()`.
###### Returns
* `targets` - List of identified targets.

```python
    for i, t in enumerate(targets):
        print('Target #{}\nx = {}\ny = {}\nz = {}\n'.format(
            i+1, t.xPosCm, t.yPosCm, t.zPosCm))
```
Iterates over the `targets` list while keeping the index of the corresponding target.  
Prints the x, y, and z values of a target (of type `TrackerTarget`).

```python
wlbt.Stop()
```
Stops Walabot when finished scanning.


```python
wlbt.Disconnect()
```
Stops communication with Walabot.

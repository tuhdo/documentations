## eLink python script API 

[TOC]

### How to run python script 

#### Run script as default with command line 

```shell
elinkviewer.exe -cons=<relative/absolute path to your script> 
# relative path from elinkviewer.exe 
```

Example: 

```
# Run script elinkviewer
elinkviewer.exe -cons=hello-world.py 
```

![run script default](https://lh3.googleusercontent.com/-9-pVwhQCHXc/W4d5w9vN0JI/AAAAAAAAAKM/nF08A8hiWccySopF5AcQZPdyIpl_DXT3gCHMYCw/s0/2018-08-30_11-58-16.gif)

#### Run script by console window in eLinkViewer

Connect vào eLinkKVM -> Click button Python Console in Tools Bar

![Runbyelinkviewer](https://lh3.googleusercontent.com/-MIGlneMqxcg/W4ej1UB9KeI/AAAAAAAAALA/hEcGVFI2EM8tiFaHvoDoqmyQx-OIcM-AgCHMYCw/s0/2018-08-30_14-58-09.gif)



#### Run Script by console 

```
elinkviewer -cons=
```

```python
elink.exec("hello-world\hello-world.py") # hello-world\hello-world.py relative from current directory of eLinkViewer.exe 
elink.exec("E:\project\elink-tutorial\hello-world\hello-world.py") # run script hello-world with absolute path 
```



### **eLink** 

#### elink.newConnection
Create a new connection to eLinkKVM. The function will return eLink object. Ví dụ: 
```python
## connect to eLinkKVM với địa chỉ IP "10.42.02"
eLinkObj = elink.newConnection("10.42.0.2)
```
#### elink.getConnection 
Get all connections exist 
```
gConnection = eLink.getConnection()

```
```python
elink.newConnection("10.42.0.3")
groupConn = elink.getConnection()
print("group obj {} - type {}".format(groupConn,type(groupConn)))
info = groupConn[0].info()
print("firmware version \t{}\neLinkKVM Name \t{}".format(info[0],info[1]))
print("firmware version \t{}\neLinkKVM Name \t{}".format(groupConn[0].info()[0],groupConn[0].info()[1]))
```




#### eLinkObj.info()

get eLink connection info 
```python 
def testGetInfo():
    eLinkObj = elink.newConnection("10.42.0.3")
    info = eLinkObj.info()
    print("eLinkObj.info return {}".format(info))
```
python std output: 

```bash
eLinkObj.info return ['01.00.01.02', 'eVirtualFriend', 'R', 1366, 768]
# <'01.00.01.02'>     :firmware version 
# <'eVirtualFriend'   :eLinkKVM name
# <'RFB 3.03'>		  :Protocol
# <1366, 768> 		  :Width-Height of current screen 
```



#### eLinkObj.close

Close eLinkObj session

```python
## connect to eLinkKVM with Ip address "10.42.02"
eLinkObj = elink.newConnection("10.42.0.2)
## close connection
elinkObj.close()
```

#### eLinkObj.sendString        			

Send key string 

```python
#eLinkKVM sends string hello world to server 
eLinkObj.sendString("hello world")	
```

#### eLinkObj.sendKey
Send Key to Server
```python
# eLinkKVM send key <LeftShift> lên server 
eLinkObj.sendKey("LeftShift") # Press LeftShift và release
eLinkObj.sendKey("LeftShift",1) # Press and hold LeftShift
eLinkObj.sendKey("LeftShift",0) # Release Left Shift 
```

#### eLinkObj.sendMouse         			
Send mouse action to server 
```python
eLinkObj.sendMouse(0, 100, 100)  # move mouse to 100,100
eLinkObj.sendMouse("RDOWN", 100, 100)  # right mouse down at 100,100
eLinkObj.sendMouse("RDOWN|CLICK", 100, 100)  # right mouse click at 100,100	(or 0x40)
eLinkObj.sendMouse("RDOWN|DCLICK", 100, 100)  # right mouse double click at 100,100 (or 0x80)
```

#### eLinkObj.sendKeyEx         			

Send Combined Key

```python
eLinkObj.sendCombinedKey(["LeftCtrl", "LeftShift", "Del"])  
# send a combination key <LeftCtrl + LeftShift + Del>
```

#### eLinkObj.getEvent          			

Get events receive from eLinkKVM. 

Event Id 

```python 
EVT_USB_EXT_RESET = 1
EVT_USB_EXT_CONFIGURED = 2
EVT_EXT_BUFFER_FULL = 3
EVT_KEY_PHANTOM = 4
EVT_USB_KEY_SET_PROTOCOL = 5
EVT_USB_KEY_SET_REPORT = 6
EVT_USB_KEY_SET_IDLE = 7
EVT_USB_MAIN_RESET = 8
EVT_USB_MAIN_CONFIGURED = 9
EVT_USB_MAIN_CONNECTED = 11
EVT_USB_MAIN_DISCONNECTED = 12
EVT_STORAGE_FIRST_READ = 13
EVT_STORAGE_FIRST_READ2 = 14
EVT_STORAGE_FIRST_WRITE = 15
EVT_STORAGE_FIRST_WRITE2 = 16
EVT_RESET_MAX_REACH = 17
EVT_FILE1_ERROR = 18
EVT_FILE2_ERROR = 19
EVT_FILE_VNC_ERROR = 20
EVT_NAND_ERROR = 21
EVT_VNC_HIP_CONNECTED = 22
EVT_STORAGE_IDLE = 23
EVT_STORAGE_REGION_COUNT = 24
EVT_KEY_TRIGGER_ON_RESET = 25
EVT_KEY_ON_POWER_DONE = 26
EVT_DISK_ON_POWER_DONE = 27
```

Example: 

```python
# below is process to check if event 5 existed => Press key F12
while True:
    e = eLinkObj.getEvent() #get event object 
    if e.getIdCode() == 5: #check event 5 (EVT_USB_KEY_SET_PROTOCOL) is existed
		eLinkObj.sendKey("F12") # send key F12 to server 
    break
```

#### eLinkObj.clrEvent

When starting Server which will though many phase including: Pre-Boot phase And OS phase. With each phase, Server will re-Initial eLinkKVM , then eLinkKVM will issue many duplicate events. So, need to have aa clean event method to clean up current queue event.

```python
# Clear all existed event in queue and waiting for new event 5
eLinkObj.clrEvent()
# below is process for waiting event 5 existed => Press key F12
while True:
    e = eLinkObj.getEvent() #get event object 
    if e.getIdCode() == 5: #check event 5 (EVT_USB_KEY_SET_PROTOCOL) is existed
		eLinkObj.sendKey("F12") # send key F12 to server 
    break

```

#### eLinkObj.setUsbMode        			

Set USB Mode

```python
#Configure eLinkKVM to USB Keyboard
USB_MODE_KEY	   = 0x0001
#Configure eLinkKVM to USB Mouse Keyboard
USB_MODE_MOUSE      = 0x0002
#Configure eLinkKVM to USB Mass storage
USB_MODE_MSC	  = 0x0004
#Special Mode, set it if want to speed up Booster Mode
USB_MODE_VNC_HID    =  0x0008
#Configure eLinkKVM to CDC device Keyboard (not support yet)
USB_MODE_CDC	    = 0x0010
#Configure eLinkKVM to USB Video class device (not support yet)
USB_MODE_UVC	    =  0x0020
#Configure eLinkKVM to USB Absolute Mouse
USB_MODE_MOUSE_ABS  = 0x0040
```

```python
eLinkObj.setUsbMode(0,0) # reset UsbMode.
# Set eLinkKVM into an multiple usb device: including
# - Usb Key board 
# - Activate USB_MODE_VNC_HID to speed up Booster mode
# - Activate USB Mass storage mode which will mount image <win10.hdd2> 
eLinkObj.setUsbMode("USB_MODE_KEY|USB_MODE_VNC_HID",0,["A:\win10.hdd2"]) 
eLinkObj.setUsbMode(0x09,0,["A:\win10.hdd2"])
#only set USB_MODE_MSC (Usb mass storage)  
#mount <win10.hdd2> 
#mount <ubuntu.hdd2> 
eLinkObj.setUsbMode(0,0,["A:\win10.hdd2"."A:\ubuntu.hdd2])
# Keep Usb KeyBoard and USB_MODE_VNC_HID (Booster)
# Unmount <win10.hdd2> 
eLinkObj.setUsbMode("USB_MODE_KEY|USB_MODE_VNC_HID",0)
#USB Keyboard 
#Usb mode hid eLinkObj (bootster) 
#Usb mouse absolute 
#Usb mass storage - mount <win10.hdd2> 
eLinkObj.setUsbMode("USB_MODE_KEY|USB_MODE_VNC_HID|USB_MODE_MOUSE_ABS",0,["A:\win10.hdd2"]

```

#### eLinkObj.setVncMode   
```
TODO Review the naming => change to eLinkObj.setOutputMode()
```
Set eLinkObj Mode

```python
# RGB mode , display VGA graphic 
VNC_MODE_RGB    = 0x01,
# Booster mode , display server graphic through Booster protocol
VNC_MODE_BOOSTER  = 0x02,
#alias Booster mode , display server graphic through Booster protocol
VNC_MODE_MSC   = 0x02,
# serial mode , display serial data from Serial port 
VNC_MODE_SERIAL = 0x03,
# IPMI mode , display IPMI SOL (Serial overlan)
VNC_MODE_IPMI   = 0x04,
```

```
eLinkObj.setVncMode("MODE_VNC_BOOSTER") #Set Booster mode
eLinkObj.setVncMode("MODE_VNC_SERIAL") #Set Serial mode
eLinkObj.setVncMode("MODE_VNC_RGB") #Set RGB mode
```


#### eLinkObj.setKeyMode        			

Set Keyboard Mode

```python
KEY_INTF_NONE = 0, # deactive keyboard 
KEY_INTF_HID  = 1, # enable HID keyboard
KEY_INTF_VNC  = 2, # enable VNC keyboard
```

```python
eLinkObj.setKeyMode("KEY_INTF_HID")
eLinkObj.setKeyMode(1)
eLinkObj.setKeyMode("KEY_INTF_VNC")
eLinkObj.setKeyMode(2)
```

#### eLinkObj.setMouseMode      			
Set Mouse mode. Mouse mode including: 
```python
# Cấu hình Mouse sử dụng HID USB 
POINT_INTF_HID      = 1,
#Cấu Hinh Mouse sử dụng mode VNC (Sử dụng VNC interface)
POINT_INTF_VNC      = 2,
#Cấu Hinh Mouse sử dụng mode USB HID Absolute 
POINT_INTF_HID_ABS  = 3,
```

Example: 

```python
# Cấu hình Mouse sử dụng HID USB 
eLinkObj.setMouseMode("POINT_INTF_HID")
eLinkObj.setMouseMode(1)
#Cấu Hinh Mouse sử dụng mode VNC (Sử dụng VNC interface)
eLinkObj.setMouseMode("POINT_INTF_VNC")
eLinkObj.setMouseMode(2)
#Cấu Hinh Mouse sử dụng mode USB HID Absolute 
eLinkObj.setMouseMode("POINT_INTF_HID_ABS")
eLinkObj.setMouseMode(3)
```

#### eLinkObj.lockKeyboard     			

Lock Keyboard Option

````
Not support yet
````

#### eLinkObj.lockMouse         			

Lock Mouse Option

````
Not support yet
````

#### eLinkObj.setVncIdle 

TODO Consider to 

```python
eLinkObj.setBoosterScreenIdle(time:int)
```

Configure eLinkKVM send Screen Idle event when Screen unchanged in specific time (Idle time) 

```python
elinkObj.setVncIdle(200) # 200 ms timeout for idle event 
```

#### eLinkObj.setKeyIdle        			

Set key idle between 2 key 

````python
eLinkObj.setKeyIdle(200) # 200ms delay between 2 keys send
# Each character in string "hello world" will be send with delay time is 200ms 
eLinkObj.sendString("hello world") #
````

#### eLinkObj.matchScreen       			
Polling current screen and recognizing reference input image whether or not exist in the screen. Return None or MachingObj which content coordinate and size of maching zone. 
Matching Object data
```python
machingObj =[[x,y,w,h],[matching_score]] 
# rectangle = machingObj[0] #  Get Maching rectangle (x,y,w,h) , (x,y) coordinate calculate from top left (0,0) of screen
# rectangle_x = rectangle[0] # x coordinate 
# rectangle_y =  rectangle[1] # y coordinate 
# rectangle_w =  rectangle[3] # Width of match zone
# rectangle_h =  rectangle[4] # Height of match zone
# matching_score = machingObj[1]  # Matching score 
```

Example:  Recognizing test1.png in current screen with score >= 0.9 (0 - 1), attention period 500ms 

```python
matchData = eLinkObj.matchScreen("test1.png",score=0.9,attentionPeriod = 500)
```
Implementation of function `waitImage` 

```python 

def waitImage(eLinkObj, img, score=0.9, attentionPeriod=3000):
    print("wait for " + repr(img))
    while True:
        loc = eLinkObj.matchScreen(img, score, attentionPeriod)
        if loc[0] != None:
            break
        sleep(2)
    sleep((attentionPeriod + 500) / 1000)
    return loc[0]

matchingData = waitImage(elinkObj,"test1.png") 
x = int(matchingData[0])
y = int(matchingData[1])
w = int(matchingData[2])
h = int(matchingData[3])
print("Found {} in screen at x:{} y:{} width:{} height:{}".format("test1.png",x,y,w,h)
```

#### eLinkObj.ipmiConnect
```python
#TODO 
#consider for IPMI methods
ipmiObj = eLinkObj.ipmiConnect(<IpAddr>,<Usrname>,<Pass>) 
ipmiObj.power()
ipmiObj.reset() 
ipmiObj.reset(mode="USB") #reset to USB boot 
ipmiObj.reset(mode="BIOS") #reset to Biso setup
ipmiObj.activateSol() #activate IPMI SOL

```


Kết nối tới IPMI server 

`ipAddr`: Server Ip address

`UsrName`: Username IPMI 

`Pass`: Password IPMI

```python
#Connect to IPMI direct 10.42.0.100
#User name: "ADMIN" 
#Password: "ADMIN" 
eLinkObj.ipmiConnect("10.42.0.100", "ADMIN", "ADMIN")
#Kết nối tới IPMI through eLinkKVM
eLinkObj.ipmiConnect("elink-ipmi", "ADMIN", "ADMIN")

```

#### eLinkObj.ipmiPower         			

Dùng IPMI để power on server

```
eLinkObj.ipmiPower()
```

#### eLinkObj.ipmiReset

dùng IPMI để reset server 

````
eLinkObj.ipmiReset(0) #reset server 
eLinkObj.ipmiReset(1) #reset server to bios setup 
````

#### eLinkObj.ipmiStatus        			

ipmi status

```python
eLinkObj = elink.newConnection("10.42.0.3")
eLinkObj.ipmiConnect("10.42.0.100", "ADMIN", "ADMIN")
status_ret = eLinkObj.ipmiStatus()
print("{}".format(status_ret))
```

```bash
#1/0 IPMI connected/disconnected
#1/0 Server power status ON/OFF
#'status' String Status
[1, 0, 'Ipmi is connected'] 
```

#### eLinkObj.ipmiSolEnable

ipmi sol enable

```
Not support Yet
```

#### eLinkObj.remoteFileList    			

Get file list content in eLinkKVM

```python
TODO
fileMnger = eLinkObj.FileManager() # return fileMnger Object (contains some methods of remote file manager 
listFile = eLinkObj.remoteFileList("/A") 
listFile = eLinkObj.remoteFileList("/B")
# change to 
listFile = fileMnger.listFiles("A") #list all files contain in disk A 
listFile = fileMnger.listFiles("B") #list all files contain in disk B 
```

Example: 

```python
eLinkObj = elink.newConnection("10.42.0.3")
listFile = eLinkObj.remoteFileList()
print("file list {}".format(listFile))
listFile = eLinkObj.remoteFileList("/A")
print("file list {}".format(listFile)) 
```
python stdou return 

```shell 
file list [['A:', 1, 0]]
file list [['ver1.0_release_patch3.epg', 0, 1806264], ['floppy.hdd', 0, 1474560], ['floppy.hddx', 0, 33], ['Win2012.hdd2', 0, 457044992]]
```
eLinkObj.remoteFileList return List object content info of each directory/file entry 

Data structure for each entry 

``` C
struct entry = {
    filename: str 
    type : int (0/file, 1/directory)
    size :int (in bytes) (0 if entry is directory)
    md5 : str //TODO if entry is file (type=1) the field will contain MD5 of file 
}
```


#### eLinkObj.remoteFileDelete  			

delete remote file
```python
eLinkObj = elink.newConnection("10.42.0.3")
listFile = eLinkObj.remoteFileList("/A")
print("file list {}".format(listFile))
eLinkObj.remoteFileDelete("/A:/ver1.0_release_patch3.epg")
listFile = eLinkObj.remoteFileList("/A")
print("file list {}".format(listFile))
```

```shell 
file list [['ver1.0_release_patch3.epg', 0, 1806264], ['floppy.hdd', 0, 1474560], ['floppy.hddx', 0, 33], ['Win2012.hdd2', 0, 457044992]]
Deleting remote '\A:\/ver1.0_release_patch3.epg' file
file list [['floppy.hdd', 0, 1474560], ['floppy.hddx', 0, 33], ['Win2012.hdd2', 0, 457044992]]
```

#### eLinkObj.remoteFileRename 

Rename remote file 

```python
eLinkObj.remoteFileRename (<source>,<des>)
```

```python
eLinkObj = elink.newConnection("10.42.0.3")

listFile = eLinkObj.remoteFileList("/A")
print("file list {}".format(listFile))
print("Rename file ")
eLinkObj.remoteFileRename("/A:/floppy.hddx","/A:/rename_floppy.hddx")
listFile = eLinkObj.remoteFileList("/A")
print("file list {}".format(listFile))
print("restore rename")
eLinkObj.remoteFileRename("/A:/rename_floppy.hddx","/A:/floppy.hddx")
listFile = eLinkObj.remoteFileList("/A")
print("file list {}".format(listFile))
```

python stdout: 

```shell
current file list [['floppy.hddx', 0, 33], ['floppy.hdd', 0, 1474560], ['Win2012.hdd2', 0, 457044992]]
Rename file list [['rename_floppy.hddx', 0, 33], ['floppy.hdd', 0, 1474560], ['Win2012.hdd2', 0, 457044992]]
redo rename file list [['floppy.hddx', 0, 33], ['floppy.hdd', 0, 1474560], ['Win2012.hdd2', 0, 457044992]]
```



#### eLinkObj.remoteFileUpload  			

upload remote file

```python
eLinkObj = elink.newConnection("10.42.0.3")
listFile = eLinkObj.remoteFileList("/A")
print("current file list {}".format(listFile))
eLinkObj.remoteFileUpload("E:\project\elinkviewer_scripts\winpe_format.py",
						  "/A:/")
listFile = eLinkObj.remoteFileList("/A")
print("upload file list {}".format(listFile))
```
python stdout 
```shell
current file list [['floppy.hddx', 0, 33], ['floppy.hdd', 0, 1474560], ['Win2012.hdd2', 0, 457044992]]
Uploading 'E:\project\elinkviewer_scripts\winpe_format.py' file
100%
upload file list [['winpe_format.py', 0, 3620], ['floppy.hddx', 0, 33], ['floppy.hdd', 0, 1474560], ['Win2012.hdd2', 0, 457044992]]
```


#### eLinkObj.remoteFileDownload			

download remote file

```
Not support yet
```

#### eLinkObj.remoteFileCopy    			

copy remote file

```python
eLinkObj = elink.newConnection("10.42.0.3")
listFile = eLinkObj.remoteFileList("/A")
print("current file list {}".format(listFile))

eLinkObj.remoteFileCopy("/A:/floppy.hddx","/A:/copy_floppy.hddx")
listFile = eLinkObj.remoteFileList("/A")
print("Copy file list {}".format(listFile))
```

### Capture screen 

Step by step to capture reference image

1. Click Pause button `||`  in toolbar 
2. Press and hold"LCtrl" combine with click and drag mouse on screen zone 
3. eLinkViewer will create an template image `tmp_<xx>.png` in eLinkViewer folder. Using the image as reference input image for recognizing. 

![capture screen](https://lh3.googleusercontent.com/-s-0ObAxnfuY/W4YQ251OwTI/AAAAAAAAAIU/YhrmlqYxlLEcRC2EDZIdUf0t01VS6xzvgCHMYCw/s0/2018-08-29_10-19-49.gif)


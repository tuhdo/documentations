## eLink python script API 
### eLink API 
#### elink.newConnection("<eLinkKVM_IP>")
Create a new connection to eLinkKVM. The function will return eLink object. Ví dụ: 
```python
## connect to eLinkKVM với địa chỉ IP "10.42.02"
eLinkObj = elink.newConnection("10.42.0.2)
```
#### Các phương thức là eLink object 

#### eLinkObj.info()
Lấy thông tin của eLinkObj
```
Update later
```
#### eLinkObj.close
Close eLinkObj session

```python
## connect to eLinkKVM với địa chỉ IP "10.42.02"
eLinkObj = elink.newConnection("10.42.0.2)
## close connection
elinkObj.close()
```

#### eLinkObj.sendString        			

Gửi chuổi key string 

```python
#eLinkKVM sẽ gửi chuỗi key "hello world" tới Server
eLinkObj.sendString("hello world")	
```

#### eLinkObj.sendKey("<key>,mode)
Gửi key <Key> tới server với các mode khác nhau.
```python
# eLinkKVM send key <LeftShift> lên server 
eLinkObj.sendKey("LeftShift") # nhấn LeftShift và nhả phím 
eLinkObj.sendKey("LeftShift",1) # nhấn và giữ LeftShift 
eLinkObj.sendKey("LeftShift",0) # nhả phím LeftShift 
```

#### eLinkObj.sendMouse         			
Điều khiển Mouse bằng hàm sendMouse(<mode>,x,y)
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

Phương thức này sẽ lấy dữ liệu event từ eLinkKVM. Dưới đây là các event Id và ví dụ cho phương thức getEvent

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

```python
# below is process to check if event 5 existed => Press key F12
while True:
    e = vnc.getEvent() #get event object 
    d = e.getData("test") # get data file in event obj
    if e.getIdCode() == 5: #check event 5 (EVT_USB_KEY_SET_PROTOCOL) is existed
		vnc.sendKey("F12") # send key F12 to server 
    break
```

#### eLinkObj.clrEvent
Server khởi động gồm nhiều phase bao gồm Pre-Boot phase và OS phase. Ứng với mỗi phase server sẽ khởi động lại eLinkKVM, như vậy tương ứng eLinkKVM sẽ có nhiều event được lặp lại. Vậy nên cần thiết để có một hàm để clear event queue

```python
# Clear all existed event in queue and waiting for new event 5
vnc.clrEvent()
# below is process for waiting event 5 existed => Press key F12
while True:
    e = vnc.getEvent() #get event object 
    if e.getIdCode() == 5: #check event 5 (EVT_USB_KEY_SET_PROTOCOL) is existed
		vnc.sendKey("F12") # send key F12 to server 
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
vnc.setUsbMode(0,0) # reset UsbMode.
# Set eLinkKVM into an multiple usb device: including
# - Usb Key board 
# - Activate USB_MODE_VNC_HID to speed up Booster mode
# - Activate USB Mass storage mode which will mount image <win10.hdd2> 
vnc.setUsbMode("USB_MODE_KEY|USB_MODE_VNC_HID",0,["A:\win10.hdd2"]) 
vnc.setUsbMode(0x09,0,["A:\win10.hdd2"])
#only set USB_MODE_MSC (Usb mass storage)  
#mount <win10.hdd2> 
#mount <ubuntu.hdd2> 
vnc.setUsbMode(0,0,["A:\win10.hdd2"."A:\ubuntu.hdd2])
# Keep Usb KeyBoard and USB_MODE_VNC_HID (Booster)
# Unmount <win10.hdd2> 
vnc.setUsbMode("USB_MODE_KEY|USB_MODE_VNC_HID",0)
#USB Keyboard 
#Usb mode hid vnc (bootster) 
#Usb mouse absolute 
#Usb mass storage - mount <win10.hdd2> 
vnc.setUsbMode("USB_MODE_KEY|USB_MODE_VNC_HID|USB_MODE_MOUSE_ABS",0,["A:\win10.hdd2"]

```

#### eLinkObj.setVncMode   
##TODO Review the naming => change to eLinkObj.setOutputMode()

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
vnc.setVncMode("MODE_VNC_BOOSTER") #Set Booster mode
vnc.setVncMode("MODE_VNC_SERIAL") #Set Serial mode
vnc.setVncMode("MODE_VNC_RGB") #Set RGB mode
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
Sử dụng phương thức này để cấu hình lại chế độ cho mouse. Các chế độ cho mouse bao gồm 
```python
# Cấu hình Mouse sử dụng HID USB 
POINT_INTF_HID      = 1,
#Cấu Hinh Mouse sử dụng mode VNC (Sử dụng VNC interface)
POINT_INTF_VNC      = 2,
#Cấu Hinh Mouse sử dụng mode USB HID Absolute 
POINT_INTF_HID_ABS  = 3,
```

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

Cấu hình eLinkKVM sẽ gửi 1 idle timeout event sau 1 khoản <time> màn hình không thay đổi

```python
elinkObj.setVncIdle(200) # 200 ms timeout for idle event 
```

#### eLinkObj.setKeyIdle        			

Cấu hình tốc độ gửi key. 

````python
eLinkObj.setKeyIdle(200) # 200ms delay between 2 keys send
````

#### eLinkObj.matchScreen       			
Kiểm tra độ tương đồng của test.png trên screen hiện tại và trả về dữ liệu bao gồm toạ độ, chiều cao, chiều dài và điểm số tương đồng. 
Ví dụ: Nhận diện screen dựa trên img sẵn có

```python
matchData = eLinkObj.matchScreen("test1.png",score=0.9,attentionPeriod = 500)
# matchData[0]: [x,y,w,h] theo thứ tự là toạ độ (x,y) và (width,heigh) trong đó x,y tính từ góc trái, phía trên của screen. 
# matchData[1]: (Score) điểm số tương đồng. Nếu score không lớn hơn score định trước(0.9) thì matchData[0] = None
```
dưới đây là 1 hàm waitImage(...). Hàm này thực hiện việc nhận dạng liên tục screen hiện tại với ảnh tham chiếu <img>, sử dụng score để lọc đi các khung hình ko có sự tương đồng. Hàm này thực việc vòng lặp. Chỉ thoát khi có sự tương đồng với điểm số lớn hoặc bằng điểm số đã định nghĩa trước.

```python 

def waitImage(vnc, img, score=0.9, attentionPeriod=3000):
    print("wait for " + repr(img))
    while True:
        loc = vnc.matchScreen(img, score, attentionPeriod)
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

#### eLinkObj.ipmiConnect(<ipAddr>,<UsrName><Pass>) 
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

`ipAddr`: Ip address v4 của server 

`UsrName`: Username IPMI 

`Pass`: Password IPMI

```python
#Kết nối tới IPMI 10.42.0.100
#User name: "ADMIN" 
#Password: "ADMIN" 
vnc.ipmiConnect("10.42.0.100", "ADMIN", "ADMIN")
```

#### eLinkObj.ipmiPower         			

Dùng IPMI để power on server

```
eLinkObj.ipmiPower()
```

#### eLinkObj.ipmiReset(resetOpt)

dùng IPMI để reset server 

````
eLinkObj.ipmiReset(0) #reset server 
eLinkObj.ipmiReset(1) #reset server to bios setup 
````

#### eLinkObj.ipmiStatus        			

ipmi status

```

```

#### eLinkObj.ipmiSolEnable

ipmi sol enable

```

```

#### eLinkObj.remoteFileList    			

Get file list content in eLinkKVM
**TODO**

```python
fileMnger = eLinkObj.FileManager() # return fileMnger Object (contains some methods of remote file manager 
listFile = eLinkObj.remoteFileList("/A") 
listFile = eLinkObj.remoteFileList("/B")
# change to 
listFile = fileMnger.listFiles("A") #list all files contain in disk A 
listFile = fileMnger.listFiles("B") #list all files contain in disk B 
```



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
eLinkObj.remoteFileList trả về List object chứa các thông tin của các file/directory bao gồm 
``` 
Files/Directory entry = {
    filename: str 
    type : int (0/file, 1/directory)
    size :int (in bytes) (0 if entry is directory)
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

#### eLinkObj.remoteFileRename (<source>,<des>)

rename remote file 

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


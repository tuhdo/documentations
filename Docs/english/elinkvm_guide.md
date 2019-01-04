[TOC]



# eLinkKVM Guide

## Chapter 1: Introduction

A KVM switch (an abbreviation stands for "Keyboard, Video and Mouse")
is a hardware device that enables a user to control multiple computers
from one or more[1] sets of keyboards, video monitors, and mice.

The eLinkKVM is a device that provides over-the-internet
functionality, or "over-IP" in short, to KVM switches that do not
have built in internetwork functionality. Operators can monitor and
access their computers from remote locations using a remote control
software. An eLinkKVM device connects to a local area network or
directly to a personal computer (PC) using a standard ethernet cable,
then uses a USB cable and a video display cables to connect to a
server and complete control it with Keyboard, Video and Mouse
functionliaty from the eLinkKVM device.

Because the eLinkKVM uses the Internet as its data communication
medium, the server it is connected to can be accessed from any
authorized computer across the Internet, regardless of physical
location.

A user at a remote location connect to the eLinkKVM via its IP
address. Once a connection has been established and authorization
granted, the remote computer can exchange keyboard, video and mouse
signals with the remote server (of which the eLinkKVM is attached to**,
just as if they were physically present and working on the equipment
directly.

### Features ###

#### Hardware ####

| Type                        | Description                                                                          |
|-----------------------------|--------------------------------------------------------------------------------------|
| Networks                    | 2 Ethernet  ports (10/100Mbps)                                                       |
| Storage                     | Internal Flash Storage (8GB) that can be accessed by eLinkViewer software            |
| Interfaces                  | Micro SD-CARD (extend up to 64GB)                                                    |
|                             | RS232 interface                                                                      |
|                             | USB Host interface to extend to USB 3G/4G, USB Wifi, USB Storage                     |
| Video                       | VGA Port, Video Full HD Resolution                                                   |
|                             | VGA Text mode: 640x350, 640x480, 720x400                                             |
|                             | VGA Graphic mode: 640x480, 800x600, 1024x768, 1152x864, 1280x1024,                   |
|                             | 1440x900,1680x1050,1600x1200,1920 x1080                                              |
| Remote Access Features      | Support  VNC Protocol                                                                |
|                             | Emulation the USB Relative Mouse and Absolute Mouse                                  |
|                             | Emulation the USB Keyboard                                                           |
|                             | Capture Full HD resolution with **Hardware Mode**                                    |
|                             | Capture all resolutions with 100% screen quality using the patented **Booster Mode** |
| Connections                 | Direct Connect Through TCP/IP                                                        |
|                             | Extension through USB 3G/4G                                                          |
|                             | Coming the Cloud Service to connect behind Firewall                                  |
| Securities                  | Secure by SSL                                                                        |
|                             | Multiple Login Accounts (Up to 8 users)                                              |
| Remote Server Power Control | Remote Reset/On/Off  Server through an IPMI GUI Interface from eLinkViewer           |
|                             | Control the External PDU through RS232                                               |
| Virtual Media               | Disk images (.iso, .raw, .hdd, .hdd2** can be mounted as a USB 2.0 devices on        |
|                             | on a remote computer for easy software installation and system updates               |


#### eLinkViewer ####

**eLinkViewer*** is an application specifically made to view remote
screen content captured by an eLinkKVM device as well as interact with
a remote computer. 

**eLinkViewer** also provides functionalities to manage an eLinkKVM device.
    
| Type                   | Description                                                                      |
|------------------------|----------------------------------------------------------------------------------|
| General                | Support multiple VNC Server and eLinkKVM                                         |
|                        | Remote protocol using VNC and extension commands for eLinkKVM                    |
|                        | Support video scaling and full screen                                            |
| Automation             | Support image recognization and Python scripting allow automation the activities |
| IPMI                   | Support IPMI protocol to control server with GUI                                 |
| Platform               | Currently support Windows                                                        |
| Bandwidth Optimization | Provide video quality settings to maximze remote performance for the available   |
|                        | network bandwith                                                                 |
| Screen scaling         | Viewer screen can be scaled to any resolution independent from remote computer's |
|                        | resolution or even enter a full-screen mode. In full-screen mode, the viewer     |
|                        | screen scales according to the remote computer's resolution.                                                                                 |


### eLinkKVM components ###

![eLinkKVM](https://drive.google.com/a/elinkgate.com/uc?id=1Inpd1l5-inhGNrO2rQHngclQskfswmQ4)

#### Front view #####

| ID | Component  | Description                                                                                      |
|----|------------|--------------------------------------------------------------------------------------------------|
| 1  | USB Type-B | power the device and acts as a communication channel between eLinkKVM and a server               |
| 2  | Power      | the secondary source is supplied by a micro USB cable. It is neccessary when the power           |
|    |            | from USB Type B port is insufficient, or keeping the connection to eLinkKVM                      |
|    |            | alive when the server is power off.                                                              |
| 3  | VGA        | For capturing and outputting video signal to send and receive over the internet.                 |
| 4  | RS232      | the serial communication port (COM port). This port will be connected to the server serial port. |

#### Rear view #####

| ID | Component         | Description                                                              |
|----|-------------------|--------------------------------------------------------------------------|
| 1  | Ethernet ports    | Master: can be configured as a DHCP server, a DHCP client or a static IP |
|    |                   | Slave: can be configured as a DHCP Client or a static IP                 |
|    |                   |                                                                          |
| 2  | SD card           | allows a user to expand storage capacity with an external micro SD card  |
| 3  | Status Leds 1,2,3 | signal device statuses through different led colors                      |
| 4  | USB Type-A        | allow to attach an external peripheral device such as USB 3G/4G,         |
|    |                   | USB Mass Storage, etc., to extend eLinkKVM functionality.                |

### Chapter 2: Hardware Setup ###

### System Requirements ###

#### Device and cables

- 1 computer to be controlled
- 1 eLinkKVM device 
- 1 Ethernet RJ45 cable
- 1 USB type B cable

Optional:

- 1 Micro USB cable connected to a 5v power source
- 1 VGA cable
- 1 RS232 cable

#### Remote computer ####
    
A remote computers is a computer connected to the control cables
(USB for input and VGA for output) that are connected to an eLinkKVM
device. The following equipment must be available a remote computer:

 - 1 VGA port
 - 1 USB Type-A port at the minimum.

#### Local computer ####

A local computer is a computer that a user physically interact with to
control a remote computer through an eLinkKVM device connected to the
remote computer.
   
#### Operating Sytems ####

Supported operating systems for a local computer:

- Windows 7, 8, 10.
- Windows Server 2012.

Supported operating systems for a remote computer:

- Windows 7, 8, 8, 10.
- Windows Server 2012.

#### eLinkKVM configuration ####

![PoweringDevice](https://drive.google.com/a/elinkgate.com/uc?id=1OAJvfReUiWDwjh7OlbuqVG67y7u4K5KJ) 

1. Use a USB Type-B cable to connect a remote computer and the Type-B port of an eLinkKVM device.
2. Use a Micro USB cable to connect to a 5v power supply.

A user can use one of the two methods or both to power up a device.

##### Network configuration #####

eLinkKVM supports two Ethernet ports for network connection:

- Ethernet Master: by default, configured as a DHCP server.
- Ethernet Slave: by default, configured as a DHCP client.

To connect to an eLinkKVM device, a network connection between a local
computer and an eLinkKVM device is required. The connection can either
be:

- *Direct connect*: An Ethernet cable connects directly between a
  local computer and an eLinkKVM device.
  
- *Local Area Network*: Both the local computer and an eLinkKVM device
  are connected to a local area network (LAN). eLinkKVM is plugged to
  the router of the network.
  
- *Over the Internet*: an eLinkKVM device is provided with a static
  address for a local computer to access it anywhere in the world.

When a connection is established, its network interface must be
configured in the operating system of the local computer. Currently,
only Windows is supported.

###### Windows ######

1. Open `Control Panel` -> `All Control Panel Items` -> `Network Connections`.

[TODO] Add an demo picture

2. Right click on Ethernet Device of the eLinkKVM connection, select `Properties.

[TODO] Add an demo picture

3. Double click `Internet Protocol version 4 (TCP/IPv4)`

[TODO] Add an demo picture

4. Check the following options:

- Ontain an IP Address automatically
- Obtain DNS server address automatically

### Chapter 3: Remote management software for eLinkKVM with eLinkViewer ###

#### Software interface ####

##### Login #####

* **Quick Connect** 

![Elink viewer login Quick Connect](https://drive.google.com/a/elinkgate.com/uc?id=1XmJUH4yOOTuo_9ddt71yyWvzMEC1m-85)

**Server**: set IP address for current eLinkKVM unit

**Connect**: request eLinkViewer to eLinkKVM at the IP address entered in **Server** field

**Options**: configure eLinkKVM-VNC connection

![Connection option UI](https://drive.google.com/a/elinkgate.com/uc?id=1RqCDvR-cw-CcmGMrVCuZFZn-O6kXr6SJ)

**Scan**: Scan for all eLinkKVM devices in the current local area network (LAN)

* **Local Account** (not yet supported)

![Login UI - Local account ](https://drive.google.com/a/elinkgate.com/uc?id=1TgNk-qYV2ITAd9XqZ6yzV2J3URya3QFL)

A user can create a personal account to store information of many eLinkKVM devices. Account information is securely stored on the PC that runs the eLinkViewer software.

* **Online account** (not yet supported)

![Login UI ](https://drive.google.com/a/elinkgate.com/uc?id=1Is5PUf2P7s50cSrh3iAeDoZ8KzRwqmys)

For **Online Account** (Beta - not support yet), eLinkViewer allows a user store login information and other eLinkKVM devices, similar to a local account. However, the information is stored on a cloud server instead of a local PC.

## Basic usage

### Power up an eLinkKVM device

A USB Type-B connector from the server to an eLinkKVM device suffices to power up the device. But in some cases, it is necessary to keep the device active, while the **Server** can be turned off. This can be done by supplying another 5V power source to the micro USB port on an eLinkKVM device.


## Static IP configuration

Steps to configure static IP for an eLinkKVM device:

1. Power up an eLinkKVM device and wait for the device to start up completely (all LED1 , LED2, LED 3 light up).

2. Use a RJ45 cable to connect a PC to the Ethernet Master port. The default IP is `*10.0.0.1***.

3. Configure network interface for the PC:

- Open **Network connections** -> Right Click on network interface to eLinkKVM (usually unidentified) ->  Click **Properties***.

Then, configured **Internet Protocol Version 4**: 

![Ethernetconfigure](https://drive.google.com/a/elinkgate.com/uc?id=1PcuZEkauX3GhBpVFTJkWjPxHQSoPUDGZ)
![EtherConfiguration](https://drive.google.com/a/elinkgate.com/uc?id=1bB02ODJ5dBMrX3R-2wmmpRe1KreA1jAo)

4. Open eLinkViewer and connect to `*10.0.0.1*`

![MasterConnect](https://drive.google.com/a/elinkgate.com/uc?id=1pDbmgGfgn38E0m4jOBbdHlOZreElEKPa)

5. eLinkKVM configuration user interface:

![eLinkKVM configure](https://drive.google.com/a/elinkgate.com/uc?id=11q7Rh8irV4Vz6LvYXo-ygD0ZcJjJ8Y89)

**Example**
![eLinkKVM configure ui](https://drive.google.com/a/elinkgate.com/uc?id=1cysTb7rS4BjjY-7PkymnbuA9-GhlAfqa)

___
## Connect to eLinkKVM

### Connection user interface

![eLinkKVMToolBar](https://drive.google.com/a/elinkgate.com/uc?id=1z8x6QtmbukgJQwigmqJuqkVsrzErp6cY)

1. Create a new connect to an eLinkKVM device
2. Store current vnc session as a `.vnc` file
3. eLinkKVM connect options
4. Current connection status
5. Pause frame transmitting
6. Request refresh current remote screen
7. Send `Ctrl + Alt + Delete` key combination
8. Press/Hold `Ctrl` key
9. Press/Hold `Alt` key
10. Open eLinkViewer `File Transfer` window
11. Scale in
12. Scale out
13. Scale (100%)
14. Auto zoom 
15. Full screen (press `Ctrl + Shift + Alt + F` to return to windowed eLinkViewer)
16. Turn booster mode on/off
17. Configure eLinkKVM 
18. Open event log 
19. Open Python script command prompt
20. Disconnect
21. Scan IPMI 

### Configure eLinkKVM

![ElinkKVMConfigurationUi](https://drive.google.com/a/elinkgate.com/uc?id=1ZAKrwEi7X0q1qR8OcmzzJ2qbD2X0WsQd)

eLinkKVM configuration includes: 

* Key:

* HID USB : use real keyboard (USB)
* HID VNC : use software keyboard (VNC protocol)
* Serial: use software keyboard (serial protocol)

* Mouse: 

* HID USB : use real mouse (USB)
* HID VNC: use software mouse (VNC protocol)
* ABS USB: use real mouse, but sync both local and remote mouse as one mouse pointer (USB absolute hid)

* Video:

* Dummy : configure network and serial connections
* VGA: configure VGA display
* Booster: enable remote management with Booster technology
* Serial: enable serial display and communication
* IPMI:  enable Serial Over Lan (SOL) with IPMI 

* File browsing and disk image mounting:

* Path 0 to 3: File paths to disk images

* `Browse` button allows navigating to the disk images with a file explorer:

![FilebrowsingELinkKVM](https://drive.google.com/a/elinkgate.com/uc?id=1CVYABQC3zRPPt84Bs9G-QeivPD2uh1AR)

* Example: Configure eLinkKVM to use USB Key, Vnc Mouse and Booster mode with `refind.hdd2` disk image: 

![](https://drive.google.com/a/elinkgate.com/uc?id=13nAvrjHhx9Y94-ct4pjFXBFSQu75mYSU)

### IPMI Command Center 

IPMI Interface:

![](https://drive.google.com/a/elinkgate.com/uc?id=1JZqcasrMUA6Nd1l--fKWEIWDT3r3WtJL)

IPMI command center allows a user to scan servers with IPMI ports in a local area network and connect to these server to run IPMI commands.

* Start IP: start IP to begin scanning
* Stop IP: End IP to end scanning
* User Name - Password: user name and password for each IPMI server. For example, default username and passwork are ADMIN/ADMIN for a SuperMicro server.
* Scan : start scanning for an IPMI server 
* Stop: End a current scanning process
* Connect: connects to an IPMI server. When an IPMI server is found, an IP address is display, click on the IP address to select then enter a Username and Password.
* Power On: Turn a server on with IPMI
* Reset  with ![option](https://drive.google.com/a/elinkgate.com/uc?id=1sc2g-bPFQP7vRPfZ6SFIddJLa21OkOUn)  
* Reset : restart a server
* Reset to Bios Setup: restart a server and enter BIOS
* Reset to USB: restart a server and boot with a USB device
* Sol Active: enable IPMI management with Serial Over Lan (SOL)
* Close : Close IPMI command center

Use IPMI command center to scan and run IPMI commands. 

* Click ![IPMI Scan](https://drive.google.com/a/elinkgate.com/uc?id=1UjcwiThAiZ_XaAnF1zviG2hflCgd4uCJ)
* Enter Start IP and end IP. Limit the ranger of IP scanning. 
* Click `Scan` to start scanning. Found IPMI servers are displayed as a list.
* Click on one of the found IPMI IP addresses, enter `Username` and `Password`, then click **`Connect`** 
* Click **`Power On`**,  **`Reset`**, etc., to run appropriate IPMI commands.

![IPMI_Scanning](https://drive.google.com/a/elinkgate.com/uc?id=1YlFJlJNrXDe7gTgu0r_rwJqCUgGSRJ1z)


### Scale in/out/100/auto 

Elinkviewer supports screen scaling.

![scalingwindow](https://drive.google.com/a/elinkgate.com/uc?id=1eH2ngwZ-V6stvPc8yc9P5rEjHpcijvFQ) 

### Upload file to an eLinkKVM device using File Transfer

![FileTransfering](https://drive.google.com/a/elinkgate.com/uc?id=1GxA_1EL_1K73yQ5nnnYQ6wVgxPXzgb-X)

eLinkViewer allows data transfer from a local PC to an eLinkKVM device  with `File Transfer`: 

* Click **`File Transfer`** on eLinkViewer toolbar . `File Transfer` window appears. To the left is a directory tree of the local PC, to the right is the directory tree of the eLinkKVM device. 
* Browse the local directory tree and select a file or directory to upload to an eLinkKVM device. Next, on the directory tree of the eLinkKVM device, select a path to store the file or directory.
* Finally, click the button **`>>`** to transfer the selected file/directory. A confirm dialog appears. Click **`Yes`** to confirm or click **`No`** cancel the action. After confirming the transfer, the transfer starts and a progress bar that displays the transfering process starts running.

### Disconnect from an eLinkKVM device

* Click the button ![ExitButton](https://drive.google.com/a/elinkgate.com/uc?id=1y4Ru1fD3a0UXBERF7mDh7IIxqA8cKRuc)
* The dialog box ![exit inform](https://drive.google.com/a/elinkgate.com/uc?id=1U4jmMjBL-9p-x9IK-kWMX2MVIIoDaqgZ) announces connection successfully terminated. 

![Exit connection ](https://drive.google.com/a/elinkgate.com/uc?id=1MC_UUz0tERNfc2TGCudEGgF-77M3aKYT)

### Remote control with Booster mode 

![Booster mode remote control](https://drive.google.com/a/elinkgate.com/uc?id=1yJGy1_O6FCYe0uyvxdja5eGSYl8vvWfC)

### Remote control with VGA mode 

![RemoteControlVGA](https://drive.google.com/a/elinkgate.com/uc?id=1GWzc9F2mUWN8A-fbLGQ3KqBzPEhhe6D9)

### Remote control with auto Booster mode 

eLinkViewer supports auto Booster mode to switch from the current mode to Booster automatically without configuring.

![BoosterToogle](https://drive.google.com/a/elinkgate.com/uc?id=1eICc_jsFSHaxtbGZoFrZM1yNJwmxYS1J)

### Customize auto Booster Mode 

To make it convenient to switch between Booster and other modes, eLinkViewer allows a user to customize Auto Booster Toggle button. Pressing this button allows a user to switch between a pre-configured Booster mode and the current mode.                                                                                          ![ToogleButtonConfig](https://drive.google.com/a/elinkgate.com/uc?id=1BtRGCSRGPBNN-vy86_nDGfr4qM823pgH)               


Steps tto configure Auto Booster mode:

1. Click `eLink Configuration`

2. From `eLink Configuration`, on `Auto Booster Mode Setting`, select a remote display mode.

3. Similarly, select a Key mode

4. Next, select a Mouse mode

5. Select `Base` to confirm configuration. This configuration is used whenever `Auto Booster Mode` button is clicked.

6. Press OK to save the configuration.

7. Press OK to confirm.

### Manual configuration with file

eLinkKVM supports configuration with a text file. Steps: 

![ConfigureFileConfig](https://drive.google.com/a/elinkgate.com/uc?id=1iKrSG4coRPMnUkbcNSEplJtHuewuhxkD)

1. Press `Enter Configuration` button an eLinkKVM device. The firmware on the eLinkKVM device then configures itself as a storage device.
2. Open the drive `ELINKCONF`.
3. In `ELINKCONF` drive, there is a configuration file that can be editted by any text editor. 
4. Edit the file following eLinkKVM configuration syntax. Store the file and reset eLinkKVM to use the new configuration.

![gifConfigureFile](https://drive.google.com/a/elinkgate.com/uc?id=1Bkt9flkzvf36T-5rNGA_HJH9VIdlZom1)

### Upgrade firmware for eLinkKVM

![firmware upgrade](https://drive.google.com/a/elinkgate.com/uc?id=1UH_-a08spJ2ufRyOcmENWefrBHTXXSit)

### Scan eLinkKVM in a local area network

eLinkViewer can scan for eLinkKVM devices in a local area network (LAN).

![ScaneLinkKVM](https://drive.google.com/a/elinkgate.com/uc?id=1JCnvvzjPa8L-eCFzl6kNBceS22OjBTGq)

[TOC]



# Hướng dẫn sử dụng eLinkKVM 

## ElinkKVM



## Các giao tiếp của thiết bị 

![eLinkKVM](D:\Project\bitbucket\elinkkvm_guide\Resource\eLinkKVM_Overview.jpeg)

Thiết bị bao gồm các cổng kết nối dưới đây: 

**Mặt trước** 

- UBS type B Cấp nguồn cho thiết bị và đồng thời làm kênh giao tiếp cho công nghệ elinkKVM 
- Power : Nguồn thứ cấp cho thiết bị. Có thể không cần 
- VGA IN : VGA đầu ra của Host - VGA đầu vào thiết bị 
- RS232 : Cổng giao tiếp kết nối serial ( COM port ). Cổng này sẽ được nối với cổng serial của server 

**Mặt sau** 

* 2 cổng Ethernet 
  * Master: .... 
  * Slave: .... 
* SD card: Giao tiếp để người dùng có thể cắm thêm thẻ micro sd để tăng dung lượng lưu trữ 
* Led trạng thái 1,2,3: Thông báo trạng thái của thiết bị bằng cách hiển thị màu led 
* USB A:  Cổng cắm các thiết bị usb mở rộng cho eLinkKVM 

## Giới thiệu phần mềm điều khiển từ xa eLinkViewer

### Giao diện phần mềm 

#### Giao diện đăng nhập

* **Quick Connect** 

![Elink viewer login Quick Connect](https://drive.google.com/a/elinkgate.com/uc?id=1XmJUH4yOOTuo_9ddt71yyWvzMEC1m-85)

**Server**: Nhập địa chỉ IP của eLinkKVM 

**Connect**: Yêu cầu eLinkViewer kết nối tới eLinkKVM ở địa chỉ ở mục **Server**  

**Options**: Yêu cầu hiện họp thoại để tuỳ chỉnh các cấu hình cho kết nối eLinkKVM-VNC 

**Giao diện cửa sổ** **Connection options **

![Connection option UI](https://drive.google.com/a/elinkgate.com/uc?id=1RqCDvR-cw-CcmGMrVCuZFZn-O6kXr6SJ)

* **Local Account** 

  ![Login UI - Local account ](https://drive.google.com/a/elinkgate.com/uc?id=1TgNk-qYV2ITAd9XqZ6yzV2J3URya3QFL)

  Người dùng có thể tạo một tài khoản cá nhân để lưu trữ các thông tin của các eLinkKVM. Thông tin tài khoản này sẽ được bảo mật và lưu trữ cục bộ tại chính PC chạy phần mềm ELinkViewer

* **Online account** 

![Login UI ](https://drive.google.com/a/elinkgate.com/uc?id=1Is5PUf2P7s50cSrh3iAeDoZ8KzRwqmys)

Đối với mục **Online Account** (Beta - not support yet). ELinkViewer cho phép người dùng tạo 1 cloud account để lưu trữ các thông tin đăng nhập và các eLinkKVM đã được kết nối. 



## Các thao tác cơ bản

### Cấp nguồn cho thiết bị

Nguồn cấp cho thiết bị có thể lấy từ từ kết nối USB từ máy chủ đến **USB Type B connector** của thiết bị. Nhưng trong một số trường hợp cần giữ cho thiết bị luôn hoạt động, trong khi đó **Máy Chủ** có thể được tắt. Nên việc cung cấp nguồn cho eLinkKVM có thể thực hiện bằng cách sử dụng nguồn điện 5V tới lỗ nguồn của thiết bị bằng kết nối USB micro



## Cấu hình địa chỉ IP cho thiết bị 

Các bước để cấu hình địa chỉ IP cho thiết bị eLinkKVM 

1. Cấp nguồn cho thiết bị eLinkKVM và đợi thiết bị khởi động xong (LED1 , LED2, LED 3 đều sáng)

2. Dùng cáp RJ45 để kết nối từ PC tới cổng Ethernet Master của thiết bị. Địa chỉ IP mặc định của thiết bị là `*10.0.0.1*`

3. Cấu hình mạng cho máy tính 

   Mở cửa sổ Network connections -> Right Click kết nối Ethernet kết nối tới eLinkKVM ->  Properties 

   Sau đó cấu hình **Internet Protocol Version 4** như sau 

   ![Ethernetconfigure](https://drive.google.com/a/elinkgate.com/uc?id=1PcuZEkauX3GhBpVFTJkWjPxHQSoPUDGZ)

   ![EtherConfiguration](https://drive.google.com/a/elinkgate.com/uc?id=1bB02ODJ5dBMrX3R-2wmmpRe1KreA1jAo)

   

4. Sử dụng eLinkViewer và kết nối tới địa chỉ `*10.0.0.1*`

   ![MasterConnect](https://drive.google.com/a/elinkgate.com/uc?id=1pDbmgGfgn38E0m4jOBbdHlOZreElEKPa)

5. Giao diện cấu hình eLinkKVM 

   ![eLinkKVM configure](https://drive.google.com/a/elinkgate.com/uc?id=11q7Rh8irV4Vz6LvYXo-ygD0ZcJjJ8Y89)

   Giao diện cấu hình eLinkKVM+

   ![eLinkKVM configure ui](https://drive.google.com/a/elinkgate.com/uc?id=1cysTb7rS4BjjY-7PkymnbuA9-GhlAfqa)



## Kết nối tới eLinkKVM

### Giao diện kết nối 

![eLinkKVMToolBar](https://drive.google.com/a/elinkgate.com/uc?id=1z8x6QtmbukgJQwigmqJuqkVsrzErp6cY)

1. Tạo một kết nối eLinkKVM mới 
2. Lưu session vnc hiện tại thành file .vnc 
3. tuỳ chọn cho eLinkKVM connection 
4. thông tin kết nối hiện tại 
5. Tạm dừng việc truyền nhận frame 
6. yêu cầu refresh lại màn hình điều khiển 
7. Gửi tổ hợp phím Ctrl + Alt + Delete 
8. nhấn/giữ phím Ctrl 
9. nhấn/giữ phím Alt 
10. mở cửa sổ eLinkViewer File Transfer 
11. phóng lớn (scale in)
12. thu nhỏ (scale out) 
13. scale (100%)
14. scale tự động 
15. Full screen (nhấn phím Ctrl + Shift + Alt + F để về trạng thái cũ)
16. Tắt/bật chế độ booster mode 
17. Cấu hình eLinkKVM 
18. Bật cửa sổ event log 
19. mở cửa sổ Python script
20. Thoát kết nối 
21. Scan IPMI 

### Cấu hình eLinkKVM

![ElinkKVMConfigurationUi](https://drive.google.com/a/elinkgate.com/uc?id=1ZAKrwEi7X0q1qR8OcmzzJ2qbD2X0WsQd)

Cấu hình eLinkKVM chia làm các mục dưới đây: 

* Key: Bao gồm 

  * HID USB : keyboard thực (USB)
  * HID VNC : Keyboard software (VNC protocol)
  * Serial: … 

* Mouse: 

  * HID USB : Mouse thực (USB)
  * HID VNC: mouse software (VNC protocol)
  * ABS USB: Mouse hardware (USB absolute hid)

* Video 

  * Dummy : màn hình dummy dùng để cấu hình network, Serial 
  * VGA: VGA display
  * Booster: kích hoạt chế độ điều khiển từ xa dùng giao thức booster 
  * Serail: kích hoạt chế độ hiển thị serial 
  * IPMI: kích hoạt chế độ hiển thị SOL với IPMI 

* Duyệt file và chỉ định mount ảnh đĩa 

  * Path 0…3 : Nhập các ảnh đĩa muốn mount vào hệ thống 

  * nút Browser cho phép duyệt file đang lưu trữ 

    ![FilebrowsingELinkKVM](https://drive.google.com/a/elinkgate.com/uc?id=1CVYABQC3zRPPt84Bs9G-QeivPD2uh1AR)

  * Ví dụ: Cấu hình eLinkKVM chế độ sử dụng Key USB, Mouse Vnc, Booster mode với ổ đĩa refind.hdd2 như sau: 

    ![](https://drive.google.com/a/elinkgate.com/uc?id=13nAvrjHhx9Y94-ct4pjFXBFSQu75mYSU)

### IPMI Command Center 

Giao diện IPMI command center 

![](https://drive.google.com/a/elinkgate.com/uc?id=1JZqcasrMUA6Nd1l--fKWEIWDT3r3WtJL)

IPMI command center cho phép người dùng scan các server có port IPMI trong mạng nội bộ (local network) và kết nối tới các server này để chạy các lệnh IPMI.

* Start IP: Địa chỉ IP bắt đầu scan 
* Stop IP: Địa chỉ IP kết thúc scan 
* User Name - Password: user name và password ứng với mỗi IPMI server. Ví dụ, Super Micro server sử dụng username/passwork là ADMIN/ADMIN. Đối với DELL thì là ROOT/<NULL> (Tự cấu hình)
* Scan : khởi động quá trình scan IPMI server 
* Stop: Dừng quá trình scan IPMI server 
* Connect: kết nối IPMI tới server. Khi tìm thấy một server IPMI, click chọn server đó, nhập Username và Password 
* Power On: Bật server dùng IPMI 
* Reset  with ![option](https://drive.google.com/a/elinkgate.com/uc?id=1sc2g-bPFQP7vRPfZ6SFIddJLa21OkOUn)  
  * Reset : khởi động lại server 
  * Reset to Bios Setup: Khởi động lại server và vào màn hình cấu hình bios 
  * Reset to USB: Khởi động lại USB và boot bằng USB 
* Sol Active: khởi động màn hình serial over LAN 
* Close : đóng cửa sổ IPMI Command Center 

Sử dụng IPMI command center để scan và thực hiện các lệnh IPMI. 

* Nhấp vào giao diện ![IPMI Scan](https://drive.google.com/a/elinkgate.com/uc?id=1UjcwiThAiZ_XaAnF1zviG2hflCgd4uCJ)
* Điền địa chỉ IP bắt đầu và địa chỉ IP kết thúc. Giới hạn phạm vi IP scan. 
* Click vào button scan -> quá trình scan bắt đầu. Các IPMI server sẽ hiển thị ở mục list box bên dưới. 
* Click vào các địa chỉ IPMI tìm được, điền User name và password sau đó click vào button **`Connect`** 
* Click vào các nút **`Power On`**,  **`Reset`** ... để thực thi các lên PIMI tương ứng

![IPMI_Scanning](https://drive.google.com/a/elinkgate.com/uc?id=1YlFJlJNrXDe7gTgu0r_rwJqCUgGSRJ1z)



### Scale in/out/100/auto 

Elinkviewer hỗ trợ việc scaling cửa sổ window

![scalingwindow](https://drive.google.com/a/elinkgate.com/uc?id=1eH2ngwZ-V6stvPc8yc9P5rEjHpcijvFQ) 

### Upload file lên eLinkKVM sử dụng File Transfer window

![FileTransfering](https://drive.google.com/a/elinkgate.com/uc?id=1GxA_1EL_1K73yQ5nnnYQ6wVgxPXzgb-X)

eLinkViewer cho phép việc truyền dữ liệu từ local đến eLinkKVM thông qua giao diện eLink File Transfer. Mở giao diện eLinkKVM bằng cách 

* Click vào icon **`File Transfer`**  in eLinkViewer toolbar . Giao diện Fire transfer hiện ra. Bên trái cửa sổ là cây thư mục của local, bên phải là cây thư mục của eLinkKVM. 
* Duyện cây thư mục ở cây thư mục và lựa chọn file hoặc thư mục muốn upload tới eLinkKVM. Sau đó, trên cây thư mục eLinkKVM lựa chọn đường dẫn muốn lưu. 
* Cuối cùng là click vào nút nhấn **`>>`** để thực hiện thao tác tải file/thư mục đã chọn. Một hộp thoại xác nhận sẽ hiện ra để confirm thao tác. Click **`Yes`** để xác nhận quá trình truyền hoặc click **`No`** để huỷ thao tác. Sau khi bấm nút OK xác nhận quá trình truyền, trên giao diện sẽ xuất hiện một thanh progress bar để hiển thị trạng thái của quá trình truyền file 

### Ngắt kết nối eLinkKVM 

* Click vào button ![ExitButton](https://drive.google.com/a/elinkgate.com/uc?id=1y4Ru1fD3a0UXBERF7mDh7IIxqA8cKRuc)
* Hộp thoại ![exit inform](https://drive.google.com/a/elinkgate.com/uc?id=1U4jmMjBL-9p-x9IK-kWMX2MVIIoDaqgZ) thông báo kết nối đã được ngắt 

![Exit connection ](https://drive.google.com/a/elinkgate.com/uc?id=1MC_UUz0tERNfc2TGCudEGgF-77M3aKYT)

### Điều khiển từ xa sử dụng booster mode 



![Booster mode remote control](https://drive.google.com/a/elinkgate.com/uc?id=1yJGy1_O6FCYe0uyvxdja5eGSYl8vvWfC)

### Điều khiển từ xa sử dụng VGA mode 

![RemoteControlVGA](https://drive.google.com/a/elinkgate.com/uc?id=1GWzc9F2mUWN8A-fbLGQ3KqBzPEhhe6D9)

### Điều khiển từ xa quick toogle booster mode 

eLinkViewer hỗ trợ quick toogle booster mode với 1 mode hiện đang cấu hình 

![BoosterToogle](https://drive.google.com/a/elinkgate.com/uc?id=1eICc_jsFSHaxtbGZoFrZM1yNJwmxYS1J)

### TODO 

Anh cần thêm mục nào vào thì cứ dùng cú pháp 

```
​```
### TODO <Nội dung cần thêm> 
​```
```


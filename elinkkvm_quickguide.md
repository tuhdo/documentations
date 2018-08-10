





[TOC]

# Quick start guide 

## Thiết bị bao gồm 

- 1 eLinkKVM 
- 2 Ethernet cable RJ45 
- 1 cáp USB type B
- 1 cáp USB micro 
- 1 nguồn USB 5V 
- 1 cáp VGA 
- 1 cáp RS232 

## Cấu hình cho thiết bị 

### Cấp nguồn cho thiết bị

![PoweringDevice](https://drive.google.com/a/elinkgate.com/uc?id=1OAJvfReUiWDwjh7OlbuqVG67y7u4K5KJ) 

1. Dùng cáp USB type B kết ngồi giữa PC và cổng USB B 
2. Dùng cáp USB micro kết nối nguồn usb với cổng Power 

![](https://drive.google.com/a/elinkgate.com/uc?id=1AEfa2yDwBeN2BnYtEs4LHTZI5bxHUZMw)

Kết nối cổng RJ45 giữa giữa PC và cổng Ethernet Master của eLinkKVM. Cấu hình card mạng của host PC 

![Configure network ](https://drive.google.com/a/elinkgate.com/uc?id=1obtGhWgw4RsYaIL0RRn4P5UuTaB_ibTT)

1. Mở cửa sổ `Control pannel` vào thư mục `Control Panel\All Control Panel Items\Network Connections` 
2. Nhấp chuột phải lên Ethernet Device kết nối với eLinkKVM -> chọn mục `Properties `
3. Nhấp đôi vào mục `Internet Protocol version 4 (TCP/IPv4)` 
4. Trong cửa sổ `Internet Protocol version 4 (TCP/IPv4) Properties` chọn option 
   - Obtain an IP Address automatically 
   - Obtain DNS server address automatically 

### Cấu hình IP address cho eLinkKVM

Địa chỉ IP mặc định cho cổng Ethernet Master của eLinkKVM là `10.0.0.1` 

![eLinkKVMConfig](https://drive.google.com/a/elinkgate.com/uc?id=1H7-BtcI8SNSALvVU2VUl4YM6_94b5jJI)

1. Chạy chương trình eLinkKVM 

2. Điền địa chỉ mặc định `10.0.0.1` của eLinkKVM vào trường `Server` 

3. Click chuột vào `Connect` để kết nối vào eLinkKVM 

4. Cửa sổ kết nối eLinkKVM hiện ra. Dùng chuột click vào các trường IP addres, Netmask ... để cấu hình 

   *Lưu ý:* 

   * Ethernet 0  tương ứng với cổng Slave
   * Ethernet 1 tương ứng với cổng Master

Ví dụ ở đây là cấu hình IP address cho Slave là  

```
Ip address: 10.42.0.2
Netmask: 	255.255.255.0 
GateWay: 	10.42.0.1 
DNS: 		10.42.0.1
```

## Điều khiển PC/Server từ xa thông qua eLinkKVM 

### Thiết bị bao gồm 

1 PC đóng vai trò điều khiển từ xa dùng phần mềm `eLinkViewer` gọi là `MASTER `

1 Server/PC bị điều khiển từ xa thông qua KVM gọi là `SLAVE` 

1 eLinkKVM 

1 cáp Ethernet RJ45 kết nối từ cổng `SLAVE` của `eLinkKVM` tới mạng nội bộ

1 VGA kết nối từ `VGA OUT` của `Slave` với `VGA IN` của `eLinkKVM`

1 USB type B kết nối giữa `Slave` tới cổng `USB B` của eLinkKVM

1 USB micro kết nối từ `Slave`/nguồn USB tới cổng `POWER` eLinkKVM

### Kết nối 

![RemoteControlConnect](https://drive.google.com/a/elinkgate.com/uc?id=1S_XSQo4rrXyqve4S7O5iEeMqfRu4HaYi)

1. Dùng cáp USB type B kết nối Slave với eLinkKVM thông qua cổng USB B 
2. Dùng cáp USB micro để cấp nguồn cho eLinkKVM bằng cổng power. Nguồn có thể được lấy từ nguồn USB của Slave hoặc nguồn USB 5V ngoài
3. Dùng cáp VGA để kết nối từ cổng VGA OUT của Slave với cổng VGA IN của eLinkKVM 
4. Dùng cáp RS232 để kết nối cổng Serial (COM PORT) của Slave tới cổng RS232 của eLinkKVM (Tuỳ chọn, có thể ko kết nối nếu PC/Server ko có cổng này)
5. Dùng cáp Ethernet (RJ45) để kết nối eLinkKVM tới mạng nội bộ thông qua cổng Ethernet Slave. Lưu ý: IP Address của eLinkKVM Ethernet Slave phải được cấu hình cùng lớp mạng với lớp mạng của mạng nội bộ. 

### Điều khiển Slave từ xa sử dụng eLinkKVM 

#### Kết nối với eLinkKVM dùng eLinkViewer 

![elinkViewerRemote](https://drive.google.com/a/elinkgate.com/uc?id=1YFUSGD-dX4wHJLaHWakQ19Hcb7gMIvyV)

Trên máy Master, dùng chương trình eLinkViewer để kết nối vào eLinkKVM như sau: 

1. Chạy chương trình eLinkKVM 

2. Điền địa chỉ IP address cổng `Slave` Ethernet của eLinkKVM. Ở đây là 10.42.0.2. 

   Tham khảo hướng dẫn `cấu hình IP address cho eLinkKVM` 

3. Bấm nút `Connect` để thiết lập kết nối 

#### Điều khiển Slave dùng VGA mode 

![](https://drive.google.com/a/elinkgate.com/uc?id=1tuh7V2DVGjloEEKGR7FLo_lOeVIjqNLr)

1. Click vào button eLink Configuration trên elinkviewer toolbar 
2.  kích hoạt chế độ Keyboard HID USB 
3.  Active HID USB
4.  kích hoạt chế độ Mouse ABS USB 
5.  Active ABS USB
6.  Chọn chế độ VGA trong Video mode
7. Click OK để xác nhận các cấu hình 

#### Điều khiển Slave dùng Booster mode 

##### Nguyên lý hoạt động của booster mode 

eLinkKVM ở chế độ booster mode sử dụng giao thức eLink. Giao thức này hoạt động dựa trên 1 agent hoạt động trên Slave thực hiện việc trao đổi dữ liệu với eLinkKVM thông qua phương thức đọc và ghi file trên USB eLinkKVM. Agent này gồm 2 loại: Agent hoạt động ở môi trường Pre-Boot và Agent hoạt động trong môi trường Hệ Điều Hành (Linux/Windows/OS X) 

- Agent Pre-Boot : là một UEFI driver sẽ được load khi Slave vừa mới khởi động. Lúc này, agent sẽ capture screen của Slave, xử lý và gửi cho USB eLinkKVM thông qua phương thức đọc/ghi dữ liệu USB trên eLinkKVM 
- Agent OSs : Tương tự là 1 software service chạy trên trên OS, tương tự như Agent Pre-boot, nó sẽ capture screen của Slave, xử lý và gửi cho eLinkKVM thông qua phương thức đọc/ghi dữ liệu USB trên eLinkKVM  

Việc trao đổi dữ liệu giữa agents và eLinkKVM được mã hoá và tuân thủ theo giao thức eLink để đảm bảo vấn đề bảo mật trên kênh truyền

Như vậy, eLinkKVM chế độ Booster về cơ bản sẽ hoạt động dựa trên phương thức đọc/ghi dữ liệu trên USB eLinkKVM, cho nên để kích hoạt chế độ Booster cần phải mount 1 ảnh đĩa (disk image) vào `Slave`. Dưới đây là hướng dẫn các bước thao tác để sử dụng chế độ Booster 

##### Kích hoạt chế độ Booster

![](https://drive.google.com/a/elinkgate.com/uc?id=1K-puF_SBb4gtgbmKIbpgin8p_boRPUXH)

1. Click vào button eLink Configuration trên elinkviewer toolbar 
2. chọn chế độ Keyboard HID USB 
3. Active HID USB 
4. chọn chế độ Mouse HID VNC 
5. Active Mouse HID VNC 
6. Video mode chọn BOOSTER mode. Đối với Booster mode, cần phải mount thêm 1 image đặt biệt định dạng HDD2 
7. Click nút Browser để duyện các image trên eLinkKVM. 
8. Điều hướng trong cây thư mục eLinkKVM, chọn 1 image `hdd2` 
9. click vào button `<<` để chỉ định image mount vào `PATH 1`
10. Click Button để xác nhận cấu hình eLinkKVM 

#### Cấu hình quick toogle booter mode 

Để thuận tiện cho việc chuyển đổi nhanh giữa booster mode và các mode khác. eLinkViewer cho phép người dùng cấu hình cho nút nhấn Quick Toogle Booster Mode. Nút nhấn này cho phép người dùng có thể chuyển đổi nhanh giữa booster mode và 1  mode đã được cấu hình trước 

![ToogleButtonConfig](https://drive.google.com/a/elinkgate.com/uc?id=1BtRGCSRGPBNN-vy86_nDGfr4qM823pgH)

Vậy để cấu hình cho Quick Toogle Booster mode cần thực hiện các thao tác sau: 

1. Click vào nút nhấn eLink Configuration 
2. Trên cửa sổ eLink Configuration, Trong mục Quick Booster Mode Setting, click vào Video list box để chọn Video sẽ sử dụng 
3. Tương tự, click chọn Mode Key 
4. Tiếp đến, click chọn Mode Mouse 
5. Nhấn chọn Base để xác nhận các thông tin cấu hình. Cấu hình này sẽ được cấu hình khi click vào nút Quick Toogle Booster Mode. 
6. Nhấn OK để lưu lại các cấu hình cài đặt


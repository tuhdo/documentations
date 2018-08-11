[TOC]

# Quick start guide eLinkKVM 

## Thiết bị và các phụ kiện 

- 1 eLinkKVM 
- 1 cáp Ethernet RJ45 
- 1 cáp USB type B
- 1 cáp USB micro 
- 1 nguồn USB 5V 
- 1 cáp VGA 
- 1 cáp RS232 

## Cấu hình cho thiết bị 

### Cấp nguồn cho eLinkKVM

![PoweringDevice](https://drive.google.com/a/elinkgate.com/uc?id=1OAJvfReUiWDwjh7OlbuqVG67y7u4K5KJ) 

1. Dùng cáp USB type B kết ngồi giữa PC và cổng USB B của eLinkKVM
2. Dùng cáp USB micro kết nối nguồn usb với Nguồn USB 5V
3. Có thể cấp nguồn dùng cách (1), (2)  hoặc cả 2 cách trên![](https://drive.google.com/a/elinkgate.com/uc?id=1AEfa2yDwBeN2BnYtEs4LHTZI5bxHUZMw)

### Cấu hình địa chỉ IP cho eLinkKVM

eLinkKVM hỗ trợ hai cổng Ethernet cho phép thiết bị được kết nối một cách linh hoạt. Cổng Ethernet Master  được cấu hình mặc định là DHCP server và cổng Ethernet Slave được cấu hình mặc định là DHCP Client.

Để đơn giản quá trình cấu hình chúng ta có thể kết nối cáp  Ethernet RJ45 giữa PC và cổng Ethernet Master của eLinkKVM. Khi đó PC sẽ được cấu hình như sau:

![Configure network ](https://drive.google.com/a/elinkgate.com/uc?id=1obtGhWgw4RsYaIL0RRn4P5UuTaB_ibTT)

1. Mở cửa sổ `Control pannel` vào thư mục `Control Panel\All Control Panel Items\Network Connections` 
2. Nhấp chuột phải lên Ethernet Device kết nối với eLinkKVM -> chọn mục `Properties `
3. Nhấp đôi vào mục `Internet Protocol version 4 (TCP/IPv4)` 
4. Trong cửa sổ `Internet Protocol version 4 (TCP/IPv4) Properties` chọn option 
   - Obtain an IP Address automatically 
   - Obtain DNS server address automatically 



**Địa chỉ IP mặc định cho cổng Ethernet Master của eLinkKVM là `10.0.0.1`** 

![eLinkKVMConfig](https://drive.google.com/a/elinkgate.com/uc?id=1H7-BtcI8SNSALvVU2VUl4YM6_94b5jJI)

1. Chạy chương trình eLinkViewer

2. Điền địa chỉ mặc định `10.0.0.1` của eLinkKVM vào trường `Server` 

3. Click chuột vào `Connect` để kết nối vào eLinkKVM 

4. Cửa sổ kết nối eLinkKVM hiện ra. Dùng chuột click vào các trường IP addres, Netmask ... để cấu hình 

   *Lưu ý:* 

   * Ethernet 0  tương ứng với cổng Slave
   * Ethernet 1 tương ứng với cổng Master

Ví dụ ở đây là cấu hình IP address cho Slave là  địa chỉ tĩnh. Trong trường hợp chúng ta chọn cấu hình thiết bị theo địa chỉ động thì chọn DHCP Client.

```
Ip address: 10.42.0.2
Netmask: 	255.255.255.0 
GateWay: 	10.42.0.1 
DNS: 		10.42.0.1
```

## Điều khiển PC/Server từ xa thông qua phần mềm eLinkViewer 

### Giới thiệu 

1 PC đóng vai trò điều khiển từ xa chạy phần mềm `eLinkViewer` gọi là `Remote PC` 

1 Server/PC bị điều khiển từ xa thông qua KVM gọi là `Server` 

1 eLinkKVM 

1 cáp Ethernet RJ45 kết nối từ cổng `SLAVE` của `eLinkKVM` tới mạng nội bộ

1 VGA kết nối từ `VGA OUT` của `Server` với `VGA IN` của `eLinkKVM`

1 USB type B kết nối giữa `Server` tới cổng `USB B` của eLinkKVM

1 USB micro kết nối từ `Slave`/nguồn USB tới cổng `POWER` eLinkKVM

### Kết nối 

![RemoteControlConnect](https://drive.google.com/a/elinkgate.com/uc?id=1S_XSQo4rrXyqve4S7O5iEeMqfRu4HaYi)

1. Dùng cáp USB type B kết nối `Server` với eLinkKVM thông qua cổng USB B 
2. Dùng cáp USB micro để cấp nguồn cho eLinkKVM bằng cổng power. Nguồn có thể được lấy từ nguồn USB của Slave hoặc nguồn USB 5V ngoài (việc cấp nguồn này không bắt buộc, thường chỉ dùng trong trường hợp cổng USB của `Server` không đủ nguồn)
3. Dùng cáp VGA để kết nối từ cổng VGA OUT của `Server` với cổng VGA IN của eLinkKVM 
4. Dùng cáp RS232 để kết nối cổng Serial (COM PORT) của `Server` tới cổng RS232 của eLinkKVM (Tuỳ chọn)
5. Dùng cáp Ethernet (RJ45) để kết nối eLinkKVM tới mạng nội bộ thông qua cổng Ethernet Slave. Lưu ý: IP Address của eLinkKVM Ethernet Slave phải được cấu hình cùng lớp mạng với lớp mạng của mạng nội bộ. 

### Điều khiển `Server` từ xa sử dụng phần mềm eLinkViewer 

![elinkViewerRemote](https://drive.google.com/a/elinkgate.com/uc?id=1YFUSGD-dX4wHJLaHWakQ19Hcb7gMIvyV)

Trên máy `Remote PC`, dùng chương trình eLinkViewer để kết nối vào eLinkKVM như sau: 

1. Chạy chương trình eLinkViewer

2. Điền địa chỉ IP address cổng `Slave` Ethernet của eLinkKVM. Theo cấu hình ở trên là 10.42.0.2. Nếu chọn lựa tính năng DHCP Client thì nhấn nút `Scan` để tìm địa chỉ của thiết bị.

   Tham khảo hướng dẫn `cấu hình IP address cho eLinkKVM` trong User Manual

3. Bấm nút `Connect` để thiết lập kết nối 

#### Điều khiển `Server` dùng VGA mode 

Thiết bị eLinkKVM cung cấp tính năng nhận tín hiệu video từ cổng VGA của `Server` , giải mã tín hiệu, số hóa và nén dữ liệu và gửi tới phần mềm eLinkViewer. Qua đó người sử dụng có thể quan sát màn hình của `Server` trên phần mềm eLinkViewer.  Để sử dụng tính năng này thực hiện các bước sau:



##### Kích hoạt chế độ VGA

![](https://drive.google.com/a/elinkgate.com/uc?id=1tuh7V2DVGjloEEKGR7FLo_lOeVIjqNLr)

1. Click vào button eLink Configuration trên elinkviewer toolbar 
2. Kích hoạt chế độ Keyboard HID USB 
3. Active HID USB
4. Kích hoạt chế độ Mouse ABS USB 
5. Active ABS USB
6. Chọn chế độ VGA trong Video mode
7. Click nút OK để xác nhận các cấu hình 



#### Điều khiển `Server` dùng Booster mode 

Ngoài chế độ VGA Mode, eLinkKVM còn có khả năng hỗ trợ booster mode. Đây là chế độ cho phép thiết bị ghi thông tin màn hình của `Server` thông qua việc sử dụng một phần mềm agent chạy trên `Server` và agnet sẽ gửi thông tin màn hình cho eLinkKVM thông qua giao thức USB.

Việc kích hoạt phần mềm Agent có thể thực hiện theo các phương pháp sau:

- Cài đặt trên hệ thống hoặc chạy chế độ tự kích hoạt (tương tự như việc cài đặt teamviewer hoặc logmein)
- Boot Server từ một ổ đĩa có cài đặt Agent cho boot hệ thống (việc cài đặt tương tự như việc cài đặt các boot loader như grub,syslinux...)

Ưu thế của chế độ này là việc sử dụng CPU của Server để thực hiện các giải thuật nén dữ liệu do đó cho phép nén hình ảnh với độ phân giải cao hơn và chất lượng tốt hơn, có thể hoạt động trong mọi hệ điều hành và môi trường Bios, UEFI.

Tuy nhiên nhược điểm của chế độ này là không điều khiển được trong Bios Setup và lỗi màn hình xanh.

Phương thức giao tiếp Booster về cơ bản sẽ hoạt động dựa trên phương thức đọc/ghi dữ liệu trên USB eLinkKVM, do đó để kích hoạt chế độ Booster cần phải mount 1 ảnh đĩa (disk image) vào `Server`. Dưới đây là hướng dẫn các bước thao tác để sử dụng chế độ Booster 

##### Kích hoạt chế độ Booster

![](https://drive.google.com/a/elinkgate.com/uc?id=1K-puF_SBb4gtgbmKIbpgin8p_boRPUXH)

1. Click vào button eLink Configuration trên elinkviewer toolbar 
2. chọn chế độ Keyboard HID USB 
3. Active HID USB 
4. chọn chế độ Mouse HID VNC 
5. Active Mouse HID VNC 
6. Video mode chọn BOOSTER mode. Đối với Booster mode, cần phải mount thêm 1 image đặt biệt định dạng HDD2 
7. Click nút Browser để duyện các image trên eLinkKVM. 
8. Điều hướng trong cây thư mục eLinkKVM, chọn 1 image `hdd2`  (trong ví dụ này là syslinux.hdd2)
9. click vào button `<<` để chỉ định image mount vào `PATH 1`
10. Click nút OK để xác nhận cấu hình


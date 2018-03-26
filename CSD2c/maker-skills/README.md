# pi zero audio project

The goal is to be able to run puredata patches on the pi zero w. An extra goal would be to run my own C++ programs which use Jack.
- [Log](#log)

## Log

#### Preparing the SD card for USB OTG
- Download the newest version of [raspbian](https://www.raspberrypi.org/downloads/raspbian/) (stretch desktop in my case)
- Flash the image onto your SD card. I've done this from my linux machine using this [guide](https://www.raspberrypi.org/documentation/installation/installing-images/linux.md)
- Locate the boot folder on your SD card using the following command:
```bash
df -h
```
The folder we're looking for was called **/media/ward/boot** in my case.
```bash
cd /media/ward/boot
```
- Open the **confix.txt** file and add the following at the bottom of the file:
```
dtoverlay=dwc2
```
- Now create a file called **ssh**
```bash
touch ssh
```
- Now edit the cmdline.txt file and add the following inbetween **rootwait** and **quiet**
```
modules-load=dwc2,g_ether
```
Make sure that there are no unnecessary spaces or other characters.

#### Connecting over ssh
- Now put the SD card into your pi and connect the pi to your pc using USB.
  - *Be sure to connect it to the micro USB port marked as USB, the other USB port only transmits power.*
  - *I had to change IPv4 addresses mode to Link-Local only in order to be able to ssh into the pi. You might be able to skip this step. See [this](https://raspberrypi.stackexchange.com/questions/66143/usb-otg-w-raspberry-pi-zero/74499) article for more info*
- Connect over SSH:
```
ssh pi@raspberrypi.local
```
- Enter the default password:
```
raspberry
```
- At this point I can't ping 8.8.8.8 (google) yet.

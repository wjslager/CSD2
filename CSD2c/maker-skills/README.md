# pi zero audio project

The goal is to be able to run puredata patches on the pi zero w. An extra goal would be to run my own C++ programs which use Jack.

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
  - Be sure to connect it to the micro USB port marked as USB, the other USB port only transmits power.
  - Linux only: I had to change IPv4 addresses mode to Link-Local only in order for it to show up as ethernet connection. You might be able to skip this step. See [this](https://raspberrypi.stackexchange.com/questions/66143/usb-otg-w-raspberry-pi-zero/74499) article for more info
- Connect over SSH:
```
ssh pi@raspberrypi.local
```
- Enter the default password:
```
raspberry
```

#### Setting the usb soundcard as default device
*Based on [this](https://raspberrytips.nl/usb-audio-gebruiken-op-een-raspberry-pi/) article*
- We assume the sound card is device #1
- We will have to edit some files. Let's open the first file with the built-in text editor (nano)
```
sudo nano /usr/share/alsa/alsa.conf
```
- Save and exit nano using the following keyboard sequence:
```
ctrl + x
y
enter
```
- Replace 0 with 1 in the following lines:
```
defaults.ctl.card 0
defaults.pcm.card 0
```
- Save and exit nano
- Now we need to create a file called .asoundrc and tell it to use device #1
```
sudo nano ~/.asoundrc
```
- Add the following lines:
```
pcm.!default {
    type hw
    card 1
}
ctl.!default {
    type hw
    card 1
}
```
- When you reboot the pi with a sound card connected, it should default to using that card.

#### Testing audio
- As test we can play some audio using ALSA's *speaker-test* utility. We will play a sinewave at 440hz over 2 channels.
```
speaker-test -c 2 -t sine -f 440
```
- Because I do not have a USB hub and thus I can't connect both my pc and the soundcard, I will let the pi execute this command on boot. Because *rc.local* is executed as root, we will have to include the complete path.
- Therefore put the following in */etc/rc.local*
```
/usr/bin/speaker-test -c 2 -t sine -f 440
```

## <ins> Klipper Configuration Tiny-M <ins>

Fysetc Cheetah V1.1 with 4 TMC2209

Fysetc Mini 12864 Display connected to Raspberry Pi with linuxy MCU klipper feature.

## How i use Linux MCU to connect Fysetc Mini 12864 Display!

Klipper Documention
https://github.com/KevinOConnor/klipper/blob/master/docs/RPi_microcontroller.md

I must extend some steps

Here my steps

1. Enable SPI in raspi-config

2. Install the rc script:
```
cd ~/klipper/
sudo cp "./scripts/klipper-mcu-start.sh" /etc/init.d/klipper_mcu
sudo chmod +x /etc/init.d/klipper_mcu
sudo update-rc.d klipper_mcu defaults
```
3. Building the micro-controller code:
```
same like in the doc
```

4. last step, replace pi with your username, which run klipper:
```
sudo usermod -a -G tty pi
```
5. Connect pins like in my [display.cfg](https://github.com/gsl12/Tiny-M/blob/master/klipper_firmware/klipper_configs/display.cfg)

U also need to connect Display pins MOSI,MISO, SCLK to PI SPI0 pins.
I played with the pins for Encoder, seams that no all pins will work.
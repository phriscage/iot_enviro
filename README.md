# IoT - EnviroPHAT Monitor

This project contains an [EnviroPHAT](https://shop.pimoroni.com/products/envirophat) monitor application that runs on an Raspberry Pi device that captures local environmental data (weather, acceleration, light, etc.)

[Prerequisites](#prerequisites)
[Quick Start](#quick_start)


## Prerequisites
Procure a Raspberry Pi device and privision with the latest Rasbian OS, Docker applications. Then configure the I2C & GPIO modprobes to enable the EnviroPHAT libary before starting.

*	[Rasperry Pi 2/3](https://www.raspberrypi.org)
*	[Rasperry Pi Rasbian OS installed](https://www.raspberrypi.org/documentation/installation/installing-images/)
*	[Docker for Rasbian installed](https://docs.docker.com/engine/install/debian/#install-using-the-convenience-script)
*	[Configuration](#configuration)
	*	[I2C and GPIO](#i2c_and_gpio)
	*	[system](#system)
*	Download this [repo](https://github.com/phriscage/iot_enviro)


### Configuration
Enable I2C, GPIO and system level components to run the application.


#### I2C and GPIO
Add *i2c-bcm2708* and *i2c-dev* to `/etc/modules` and `/etc/udev/rules.d/99-i2c.rules`

	sudo echo "i2c-bcm2708" >> /etc/modules;
	sudo echo "i2c-dev" >> /etc/modules;

	sudo echo "SUBSYSTEM=="i2c-bcm2708", MODE="0666" >> /etc/udev/rules.d/99-i2c.rules;
	sudo echo "SUBSYSTEM=="i2c-dev", MODE="0666" >> /etc/udev/rules.d/99-i2c.rules;

Create the logging/data directory and logrotate configuration

	sudo mkdir -p /var/log/iot_enviro && sudo chown `whoami`:`whoami` /var/log/iot_enviro;

```
sudo tee -a /etc/logrotate.d/iot_enviro > /dev/null <<EOT
/var/log/iot_enviro/*.log {
  weekly
  rotate 10
  copytruncate
  delaycompress
  compress
  notifempty
  missingok
}
EOT
```


## Quick Start
Download this [repo](https://github.com/phriscage/iot_enviro) and start the application with `make`

	make

View the data events in `/var/log/iot_enviro/data.log`

	tail -f /var/log/iot_enviro/data.log


#### Running privileged on IoT
The GPIO examples require access to /dev/mem as root, privileged mode. Specifically, `--cap-add SYS_RAWIO --device /dev/mem` for these examples. A sample for this is below

	 docker run -it --rm --cap-add SYS_RAWIO --device /dev/mem phriscage/iot_gpio-enviro python app.py
	 docker run -it --rm --privileged phriscage/iot_gpio-enviro python app.py


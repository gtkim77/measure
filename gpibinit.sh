raspi-config nonint do_spi 1
modprobe gpib_bitbang
gpib_config
raspi-config nonint do_spi 0
modprobe gpib_bitbang
gpib_config

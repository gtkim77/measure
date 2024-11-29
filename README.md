<h1>Setup of GPIB raspberry conrollers for the electrical characterization</h1>

python programs for controlling a GPIB4PI card or an NI-GPIB-USB-HS. <br>

1. Installation of the libraries for a GPIB4PI card
   - Raspberry pi for GPIB : <a href="https://www.hackster.io/lightside-instruments/the-gpib4pi-gpib-for-raspberry-pi-shield-4b3e9a">Link</a>
     
2. Installation of the libraries for an NI-GPIB-USB-HS interface
   - NI GPIB-USB-HS : <a href="https://zenn.dev/hroabe/articles/ceccb8ce114372">Link</a>
   - Linux Kernel for RPi: <a href="https://www.raspberrypi.com/documentation/computers/linux_kernel.html">Link</a>
      * Depending on the version of RP, a proper version of kernel should be installed.
      * Establish, activate & deactivate the virtual environment
        - python3 -m venv venv
        - . . /venv/bin/activate
        - deactivate


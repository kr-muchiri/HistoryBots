# Control GPIO pins
gpio read 17

# Configure system settings
sudo raspi-config

# Check CPU temperature
vcgencmd measure_temp

# Capture image using the camera module
raspistill -o image.jpg

# Record video using the camera module
raspivid -o video.h264

# Control GPIO pins remotely
sudo pigpiod

# Detect I2C devices
i2cdetect -y 1

# View network interfaces
ifconfig

# Securely connect to a remote Raspberry Pi
ssh pi@192.168.1.100

# Schedule tasks using cron
crontab -e

# Manage system services
sudo systemctl start service-name

# View system logs
tail -f /var/log/syslog

# Check network connectivity
ping google.com

# Mount a disk or partition
sudo mount /dev/sdb1 /mnt

# View system information
cat /proc/cpuinfo

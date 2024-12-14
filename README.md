Please note that root access is required.  
#### Using installer
 ```
pkg update
pkg upgrade
pkg install tsu
pkg install python
pkg install git
pkg install -y root-repo
pkg install -y git tsu python wpa-supplicant pixiewps iw openssl
termux-setup-storage
 ```
**Getting WIFI-WIFI-2.0**
 ```
 git clone https://github.com/WilDev26/wifi-hack.git
 ```
#### Running
 ```
 sudo python wifi-hack/Wildev-Wifi.py -i wlan0 -K
 ```
## [Termux](https://termux.com/)


# Usage
```
 Wildev-WIFI-2.0.py <arguments>
 Required arguments:
     -i, --interface=<wlan0>  : Name of the interface to use

 Optional arguments:
     -b, --bssid=<mac>        : BSSID of the target AP
     -p, --pin=<wps pin>      : Use the specified pin (arbitrary string or 4/8 digit pin)
     -K, --pixie-dust         : Run Pixie Dust attack
     -B, --bruteforce         : Run online bruteforce attack
     --push-button-connect    : Run WPS push button connection

 Advanced arguments:
     -d, --delay=<n>          : Set the delay between pin attempts [0]
     -w, --write              : Write AP credentials to the file on success
     -F, --pixie-force        : Run Pixiewps with --force option (bruteforce full range)
     -X, --show-pixie-cmd     : Alway print Pixiewps command
     --vuln-list=<filename>   : Use custom file with vulnerable devices list ['vulnwsc.txt']
     --iface-down             : Down network interface when the work is finished
     -l, --loop               : Run in a loop
     -r, --reverse-scan       : Reverse order of networks in the list of networks. Useful on small displays
     --mtk-wifi               : Activate MediaTek Wi-Fi interface driver on startup and deactivate it on exit
                                (for internal Wi-Fi adapters implemented in MediaTek SoCs). Turn off Wi-Fi in the system settings before using this.
     -v, --verbose            : Verbose output
 ```

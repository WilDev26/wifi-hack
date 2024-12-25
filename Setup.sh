clear
echo -e '\e[1;37mUpdate & Upgrade...\e[0m'
clear
pkg update
pkg upgrade
clear
echo -e '\e[1;37mDownload File...\e[0m'
wget -o wifi-hack.tar.gz https://github.com/WilDev26/wifi-hack/raw/refs/heads/main/wifi-hack.tar.gz
clear
echo -e '\e[1;37mInstalling Wifi-hack...\e[0m'
tar -xvzf wifi-hack.tar.gz
rm wifi-hack.tar.gz
clear
echo -e '\e[1;37mTunggu harap bersabar...\e[0m'
pkg install tsu
pkg install wget
pkg install python
pkg install git
pkg install -y root-repo
pkg install -y git tsu python wpa-supplicant pixiewps iw openssl
termux-setup-storage
wget -O wifi-hack https://raw.githubusercontent.com/WilDev26/wifi-hack/refs/heads/main/wifi-hack.py
chmod +rwx wifi-hack.py && sudo wifi-hack.py
clear

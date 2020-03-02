# install/start
$ sudo apt update && apt upgrade -y <br>
$ sudo apt install git <br>
$ git clone https://github.com/paraparap/geoinfo <br>
$ cd geoinfo <br>
$ sudo chmod +x install.sh <br>
$ sudo ./install.sh <br>
$ sudo ./geoinfo.py

# and in new terminal
$ cd geoinfo <br>
$ sudo ./ngrok http 8080

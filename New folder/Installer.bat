#!/bin/bash

cur_usr = $env:UserName

echo "Installing Dependencies"
pip install -q pygame 
pip install -q pytmx 

echo "Installing"
mkdir /home/$cur_usr/Desktop/SavingSamhain
git clone https://github.com/aflytle/AlyGame /home/$cur_usr/Desktop/SavingSamhain

cp /home/$cur_usr/Desktop/SavingSamhain/SvngSmhn.exe /home/$cur_usr/Desktop/

cd Desktop

chmod u+x SvngSmhn.exe


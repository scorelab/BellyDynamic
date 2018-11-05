#!/bin/bash

wget https://snap.stanford.edu/snappy/release/snap-4.1.0-4.1-centos6.5-x64-py2.6.tar.gz;
tar zxvf snap-4.1.0-4.1-centos6.5-x64-py2.6.tar.gz;
cd snap-4.1.0-4.1-centos6.5-x64-py2.6;
sudo python setup.py install & cd ..;
cp snap-4.1.0-4.1-centos6.5-x64-py2.6/snap.py ./bellydynamic-adv/;
cp snap-4.1.0-4.1-centos6.5-x64-py2.6/_snap.so ./bellydynamic-adv/
chmod +x ./bellydynamic-adv/snap.py;
chmod +x ./bellydynamic-adv/_snap.so;


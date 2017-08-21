#!/bin/sh
wget https://snap.stanford.edu/snappy/release/snap-4.0.0-4.0-centos6.5-x64-py2.6.tar.gz
tar zxvf snap-4.0.0-4.0-centos6.5-x64-py2.6.tar.gz
cd snap-4.0.0-4.0-centos6.5-x64-py2.6.tar.gz
sudo python setup.py install
cp snap.py ../bellydynamic-travis/
cp _snap.so ../bellydynamic-travis/
chmod +x ../bellydynamic-travis/snap.py
chmod +x ../bellydynamic-travis/_snap.so
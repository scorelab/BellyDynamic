#!/bin/bash

set -e

VERSION="4.1.0-4.1-centos6.5"

wget https://snap.stanford.edu/snappy/release/snap-${VERSION}-x64-py2.6.tar.gz
tar zxf snap-${VERSION}-x64-py2.6.tar.gz
cd snap-${VERSION}-x64-py2.6
sudo python setup.py install
cd ..
cp snap-${VERSION}-x64-py2.6/snap.py ./bellydynamic-adv/
cp snap-${VERSION}-x64-py2.6/_snap.so ./bellydynamic-adv/
chmod +x ./bellydynamic-adv/snap.py
chmod +x ./bellydynamic-adv/_snap.so
wget https://snap.stanford.edu/snappy/release/snap-4.0.0-4.0-centos6.5-x64-py2.6.tar.gz
tar zxvf snap-4.0.0-4.0-centos6.5-x64-py2.6.tar.gz
cd snap-4.0.0-4.0-centos6.5-x64-py2.6
cp snap.py ../bellydynamic-adv/
cp _snap.so ../bellydynamic-adv/
cd ../bellydynamic-adv
chmod +x snap.py
chmod +x _snap.so
python SchemaGraph.py
python SwedenGraph.py

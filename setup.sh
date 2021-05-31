#setup.sh

echo $parentdir

echo "python version: "

python3 --version


pip3 install pygame --user
pip3 install pyserial --user
pip3 install pathlib --user

python3 dev/polloshiba/polloshiba_v1.py --test
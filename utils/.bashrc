# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

alias pycharm=/home/cgrubitz/IDE/pycharm-files/pycharm-community-2016.2.3/bin/pycharm.sh

alias clion=/home/cgrubitz/IDE/clion-2016.2.2/bin/clion.sh
alias servermount="sshfs tdaq1:/home_local ~/server"
alias serverumount="fusermount -u ~/server"
alias compile-g4=/home/cgrubitz/myon-detector/utils/compile-g4.sh

export PATH=~/bin:$PATH


export GEANT4_INSTALL=/opt/geant4.10.01.p03
export LD_LIBRARY_PATH=$GEANT4_INSTALL/lib64:lib:/opt/shibboleth/lib64:$LD_LIBRARY_PATH

export PYTHONPATH=/opt/g4py/lib64:$PYTHONPATH

export G4LEDATA=/opt/geant4.10.01.p03/share/Geant4-10.1.3/data/G4EMLOW6.41

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions

# EXEGOL CHEAT SHEET

### VARIABLES
The variables are stored in `/opt/tools/Exegol-history/profile.sh` and look like so:
```text
#export INTERFACE='eth0'
#export DOMAIN='DOMAIN.LOCAL'
#export DOMAIN_SID='S-1-5-11-39129514-1145628974-103568174'
#export USER='someuser'
#export PASSWORD='somepassword'
#export NT_HASH='c1c635aa12ae60b7fe39e28456a7bac6'
#export DC_IP='192.168.56.101'
#export DC_HOST='DC01.DOMAIN.LOCAL'
#export TARGET='10.10.251.98'
#export ATTACKER_IP='tun0'
```
So what you need is uncomment the line you need and replace the values with the one you need

```text
#export INTERFACE='eth0'
#export DOMAIN='DOMAIN.LOCAL'
#export DOMAIN_SID='S-1-5-11-39129514-1145628974-103568174'
#export USER='someuser'
#export PASSWORD='somepassword'
#export NT_HASH='c1c635aa12ae60b7fe39e28456a7bac6'
#export DC_IP='192.168.56.101'
#export DC_HOST='DC01.DOMAIN.LOCAL'
export TARGET='10.10.251.98'
export ATTACKER_IP='tun0'
```

Tomate Indicator Plugin
=======================

Tomate plugin that shows the session progress in indicator.

Installation
------------

### Ubuntu (14.04, 14.10)

```
RELEASE=`sed -n 's/VERSION_ID="\(.*\)"/\1/p' /etc/os-release`
sudo wget -O- http://download.opensuse.org/repositories/home:/eliostvs/xUbuntu_$RELEASE/Release.key | sudo apt-key add -
sudo bash -c "echo 'deb http://download.opensuse.org/repositories/home:/eliostvs/xUbuntu_$RELEASE/ ./' > /etc/apt/sources.list.d/tomate.list"
sudo apt-get update && sudo apt-get install tomate-indicator-plugin
```

### Opensuse (13.2)

```
RELEASE=`cat /etc/SuSE-release | sed -n "s/VERSION = \(.*\)$/\1/p"`
sudo zypper ar -f http://download.opensuse.org/repositories/home:/eliostvs/openSUSE_$RELEASE/home:eliostvs.repo
sudo zypper install tomate-indicator-plugin
```

## Fedora (20, 21)

```
RELEASE=`cat /etc/fedora-release | grep -o '[0-9][0-9]*'`
sudo yum-config-manager --add-repo http://download.opensuse.org/repositories/home:/eliostvs/Fedora_$RELEASE/home:eliostvs.repo
sudo yum install tomate-indicator-plugin
```

Bugs and Suggetions
-------------------

Bugs and suggestions should be reported at: https://github.com/eliostvs/tomate-indicator-plugin/issues

License
-------

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License version 3, as published
by the Free Software Foundation.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranties of
MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program.  If not, see <http://www.gnu.org/licenses/>.
# linux-utils
Linux Utils

# Debian KDE, Kubuntu and MX Linux KDE (MX Linux is by far the most feature full and polished)
These are by far the most stable, fast, modern desktops. 
======= adding at top again ===== of all the linux distros I have used - reiterating -- Debian KDE, Kubuntu and MX Linux  are the most modern, polished, stable and easy to use linux. Everything works out of the box. Then linux-mint and ubuntu-mate. 

* zoom
* citrix plugin
* vlc
* tixati
* vim
* git
* intellij idea community
* pycharm community 
* git clone
* obsidian
* xp pen
* firefox
* chrome
* Timeshift
* Google-Keep as webapp (best for syncing text, keeping quick notes)
* THermald (apt install thermald, and keep it running - its good for laptop heat )
* install pipx
* cameractrls (this controls resolution/crop/zoom of camera feeds - nice)
* Any issues with citrix + external Camera ---> this is citrix version issue, the following combination works:
*     Citrix (https://www.citrix.com/downloads/workspace-app/legacy-workspace-app-for-linux/workspace-app-for-linux-2604.html)  THE VERSION JUST AFTER THAT BROKE SOMETHING
*     And make sure that ZOOM VDI matches the version of ZOOM in NDS -- and VDI tab in zoom settings from within NDS shows the version and connection status.


Fedora KDE Tweaks (Debian KDE didn't even need these tweaks)
    1. for citrix - in case any issues, just refer the uploaded wfclient.ini file.
    2. for citrix clean launch (if it doesn't launch cleanly , issue with latest kernel - not with fedora, but can be easily fixed )  :  use the attached citrix-start.sh and citrix-start.desktop files, and associate .ica files to launch with this .desktop file, done.
    3. for epos wireless headsets - although they work better in Fedora compared to other distros , but can easily fix it to be rock solid, follow next steps:
    3.a. upload these pipewire sticks configuraiton for Citrix ZOOM , copy the following 2 files, in this folder, as shown (the files are checked in )
    naveenksoni@fedora:~$ ls ~/.config/wireplumber/wireplumber.conf.d/
    11-bluetooth-policy.conf  51-disable-ducking.conf  52-epos-pro-audio.conf  53-zoom-vdi-routing.conf
    
    
    3.b. install pavucontrol, and check which number profile "pro audio" comes in. because thats the profile which works. just needs nudging sometimes - when zoom starts, thats where this button helps -> add this quick nudge button on task bar , script is : headsets_profile_toggle.sh , desktop file: headsets_profile_toggle.desktop. and add this to taskbar. (you might need to just change the profile number in the script.) 
    
    After these tweaks + installed applications -> its a very smooth, stable, fast and modern distro.
  
  
    ### FOR FEDORA KDE - you don't even need scaling hacks for 4k multimonitors, silent play wav hacks etc for headsets. etc.. it has eveyrthing out of the box - even multiple taskbars/different wallpapers, login image things -- everything out of the box and works very smoothly ####


KDE connect is awesome tool.

===============

some troubleshooting help:
bluetooth pairing --> double check if device itself is in pairing mode

windows ntfs read write mount --> sudo ntfsfix -d /dev/sde1  OR windows might be in hibernate status [sudo ntfs-3g -o remove_hiberfile /dev/nvme0n1p3 /run/media/naveenksoni412]

github login in any IDE including obsidian --> using token  --> https://token@github.com...repo.


git:

origin	https://github.com/nsthethunderbolt/multi-params-visualizer.git

https://github.com/nsthethunderbolt/givingmybestwithgodsgrace

============================================================================================================================




# For headsets/audio issue (not required for debian kde, kubuntu and mx linux)
### the following creates a silent wav file
ffmpeg -f lavfi -i anullsrc=r=8000:cl=mono -t 10 -acodec pcm_u8 silence.wav
### the following uns it infinitely, which avoids any headsets sleep etc
mpv --no-video --loop-file=inf --volume=0 --really-quiet silence.wav
#### better to use the python and .desktop file and create panel using that, which automatically plays this file (take a look at contents if any edit required in those)
#### simply put the python file in some location, and .desktop in /.local/share/applications/..
#### and in  ~/.config/autostart/ to autostart. can be done using settings 


# Backup
Run the following provide src and dest:

./backup.sh /run/user/1000/gvfs/mtp\:host\=Google_Pixel_9_Pro_45201FDAP002AK/Internal\ shared\ storage/DCIM/Camera/  to_path

Compression [if explicit compression is required]
once data is backed up (in laptop and harddisk), then
1. to compress videos:
python3 video-compressor.py /run/user/1000/gvfs/mtp\:host\=Google_Pixel_9_Pro_45201FDAP002AK/Internal\ shared\ storage/DCIM/Camera/

# this will compress all videos in that folder - will create a -compressed file for each of them.

2. to copy metadata from original videos to -compressed videos (follow instructions in that git project)
run the apk from https://github.com/nsthethunderbolt/android-utils

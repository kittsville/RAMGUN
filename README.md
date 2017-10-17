# RAMGUN

RAMGUN adds magnet links from your browser to ruTorrent, saving a small amount of time.

# Usage

1. Click magnet link in browser:  
![Screenshot of magnet link being clicked](../master/screenshots/01-click-link.png?raw=true)
2. Enter `Y` in command line pop-up to confirm adding the torrent:  
![Screenshot of Python command line where confirmation has been accepted](../master/screenshots/02-confirm-add.png?raw=true)
3. Check in ruTorrent that the torrent has appeared:  
![Screenshot torrent in ruTorrent](../master/screenshots/03-success.png?raw=true)

# Requirements

- Python 2.7
- Requests library `pip install requests`

# Installation (Windows)

For Linux/OS X you'll need to Google `$OS_Name associate protocol with python script`

1. Download from GitHub
2. Put somewhere you won't move/delete it
3. [Add registry entries to associate magnet protocol with the script](https://support.shotgunsoftware.com/hc/en-us/articles/219031308-Launching-applications-using-custom-browser-protocols)

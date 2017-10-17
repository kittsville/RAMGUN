# RAMGUN

RAMGUN adds magnet links from your browser to ruTorrent, saving a small amount of time.

Note that RAMGUN cannot add .torrent files, just magnet links.

# Usage

1. Click magnet link in browser:  
![Screenshot of magnet link being clicked](../master/screenshots/01-click-link.png?raw=true)
2. Enter `Y` (then Enter) in command line pop-up to confirm adding the torrent. This step can be disabled in the [config file](#config).
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
3. Open `config.ini` and add ruTorrent configuration and preferences, see [config guide](#config)
4. Open command line and navigate to your copy of RAMGUN
5. Check it works with `python ramgun.py "magnet link here"`
6. [Add registry entries to associate magnet protocol with the script](https://support.shotgunsoftware.com/hc/en-us/articles/219031308-Launching-applications-using-custom-browser-protocols)

# Config

| Key                 | Meaning                                                                                                                               |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| url                 | The URL you'd normally use to access ruTorrent                                                                                        |
| username            | ruTorrent username. The one entered when opening ruTorrent                                                                            |
| password            | ruTorrent password. The one entered when opening ruTorrent                                                                            |
| label               | Equivalent to the Label field when adding a torrent via ruTorrent                                                                     |
| directory           | Equivalent to the Directory field when adding a torrent via ruTorrent                                                                 |
| requireConfirmation | Whether to ask before adding the magnet link. Setting to anything other than `True` will mean the magnet link is added straight away. |

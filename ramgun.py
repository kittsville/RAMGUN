import requests
import ConfigParser
import sys
import time

configParser = ConfigParser.ConfigParser()
configParser.read('config.ini')

ruTorrentConf  = dict(configParser.items('ruTorrent'))
torrentDetails = dict(configParser.items('TorrentDetails'))

payload = {
    'url' : sys.argv[1]
}

message = "You're about to add the magnet link:\n{0}\nARE YOU SURE ABOUT THAT? Y/N".format(payload['url'])
confirmation = raw_input(message)

if confirmation.upper() == 'Y':
    print 'Adding...'
else:
    print 'Cancelling...'
    sys.exit(0)

ruTorrentAuth = (ruTorrentConf['username'], ruTorrentConf['password'])

urlParams = {
    'dir_edit' : torrentDetails['directory'],
    'label'    : torrentDetails['label']
}

response = requests.post(
    ruTorrentConf['url'] + 'php/addtorrent.php',
    auth=ruTorrentAuth,
    params=urlParams,
    data=payload
)

if response.status_code == 200 and response.text[:-3].endswith('success'):
    print 'Added Torrent'
else:
    print "Something went wrong :'("

time.sleep(1)

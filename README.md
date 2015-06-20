# cloudflare-ddns
Cloudflare DYNDNS update script

It runs perfect on linux/mac/windows.

Tested on MAC OSX 10.10 and CentOS 7.

I use it along with crontab to run every 5 minutes.

Do a ```crontab -e``` and insert the following line of code (also replace path!!):

```*/5 * * * * python /path-to/cloudflare-ddns.py```

Ctrl+wq and enter , and it's done!

#!/usr/bin/python
##Cloudflare DDNS (dynamic dns) updater script for non-static ips :)
##it updates cloudflare records on a specified zone and subdomain with your current ip (i use it for a home server)
import urllib2
import json
import commands

#settings
EMAIL="cf-email@mail.com"
API_KEY="123123123APIKEYHERE"

ZONE="hackalin.me"

SUBDOMAINS=[
	"ilo.hackalin.me",
	"cloud.hackalin.me"
]

ONLYSSIDS = [
  "adita"
]

ssid = commands.getstatusoutput("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I | awk '/ SSID/ {print substr($0, index($0, $2))}'")[1]

found = True
try:
  ONLYSSIDS.index( ssid )
except ValueError, e:
  found = False

if False == found:
  exit(0)

myip = urllib2.urlopen("https://wtfismyip.com/text").read().rstrip('\n')

def getJSONrecords():
  API_REQUEST = "https://www.cloudflare.com/api_json.html?a=rec_load_all&tkn="+API_KEY+"&email="+EMAIL+"&z="+ZONE
  req = urllib2.urlopen(API_REQUEST)
  return json.loads(req.read())

def update_record(recordid,recordname,servicetype):
  recordname = recordname.partition(".")[0]
  API_REQUEST = "https://www.cloudflare.com/api_json.html?a=rec_edit&tkn="+API_KEY+"&id="+recordid+"&email="+EMAIL+"&z="+ZONE+"&type=A&name="+recordname+"&content="+myip+"&service_mode="+servicetype+"&ttl=1"
  urllib2.urlopen(API_REQUEST)

jdata = getJSONrecords()

for record in jdata['response']['recs']['objs']:
  if record['name'] in SUBDOMAINS:
    update_record(record['rec_id'],record['name'],record['service_mode']) #service mode = cloudflare passthrough (orange or gray cloud)


##this is a fail script , use python instead.
##Cloudflare needs record id (rec_id) to identify the subdomain of the zone.

#!/bin/bash
##Cloudflare Dynamic DNS shell script by Alin1337 (catalin@live.jp)

#Cloudflare zone,email and api key
API_KEY="CFKEY"
EMAIL="EMAIL@domain.com"
ZONE="hackalin.me"
SUBDOMAINS="ilo cloud" #subdomains to update the ip.

#Get IP
MYIP=$(curl -f -s -S -k https://wtfismyip.com/text)
echo "$MYIP $API_KEY"

for SUBDOM in ${SUBDOMAINS[*]}
do
 echo $(curl -s -f -S -k https://www.cloudflare.com/api_json.html \
  -d 'a=rec_edit' \
  -d 'tkn=$API_KEY' \
  -d 'id=0' \ #<< HERE IT NEEDS RECORD_ID FROM rec_load_all API CALL.
  -d 'email=$EMAIL' \
  -d 'z=$ZONE' \
  -d 'type=A' \
  -d 'name=$SUBDOM' \
  -d 'content=$MYIP' \ 
  -d 'service_mode=1' \
  -d 'ttl=1') 
done

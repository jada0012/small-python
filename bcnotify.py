import requests
ifttt_url = "https://maker.ifttt.com/trigger/price_update/with/key/eBLWHg-p1txKna9zAC6NJDVn9Wx8KXXkh-mmb_M3J_h"
for i in range(5):
    requests.post(ifttt_url)

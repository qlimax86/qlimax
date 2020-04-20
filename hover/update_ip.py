import requests
import json
import ipaddress

with open('config.json', 'r') as fp:
    config = json.load(fp)

username = config['username']
password = config['password']
dns_id = config['dns_id']


class HoverException(Exception):
    pass


class HoverAPI:
    def __init__(self):
        self.session = requests.Session()
        r = self.session.get("https://www.hover.com/signin")
        r.raise_for_status()

        r = self.session.post("https://www.hover.com/signin/auth.json", json={
            'username': username,
            'password': password
        })
        r.raise_for_status()

        if not r.cookies.get('hoverauth'):
            raise HoverException('hoverauth not in cookies')

    def update_ip(self):
        response = self.session.get('https://www.hover.com/api/dns')
        response.raise_for_status()
        hover_data = response.json()
        if not hover_data.get('succeeded'):
            raise HoverException('response not succeeded')

        current_ip = get_public_ip()
        for domain in hover_data["domains"]:
            for entry in domain["entries"]:
                if entry["id"] == dns_id:
                    if entry['content'] != current_ip:
                        response = self.session.put('https://www.hover.com/api/dns/' + dns_id, {"content": current_ip})
                        response.raise_for_status()
                        hover_data = response.json()
                        if not hover_data.get('succeeded'):
                            raise HoverException('response not succeeded')
                return


def get_public_ip():
    response = requests.get("http://whatismyip.akamai.com/")
    response.raise_for_status()
    ip = ipaddress.IPv4Address(response.content.decode())
    return str(ip)


hover = HoverAPI()
hover.update_ip()

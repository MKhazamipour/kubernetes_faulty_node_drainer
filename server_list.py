import re
import subprocess
import json

def get_openstack_not_active_servers():
    openstack_servers = subprocess.Popen(
                        ['openstack', 'server', 'list', '-f', 'json'],
                        stdout=subprocess.PIPE
    )
    data = (openstack_servers.stdout.read())
    jsonfile = json.loads(data)
    with open('bad_servers.txt', 'w') as file:
        for d in jsonfile:
            if (d['Status']) != 'ACTIVE':
                file.write(d['Name'] + '\n')

def server_match_regex():
    get_openstack_not_active_servers()
    with open('bad_servers.txt', 'r') as servers_to_check:
        with open('servers.txt', 'w') as servers_to_write:
            for lines in servers_to_check:
                match = re.findall(r"^(?:(?:node-.*)|(?:infra-.*)).ir-thr-at1.arvan.run$",lines)
                for m in match:
                    servers_to_write.write(m + '\n')

def get_server_list():
    server_match_regex()
    servers = []
    with open('servers.txt', 'r') as servers_to_check:
        for lines in servers_to_check:
            servers.append(lines.strip())
        return servers
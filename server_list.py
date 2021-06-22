def get_server_list():
    servers = []
    with open('servers.txt', 'r') as servers_to_check:
        for lines in servers_to_check:
            servers.append(lines.strip())
        return servers
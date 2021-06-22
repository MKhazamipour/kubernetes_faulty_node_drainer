import subprocess
import os

kubeconfig_file = os.getenv('kube_config_path')


def get_server_list():
    servers = []
    with open('servers.txt', 'r') as servers_to_check:
        for lines in servers_to_check:
            servers.append(lines.strip())
        return servers


def cordon_faulty_servers(bad_server):
    for i in range(len(bad_server)):
        node_drain = subprocess.run(
                     ['kubectl', '--kubeconfig', kubeconfig_file, 'drain', bad_server[i],'--force', '--grace-period=0','--ignore-daemonsets','--delete-local-data'],
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE
                                    )
        print(node_drain.stdout.decode())
        print(node_drain.stderr.decode())
        i +=1


cordon_faulty_servers(get_server_list())
import subprocess
import os

from server_list import get_server_list

kubeconfig_file = os.getenv('kube_config_path')

faulty_servers = get_server_list()

def cordon_faulty_servers(sv):
    for i in range(len(sv)):
        node_drain = subprocess.run(
                     ['kubectl', '--kubeconfig', kubeconfig_file, 'drain', sv[i],'--force', '--grace-period=0','--ignore-daemonsets','--delete-local-data'],
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE
                                    )
        print(node_drain.stdout.decode())
        print(node_drain.stderr.decode())
        i +=1


cordon_faulty_servers(faulty_servers)
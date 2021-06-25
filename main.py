import subprocess
import os
import sys

from server_list import get_server_list

kubeconfig_file = os.getenv('kube_config_path')

faulty_servers = get_server_list()

def cordon_faulty_servers(sv):
    if len(sv) == 0:
        print("No server to drain... Exiting with code 0")
        sys.exit(0)
    else:
        for i in range(len(sv)):
            try:
                node_drain = subprocess.run(
                            ['kubectl', '--kubeconfig', kubeconfig_file, 'drain', sv[i],'--force', '--grace-period=0','--ignore-daemonsets','--delete-local-data'],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE
                                            )
                print(node_drain.stdout.decode())
                print(node_drain.stderr.decode())
                i +=1
            except TypeError:
                print("Please provide kubeconfig file path as 'kube_config_path' environment variable")
                sys.exit(1)


cordon_faulty_servers(faulty_servers)
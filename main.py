import subprocess
import os

#Check the status of servers
  #if all servers are okay flush redis
    # uncordon drained node
  #if any server is faulty add it to redis
    # drain faulty servers
kubeconfig_file = os.getenv('kube_config_path')

#r = redis.Redis(host='localhost', port=6379)

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
























""" def add_to_redis(sv_ip):
    if len(sv_ip) == 0:
        print("flushing redis")
        r.flushall()
    else:
        for i in range(len(sv_ip)):
            try:
                r.set('server_number'+str(i), servers[i])
                i += 1
            except redis.ConnectionError:
                print("Unable to connect to redis")
                sys.exit(1)



for srv in r.get():
    print(srv)
        
#k = subprocess.run(
#    ['kubectl', '--kubeconfig', kubeconfig_file, 'get', 'pods','--all-namespaces'],
#    stdout=subprocess.PIPE,
#    stderr=subprocess.PIPE
#)
#
#print(k.stdout.decode())
#print(k.stderr.decode())

to_redis = get_server_list()
add_to_redis(to_redis)


 """







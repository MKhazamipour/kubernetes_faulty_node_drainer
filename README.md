# kubernetes_faulty_node_drainer
Automatically drain a faulty kubernetes node to schedule load on other nodes

# Requirements
#### Openstack Client Envs
This script work with **Openstack Client** to get list of server that are not in **ACTIVE** state.
To work with openstack these **Environment Variables** should be passed to container

```bash
OS_AUTH_URL
OS_PROJECT_NAME
OS_USERNAME
OS_PASSWORD
OS_PROJECT_DOMAIN_NAME
OS_USER_DOMAIN_NAME
OS_IDENTITY_API_VERSION
OS_REGION_NAME
```

#### Kubeconfig

kubeconfig file path should be passed as **kube_config_path** environment variable to the container.

## Deploy inside kubernetes Cluster

To Deploy this script inside cluster you can create a **configMap** contains **kubeconfig** and mount it in a **CronJob** in kubernetes as following:

```bash
configMap:
```

```yaml
kind: ConfigMap
apiVersion: v1
metadata:
  name: config
  namespace: kubernetes-drainer
  labels:
    app: config
data:
  config: |
    KUBECONFIG FILE
```
---
```bash
CronJob:
```

```yaml
kind: CronJob
apiVersion: batch/v1beta1
metadata:
  name: drainer
  namespace: kubernetes-drainer
spec:
  schedule: '* * * * *'
  concurrencyPolicy: Forbid
  suspend: false
  jobTemplate:
    metadata:
      creationTimestamp: null
    spec:
      template:
        metadata:
          creationTimestamp: null
        spec:
          volumes:
            - name: config
              configMap:
                name: config
                defaultMode: 420
          containers:
            - name: drainer
              image: 'mormoroth/kubernetes-auto-node-drainer:v0.0.4'
              env:
                - name: OS_AUTH_URL
                  value: ''
                - name: OS_PROJECT_NAME
                  value: 
                - name: OS_USERNAME
                  value: 
                - name: OS_PASSWORD
                  value: 
                - name: OS_PROJECT_DOMAIN_NAME
                  value: 
                - name: OS_USER_DOMAIN_NAME
                  value: 
                - name: OS_IDENTITY_API_VERSION
                  value: ''
                - name: OS_REGION_NAME
                  value: 
                - name: kube_config_path
                  value: /app/config/config
              resources: {}
              volumeMounts:
                - name: config
                  mountPath: /app/config
              terminationMessagePath: /dev/termination-log
              terminationMessagePolicy: File
              imagePullPolicy: IfNotPresent
          restartPolicy: OnFailure
          terminationGracePeriodSeconds: 30
          dnsPolicy: ClusterFirst
          securityContext: {}
          schedulerName: default-scheduler
  successfulJobsHistoryLimit: 1
  failedJobsHistoryLimit: 1



## SSH
```bash
ssh root@192.168.188.3
```

## Alias
```bash
alias kubectl="inf-cli exec -i $(inf-cli get pods -a | awk '/ec-system/{print $2}') kube-apiserver -n kube-system -- kubectl --kubeconfig /etc/kubernetes/admin.conf"
```

## ESX Operator
```bash
kubectl get crd | grep esx
kubectl -n esx-system get HostConfiguration 
kubectl -n esx-system get HostConfiguration keswick-host-config -o yaml
kubectl -n esx-system get HostConfiguration esx-base-profile -o json
```

## VM Operator
```bash
kubectl get crd | grep vmoperator
kubectl get vm -o wide
```

## Face Detect

```bash
kubectl -n face-detector get all
kubectl -n face-detector get pods
kubectl -n face-detector get pods -o custom-columns='NAME:.metadata.name,IMAGE:.spec.containers[*].image'
kubectl -n face-detector get services
```

## Log Ship

```bash
kubectl -n log-ship get all

kubectl -n log-ship rollout restart deployment log-ship-deployment

kubectl exec -it pod/log-ship-deployment-b86558fc-8clf6 -- /bin/sh

sudo mount -t nfs 192.168.1.201:/nfs_share /Users/darrylcauldwell/mount/nfs
cp /path/to/local/file /mount/point/destination/
```

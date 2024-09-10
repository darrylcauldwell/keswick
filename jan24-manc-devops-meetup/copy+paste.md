
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
kubectl -n face-detector get services
```

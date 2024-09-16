# My notes

Project Keswick Tech Showcase

```url
https://veco929-kiad1.velocloud.net
```

The ESXi root password should be specified in the KS.cfg file.

Kubernetes runs on a VM,  it is possible to run commands from ESXi SSH using crx-cli and a config file.  It can be easier to create an alias and run commands directly from ESXi.

```bash
alias kubectl="inf-cli exec -i $(inf-cli get pods -a | awk '/ec-system/{print $2}') kube-apiserver -n kube-system -- kubectl --kubeconfig /etc/kubernetes/admin.conf"
```

While the NUC only has one NIC and so it will always have management running on default vmnic0.  When running on a device with multiple NICs can add a parameter to ensure correct NIC is used eg:

```bash
network --bootproto=dhcp --device=vmnic5
```

RTSP Authentication

```bash
rtsp://camera:password@192.168.1.127/stream1
rtsp://camera:password@192.168.1.127/stream2
```


.

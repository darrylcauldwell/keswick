# My notes

Project Keswick Tech Showcase

```url
https://keswick.showcase.vmware.com/ 
```

The ESXi root password should be specified in the KS.cfg file.

Kubernetes runs on a VM,  it is possible to run commands from ESXi SSH using crx-cli and a config file.  It can be easier to create an alias and run commands directly from ESXi.

```bash
alias kubectl="/bin/crx-cli exec --env 'KUBECONFIG=/mnt/volumes/volumes/kubernetes.io~empty-dir/etc-k8s/admin.conf' $(/bin/crx-cli list | grep infravisor-pod | awk '{print $1}') /infravisor/rootfs/keswick-control-plane/usr/bin/kubectl"
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


# 6.Minikube y AWS

Assumptions: vpc, security groups, .pem key, role must be configured and created. See: [1.1.Configuracion de servicios basicos para uso de AWS](https://github.com/ITAM-DS/analisis-numerico-computo-cientifico/wiki/1.1.Configuracion-de-servicios-basicos-para-uso-de-AWS)

For some Kubernetes references see: [What is Kubernetes?](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/), [4.AWS y Kubernetes](https://github.com/ITAM-DS/analisis-numerico-computo-cientifico/wiki/4.AWS-y-Kubernetes), [kubernetes-objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/)

Here a [video](https://www.youtube.com/watch?v=xL91E3FBgAg) that will guide you through next steps

# **First step**

Select AMI: `opt2-aws-educate-17-03-2021`

Select `m5.2xlarge`

# **Second step**

```
#!/bin/bash
##variables:
region=us-east-1 #make sure instance is in Virginia
name_instance=minikube
##System update
apt-get update -yq
##Tag instance
INSTANCE_ID=$(curl -s http://instance-data/latest/meta-data/instance-id)
PUBLIC_IP=$(curl -s http://instance-data/latest/meta-data/public-ipv4)
aws ec2 create-tags --resources $INSTANCE_ID --tag Key=Name,Value=$name_instance-$PUBLIC_IP --region=$region

```
# **Third Step**

ssh to instance:

```
ssh -o ServerAliveInterval=60 -i <your key> admin@<ipv4 of ec2 instance>
```

# **Four Step**

Change to root:

```
sudo su
```
Deploy minikube:

```
cd /root && minikube start --driver=none
```

# **Fifth Step**


Deploy kubeflow
```
cd /opt/kf-educate && /root/kfctl apply -V -f kfctl_k8s_istio.v1.0.2.yaml
```

After 3 mins check with

```
kubectl get pods -n kubeflow
```

all must be with status "Running" (and one with "Completed")

To access kubeflow UI set:

```
export INGRESS_HOST=$(minikube ip)
export INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].nodePort}')
```
Retrieve port

```
echo $INGRESS_PORT
```

(it's probable that the port will be 31380)

And go to:

```
http://<ipv4 of ec2 instance>:$INGRESS_PORT
```
->Enable port `$INGRESS_PORT` in security groups



# For Kubeflow namespace next will deploy services:

__Use next bash script in User data:__


Set:

```
OPT_LOAD_BALANCER_SERVICE=loadbalancer-opt-0.1-hostpath-pv
OPT_PV=hostpath-pv
OPT_PVC=hostpath-pvc
OPT_JUPYTERLAB_SERVICE=jupyterlab-opt-0.1-hostpath-pv
OPT_URL=https://raw.githubusercontent.com/jlrzarcor/OptAvzda-2021-hill-eureka/main/deployments/minikube/
```



Create storage:

```
kubectl create -f $OPT_URL/hostpath_pv/$OPT_PV.yaml
kubectl create -f $OPT_URL/hostpath_pv/$OPT_PVC.yaml
```

Create service:

```
kubectl create -f $OPT_URL/hostpath_pv/$OPT_LOAD_BALANCER_SERVICE.yaml
```

Create deployment:

```
kubectl create -f $OPT_URL/hostpath_pv/$OPT_JUPYTERLAB_SERVICE.yaml
```

And after 3 mins go to


```
http://<ipv4 of ec2 instance>:30001/hillandgradiant
```

all must be with status "Running" (and one with "Completed")

Delete:

```
kubectl delete service -n kubeflow $OPT_LOAD_BALANCER_SERVICE
kubectl delete pvc -n kubeflow $OPT_PVC
kubectl delete pv -n kubeflow $OPT_PV
kubectl delete deployment -n kubeflow $OPT_JUPYTERLAB_SERVICE 
```

# JUPYTERLAB SERVICE IS USING DOCKER IMAGE FROM NEXT [Dockerfile](https://github.com/jlrzarcor/OptAvzda-2021-hill-eureka/tree/main/dockerfiles/pkg)



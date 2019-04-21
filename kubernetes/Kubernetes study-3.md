# Kubernetes study

### Orchestrating the Cloud with Kubernetes



시작하기전에, 아래 repo 를 받아서 세팅해보자.

```bash
git clone https://github.com/googlecodelabs/orchestrate-with-kubernetes.git
```



## Nginx with Kubernetes

Kubernetes 에 Nginx 를 설치해서 사용해 보자.



```bash
kubectl run nginx --image=nginx:1.10.0 
```

nginx 1.10.0 이미지로 nginx 라는 이름으로 deployment 를 생성한다.



```bash
kubectl expose deployment nginx --port 80 --type LoadBalancer
```

nginx 를 위해서 80번 포트를 nginx deployment 에 열어주고  External IP 로 container 에 접근하기 위해서 service를 만들어주고 type 은 LoadBalancer로 해준다.

이 service 는 하위 Pod 들에 들어가는 트래픽들에 대한 Load Balancer 역활을 하게 된다.

```bash
$ kubectl get services
NAME         TYPE           CLUSTER-IP     EXTERNAL-IP       PORT(S)        AGE
kubernetes   ClusterIP      10.7.240.1     <none>            443/TCP        10m
nginx        LoadBalancer   10.7.247.238   104.198.186.195   80:31357/TCP   6m
```

```bash
$ curl http://104.198.186.195:80
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>
<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>
<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

성공!



## Pods

![fb02d86798243fcb.png](https://gcpstaging-qwiklab-website-prod.s3.amazonaws.com/bundles/assets/b73bcce701677c046738d0175fdea7cfc3a0a8e6b58a1c7a90293e7a531a91fc.jpg)

Pod은 하나 이상의 container 로 구성되어있다. 



Pod 에는 몇가지 특징들이 있다.

- Pod 내부의 컨테이너들은 IP 와 Port 정보를 공유한다. 이렇게 되면, 다른 컨테이너를 localhost 를 통해서 접근할 수 있게 된다.
- Pod 내부의 컨테이너들은 디스크 볼륨을 공유한다. 따라서 같은 Pod 이라면 다른 컨테이너의 디스크 볼륨에 접근할 수 있게 된다.

Pod 이 시작/재시작 될때, 컨테이너마다 로컬 디스크를 생성하여 시작하게 되는데, 이 로컬 디스크는 시작/재시작 될때마다 새롭게 정의되어 정보가 사라지게 된다.



DB 같이 영구적으로 데이터를 보관해야 하는경우, 시작과 재시작에 영향을 받지 않아야 하는 경우, **volumn** 이라는 스토리지를 사용해야 한다.

Volumn 은 컨테이너 입장에서는 외장하드 느낌으로, Pod 이 시작/재시작 할때 컨테이너에 마운트해서 사용할 수 있다.



Pod 은 Pod configuration file 로 생성될 수 있다. 한번 예제의 config를 보자.



```bash
$ cat pods/monolith.yaml
apiVersion: v1
kind: Pod
metadata:
  name: monolith
  labels:
    app: monolith
spec:
  containers:
    - name: monolith
      image: kelseyhightower/monolith:1.0.0
      args:
        - "-http=0.0.0.0:80"
        - "-health=0.0.0.0:81"
        - "-secret=secret"
      ports:
        - name: http
          containerPort: 80
        - name: health
          containerPort: 81
      resources:
        limits:
          cpu: 0.2
          memory: "10Mi"
```

이 Pod 은 하나의 container 로 구성되어있으며, image 는  kelseyhightower/monolith:1.0.0 이다.

이 Pod 이 시작되면서, 3가지 argument 가 monolith container 로 전달된다.

http 는 80번 포트로, health 정보는 81번 포트로 전달된다.



이 파일을 기반으로 Pod을 만들어보자.



```bash
kubectl create -f pods/monolith.yaml
```



```bash
$ kubectl get pods
NAME                     READY     STATUS    RESTARTS   AGE
monolith                 1/1       Running   0          24s
nginx-68c5b54745-7s42x   1/1       Running   0          24m

$ kubectl get deployment
NAME      DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
nginx     1         1         1            1           25m
```

deployment 로 Pod 을 생성했을때와는 다르게, name 뒤에 특정 string 이 없다.

또한 deployment 에도 등록되어있지 않다.



pod 이 실행중이라면, 아래 명령어로 pod의 정보를 알 수 있다.

```bash
kubectl describe pods monolith
```



## interacting with Pods

Pod 은 private IP 를 가지며 Cluster 를 통해서 접근하지 않으면 접근할 수 없다.

`kubectl port-forward` 명령어를 통해서 Pod 내부의 port 와 외부의 port 를 연결해줄 수 있다.

```bash
$ kubectl port-forward monolith 10080:80
Forwarding from 127.0.0.1:10080 -> 80

Handling connection for 10080
Handling connection for 10080
```

```bash
$ curl http://127.0.0.1:10080
{"message":"Hello"}
```

10080 port 가 pod 내부의 80번 포트로 연결된 것을 알 수 있다.



이제 한번 로그인 기능을 이용해 보자.

```bash
TOKEN=$(curl http://127.0.0.1:10080/login -u user|jq -r '.token')
```

정상적으로 하위 path 도 접근할 수 있는것을 알 수 있다.

```bash
$ curl -H "Authorization: Bearer $TOKEN" http://127.0.0.1:10080/secure
{"message":"Hello"}
```



monolith 의 로그를 보면 http request log들이 있다.

```bash
)$ kubectl logs 
monolith
2019/01/13 11:16:49 Starting server...
2019/01/13 11:16:49 Health service listening on 0.0.0.0:81
2019/01/13 11:16:49 HTTP service listening on 0.0.0.0:80
127.0.0.1:52816 - - [Sun, 13 Jan 2019 11:24:41 UTC] "GET / HTTP/1.1" curl/7.52.1
127.0.0.1:52830 - - [Sun, 13 Jan 2019 11:25:01 UTC] "GET / HTTP/1.1" curl/7.52.1
127.0.0.1:52896 - - [Sun, 13 Jan 2019 11:27:51 UTC] "GET /login HTTP/1.1" curl/7.52.1
127.0.0.1:52908 - - [Sun, 13 Jan 2019 11:27:58 UTC] "GET /login HTTP/1.1" curl/7.52.1
127.0.0.1:52940 - - [Sun, 13 Jan 2019 11:29:28 UTC] "GET /secure HTTP/1.1" curl/7.52.1
```



log 에 -f 옵션을 붙이면 log stream 을 얻어 real-time 으로 log 를 볼 수 있다.

```bash
$ kubectl logs -f monolith
2019/01/13 11:16:49 Starting server...
2019/01/13 11:16:49 Health service listening on 0.0.0.0:81
2019/01/13 11:16:49 HTTP service listening on 0.0.0.0:80
127.0.0.1:52816 - - [Sun, 13 Jan 2019 11:24:41 UTC] "GET / HTTP/1.1" curl/7.52.1
127.0.0.1:52830 - - [Sun, 13 Jan 2019 11:25:01 UTC] "GET / HTTP/1.1" curl/7.52.1
127.0.0.1:52896 - - [Sun, 13 Jan 2019 11:27:51 UTC] "GET /login HTTP/1.1" curl/7.52.1
127.0.0.1:52908 - - [Sun, 13 Jan 2019 11:27:58 UTC] "GET /login HTTP/1.1" curl/7.52.1
127.0.0.1:52940 - - [Sun, 13 Jan 2019 11:29:28 UTC] "GET /secure HTTP/1.1" curl/7.52.1
127.0.0.1:52996 - - [Sun, 13 Jan 2019 11:31:53 UTC] "GET / HTTP/1.1" curl/7.52.1
127.0.0.1:53006 - - [Sun, 13 Jan 2019 11:31:58 UTC] "GET / HTTP/1.1" curl/7.52.1
```



kubectl exec 명령어를 통해서 Pod 내부에 interactive 하게 shell 명령어를 작성할 수 있다.

외부에서 cluster 를 통해서만 Pod 을접근할 수 있지만, Pod 내부에서 외부로 접근할 때는 크게 작업할 필요 없다.

exit 명령어를 통해서 나올 수 있다.



```bash
$ kubectl exec 
monolith --stdin --tty -c monolith /bin/sh
/ # ls
bin      etc      lib      media    proc     run      sys      usr
dev      home     linuxrc  mnt      root     sbin     tmp      var
/ # pwd
/
/ # ping -c 3 google.com
PING google.com (108.177.112.138): 56 data bytes
64 bytes from 108.177.112.138: seq=0 ttl=51 time=0.831 ms
64 bytes from 108.177.112.138: seq=1 ttl=51 time=0.455 ms
64 bytes from 108.177.112.138: seq=2 ttl=51 time=0.585 ms
--- google.com ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 0.455/0.623/0.831 ms
/ # exit
google2203930_student@cloudshell:~/orchestrate-with-kubernetes/kubernetes (qwiklabs-gcp-3e633d0123b51044)$
```



## Services

![393e02e1d49f3b37.png](https://gcpstaging-qwiklab-website-prod.s3.amazonaws.com/bundles/assets/260d13ff7dba012c2a783d6f0143c1587e70d43ff4a199facf9990e4cb9bc0bf.jpg)

Pod 은 영원하지 않다. 하나의 Pod은 멈출수도 있고, 재시작될 수 있다. 또한 서로 다른 Pod 이거나, Pod 이 재시작될경우 IP 가 달라질 수 있다. 

Service 가 이러한 문제를 해결할 수 있다.

Service 는 Pod의 stable endpoints 가 된다.

Service 가 자신에게 포함된 Pod을 찾아야하는 문제가 있다. Pod 들은 동적으로 생성 및 재시작 등의 결과를 거치면서 IP 가 유동적으로 바뀌기 때문에 해당 Pod 이 어떤것인지 식별할 필요가 있다.

따라서 Service 는 Label 을 이용하여 어떤 Pod에 자신이 작업해야하는지 탐지한다.

Pod 에 Label 이 올바르게  작성되어있다면 service 가 자동으로 연결한다.



service 가 Pod 에 접근할때는 총 3가지 타입이 있다.

- Cluster IP : 기본 type 으로, service 는 오직 cluster 를 통해서만 볼 수 있다.
- NodePort : cluster 내부의 node들에게 각각 외부에서 접근할 수 있는 IP 를 부여한다.
- LoadBalancer : Service 에서 node 로 가는 traffic 을 관리하는 load balancer 를 부여한다.



Service 를 만들어보자

```bash
kubectl create secret generic tls-certs --from-file tls/
kubectl create configmap nginx-proxy-conf --from-file nginx/proxy.conf
kubectl create -f pods/secure-monolith.yaml
```



monolith service 의 config file 을 보자

```bash
cat services/monolith.yaml
kind: Service
apiVersion: v1
metadata:
  name: "monolith"
spec:
  selector:
    app: "monolith"
    secure: "enabled"
  ports:
    - protocol: "TCP"
      port: 443
      targetPort: 443
      nodePort: 31000
  type: NodePort
```

selector 라는것이 있는데, 자동으로 label 이 `app=monolith` 이고 `secure=enable` 인 Pod 들을 찾고 expose 한다.

내부 nginx port 는 443번이고 해당 port 를 nodeport type 으로 31000 port 로 연결한다.



-f 옵션으로 service 를 config 파일로 부터 생성해보자.

```bash
kubectl create -f services/monolith.yaml
```



gcp 상의 firewall 에 규칙을 추가하자. 방금 연 31000 port 로 외부에서 접속할 수 있도록 허용해준다.

```bash
gcloud compute firewall-rules create allow-monolith-nodeport --allow=tcp:31000
```



node 들의 external ip 를 알아보자.

```bash
$ gcloud compute instances list
NAME                               ZONE           MACHINE_TYPE   PREEMPTIBLE  INTERNAL_IP  EXTERNAL_IP     STATUS
gke-io-default-pool-86dc662c-69sr  us-central1-b  n1-standard-1               10.128.0.3   35.184.107.121  RUNNING
gke-io-default-pool-86dc662c-ct4j  us-central1-b  n1-standard-1               10.128.0.2   35.192.182.96   RUNNING
gke-io-default-pool-86dc662c-z5jp  us-central1-b  n1-standard-1               10.128.0.4   35.238.154.37   RUNNING
```

위의 external ip 를 통해서

https://<EXTERNAL_IP>:31000 로 접근해볼려 하지만, time out 이 발생한다.



```bash
$ kubectl get services monolith
NAME       TYPE       CLUSTER-IP    EXTERNAL-IP   PORT(S)         AGE
monolith   NodePort   10.7.255.99   <none>        443:31000/TCP   4m
```

```bash
$ kubectl describe services monolith
Name:                     monolith
Namespace:                default
Labels:                   <none>
Annotations:              <none>
Selector:                 app=monolith,secure=enabled
Type:                     NodePort
IP:                       10.7.255.99
Port:                     <unset>  443/TCP
TargetPort:               443/TCP
NodePort:                 <unset>  31000/TCP
Endpoints:                <none>
Session Affinity:         None
External Traffic Policy:  Cluster
Events:                   <none>
```

일단 service 에 external ip 가 부여되지 않았고, lable 도 none이다.

현재 monolith service 는 endpoints 를 가지고 있지 않는다. 

```bash
$ kubectl get pods -l "app=monolith"
NAME              READY     STATUS    RESTARTS   AGE
monolith          1/1       Running   0          43m
secure-monolith   2/2       Running   0          12m
$ kubectl get pods -l "app=monolith,secure=enabled"
No resources found.
```

`app=monolith,secure=enabled` 를 만족하는 pod 이 존재하지 않는다.

위의 node 들에 label 들을 달아줘야 service 가 pod 을 탐지할 것이다.



`kubectl label` 을 통해서 label 을 추가해주자.

```bash
$ kubectl labelpods secure-monolith 'secure=enabled'
pod "secure-monolith" labeled
$ kubectl get pods -l "app=monolith,secure=enabled"
NAME              READY     STATUS    RESTARTS   AGE
secure-monolith   2/2       Running   0          14m
```



다시 monolith service 의 정보를 보자

```bash
$ kubectl describe services monolith
Name:                     monolith
Namespace:                default
Labels:                   <none>
Annotations:              <none>
Selector:                 app=monolith,secure=enabled
Type:                     NodePort
IP:                       10.7.255.99
Port:                     <unset>  443/TCP
TargetPort:               443/TCP
NodePort:                 <unset>  31000/TCP
Endpoints:                10.4.1.7:443
Session Affinity:         None
External Traffic Policy:  Cluster
Events:                   <none>
```

End point 가 생겼다! 이제 접속할수 있다.



## Deploying Application with kubernetes

![f96989028fa7d280.png](https://gcpstaging-qwiklab-website-prod.s3.amazonaws.com/bundles/assets/d540fb3133f4671c1e704ffae0c25234e3fc401eec53dad32343d2bf4f0e573d.jpg)

Deployment 를 사용하면, Pod 을 low level 에서 건드릴 필요가 없어진다. Deployment 는 Replica set 이라는것으로 Pod 을 managing 한다.

![b2e31eed284e4cfe.png](https://gcpstaging-qwiklab-website-prod.s3.amazonaws.com/bundles/assets/7c7e19c4637183928b072e7291bc0a3484bd30827d72070c103ba10746bdb81a.jpg)

각 노드에 1개씩 Pod 이 있던 상태에서 Node 3 가 down 될 경우, Deployment는 다른 node 에 새로운 Pod 을 생성한다. 

> Service 에 직접 Pod 을 연결하는것이 아닌 Deployment 로 Pod 의 managing 을 맡기고,
>
> service 와 deployment 를 연결시키는 것 같은데 확실하지는 않다. 아직 뇌피셜.



## Creating Deployment 

deployment config file 을 통해서 deployment 를 생성하고, 설정들을 탐색해보자.



``` bash
$ cat deployments/auth.yaml

apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: auth
spec:
  replicas: 1
  template:
    metadata:
      labels:
        app: auth
        track: stable
    spec:
      containers:
        - name: auth
          image: "kelseyhightower/auth:1.0.0"
          ports:
            - name: http
              containerPort: 80
            - name: health
              containerPort: 81

```

하나의 replica 를 가지는 deployment 이다.



이제 deployment 를 만들고 이 deployment 를 위한 service 를 만들어보자



```bash
kubectl create -f deployments/auth.yaml
kubectl create -f services/auth.yaml

kubectl create -f deployments/hello.yaml
kubectl create -f services/hello.yaml

kubectl create configmap nginx-frontend-conf --from-file=nginx/frontend.conf
kubectl create -f deployments/frontend.yaml
kubectl create -f services/frontend.yaml
```


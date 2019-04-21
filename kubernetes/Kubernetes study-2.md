# Kubernetes study

### Hello Node Kubernetes

![ba830277f2d92e04.png](https://gcpstaging-qwiklab-website-prod.s3.amazonaws.com/bundles/assets/641fcb4eefdf381baeeecbda634fe27abfd2bdb25d7c5dcbadbff9c285de79c2.png)

![Why Containers?](https://d33wubrfki0l68.cloudfront.net/e7b766e0175f30ae37f7e0e349b87cfe2034a1ae/3e391/images/docs/why_containers.svg)



Kubernetes 오픈소스로, 다양한 환경에서 실행될 수 있으며 컨테이너 매니징 해주는 컨테이너 운영 환경 이다. 컨테이너 스케쥴링, 모니터링, 삭제 관리 등 컨테이너를 종합적으로 관리해주는 운영환경이다.





## 간단한 Docker container 만들기

```javascript
const http = require('http');
const handleRequest = (req, res) => {
	res.writeHead(200);
	res.end("Hello World!");
}

const www = http.createServer(handleRequest);
www.listen(8080);
```

간단한 node 앱



docker 를 이용하기 위해서 Dockerfile 파일 정의



```dockerfile
FROM node:10.14.2
EXPOSE 8080
COPY server.js .
CMD node server.js
```

docker hub 에서 node의 10.14.2 tag 이미지를 찾아서 시작한다.

8080포트를 외부와 연결할 수 있게 열어두고

server.js 파일을 image 로 복사한다.



docker 빌드 밑 실행

```bash
docker build -t gcr.io/qwiklabs-gcp-14dd3142938af82d/hello-node:v1 .
```

```bash
docker run -d -p 8080:8080 gcr.io/qwiklabs-gcp-14dd3142938af82d/hello-node:v1
```

gcr 에 푸쉬하기 위해서 image 이름을 `gcr.io/프로젝트ID/프로젝트명` 로 만든다.



다음 명령어로 gcr 에 container 를 푸쉬한다.

```bash
gcloud docker -- push gcr.io/qwiklabs-gcp-14dd3142938af82d/hello-node:v1
```

> -- 와 push 사이에 공백이 한번 있다. 주의하자.



## Cluster 생성하기

cluster 는 구글에서 호스팅하는 Kubernetes master API server 와 worker nodes 들의 집합으로 구성되어있다.

![img](https://d33wubrfki0l68.cloudfront.net/99d9808dcbf2880a996ed50d308a186b5900cec9/40b94/docs/tutorials/kubernetes-basics/public/images/module_01_cluster.svg)

Worker node 들은 쿠버네티스 클러스터 내 워커 머신으로써 동작하는 VM 또는 물리적인 컴퓨터 이다.

Application 을 kubernetes 에 배포한다는것은, 마스터에 app container 를 구동하라고 지시하는것이다.

마스터는 container를 어떤 cluster 에 구동시킬지 스케쥴한다. 

node들은 마스터가 제공하는 k8s api 를 통해서 마스터와 통신한다.

최종적으로 사용자는 k8s api 를 통해 클러스터와 상호작용 한다.



gcloud 를 통해서 cluster 를 생성하보자

```bash
gcloud container clusters create hello-world \
                --num-nodes 2 \
                --machine-type n1-standard-1 \
                --zone us-central1-a
```



n1-standard-1 머신 사용하는 노드 2개를 하나의 클러스터로 설정해서 생성한다.

클러스터의 이름은 hello-world 이고 VM 은 us-central1-a 에 생성한다.



| 시스템 이름     | 설명                                                         | 가상 CPU1 | 메모리(GB) | PD(영구 디스크) 최대 개수2                                   | 최대 총 PD 크기(TB) |
| :-------------- | ------------------------------------------------------------ | --------- | ---------- | ------------------------------------------------------------ | ------------------- |
| `n1-standard-1` | 1개의 가상 CPU, 3.75GB 메모리를 사용하는 표준 머신 유형입니다. | 1         | 3.75       | 16([**베타**는 32](https://cloud.google.com/compute/docs/disks#pdnumberlimits)) | 64                  |



아래와같은 log 가 뜨면 성공적으로 cluster 가 생성된것이다.

```bash
Creating cluster hello-world in us-central1-a...done.
Created [https://container.googleapis.com/v1/projects/qwiklabs-gcp-8ad3c094cf3410ed/zones/us-central1-a/clusters/hello-world].
To inspect the contents of your cluster, go to: https://console.cloud.google.com/kubernetes/workload_/gcloud/us-central1-a/hello-world?project=qwiklabs-gcp-8ad3c094cf3410ed
kubeconfig entry generated for hello-world.
NAME         LOCATION       MASTER_VERSION  MASTER_IP       MACHINE_TYPE   NODE_VERSION  NUM_NODES  STATUS
hello-world  us-central1-a  1.10.9-gke.5    35.225.105.202  n1-standard-1  1.10.9-gke.5  2          RUNNING
```

> 또한 GCP 의 console 을 통해서도 cluster 를 생성할 수 있다.
>
> Kubernetes Engine > Kubernetes clusters > Create cluster



## Pod 생성하기

kubernetes pod 은 container들의 그룹으로 kubernetes 에서 가장 기본적인 배포 단위다.

kubernetes 는 하나의 컨테이너를 개별적으로 배포하지 않고, Pod 단위로 배포하며 Pod 은 하나 이상의 컨테이너를 가지고 있다.



Pod 에는 몇가지 특징들이 있다.

- Pod 내부의 컨테이너들은 IP 와 Port 정보를 공유한다. 이렇게 되면, 다른 컨테이너를 localhost 를 통해서 접근할 수 있게 된다.
- Pod 내부의 컨테이너들은 디스크 볼륨을 공유한다. 따라서 같은 Pod 이라면 다른 컨테이너의 디스크 볼륨에 접근할 수 있게 된다.

Pod 이 시작/재시작 될때, 컨테이너마다 로컬 디스크를 생성하여 시작하게 되는데, 이 로컬 디스크는 시작/재시작 될때마다 새롭게 정의되어 정보가 사라지게 된다.



DB 같이 영구적으로 데이터를 보관해야 하는경우, 시작과 재시작에 영향을 받지 않아야 하는 경우, **volumn** 이라는 스토리지를 사용해야 한다.

Volumn 은 컨테이너 입장에서는 외장하드 느낌으로, Pod 이 시작/재시작 할때 컨테이너에 마운트해서 사용할 수 있다.



`kubectl run` 을 통해서 Pod 을 생성할 수 있다.

```bash
kubectl run hello-node \
    --image=gcr.io/qwiklabs-gcp-14dd3142938af82d/hello-node:v1 \
    --port=8080
deployment.apps "hello-node" created
```



log 에 `deployment.apps` 라고 뜬것을 볼 수 있듯이,  deployment object 를 생성하면 Pod이 생성된다.

새로운 deployment 는 single pod replica 



아래 명령어를 통해서 deployment 들의 정보들을 볼 수 있다.

```bash
kubectl get deployments
```



```bash
google2202782_student@cloudshell:~ (qwiklabs-gcp-14dd3142938af82d)$ kubectl get deployments
NAME         DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
hello-node   1         1         1            1           39s
```



아래 명령어를 통해서 deployment 에 의해 생성된 pod 의 정보를 볼 수 있다.

```bash
kubectl get pods
```



```bash
google2202782_student@cloudshell:~ (qwiklabs-gcp-14dd3142938af82d)$ kubectl get pods
NAME                          READY     STATUS    RESTARTS   AGE
hello-node-68847f89d4-d75jc   1/1       Running   0          55s
```



아래는 몇가지 kubetl 명령어 들이다

```bash
kubectl cluster-info
	cluster 의 정보를 불러온다
kubectl config view
	# Show Merged kubeconfig settings.
아래 명령어들은 trobuleshooting 을 위한 명령어들이다.
kubectl get events
kubectl logs <pod-name>
```



## Allow external traffic

기본적으로, Pod 은 cluster의 internal IP를 통해서만 접근할 수 있다. 쿠버네티스 외부에서 app에 접근하기 위해서는 kubernetes service 를 통해 expose 해야한다.



Pod을 public internet으로 expose 하기 위해선 아래와 같은 명령어를 사용한다.

```bash
kubectl expose deployment hello-node --type="LoadBalancer"
```

expose 하는 대상은, deployment 이여야 한다. Pod 을 expose 하면 안된다.

service 가 트래픽을 deployment 에 포함되는 모든 Pod들을 대상으로 Load Balancing 하면서 모든 Pod들을 관리해야하기 떄문이다.



```bash
google2202782_student@cloudshell:~ (qwiklabs-gcp-14dd3142938af82d)$ kubectl get services
NAME         TYPE           CLUSTER-IP      EXTERNAL-IP      PORT(S)          AGE
hello-node   LoadBalancer   10.31.244.254   35.226.201.119   8080:30430/TCP   3m
kubernetes   ClusterIP      10.31.240.1     <none>           443/TCP          26m
```



hello-node deployment 의 External IP 가 35.226.201.119 이므로

`http://35.226.201.119:8080/` 로 접속해보자.

```bash
google2202782_student@cloudshell:~ (qwiklabs-gcp-14dd3142938af82d)$ curl http://35.226.201.119:8080/
Hello World!
```



## Scale up your service

kubernetes 의 강력한 기능중 하나는, 바로 application 을 쉽게 scaling 할 수 있다는것이다.

Scale Up 하기 위해서 는 Replication controller 에게 명령을 내리면 된다.

Replication controller 는 Pod 의 replica 를 더 생성하게 된다.



```bash
kubectl scale deployment hello-node --replicas=4
```

```bash
$ kubectl get deployment
NAME         DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
hello-node   4         4         4            4           35m

$ kubectl get pods
NAME                          READY     STATUS    RESTARTS   AGE
hello-node-68847f89d4-5llq6   1/1       Running   0          1m
hello-node-68847f89d4-d75jc   1/1       Running   0          35m
hello-node-68847f89d4-jlktx   1/1       Running   0          1m
hello-node-68847f89d4-stpcn   1/1       Running   0          1m
```



## Roll out an upgrade to your service

일부 버그fix 등의 코드에서 변경점이 있을경우 새로운 버전을 deploy 해야할때, 어떻게 해야할까?



일단, 코드를 수정후 docker를 다른 tag 로 빌드한 후 새로운 container image 를 publish 한다.

```bash
docker build -t gcr.io/qwiklabs-gcp-14dd3142938af82d/hello-node:v2 .
gcloud docker -- push gcr.io/qwiklabs-gcp-14dd3142938af82d/hello-node:v2
```



그 후 kubectl 의 에서 image 설정을 바꿔주면 된다.

```bash
kubectl edit deployment hello-node
```

```bash
# Please edit the object below. Lines beginning with a '#' will be ignored,
# and an empty file will abort the edit. If an error occurs while saving this file will be
# reopened with the relevant failures.
#
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  annotations:
    deployment.kubernetes.io/revision: "1"
  creationTimestamp: 2016-03-24T17:55:28Z
  generation: 3
  labels:
    run: hello-node
  name: hello-node
  namespace: default
  resourceVersion: "151017"
  selfLink: /apis/extensions/v1beta1/namespaces/default/deployments/hello-node
  uid: 981fe302-f1e9-11e5-9a78-42010af00005
spec:
  replicas: 4
  selector:
    matchLabels:
      run: hello-node
  strategy:
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 1
    type: RollingUpdate
  template:
    metadata:
      creationTimestamp: null
      labels:
        run: hello-node
    spec:
      containers:
      #- image: gcr.io/PROJECT_ID/hello-node:v1     # v1 을 v2 로 변경
      - image: gcr.io/PROJECT_ID/hello-node:v2
        imagePullPolicy: IfNotPresent
        name: hello-node
        ports:
        - containerPort: 8080
          protocol: TCP
        resources: {}
        terminationMessagePath: /dev/termination-log
      dnsPolicy: ClusterFirst
      restartPolicy: Always
      securityContext: {}
      terminationGracePeriodSeconds: 30
```



이 작업을 하는동안, 유저는 서비스에서 어떤 interruption 도 경험하지 못하게 된다. 초기에 잠깐 버전을 바꾸는 작업이 있는 후에, 정상적으로 접근할 수 있게 된다.



## Kubernetes graphical dashboard

Kubernetes 를 gui dashborad 로 관리

---

참고문서

http://bcho.tistory.com/1255

https://kubernetes.io/ko/docs/concepts/overview/what-is-kubernetes/

https://lng1982.tistory.com/270
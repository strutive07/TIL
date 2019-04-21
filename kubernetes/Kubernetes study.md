# Kubernetes study

### Introduction to Docker



### GCP 설명



- Google cloud Shell

  Shell 형태로 google cloud 를 관리.

- gcloud

  command line tool 로써 pre-installed 되어있음. GCP 를 컨트롤하는 용도.

  - Commands

    - gcloud auth list

      active account names 출력

    - gcloud config list project

      project ID 출력

    - gcloud document : https://cloud.google.com/sdk/gcloud



## 시작

```bash
docket run hello-world
```



docker daemon은 hello-world image 를 서치한다.

로컬에 설치되어있지 ㅇ낳으면, public registry 인 Docker Hub 에서 pull한다.



```bash
docker images
```



```bash
sniperzkzl@cloudshell:~ (silken-forest-214415)$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
hello-world         latest              fce289e99eb9        10 days ago         1.84kB
```



```bash
docker ps
docker ps -a
```



-a 를 안붙이면 실행중인 docker 프로세스.

-a 를 붙이면 exited 된 프로세스 목록까지 보여줌.



## Build

```bash
cat > Dockerfile<<EOF

# Use an official Node runtime as the parent image
# node version 6 의 base parent image 를 사용한다.
FROM node:6

# Set the working directory in the container to /app
# working dir 설정
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Make the container's port 80 available to the outside world
# 80번 포트가 외부에서 접근할 수 있도록 설정,
EXPOSE 80

# Run app.js using node when the container launches
# node app.js 명령어 실행
CMD ["node", "app.js"]
EOF
```





```bash
cat > app.js <<EOF

const http = require('http');

const hostname = '0.0.0.0';
const port = 80;

const server = http.createServer((req, res) => {
    res.statusCode = 200;
      res.setHeader('Content-Type', 'text/plain');
        res.end('Hello World\n');
});

server.listen(port, hostname, () => {
    console.log('Server running at http://%s:%s/', hostname, port);
});

process.on('SIGINT', function() {
    console.log('Caught interrupt signal and will exit');
    process.exit();
});
EOF

# nodejs 간단한 서버 작성
```



```bash
docker build -t node-app:0.1 .
```



현재 디렉토리에 있는 `Dockerfile` 을 실행할것이다.

-t 옵션은 이미지에 name: tag 형식으로 넣어주기 위함이다.



## Run

```bash
docker run -p 4000:80 --name my-app node-app:0.1
```

4000번 포트를 container의 80번 포트와 연결한다.

image 는 name은 node-app 이고, tage 는 0.1인것을 사용하고 name 은 my-app 이라고 명명한다.



만약 컨테이너가 background 에서 돌고있게 할려면, -d 옵션을 주면 된다.

해당 container 를 멈추기 위해서는 다음 명령어를 사용하면 된다.

```bash
docker stop my-app
```



삭제는 다음 명령어를 사용하면 된다.



```bash
docker rm my-app
```



container 가 실행중이라면, log 를 볼 수 있다.



```bash
docker logs [container-id]
```

 

신 버전을 새로 빌드할때, tag 의 값을 올려주기만 하면 같은 name 다른 버전의 빌드를 유지할 수 있다.



```bash
# 파일 일부 수정 후
docker build -t node-app:0.2 .
docker run -p 8080:80 --name my-app-2 -d node-app:0.2
```





## Debug



log를 cat 같이 한번만 보여주는게 아니라, 지속적으로 해당 세션의 정보를 띄우게 할려면 -f 옵션을 붙이면 된다.



```bash
docker logs -f [container_id]
```



러닝중인 container 의 command line 의 세션을 가져와서 명령어를 실행시키고 싶을경우 다음 명령어를 사용하면 된다.



```bash
docker exec -it [container_id] bash
```



그럼 앞의 command lien 이

```bash
sniperzkzl@cloudshell:~ (silken-forest-214415)$
sniperzkzl@cloudshell:~ (silken-forest-214415)$ docker exec -it 87a bash
root@87a5ef1d7cfd:/app#
```

이렇게 변경되었다.



```bash
root@87a5ef1d7cfd:/app# ls
Dockerfile  app.js
root@87a5ef1d7cfd:/app# pwd
/app
root@87a5ef1d7cfd:/app# cd ..
root@87a5ef1d7cfd:/# ls
app  bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@87a5ef1d7cfd:/# cd
root@87a5ef1d7cfd:~# ls 
root@87a5ef1d7cfd:~# exit
exit
sniperzkzl@cloudshell:~ (silken-forest-214415)$ ls
README-cloudshell.txt  test
sniperzkzl@cloudshell:~ (silken-forest-214415)$ cd test/
sniperzkzl@cloudshell:~/test (silken-forest-214415)$ ls
app.js  Dockerfile
sniperzkzl@cloudshell:~/test (silken-forest-214415)$
```

working dir 였던 app dir 가 특별히 마운트되어있는 모습을 볼 수 있다.



container 의 metadata를 탐색하기 위해선 inspect 명령어를 사용한다.

```bash
docker inspect [container_id]
```



--format 옵션을 통해서 JSON 형식의 metatdata 속 특정 field 만 지정하여 볼 수도 있다.



```bash
sniperzkzl@cloudshell:~/test (silken-forest-214415)$ docker inspect --format='{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' 87a
172.18.0.2
```



## Publish

Google container Registry  라는곳에 image 를 push 할수 있다.



```bash
gcloud config list project
docker tag node-app:0.2 gcr.io/[project-id]/node-app:0.2
gcloud docker -- push gcr.io/[project-id]/node-app:0.2
```

`[hostname]/[project-id]/[image]:[tag]` 형식으로 작성한 후, gcloud 로 push 하면된다.



```bash
docker stop $(docker ps -q)
docker rm $(docker ps -aq)
# 주의. 모든 container 를 중지하고 지우는 명령어
```


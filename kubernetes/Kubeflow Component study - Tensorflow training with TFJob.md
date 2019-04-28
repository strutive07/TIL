# Kubeflow Component study - Tensorflow training with TFJob

TFJob 은 kubernetes custom resource 로, kubernetes 위에서 tensorflow training 을 하기 위해 만들어진 것이다.

tfjob 의 최대 장점은 **kubernetes 위에서 돌아가는 병렬 학습** 이다.



잠시 tfjob 의 yaml 파일을 살펴보자.

```yaml
apiVersion: kubeflow.org/v1beta1
kind: TFJob
metadata:
  generateName: tfjob
  namespace: kubeflow
spec:
  tfReplicaSpecs:
    PS:
      replicas: 1
      restartPolicy: OnFailure
      template:
        spec:
          containers:
          - name: tensorflow
            image: gcr.io/your-project/your-image
            command:
              - python
              - -m
              - trainer.task
              - --batch_size=32
              - --training_steps=1000
            env:
            - name: GOOGLE_APPLICATION_CREDENTIALS
              value: "/etc/secrets/user-gcp-sa.json"
            volumeMounts:
            - name: sa
              mountPath: "/etc/secrets"
              readOnly: true
          volumes:
          - name: sa
            secret:
              secretName: user-gcp-sa
    Worker:
      replicas: 1
      restartPolicy: OnFailure
      template:
        spec:
          containers:
          - name: tensorflow
            image: gcr.io/your-project/your-image
            command:
              - python
              - -m
              - trainer.task
              - --batch_size=32
              - --training_steps=1000
            env:
            - name: GOOGLE_APPLICATION_CREDENTIALS
              value: "/etc/secrets/user-gcp-sa.json"
            volumeMounts:
            - name: sa
              mountPath: "/etc/secrets"
              readOnly: true
          volumes:
          - name: sa
            secret:
              secretName: user-gcp-sa
    Master:
          replicas: 1
          restartPolicy: OnFailure
          template:
            spec:
              containers:
              - name: tensorflow
                image: gcr.io/your-project/your-image
                command:
                  - python
                  - -m
                  - trainer.task
                  - --batch_size=32
                  - --training_steps=1000
                env:
                - name: GOOGLE_APPLICATION_CREDENTIALS
                  value: "/etc/secrets/user-gcp-sa.json"
                volumeMounts:
                - name: sa
                  mountPath: "/etc/secrets"
                  readOnly: true
              volumes:
              - name: sa
                secret:
                  secretName: user-gcp-sa
```

병렬처리는 tensorflow를 통해 하게 된다. `tf.train.ClusterSpec` , `tf.train.Server` 로 cluster 를 구성하고, 서버를 키는 작업이 있다.

```python
 # Create a cluster from the parameter server and worker hosts.
  cluster = tf.train.ClusterSpec({"ps": ps_hosts, "worker": worker_hosts})

  # Create and start a server for the local task.
  server = tf.train.Server(cluster,
                           job_name=FLAGS.job_name,
                           task_index=FLAGS.task_index)
```

그 후, `tf.train.MonitoredTrainingSession` 에서 분산 학습을 하게 된다.

```python
 with tf.train.MonitoredTrainingSession(master=server.target,
                                           is_chief=(FLAGS.task_index == 0),
                                           checkpoint_dir="/tmp/train_logs",
                                           hooks=hooks) as mon_sess:
      while not mon_sess.should_stop():
        # Run a training step asynchronously.
        # See `tf.train.SyncReplicasOptimizer` for additional details on how to
        # perform *synchronous* training.
        # mon_sess.run handles AbortedError in case of preempted PS.
        mon_sess.run(train_op)
```

tensorflow 에서 지원하는 병렬 학습을 하기 위해서는, 많은 환경 설정이 필요한데, 이 환경 설정을 자동화 해주는 역활이 바로 kubeflow 의 역활이다.

그 자동화 된 application 의 코드를 짜는것을 우리가 해야할 일이다.

tensorflow 병렬처리에서 나온 4가지 processor 는 kubeflow tfjob 의 4가지 processor 와 유사하다

- chief: 일종의 master 역활이다. training 을 오케스트레이셔닝 한다.
- ps: parameter server 이다.distributed data store 를 제공한다.
- worker: 실제로 학습을 진행하는 worker 이다.
- evaluator: train 된 model 의 metric과 성능을 평가한다.



관련 자료

<https://github.com/tensorflow/examples/blob/master/community/en/docs/deploy/distributed.md>


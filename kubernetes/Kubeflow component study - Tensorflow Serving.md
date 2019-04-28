# Kubeflow component study - Tensorflow Serving

Kubeflow 에서 model deploy 를 하는 component 는 크게 2가지가 있다. 하나는 tf-serving deployment 이고, 하나는 tf-serving-service 이다.



일단 kubeflow 버전의 tf-serving service, deployment 를 알기 전에, tensorflow serving 에 대해 알아보자.

tensorflow serving 은 tensorflow model 을 서빙하기 위해 있는 기능이다.



Key concpets

![tf serving architecture diagram](https://www.tensorflow.org/tfx/serving/images/serving_architecture.svg)



- Servables

  - machine learned model 은 많은 알고리즘과 weight 들 embedding table 들을 가진다. 
  - 다른 component 들의 가장 중심이자 중심 abstarct class
  - 보통 tf-SavedModelBundle  를 가지거나, lookup table, embedding 등을 가진다.
  - Servable Version
    - servable 은 하나 이상의 version 을 가질 수 있다.
    - version 을 가질 수 있으므로, 하나의 서버가 여러가지 알고리즘, weight 등을 가질 수 있다.
    - 1개 이상의 version 이 동시에 존재할 수 있다.
    - client 는 version 을 명시해서 request 를 날릴 수 있다.

- models

  - model 을 가리킨다. 
  - 여러 모델을 독립적으로 둘 수 있고, 합성해서 하나의 servable 으로 둘 수도 있다.

- loaders

  - servable 객체들의 life cycle 을 관리한다.

- sources

  - servable 들을 file system에 저장한다.

  - loader 로 servable 객체를 준다.

  - 다수의 servable 이나 version 에서 공유되는 자원들의 state 를 관리할 수 있다.

  - Aspired Versions

    - Aspired Versions 는 load and ready 되어야 하는 version 들의 set 이다.

    - source 는 단일 servable stream 으로 이 servable versions 들과 communicate 한다.

    - source 가 manager 에게 새로운 aspired version 을 준다면, version 을 교체? 한다(supercedes 가 무슨뜻인지 모르겠다..

      >  When a Source gives a new list of aspired versions to the Manager, it supercedes the previous list for that servable stream. The Manager unloads any previously loaded versions that no longer appear in the list.

- Managers

  - Managers 는 servable 의 모든 life cycle 을 관리한다.

    

kubeflow 의 예제 코드를 많이 참조합니다.

`tf.estimator.export.ServingInputReceiver` 를 통해서 input 을 정의합니다.

rest api 를 만들었을때, body 에 넣어줄 input 이 된다.



```python
def cnn_serving_input_receiver_fn():
  inputs = {X_FEATURE: tf.placeholder(tf.float32, [None, 28, 28])}
  return tf.estimator.export.ServingInputReceiver(inputs, inputs)
```

tf.estimator.FinalExporter 에 serving_input_receiver_fn 에 해당 tf.estimator.export.ServingInputReceiver 를 리턴하는 함수를 넣어준다.

```python
export_final = tf.estimator.FinalExporter(
    args.tf_export_dir, serving_input_receiver_fn=cnn_serving_input_receiver_fn)
```



이 외에, tf.estimator 사용법은 나중에 살펴보자.

<https://github.com/kubeflow/examples/blob/master/mnist/model.py>



자, 이렇게 tensorflow 로 학습된 모델이 tensorflow serving 으로 servable model 이 만들어진다.

이 모델파일은 보통 file storage 에 저장하게 되는데, AWS 면 s3 에 저장하게된다.



이후에 bazel 같은 복잡한 작업은 kubeflow 가 담당하게 된다.

모델이 저장되어있는 s3 저장소의 정보를 넣어주고 이 모델을 가져와 kubeflow 가 deploy 하게 된다.
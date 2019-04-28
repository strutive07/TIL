# Kubeflow Components



보통 container 로 모든 component 들을 관리하고, 이 container 들은 kubernetes 에서 돌아가게 된다.

component list

- [Chainer Training](https://www.kubeflow.org/docs/components/chainer/)
- [Hyperparameter Tuning (Katib)](https://www.kubeflow.org/docs/components/hyperparameter/)
- [Istio Integration (for TF Serving)](https://www.kubeflow.org/docs/components/istio/)
- [Jupyter Notebooks](https://www.kubeflow.org/docs/components/jupyter/)
- [ModelDB](https://www.kubeflow.org/docs/components/modeldb/)
- [ksonnet](https://www.kubeflow.org/docs/components/ksonnet/)
- [MPI Training](https://www.kubeflow.org/docs/components/mpi/)
- [MXNet Training](https://www.kubeflow.org/docs/components/mxnet/)
- [Pipelines](https://www.kubeflow.org/docs/components/pipelines/)
- [PyTorch Training](https://www.kubeflow.org/docs/components/pytorch/)
- [Seldon Serving](https://www.kubeflow.org/docs/components/seldon/)
- [NVIDIA TensorRT Inference Server](https://www.kubeflow.org/docs/components/trtinferenceserver/)
- [TensorFlow Serving](https://www.kubeflow.org/docs/components/tfserving_new/)
- [TensorFlow Batch Predict](https://www.kubeflow.org/docs/components/tfbatchpredict/)
- [TensorFlow Training (TFJob)](https://www.kubeflow.org/docs/components/tftraining/)
- [PyTorch Serving](https://www.kubeflow.org/docs/components/pytorchserving/)



기본적인 몇가지 컴포넌트를 보자면, kubeflow 를 구성하고 deploy 관리 및 kubernetes cluster 생성 및 관리는 ksonnet 으로 한다.

![img](https://codelabs.developers.google.com/codelabs/kubeflow-introduction/img/79510abb19809cc2.png)



ksonnet 으로 kubernetes 를 구성하고 나면, 이제 tensorflow, pytorch 같은 머신러닝 프레임워크로 model 을 제작한다.

머신러닝 프레임워크들 또한 컴포넌트 형식으로 제공한다.

Data processing 의 경우, TFX 에 있는 TFDV, TFT 등을 컴포넌트로 제공한다.

로컬에서 작업할수도 있지만, kubeflow 는 jupyter notebook server 를 제공한다. 이 위에서 모델을 작성할 수 있다.

tensorflow 학습의 경우, local 머신에서 구축한 모델을 container 형식으로 올린다. 이때 올라가는 컴포넌트가 `TFJob ` 이다.

tfjob 은 kubernetes 위에서 tensorflow training 을 하기 위한 custom resource 이다.

하이퍼 파라미터 튜닝도 이젠 주먹구구 식으로 할순 없다. 하이퍼 파라미터 튜닝을 위한 컴포넌트로 katLib 을 지원한다.

모델을 만들 경우, 학습된 모델은 S3 등 storage 에 저장되게 된다. 저장된 모델을 서빙할때는 tfx 에 있는 tensorflow serving 이나 seldon 을 사용하게 된다.



API Gateway

![kubeflow-ambassador](https://d33wubrfki0l68.cloudfront.net/0056db8c6096c756d2ad3e5517bc4521337aea8c/532e3/images/blog/2018-06-01-dynamic-ingress-kubernetes/kubeflow-ambassador.png)



kubeflow 의 api gateway 역활을 하는것이 ambassador 이다. kubernetes 에서는 `ingress component` 라고도 부르는데, 다른 ingress component 로는 kong 이 있다.

url 기반으로 api 라우팅을 해준다.



이 외에도 많은 컴포넌트가 있지만, 우선 이정도만 이해하고 이 컴포넌트들 배치해주는 ksonnet 을 알아야 할꺼같다.(물론 kuberentes 는 기본으로 알아야할거같다..)


# cs231n lecture 7-5, Traning Neural Networks-2



![cs231n_2017_lecture7-86](A:/desktop/TIL/images/cs231n_2017_lecture7-86.jpg)

한국말로 '전이학습' 이라고 부르는 transfer learning 입니다.



![cs231n_2017_lecture7-87](A:/desktop/TIL/images/cs231n_2017_lecture7-87.jpg)

CNN 학습에는 많은 데이터가 필요하다! 라는 생각을 부순것이 바로 tansfer learning 입니다.

사실 완전히 부숴졌다고는 못하겠습니다. 이미 pre-train 된 모델이 있어야하는데 이 모델은 이미 많은 양의 데이터를 통해서 만들어진거니까요.

하지만 새로운 모델을 만들떄 base model 을 가지고 적은 양의 데이터를 추가로 사용한다는 transfer learning 은 충격적이기는 합니다.



![cs231n_2017_lecture7-90](A:/desktop/TIL/images/cs231n_2017_lecture7-90.jpg)



일단 base model 은 큰 데이터셋으로 학습을 하게 됩니다.

그 후 이 모델을 기반으로 다른 모델을 학습해볼겁니다.

예를들어, 1000 개의 class 를 가진 image net이 있다고 가정해봅시다.

이 데이터를 기반으로 모델을 학습한 후, 우리는 10개의 개의 종을 분류하는 모델을 다시 학습한다고 해봅시다.

우리가 가지고 있는 데이터가 적은 데이터일 경우, 맨 위의 FC layer 를 변경해서 re-initialize 한 후 학습하여 사용하면 된다고 합니다.



많은 데이터셋을 다시 학습시킬경우 조금 더 위의 FC layer 들을 fine tunning 하면 된다고 합니다.

그리고 transfer learning을 할때는 이미 모델이 잘 학습되어있으므로 learning rate 을 낮춰서 학습해야한다고 합니다.



![cs231n_2017_lecture7-93](A:/desktop/TIL/images/cs231n_2017_lecture7-93.jpg)



우리가 가지고 있는 데이터에따라 4가지 시나리오를 그릴 수 있습니다.

일단 데이터가 적은데 기존 모델과 다른 데이터셋이다..흠 이러면 문제가 있습니다. 다른 방법을 찾아야 합니다.

데이터가 적은데 기존 데이터셋과 비슷한경우 맨 위에 linear classifier 를 추가하면 된다고 합니다.



데이터가 많은데 원래 데이터셋과 다르다면? 기존보다 훨씬 많은 layer 를 fine-tunning 해야합니다.

데이터가 많은데 원래 데이터 셋과 비슷하다면 적은양의 layer 를 fine-tunning 하면 된다고 합니다.



![cs231n_2017_lecture7-96](A:/desktop/TIL/images/cs231n_2017_lecture7-96.jpg)



![cs231n_2017_lecture7-97](A:/desktop/TIL/images/cs231n_2017_lecture7-97.jpg)



요즘 computer vision 영역에서는 base model 부터 시작하는 경우는 적다고 합니다.

이미 많은 데이터로 학습이 잘 되어있는 pre-trained model 을 기반으로 transfer learning 하는 경우가 많다고 합니다.

![cs231n_2017_lecture7-98]()
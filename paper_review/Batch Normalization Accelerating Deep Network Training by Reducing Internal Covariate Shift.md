# [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://arxiv.org/pdf/1502.03167.pdf)
- ICML 2015
- Sergey Ioffe, Christian Szegedy

Google Inc.

## Keywords
-  Batch Normalization, mini-batch, internal covariate shift

## Contribution 
- gradient vanishing/exploding problem이 발생하지 않으면서 learning late을 크게 설정할수 있어 학습 속도가 빠르다.
- 각 layer 에서 input distribution 에 따라 training 되는 데이터가 달라서 학습이 불안정하다. 이 문제를 정규화를 통해 푼다.
- 자체적으로 regularization 효과도 있다.

## Proposed Architecture
 학습도중의 input distribution이 일정하지 않아 learning rate 를 높게 줘버리면 특정 skwed input distribution에 의해 데이터가 학습이 안될 수 있다.
각 Layer들의 input distribution이 consistent 하지 않는 현상을 internal covariate shift라고 한다.
이를 막기 위해서 나이브한 방법으론 Whitening 을 사용할 수있다.
Whitening은 그저 input distribution 을 평균 0 분산 1의 normal distribution 으로 normalize 시키는것이다.
하지만 이는 많은 문제가 있다.
크게 2가지를 설명해보자면,
1. 학습 parameter가 무시될 수 있다. 예를들어, 해당 layer 에서 w = u + b 라는 연산을 거치고 b를 학습한다고 가정해보자.
  이때 result를 normalize하기 위해 평균을 뺀다고 생각해보자
  ![image](https://user-images.githubusercontent.com/26921984/52725336-5d93be00-2ff4-11e9-972b-c18c7eed2ce6.png)
  이렇게되면 문제는 우리가 학습해야할 b 가 평균에의해 무시될 수 있게 된다.
> The combination of the update to b and subsequent change in normalization led to no change in the output of the layer nor, consequently, the loss.
2. 또한, NORMALIZE 과정에서 square root 의 계산량이 매우 많기 필요하기 때문에 좋지 않다.
  Convariance matrix 와 inverse squre root 를 계산하는데 
> Within this framework, whitening the layer inputs is expensive, as it requires computing the covariance matrix Cov[x] = Ex∈X [xx^T] − E[x]E[x]^T and its inverse square root, to produce the whitened activations Cov[x]−1/2 (x − E[x]), as well as the derivatives of these transforms for backpropagation.

이러한 문제들을 해결하면서 everywhere differntiable 하면서 backpropagation 에 적용할 수 있는 2가지 해결방법이 제시된다.

### 첫 번째 방법은 계산량 입장이다. 이는 위의 '계산량' 입장에서 시간이 오래 걸렸던 이유가 모든 feature 들이 correlated 되어있다고 가정했기 때문이다.
각 feature 들이 independent 하다고 가정한다면, 각각의 feature 들에 단순 scalar 연산을 통해 평균 0 분산 1의 normalize 를 할수 있게 된다. 이는 계산량도 적다!
>The first is that instead of whitening the features in layer inputs and outputs jointly, we will normalize each scalar feature independently, by making it have the mean of zero and the variance of 1. 
>![image](https://user-images.githubusercontent.com/26921984/52726239-28886b00-2ff6-11e9-90c1-469c0b9085c6.png)

물론 correlation을 무시하고 learning 하계 되면 각 feature의 중요한 관계가 training 되지 못할 수 있다.
이를 방지하기 위해 linear transform 하기 위해서 2가지 parameter 를 사용한다.![image](https://user-images.githubusercontent.com/26921984/52726547-bc5a3700-2ff6-11e9-8468-eb34ec5cbd9b.png) 이 2가지 parameter 는 scale 과 shift 를 담당하게된다.

![image](https://user-images.githubusercontent.com/26921984/52726552-bfedbe00-2ff6-11e9-8a55-454fa0287668.png)
각 파라미터는 다음 내용을 나타낸다 ![image](https://user-images.githubusercontent.com/26921984/52726597-d7c54200-2ff6-11e9-945f-089d9b12e499.png)![image](https://user-images.githubusercontent.com/26921984/52726603-da279c00-2ff6-11e9-84a5-29e7e8e97886.png) 

이 파라미터들은 neural network 를 train할때 weight 를 update 하는거처럼 같이 update 되는 model parameter 가 된다.


### 두 번째로, 전체 데이터에 대해 mean/variance를 계산하는 대신 현재 mini-batch에 대해서만 sample mean/variance를 구한 다음 inference를 할 때에만 real mean/variance를 예측한다.

각 mini-batch 는 각 activation의 mean 과 variance 추정할것이다. 이는 SGD training의 특성처럼 mini-batch를 통해서 추정하고 gradient backpropagation 를 진행할 수있다.
>Note that the use of minibatches is enabled by computation of per-dimension variances rather than joint covariances; in the joint case, regularization would be required since the mini-batch size is
>likely to be smaller than the number of activations being whitened, resulting in singular covariance matrices.
>위에껀 무슨말인지 이해가 안된다 ㅠㅠ 
>
>> 아마도 sample 을 사용하게되면 각 dimension의 variance를 따로따로 계산해도 된다를 mini-batch 에서도 사용할수 있다는 말인거같다. 이 논문에서 최대한 joint covariance 를 계산하는것을 꺼려한다. 계산량이 많으니까. 그래서 사용하는것이 1번 방법에서의 shift 와 scale 값을 각 러닝에서 input 을 통해 학습하는거였는데, 여기서 어떤 input 으로 학습하는가? 에 대한 대답으로 각 mini-batch 의 데이터들을 통해서 학습한다는것 같다. 1번과 2번이 같이 사용된다.

![image](https://user-images.githubusercontent.com/26921984/52727759-42777d00-2ff9-11e9-95ae-cb68cb7b9142.png)
1번 식을 mini-batch 버전으로 적용한것이다.

결국 r, b 값을 학습해야하기 때문에 이 값들은 back-propagation을 통해서 학습하게 된다.
![image](https://user-images.githubusercontent.com/26921984/52796944-1c64e200-30b8-11e9-9470-07cbddb470d1.png)

하지만 여기서 주의해야하는것이, activation들의 normalization은 mini-batch데이터를 기반으로 매우 효율적으로 학습 되었겠지만, inference 단계에서 mini-batch 때와 같은 규칙을 적용하게되면 mini-batch의 어느 부분이 닮았느냐? 라는 mini-batch의 랜덤하게 분포되는것에 좌지우지 될수 있다. 우리가 원하는것은, 결국 원본 input 에 영향을 받는거지, mini-batch 에 영향을 받고싶은것은 아니다.
따라서 inference 단계에서는 다른 방식을 사용해야 한다.
network 가 한번 학습이 되었으면, test 에는 deterministically 한 결과를 내야하므로 sample mean/variance 는 사용하지 않고 지금까지의sample mean/variance를 기반으로 unbiased mean/variance 를 예측하여 사용하게된다.
![image](https://user-images.githubusercontent.com/26921984/52800325-dfe8b480-30be-11e9-924f-445fbd582cb3.png) ![image](https://user-images.githubusercontent.com/26921984/52800232-a9ab3500-30be-11e9-86ba-95e4af8aa918.png)

결론적으로, interence 단계에서는 mean 과 variance 가 고정되고, normalization 작업은 각 activation을  linear transform 한것이 되게 된다.

전체적인 알고리즘은 다음과 같다
![image](https://user-images.githubusercontent.com/26921984/52727820-6470ff80-2ff9-11e9-9ff9-1f1d17702a52.png)

###  논문에서 주장하는 Batch Normalization의 장점은 다음과 같다.

- 기존 Deep Network에서는 learning rate를 너무 높게 잡을 경우 gradient explode 하게 된다.  이는 parameter들의 발산하기 때문인데, Batch Normalization을 사용할 경우 propagation 할 때 parameter들이 발산하지 않게 된다. 따라서 상대적으로 높은 learning rate 을 사용하여 빠르게 학습할 수 있다.
- Batch Normalization은 regularization 효과가 있다. 이는 기존에 사용하던 weight regularization term 등을 제외할 수 있게 하며, 나아가 Dropout을 제외할 수 있게 한다. Dropout 이 최근에 여러가지 이슈를 거치면서 local min에 빠지게 되면 학습이 안되게되는 오류들이 종종 발생하지만 성능이 좋고 대체제가 없어 사용했지만, Dropout 을 효과적으로 빼면서 regularization을 할 수 있으면 Dropout은 더이상 안 쓰고 Batch Normalization만 쓰지 않을까? (하지만 이건 regularization이라는 입장에서 아예 명확한 성능 차이를 보이기 때문에 아예 배제될것같지는 않다.)

###  추가적으로 더 주의해야하는것은, 일반적인 layer 에서 BN 이 사용되는것과, CNN 에서 BN 이 사용되는것이 다르다는것이다.
Convolution layer 의 activation function은 보통 Wx+b 형태로 weight 을 적용하는데, BN 의 Normalize 과정에서 학습하는 beta 값이 Wx+b 의 b 값의 역활가 동일하다. 따라서 activation의 b 를 삭제해야한다.
또한 Convolution의 성질을 유지해야하기 때문에 각 Channel 들에 독립적으로 Batch Normalization을 넣는다(r, b 값을 각 channel 마다 할당해 준다.) 

### BN 의 성능을 높이는 방법은 다음과 같다.
1. learning rate 를 높인다
2. dropout 을 제거한다
3. l2 regularization을 줄인다.
4. learning rate decay 를 가속한다.
5. local response normalization을 제거한다. BN 에는 필요하지 않다고 한다.
6. Shuffle training examples more thoroughly
7. Reduce the photometric distortions

대부분 BN을 적용하면서, regularization 문제를 같이 해결해주기떄문에, 이와 동일한 역할을 하는 dropout, l2 regularization 등을 제거하는쪽으로 가는것 같다.


## Dataset & Experience

첫 번째 실험 

조건
- MNIST dataset (LeCun et al., 1998a).
- with a 28x28 binary image as input, and 3 fully-connected hidden layers with 100 activations each.
- Each hidden layer computes y = g(Wu+b) with sigmoid.
- W initialized to small random Gaussian values
- The last hidden layer is followed by a fully-connected layer with 10 activations (one per class) and cross-entropy loss.

![image](https://user-images.githubusercontent.com/26921984/52801671-c09f5680-30c1-11e9-8706-aa4ecbf9c4ec.png)

위 사진은 BN 이 사용되었을때와 사용되지 않았을때의 accuracy 와 internal covariate shift 를 보여준 그래프이다.
BN 을 사용하면 당연히도 normalization 을 하였으므로 internal coveriate shift 는 효과적으로 줄어든다.
이와 더불어 accuracy 또한 빠르게 학습되는것을 알 수 있다.


두 번째 실험

- ImageNet classification

![image](https://user-images.githubusercontent.com/26921984/52802132-a619ad00-30c2-11e9-93dc-25cc34412eba.png)

모든 세팅을 동일하게 해두고, Inception network (Szegedy et al., 2014), trained on the ImageNet classification task (Russakovsky et al., 2014). 이 네트워크에 BN 을 적용한것과 적용하지 않은것, 많이 적용한것등을 비교한것이다.
BN 을 적용한것이 월등히 빠른 학습을 보이는것을 알 수 있고, 이 과정에서 accuracy 가 더 높아지는 경향도 볼 수 있다.


## Valuable Relative Works
- 
- 
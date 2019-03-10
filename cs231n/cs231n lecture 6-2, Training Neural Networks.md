# cs231n lecture 6-2, Training Neural Networks

![1552221569589](A:/desktop/TIL/images/2019-03-11-1552221569589.png)

![1552221513038](A:/desktop/TIL/images/2019-03-11-1552221513038.png)



```markdown
데이터 전처리 과정에서는 여러가지가 있지만
대부분은 정규화 작업이다.
zero-centered data 로 만들고, 데이터를 잘 학습할 수 있다록 정규화를 해준다
```



![1552221537831](A:/desktop/TIL/images/2019-03-11-1552221537831.png)



```markdown
또한 PCA 와 Whitening 이라는 방법도 있다.
```



![1552221579344](A:/desktop/TIL/images/2019-03-11-1552221579344.png)



![1552221605090](A:/desktop/TIL/images/2019-03-11-1552221605090.png)



```markdown
초기에 Neural Network에는 많은 W, b 등등 parameter 가 있다.
이 parameter 의 초기값을 어떻게 설정해야할까?
0으로 초기화하면 학습이 안되므로
일단 작은값으로 랜덤하게 넣어본다고 가정하자.
일단 돌아가기는 하는데 많은 문제가 있다.
```





![1552221595544](A:/desktop/TIL/images/2019-03-11-1552221595544.png)



```markdown
작은 값으로 init 할경우,
초기 layer 는 가우시안분포를 잘 따르지만
뒤로갈수록 gradient 가 작아져서 update 되지 못하는 문제가 발생함
```





![1552221617523](A:/desktop/TIL/images/2019-03-11-1552221617523.png)



```markdown
큰 값으로 init 하게 되는경우
W값이 너무 크게되어 오버슈팅이 되버린다. 따라서 -1 과 1에 모든 값이 들어가버린다.
```



![1552221628497](A:/desktop/TIL/images/2019-03-11-1552221628497.png)



```markdown
여기서 나온 해결법이 바로 Xavier initialization 이다.
위의 두 가지 방법은 입력 데이터 수가 커지면 분산도 커진다는 단점이 있다.
Xavier initialization 방법은 W vector 를 입력 데이터수의 제곱근 값으로 나누는 방법이다.
이 방법은 뉴런의 출력의 분산을 1로 정규화하는 효과를 가진다.
즉 input 의 개수가 많아지면 값이 작아지고, input의 개수가 적으면 weight가 커지게된다.

```



![1552221938295](A:/desktop/TIL/images/2019-03-11-1552221938295.png)



```markdown
문제는 Relu가 잘 적용이 안된다.
출력값들이 점점 0에 수렴해버리는 문제가 발생한다.
```



![1552221989500](A:/desktop/TIL/images/2019-03-11-1552221989500.png)



```markdown
2015년에 위 방식에서 입력사이즈에 2를 나눠 정규화하면 잘 돌아간다고 한다.
```


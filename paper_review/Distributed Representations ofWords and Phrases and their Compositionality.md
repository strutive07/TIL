# [Distributed Representations ofWords and Phrases and their Compositionality](http://papers.nips.cc/paper/5021-distributed-representations-of-words-andphrases)
- NIPS 2013
- Tomas Mikolov, Ilya Sutskever, Kai Chen, Greg S. Corrado, Jeff Dean

Google Inc

## Keywords
-  word Embedding, word2vec, distributed representations of words
## Contribution 
- 기존 NN 기반 학습과 유사하지만, 계산량을 줄이기위한 테크틱들이 엄청 효율적이여서 많이 쓰는 방식.
- Negative sampling, Subsampling of FrequentWords 등 많은 최적화 방법들을 고안해냄.

## Proposed Architecture
![image](https://user-images.githubusercontent.com/26921984/49359923-f10a6200-f71a-11e8-8814-281591079a44.png)
Skip-gram 방식으로 학습함.
![image](https://user-images.githubusercontent.com/26921984/49359950-0d0e0380-f71b-11e8-82a3-98ee985e3544.png)
이 식을 최대화 하는 쪽으로 학습함.
![image](https://user-images.githubusercontent.com/26921984/49359960-17300200-f71b-11e8-87e2-95ffa2bd3ebd.png)
p(wt+j |wt) 는 아래와 같이 softmax 로 나타낼 수 있음.

![image](https://user-images.githubusercontent.com/26921984/49360009-447cb000-f71b-11e8-810b-785c3b390ae1.png)

하지만 연산시간이 W 에 비례 하므로 너무 많은 시간이 소모된다.
이떄 W 와 W' 는 각각 input, output vector 이다. size는 N*V. (N: Vocab 수, V : 한 element 의 vector 크기)

두 가지 방식으로 시간을 최적화 시킨다.

첫 번째 시간 최적화는  softmax 단계에서의 방대한 계산량을 최적화 한다.

여기서 시간이 오래 걸리는 구간은, loss를 계산하기 위해 softmax 를 계산해서 normalization 하는 부분이다. 하나의 연산마다 전체 코퍼스에 대한 softmax를 계산하는곳에서 엄청난 계산량이 발생한다.

여기서 2가지 방식이 있다.
1 - 1. Hierarchical Softmax
![image](https://user-images.githubusercontent.com/26921984/49361308-0c776c00-f71f-11e8-8d6e-62b3e16ca588.png)

 - binary tree representation of the output layer with the W words as its leaves
 - explicitly represents the relative probabilities of its child nodes
 - L(w)는 w라는 leaf에 도달하기 까지의 path의 길이를 의미한다.
 - n(w, i) 는 root에서부터 w leaf에 도달하는 path에서 만나는 i번째 노드를 의미한다.
 - n(w, 1) 는 root, n(w, L(w)) = w
 - ch(node) node 에 고정된 자식
 - [[x]] 는 true : 1, false : -1 반환
 - W’ matrix를 사용하지 않는다. 대신, V-1개의 internal node가 각각 길이 N짜리 weight vector를 가지게 된다. 이것들을 v'_t 이다.
 - ![image](https://user-images.githubusercontent.com/26921984/49361797-32e9d700-f720-11e8-8590-300c99f3a28b.png) 는 sigmoid function 1/(1+exp(-x)) 이다.

최종적으로 아래 식을 계산하는데 걸리는 시간은 L(wO) 에 비례하고, 이 값은 logW 보다 작다.

![image](https://user-images.githubusercontent.com/26921984/49361466-78f26b00-f71f-11e8-813c-65d0f44ade48.png)

Full Binary Tree를 사용해야 하기떄문에, 보통은 Binary Huffman Tree 를 사용한다.

tree 를 이동할떄는 다음과같은 연산을 한다.
![image](https://user-images.githubusercontent.com/26921984/49361797-32e9d700-f720-11e8-8590-300c99f3a28b.png) 를 A(x)라 한다면, 
1. left child 로 이동할때 : A(x)
2. right child 로 이동할떄 : A(-x) = 1 - A(x)
  최종적으로, left chlid 와 right child의 합이 1이 되므로, softmax function에서 모든 softmax 를 구하고 1 로 normalization 하는 과정이 없어진다.
  left node에서 최종적으로 원하는 softmax 값이 나오고 이 단계에서 loss funciton을 계산하므로 시간복잡도는 O(NV) 에서 O(N logV)로 줄어들게 된다.

1 - 2. Negative Sampling
![image](https://user-images.githubusercontent.com/26921984/49362799-1bf8b400-f723-11e8-88a2-ad7658733afc.png)

전체 softmax를 하는게 아니라, positive word 와 임의로 뽑은 일부 negative word만 softmax를 돌린다.
k개의 negative word를 noise distribution 기반으로 뽑는다.
noise distribution 은 free parameter로 실험적으로 구한 가장 좋은 distribution 은
unigram distribution U(w) raised to the 3/4rd power (i.e., U(w)3/4/Z) 이다.

> ## Questions
> * Negative Sampling 에서 Pos / Neg 를 가르는 방법이 정확히 뭔가요?

![image](https://user-images.githubusercontent.com/26921984/49707915-b51e5200-fc70-11e8-9835-fad622734cb4.png)

좌측항이 positive sample, 우측 항이 negative samples 입니다.
이 수식에서는, positive sample은 target word 1개를 의미하고, negative sample 은 랜덤하게 잡은 k 개의 word들 을 대상으로 음의 내적을 합니다.

이렇게 되면 positive sample 1개에 대해서 Vw_I 로 당겨지는 효과를, 다른 negative smaples 들은 멀어지는 효과를 가져옵니다.



2. Subsampling of Frequent Words
  ![image](https://user-images.githubusercontent.com/26921984/49362634-9b39b800-f722-11e8-967a-37bbb81412dc.png)

imbalance between the rare and frequent words 를 막기 위해, Frequency 기반으로 단어를 subsampling 한다.
t 는 일종의 threshold 값으로, frequency가 t가 넘어가야 subsampling 한다.

P(w_i)가 만약 40% 라면? -> 100번중 40번은 학습에서 제외된다는 의미가 된다.
![image](https://user-images.githubusercontent.com/26921984/49362816-2adf6680-f723-11e8-95d5-332d127bc142.png)

![image](https://user-images.githubusercontent.com/26921984/49363970-6def0900-f726-11e8-9cc1-d776422dc37a.png)



## Dataset

![image](https://user-images.githubusercontent.com/26921984/49364094-bc040c80-f726-11e8-811e-76cf23af91f2.png)

![image](https://user-images.githubusercontent.com/26921984/49364088-b5759500-f726-11e8-92d2-da5ed696d05f.png)

![image](https://user-images.githubusercontent.com/26921984/49364240-29b03880-f727-11e8-9132-afd5c7c33685.png)

analogical reasoning task 를 사용한다.





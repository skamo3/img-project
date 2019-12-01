# skamo3 README

## 모델 기본 구성
 - Input shape == 96,96,1
 - Conv2D - BatchNormalization - ReLU (3단계 3회 반복) - maxpooling - Dropout - GlovalAveragePooling - 'sotfmax' - classification(7)
 - Layer 진행 8x3 - 32x3 - 64x3 - 128x3 - 256 - 128 - 7
 - optimizer = Adam
 - loss Function = sparse_categorical_crossentropy
 
 
## 1차 TEST
 - epochs = 60
 - loss : 0.3132
 - train accuracy : 0.8855
 - test accuracy : 0.6439  
 

 ### 문제
 - epochs 에 변화를 주어도 train accuracy는 올라가지만 test accuracy는 0.65 근처에서 더 이상 올라가지 않는 현상 발견
 - 오히려 일정 수준부터는 떨어짐
 ### 원인 분석  
 - Dataset의 문제점 : 사람의 표정이란 것은 실제 사람이 보기에도 구분이 불가능 할 때가 있음   
    1. 학습 방법의 변화 - 전체를 한번에 분류하는 방법이 아닌 angry-disgust 로 묶어서 한번 비교 후 +sad 로 묶어 또 한번 비교하는 식으로 각 표정별로 하나하나 비교해보기
    2. Model의 depth는 줄이고 filter의 갯수는 늘려서 큰 feature들을 가지고 분류해 보기
    3. 다른 Dataset을 이용해서 Model이 잘 맞는지 확인해 보기

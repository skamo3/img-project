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

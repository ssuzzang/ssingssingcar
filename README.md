# ssingssingcar

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/50cb4134-4666-49df-b62c-def86bd63082/Untitled.png)

Date : 2022.7.11~2022.8.5

Tags : `RaspberryPi` `OpenCV` `Tensorflow` `Keras` `Python`

Link : 

[https://github.com/ssuzzang/ssingssingcar](https://github.com/ssuzzang/ssingssingcar)

발표영상 : 

[Portfolio_5](https://youtu.be/etcQFuLz-nA)

시연영상 : 

[Portfolio_5_시연영상_2](https://www.youtube.com/watch?v=qjYvi7tAHwM)

---

# **프로젝트 내용**

---

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/dcd13b51-c994-4c0f-b1a6-d1420c145d43/Untitled.png)

---

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fd1d3c00-2365-4d89-9dc6-77b1b0fd4d56/Untitled.png)

- 주제는 라즈베리파이를 이용한 자율주행 RC카 입니다.

---

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a1a54ef6-ca05-4d0a-9c6e-b94145001c43/Untitled.png)

- 선정 배경  : 자율주행이 사고방지 및 운전자의 편의성에 얼마나 영향을 주는지 알아내기 위해
- 기대 효과 :
    
     1.   사전에 위험을 인지해 사고 예방
    
    1. 운전자를 서포트하여 주행을 도와주어 편리성을 향상 시킨다.

---

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/391feb39-8357-4879-9c6e-6ecdd1f20355/Untitled.png)

- 라즈베리파이와 전용 RC카 모듈키트
- Pi 카메라 와 RC카를 원격으로 제어할 컴퓨터
- 개발 환경에서 필요한 라이브러리마다 호환 여부를 판단하여 알맞은 버전 설치

---

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/30a6a67d-2a0b-4021-81dd-b5684b41cd79/Untitled.png)

- 2인 팀으로 구성되어 있으며 각자 역할을 두지 않고 자유롭게 소통하며 단계를 나누어 필요한 기술 스택을 쌓으며 협업하는 방식으로 진행하였습니다.

---

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0205fca0-0bac-477f-a4e5-2a4f2a678e4c/Untitled.png)

수행 절차 및 방법

1. 프로젝트 진행 방향에 대한 기획서를 작성하면서 필요한 기술 스택 여부 및 필요한 장비를 파악하여 공유 및 장비 구매를 진행
2. 구동에 필요한 소프트웨어 및 하드웨어 조립 진행
3. OpenCV를 이용한 차선인식을 RC카로 구동 테스트를 완료 후 차선 검출 테스트를 진행
4. cnn을 이용한 딥러닝 트레이닝을 진행하던 도중 라이브러리 충돌로 인해 환경을 재구축하여 차선인식 주행 까지 진행

---

![스크린샷 2022-09-03 오후 7.23.00.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ed98adfe-783e-4c5e-95cd-330cf411ec3d/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-09-03_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_7.23.00.png)

1. 라즈베리파이에 라즈비안OS를 설치하고 기본 환경 세팅을 합니다.
2. 프로젝트에 필요한 환경 구축을 위해 파이썬, opencv등 라이브러리를 설치합니다.
3. 하드웨어 조립한 뒤 구동 테스트를 합니다.
4. RC카를 구동하기 위해 adafruit , gpio 를 세팅합니다.
5. 라벨링한 데이터를 딥러닝 학습 후 차선 인식 주행을 합니다.

---

![스크린샷 2022-09-03 오후 7.38.02.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f5375924-8216-47e8-9141-adfd2d381c1f/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-09-03_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_7.38.02.png)

- Raspberry Pi
    - Raspbian os 64bit 설치하였습니다.
    - VNC를 이용하여 원격 환경을 조성하였습니다.
    - 파이썬은 3.9.2버전을 설치하였습니다.
    - opencv는 4.6.0버전을 설치하였습니다.
    - Tensorflow,keras 2.8.0버전을 설치하였습니다.
    - 각 라이브러리마다 호환 여부가 틀리기 때문에 환경을 재구축 하는 등 시행착오가 많았습니다.
- 하드웨어 조립
    - GPIO 라이브러리로 모터 속도를 제어하였습니다.
    - adafruit 라이브러리로 조향용 서보모터를 제어하였습니다.

---

![스크린샷 2022-09-04 오전 10.40.54.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/be3d0147-fd6d-44d5-8657-906084664824/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-09-04_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_10.40.54.png)

- 카메라를 통해 opencv 라이브러리를 이용하여 기초적인 차선 인식 주행을 하였습니다.
- Lane detection Algorithms를 이용하였습니다.
- RGB인 이미지가 사용하는 색 공간은 HSV 색 공간으로 변환하고 변환된 이미지를 Canny edge detectioin으로 이미지의 가장자리를 감지합니다.
- 라인 세그먼트를 1또는 2개의 차선 라인으로 결합해 라인 기울기에 따라 좌우 차선을 감지합니다.
- 최선 좌표를 기반해 조향 각도를 찾은 뒤 감지한 차선을 따라 주행을 하며 데이터 가공을 위한 영상 데이터를 수집합니다.

---

- 프로젝트 수행 결과

![스크린샷 2022-09-04 오전 10.54.35.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/964b0508-0017-4a1a-9a73-b0fa2698b175/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-09-04_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_10.54.35.png)

![스크린샷 2022-09-04 오전 10.54.46.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1bc2aa17-0940-45f6-8b38-da2ff2e3943e/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-09-04_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_10.54.46.png)

- 딥러닝 차선 인식 주행을 하기 위해 PNG이미지와 이미지에 기록된 차선 각도를 이용하여 데이터 라벨링을 하였습니다.
- 이미지를 사용하여 정보를 정확히 파악하고 자동차의 조향 각도를 예측하기 위해 Nvidia모델을 사용하였습니다.
- Nvidia Model
    - 카메라로 입력 받아 차량의 조향 각도를 예측하여 출력하는 회귀 모델입니다.
    - Nvidia모델에 사용된 CNN 레이어는 총 30개 층으로 구성되며 먼저 선과 가장자리를 추출한 뒤 마지막 신경 레이어를 통과하여 조향각도를 예측합니다.
    - 예측 각도는 주어진 이미지에서 원하는 조향 각도와 비교되고 오류는 역전파를 통해 CNN훈련 프로세스로 피드백 됩니다.

---

- 시연 영상 1
    
    [Portfolio_5_시연영상_1](https://youtube.com/shorts/YQ5VaTC-17k)
    
- 시연 영상 2

    [https://youtu.be/qjYvi7tAHwM](https://youtu.be/qjYvi7tAHwM)

---

- 느낀점
    - 처음 목표는 자율 주행과 객체 탐지를 접목하여 구동하는 RC카를 만드는 것이었습니다.
    - Raspberry Pi에 개발 환경을 구축하는 게 생각보다 힘들었고 거기에 많은 시간을 소비해서 목표한 바를 이루지 못해 아쉽습니다.
    - 처음부터 시간을 잘 분배했다면 완성도가 더 높았을 거 같습니다.
    - 이번 프로젝트를 통해 자율 주행에 더 흥미를 느끼게 되었고 미완성된 프로젝트를 마무리 하고 싶습니다.

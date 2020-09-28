# ML pipeline with Tibero & WAS

## 구성
* WAS : ML 결과 보여줄 WAS 배포
* Output : pipeline에서 사용 혹은 생성할 data를 저장하는 PV의 hostPath 저장소
* 00-Volume : pipeline에서 data 전달할 PV, WAS 이미지 소스에 ML result image 저장할 PV에 관한 k8s manifests
* 01-TiberoAgent : Tibero JDBC를 이용하여 필요한 데이터 추출하는 도커 이미지 형성
* 02-1-Trans : 추출 데이터 1을 가공하는 도커 이미지 형성
* 02-2-Trans : 추출 데이터 2를 가공하는 도커 이미지 형성
* 03-ML : 추출 데이터 가공하는 도커 이미지 형성
* 04-Visualize : 학습 데이터를 시각화하기 위해 그래프 이미지 파일을 저장하는 도커 이미지 형성
* build_images.sh : 도커 이미지 빌드 및 푸시 명령 쉘 스크립트 파일
* pipeline.py : pipeline 생성 manifest 컴파일
* pipeline.py.tar.gz : pipeline 형성 파일의 컴파일 결과물


## 순서
### 1. 웹 페이지 배포 (WAS 폴더 참고)

### 2. Tibero 연결
* $ tbdown clean
* $ tbboot

### 3. 필요한 Docker Images 빌드 및 푸시
* build_images.sh 스크립트에서 도커 이미지들의 적당한 version을 맞춤
* $ ./build_images.sh

### 4. k8s에 PV 생성 및 확인 (로컬저장소/Output 및 /WAS/static/images 와 hostPath로 연결)
* $ kubectl -n kubeflow apply -f pv-ml.yaml (/Output 와 연결)
* $ kubectl -n kubeflow apply -f pv-result.yaml (/WAS/static/images 와 연결)
* $ kubectl -n kubeflow get pv (pv 이름)

### 5. pipeline 생성 manifest 컴파일
* pipeline.py 스크립트에서 파이프 라인의 적당한 version을 맞춤
* $ python pipeline.py

### 6. flow job 실행 (Argor, Kubeflow, ..)

### 7. 웹페이지 확인
* {IP주소}:{8080}

### (8. PVC 삭제)
* pvc1 삭제 명령: $ kubectl -n kubeflow delete pvc pvc-ojt-ml
* pvc2 삭제 명령: $ kubectl -n kubeflow delete pvc pvc-ojt-result
* pvc1 삭제 보호설정 해지 명령: $ kubectl -n kubeflow patch pvc pvc-ojt-ml -p '{"metadata":{"finalizers":null}}'
* pvc2 삭제 보호설정 해지 명령: $ kubectl -n kubeflow patch pvc pvc-ojt-result -p '{"metadata":{"finalizers":null}}'
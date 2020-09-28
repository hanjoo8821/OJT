# ML 결과 Graph Image 보여주는 웹페이지

## 구성
* static : css파일과 이미지 소스 저장하는 폴더
* templates : html파일 저장 폴더
* app.py : 서버 빌드 파일
* requirements.txt : 도커 이미지 형성 시 다운로드 받아야 할 library 등 리스트
* Dockerfile : 소스 파일 복사 및 서버 빌드 수행 이미지 형성 파일
* build_image.sh : 도커 이미지 빌드 및 푸시 명령 쉘 스크립트 파일
* pv.yaml : ./static/images 와 연결하는 k8s Persistent Volume 형성 manifest 파일
* pvc.yaml : pv와 바인딩하는  k8s Persistent Volume Claim 형성 manifest 파일
* was-flask.yaml : 웹페이지 배포 k8s manifest 파일

## 순서
### 1. Docker Image 빌드 및 푸시
* build_image.sh 스크립트에서 도커 이미지의 적당한 version을 맞춤
* $ ./build_image.sh

### 2. k8s에 PV 생성 및 확인 (로컬저장소/static/images 와 hostPath로 연결)
* $ kubectl -n kubeflow apply -f pv.yaml
* $ kubectl -n kubeflow get pv (pv 이름)

### 3. k8s에 PVC 생성 및 확인 (PV와 바인딩: StarageClassName = ojt-tibero-was)
* $ kubectl -n kubeflow apply -f pvc.yaml
* $ kubectl -n kubeflow get pvc (pvc 이름)

### 4. k8s에 WAS Deployment 및 Service 등록 (2개의 Replica PODs. PVC와 연결한 Volume을 POD container의 /WAS/static/images에 마운트)
* $ kubectl -n kubeflow apply -f was-flask.yaml

### 5. 웹페이지 생성 확인 
* $ kubectl -n kubeflow get deployment
* $ kubectl -n kubeflow get svc
* $ kubectl -n kubeflow get pod

### 6. 웹브라우저에서 Service에서 확인한 IP와 port 번호(8080)으로 웹페이지 접속
* {IP주소}:{8080}

### (7. PVC 삭제)
* pv(pvc) 삭제 명령: $ kubectl -n delete pv(pvc) pv-ojt-was(pvc-ojt-was)
* pv(pvc) 삭제 보호설정 해지 명령: $ kubectl -n kubeflow patch pv(pvc) pv-ojt-was(pvc-ojt-was) -p '{"metadata":{"finalizers":null}}'
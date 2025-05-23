    
    이 bootcamp project는 ChatGPT의 도움을 받아 강의와 메타데이터에 대한 모델, admin page, 간단한 강의 검색 시스템을 구현한 결과다.
    
    
    박예강 프로젝트 공부 내용:
    
    SQL은 데이터베이스(딕셔너리처럼 동작하는 테이블)를 조작하기 위한 언어이다. SQL 문법을 통해 테이블을 생성하고, 원하는 컬럼이나 행을 추출하며, 서로 관계가 있는 컬럼들을 기반으로 테이블 간 연결도 가능하다.

    반면, DBMS는 이러한 SQL을 실행할 수 있는 환경을 제공하는 시스템이다. SQL은 우리가 데이터베이스에 내리는 명령어이며, 그 명령어를 실제로 수행하는 것이 DBMS의 역할이다. (참고로 우리는 Django를 사용하기 때문에, SQL을 직접 작성하기보다는 Python 문법으로 데이터를 조작하지만, 결국 Django 내부에서는 SQL로 변환되어 DBMS가 실행하게 된다.)


    Django는 기본적으로 SQLite를 내장 DBMS로 제공한다. 그러나 SQLite는 단일 사용자 환경이나 소규모 데이터를 다룰 때 적합하며, 대용량의 비디오와 그에 대한 메타데이터를 다뤄야 하는 본 프로젝트에는 적합하지 않다. 따라서 Django settings.py에서 DBMS를 PostgreSQL로 변경할 필요가 있다.

    또한, AWS에서 제공하는 두 가지 서비스인 S3와 EC2는 각각 다음과 같은 역할을 맡게 될 것이다.
    S3는 원격 저장소(하드디스크)로서 대용량의 영상 파일을 저장하고, EC2는 Django 서버가 실제로 실행될 원격 컴퓨터(클라우드 인스턴스) 역할을 한다. 개발 과정에서는 로컬 노트북을 사용할 수 있지만, 배포 단계에서는 안정적이고 확장 가능한 클라우드 서버 환경이 필요하므로, AWS S3와 EC2를 통해 스토리지와 서버를 각각 운영할 예정이다.


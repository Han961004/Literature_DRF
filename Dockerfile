# Python 3.11 이미지 사용
FROM python:3.11

# 작업 디렉토리 설정
WORKDIR /app

# Python 의존성 파일 복사 및 설치 (캐싱 활용)
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY . .

# 환경 변수 설정
ENV DJANGO_SETTINGS_MODULE=literature.settings

# 명령어 실행 (개발 환경)
CMD ["python", "literature/manage.py", "runserver", "0.0.0.0:8000"]

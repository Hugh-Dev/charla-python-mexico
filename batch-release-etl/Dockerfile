FROM python:3.12

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /Users/psf/Projects/pylab/charla-python-mexico/batch-release-etl/

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD ["python", "-u", "scripts/main.py"]
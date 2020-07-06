FROM python:3.8.3

ADD init.sh /init.sh

WORKDIR /workspace

COPY requirements.txt ./

COPY settings.ini ./

RUN apt-get install -y tzdata

ENV PYTHONUNBUFFERED=1

ENV TZ=America/Sao_Paulo

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install sqlite3 libsqlite3-dev -ys

RUN chmod +x /init.sh && \
    pip install --no-cache-dir -r requirements.txt && \
    python -m nltk.downloader stopwords && \
    python -m nltk.downloader punkt && \
    python -m nltk.downloader rslp && \
    python -m spacy download en && \
    python -m spacy download pt

EXPOSE 8787

ENTRYPOINT ["/init.sh"]

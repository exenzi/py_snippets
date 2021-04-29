FROM python:alpine

WORKDIR /app

# Вывод в терминал без буферизации:
ENV PYTHONUNBUFFERED=1
ENV WORKON_HOME=/app/.venvs
VOLUME [ "/app/.venvs" ]

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install pipenv

RUN apk --no-cache add \
    # Pillow deps
    build-base \
    freetype-dev \
    fribidi-dev \
    harfbuzz-dev \
    jpeg-dev \
    lcms2-dev \
    openjpeg-dev \
    tcl-dev \
    tiff-dev \
    tk-dev \
    zlib-dev \
    # psycorg2 deps
    postgresql-dev

COPY Pipfile.lock .

COPY Pipfile .

RUN pipenv install

COPY . /app

EXPOSE 8000

CMD ["pipenv", "run", "dev"]
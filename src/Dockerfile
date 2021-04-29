FROM python:alpine

WORKDIR /app

# Вывод в терминал без буферизации:
ENV PYTHONUNBUFFERED=1

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

RUN pipenv install --system --deploy --ignore-pipfile

COPY . .

EXPOSE 8000
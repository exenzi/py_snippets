FROM python:alpine

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

WORKDIR /app

COPY Pipfile .

COPY Pipfile.lock .

RUN pipenv install

COPY . /app

EXPOSE 8000

CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1
WORKDIR /app

RUN apk update \
  # psycopg2 dependencies
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  # Pillow dependencies
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
  # CFFI dependencies
  && apk add libffi-dev py-cffi

# Requirements are installed here to ensure they will be cached.
COPY pyproject.toml ./
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry install

COPY ./docker/entrypoint /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint

ENTRYPOINT ["/entrypoint"]

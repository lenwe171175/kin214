FROM python:3.10-alpine
WORKDIR /kin214

COPY requirements.txt .
RUN apk add --no-cache gcc libressl-dev musl-dev libffi-dev build-base git curl libspatialite gdal mariadb-dev libpq-dev tk geos binutils proj-dev
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["sh", "entrypoint.sh"]
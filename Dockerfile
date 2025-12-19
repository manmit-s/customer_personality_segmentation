# ---------- BUILDER ----------
FROM python:3.10-slim AS builder
WORKDIR /app

COPY requirements.txt .

# install ONLY wheels, no source builds
RUN pip install --no-cache-dir --only-binary=:all: \
    --prefix=/install \
    -r requirements.txt


# ---------- RUNTIME ----------
FROM python:3.10-slim
WORKDIR /app

COPY --from=builder /install /usr/local
COPY . .

EXPOSE 8000

CMD ["uvicorn", "scripts.app:app", "--host", "0.0.0.0", "--port", "8000"]

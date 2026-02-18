# Stage 1: Build Python environment
FROM python:3.9-slim as python-build
RUN groupadd -r autodevhub && useradd -r -g autodevhub autodevhub
USER autodevhub
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Stage 2: Build TypeScript environment
FROM node:16-alpine as ts-build
RUN groupadd -r autodevhub && useradd -r -g autodevhub autodevhub
USER autodevhub
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

# Stage 3: Build Terraform environment
FROM hashicorp/terraform:1.3 as terraform-build
RUN groupadd -r autodevhub && useradd -r -g autodevhub autodevhub
USER autodevhub
WORKDIR /app
COPY terraform .

# Stage 4: Final image
FROM python:3.9-slim
RUN groupadd -r autodevhub && useradd -r -g autodevhub autodevhub
USER autodevhub
WORKDIR /app
COPY --from=python-build /app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY --from=python-build /app/. .
COPY --from=ts-build /app/package*.json .
COPY --from=ts-build /app/node_modules .
COPY --from=terraform-build /app/terraform .
RUN npm install
HEALTHCHECK --interval=10s --timeout=5s --retries=3 \
  CMD curl --fail http://localhost:8000/ || exit 1
CMD ["python", "app.py"]

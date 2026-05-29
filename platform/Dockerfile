# 水产病原噬菌体安全筛查/设计平台 — 容器化 (NAR Database 要求免登录全功能公开部署)
FROM python:3.13-slim

# uv (与项目其余部分一致的依赖管理)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app
COPY pyproject.toml uv.lock* ./
RUN uv sync --no-dev --frozen || uv sync --no-dev

COPY . .

EXPOSE 8000
# 免登录全功能服务
CMD ["uv", "run", "uvicorn", "aquaphage_platform.main:app", "--host", "0.0.0.0", "--port", "8000"]

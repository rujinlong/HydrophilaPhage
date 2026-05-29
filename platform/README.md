# AquaPhage Safety & Design Platform (线②)

水产病原噬菌体**治疗安全筛查 + 杀菌酶资源 + safe-phage 设计**在线平台。
PI 预置的 FastAPI 后端骨架，**学生 B 接手填业务逻辑**（缓解 NAR 致命路径）。

> 母战略 DEC-D010 线② · 详见 `../analyses/data/program-docs/student-brief-B-safety-platform.md` + `line2-db-schema.md`
> 定位：最强 novelty（host 切分 + 治疗安全评分 + safe-phage 设计层），区别于 PhageScope/Sphae/IMG-VR/PhageDive。

## ⚠ NAR Database 硬要求
- **免登录 / 免注册 / 全功能**，投稿时即须可评审（**不要加鉴权中间件**）。
- deadline：7/1 pre-submission inquiry → 8/15 manuscript（见 `sprint-NAR-review-line2.md`）。
- 过不去时降级 *Database*(Oxford) / *Scientific Data*。

## 架构
- 后端：FastAPI + SQLAlchemy 2.0，SQLite(alpha) → PostgreSQL（设 `DATABASE_URL`）
- 前端：streamlit/gradio(alpha，压低工程量) → React(后续) ← **待建**
- 容器：`Dockerfile`
- 数据：来自共享底座 `analyses/406-master_table` 的 `master_annotation.sqlite`（ETL 进本库）

## 结构
```
platform/
├── pyproject.toml          # uv 管理依赖
├── Dockerfile
└── src/aquaphage_platform/
    ├── models.py           # 5 表 ORM (phages/safety/enzymes/hosts/designs)
    ├── db.py               # engine / session / init_db
    └── main.py             # FastAPI app + 6 endpoints (stub)
```

## 运行
```bash
cd platform
uv sync
uv run uvicorn aquaphage_platform.main:app --reload
# 文档: http://127.0.0.1:8000/docs
```

## 学生 B 接手清单
1. 6 个 endpoint 的 `TODO[学生B]` 业务逻辑（`main.py`）
2. ETL：从 `406-master_table` 的 master 表导入数据（`db.init_db()` 之外的装载脚本）
3. 前端：streamlit/gradio alpha（浏览 + 安全报告 + 酶查询，免登录）
4. ⭐ safe-phage 设计层 POC（`POST /api/design`，溶原模块切除靶点）
5. 公开部署 + 压测（免登录全功能 URL，对标 TCMSP 持续可访问）

## API（详见 `line2-db-schema.md §2`）
| Method | Path | 用途 |
|---|---|---|
| GET | `/api/phages` | 检索/筛选 |
| GET | `/api/phage/{id}` | 治疗适配卡片 |
| GET | `/api/safety/{id}` | 安全筛查报告 |
| GET | `/api/enzymes` | 酶查询 |
| POST | `/api/design` | ⭐ safe-phage 设计层 |
| GET | `/api/download` | 批量下载（免登录） |

"""FastAPI app — 水产病原噬菌体安全筛查/设计平台 (line②).

PI 预置骨架。**学生 B 只需填充每个 endpoint 的业务逻辑**（见 ``TODO[学生B]``）。

- Endpoints 源: ``program-docs/line2-db-schema.md §2``
- novelty: host 切分 + 治疗安全评分 + safe-phage 设计层
- ⚠ NAR Database 硬要求: **免登录 / 免注册 / 全功能 / 投稿时可评审**。
  不要加任何鉴权中间件。

本地运行:
    uv run uvicorn aquaphage_platform.main:app --reload
"""

from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from .db import get_db, init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()  # 建表（数据 ETL 由学生 B 的脚本完成）
    yield


app = FastAPI(
    title="AquaPhage Safety & Design Platform",
    version="0.0.1-alpha",
    description=(
        "水产病原噬菌体治疗安全筛查 + 杀菌酶资源 + safe-phage 设计平台。"
        "免登录全功能 (NAR Database)。"
    ),
    lifespan=lifespan,
)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/api/phages")
def list_phages(
    host: str | None = None,
    lifestyle: str | None = None,
    safe: bool | None = None,
    db: Session = Depends(get_db),
):
    """检索/筛选 phage (e.g. ?host=Aeromonas&lifestyle=virulent&safe=true).

    TODO[学生B]: query Phage (+join Safety)，按 host_genus / lifestyle /
    safety_grade=='safe' 过滤，分页返回。
    """
    raise HTTPException(status_code=501, detail="TODO[学生B]: implement phage filter query")


@app.get("/api/phage/{phage_id}")
def get_phage_card(phage_id: str, db: Session = Depends(get_db)):
    """治疗适配性卡片: lifestyle + 宿主谱 + safety + enzymes.

    TODO[学生B]: 聚合 Phage + Host + Safety + Enzyme 返回一张卡片。
    """
    raise HTTPException(status_code=501, detail="TODO[学生B]: implement therapy-fitness card")


@app.get("/api/safety/{phage_id}")
def get_safety_report(phage_id: str, db: Session = Depends(get_db)):
    """安全筛查报告: VFDB / CARD / 溶原 + grade.

    TODO[学生B]: 返回 Safety 行 + 人类可读解释 (gating step for therapy)。
    """
    raise HTTPException(status_code=501, detail="TODO[学生B]: implement safety report")


@app.get("/api/enzymes")
def list_enzymes(
    type: str | None = None,
    host: str | None = None,
    db: Session = Depends(get_db),
):
    """酶查询 (e.g. ?type=depolymerase&host=Aeromonas).

    TODO[学生B]: query Enzyme (+join Phage for host)，按 type/host 过滤。
    """
    raise HTTPException(status_code=501, detail="TODO[学生B]: implement enzyme query")


@app.post("/api/design")
def design_safe_phage(phage_id: str, db: Session = Depends(get_db)):
    """⭐ safe-phage 设计层: 输入 phage -> 溶原模块切除靶点 + 改造设计.

    这是区别于纯描述性 DB 的关键 novelty。
    TODO[学生B]: ① 定位 integrase/repressor/att 边界 + 毒力 cassette
                 ② 标记可切除模块 ③ 输出改造 genome 设计 + 风险评分。
    """
    raise HTTPException(status_code=501, detail="TODO[学生B]: implement safe-phage design layer")


@app.get("/api/download")
def download(phage_id: str | None = None, db: Session = Depends(get_db)):
    """基因组/注释批量下载 (免登录).

    TODO[学生B]: 返回 FASTA/GBK/注释表 (单个或打包)。
    """
    raise HTTPException(status_code=501, detail="TODO[学生B]: implement download endpoint")

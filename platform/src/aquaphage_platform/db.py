"""Database engine + session.

Alpha 用 SQLite，生产切 PostgreSQL：设环境变量 ``DATABASE_URL``。
数据由共享底座 ``analyses/406-master_table`` 的 master 表 ETL 而来。
"""

import os
from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from .models import Base

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./aquaphage.db")

_connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, connect_args=_connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[Session, None, None]:
    """FastAPI dependency: 每请求一个 session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db() -> None:
    """建表。

    学生 B: 真正的数据装载走 ETL —— 从 ``406-master_table`` 产出的
    ``master_annotation.sqlite`` / ``.parquet`` 读入并 upsert 到本库。
    这里只负责 schema 创建。
    """
    Base.metadata.create_all(bind=engine)

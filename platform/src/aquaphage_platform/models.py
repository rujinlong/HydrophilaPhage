"""SQLAlchemy ORM models — 水产病原噬菌体安全筛查/设计平台 (line②).

Schema 的 single source of truth: ``program-docs/line2-db-schema.md §1`` (5 张表).
数据来源: 共享底座 ``analyses/406-master_table`` 的 ``master_annotation.sqlite`` (ETL 进本库).

学生 B: 字段已按 spec 预置。若调整 schema，请**同步**更新 line2-db-schema.md，
保持文档与代码一致 (NAR 评审会核对 comprehensiveness)。
"""

from __future__ import annotations

from sqlalchemy import ForeignKey, JSON
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Host(Base):
    """hosts — 水产病原宿主菌 (host 切分是本平台 novelty 之一)."""

    __tablename__ = "hosts"

    host_taxid: Mapped[int] = mapped_column(primary_key=True)
    host_name: Mapped[str | None]
    pathogen_of: Mapped[str | None]  # 鱼/虾 species
    disease: Mapped[str | None]

    phages: Mapped[list[Phage]] = relationship(back_populates="host")


class Phage(Base):
    """phages — 噬菌体基因组 + 注释主表."""

    __tablename__ = "phages"

    phage_id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str | None]
    accession: Mapped[str | None]
    host_genus: Mapped[str | None]
    host_species: Mapped[str | None]
    host_taxid: Mapped[int | None] = mapped_column(ForeignKey("hosts.host_taxid"))
    genome_len: Mapped[int | None]
    gc: Mapped[float | None]
    molecule: Mapped[str | None] = mapped_column(default="dsDNA")
    checkv_completeness: Mapped[float | None]
    checkv_quality: Mapped[str | None]
    lifestyle: Mapped[str | None]  # virulent / temperate
    taxonomy_family: Mapped[str | None]
    taxonomy_genus: Mapped[str | None]
    source_db: Mapped[str | None]
    seq_path: Mapped[str | None]

    host: Mapped[Host | None] = relationship(back_populates="phages")
    safety: Mapped[Safety | None] = relationship(back_populates="phage", uselist=False)
    enzymes: Mapped[list[Enzyme]] = relationship(back_populates="phage")
    designs: Mapped[list[Design]] = relationship(back_populates="parent_phage")


class Safety(Base):
    """safety ⭐ — 治疗安全筛查 (本平台核心卖点; 规则见 line2-db-schema §1)."""

    __tablename__ = "safety"

    phage_id: Mapped[str] = mapped_column(ForeignKey("phages.phage_id"), primary_key=True)
    n_vfdb_virulence: Mapped[int | None] = mapped_column(default=0)
    vfdb_hits: Mapped[dict | None] = mapped_column(JSON)
    n_card_arg: Mapped[int | None] = mapped_column(default=0)
    card_hits: Mapped[dict | None] = mapped_column(JSON)
    lysogeny_flag: Mapped[bool | None] = mapped_column(default=False)
    integrase: Mapped[bool | None] = mapped_column(default=False)
    repressor: Mapped[bool | None] = mapped_column(default=False)
    recombinase: Mapped[bool | None] = mapped_column(default=False)
    known_toxin: Mapped[bool | None] = mapped_column(default=False)
    # 规则: 有 ARG 或 毒力 或 溶原模块(integrase+repressor) -> caution/unsafe; 全清 -> safe
    safety_grade: Mapped[str | None]  # safe / caution / unsafe

    phage: Mapped[Phage] = relationship(back_populates="safety")


class Enzyme(Base):
    """enzymes ⭐ — 杀菌酶资源 (depolymerase/endolysin/holin/spanin)."""

    __tablename__ = "enzymes"

    enzyme_id: Mapped[str] = mapped_column(primary_key=True)
    phage_id: Mapped[str] = mapped_column(ForeignKey("phages.phage_id"))
    type: Mapped[str | None]  # depolymerase / endolysin / holin / spanin
    domain_arch: Mapped[str | None]
    length_aa: Mapped[int | None]
    structure_model: Mapped[str | None]  # ESMFold / AF
    foldseek_top_hit: Mapped[str | None]
    predicted_activity: Mapped[str | None]

    phage: Mapped[Phage] = relationship(back_populates="enzymes")


class Design(Base):
    """designs — safe-phage 逆向工程设计层 (区别于纯描述性 DB 的关键 novelty)."""

    __tablename__ = "designs"

    design_id: Mapped[str] = mapped_column(primary_key=True)
    parent_phage_id: Mapped[str] = mapped_column(ForeignKey("phages.phage_id"))
    removed_module: Mapped[str | None]  # integrase / repressor / 毒力 cassette
    rationale: Mapped[str | None]
    status: Mapped[str | None]  # proposed / built / validated

    parent_phage: Mapped[Phage] = relationship(back_populates="designs")

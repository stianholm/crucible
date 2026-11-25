"""Candidate artifact storage. Fills the `artifact_uri` column the Phase 2
schema always had a place for but never used — Phase 2's single hill
climber only ever needed the current in-memory incumbent, never a lookup
of historical candidate text. Phase 3 selects arbitrary past elites as
parents, which means their actual code has to be retrievable by more than
a one-way sha256 hash.

Uses MinIO (already running from Phase 0, S3-compatible) via boto3.
"""

from __future__ import annotations

import os

import boto3
from botocore.client import Config

BUCKET = "candidates"

_client = None


def s3_client():
    global _client
    if _client is None:
        _client = boto3.client(
            "s3",
            endpoint_url=os.environ.get("MINIO_ENDPOINT", "http://localhost:9002"),
            aws_access_key_id=os.environ.get("MINIO_ROOT_USER", "minio"),
            aws_secret_access_key=os.environ["MINIO_ROOT_PASSWORD"],
            config=Config(signature_version="s3v4"),
            region_name="auto",
        )
    return _client


def put_candidate(sha: str, block: str) -> str:
    """Returns the artifact_uri to store in the iteration row."""
    key = f"{sha}.py"
    s3_client().put_object(Bucket=BUCKET, Key=key, Body=block.encode())
    return f"s3://{BUCKET}/{key}"


def get_candidate(sha: str) -> str | None:
    key = f"{sha}.py"
    try:
        obj = s3_client().get_object(Bucket=BUCKET, Key=key)
        return obj["Body"].read().decode()
    except s3_client().exceptions.NoSuchKey:
        return None

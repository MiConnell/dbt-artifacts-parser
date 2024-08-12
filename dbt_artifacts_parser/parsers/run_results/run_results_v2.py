# generated by datamodel-codegen:
#   filename:  run-results_v2.json

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import AwareDatetime, ConfigDict

from dbt_artifacts_parser.parsers.base import BaseParserModel


class BaseArtifactMetadata(BaseParserModel):
    model_config = ConfigDict(
        extra="allow",
    )
    dbt_schema_version: str
    dbt_version: Optional[str] = '0.20.0rc1'
    generated_at: Optional[AwareDatetime] = '2021-06-07T14:49:01.097134Z'
    invocation_id: Optional[str] = None
    env: Optional[Dict[str, str]] = {}


class Status(Enum):
    success = 'success'
    error = 'error'
    skipped = 'skipped'


class Status1(Enum):
    pass_ = 'pass'
    error = 'error'
    fail = 'fail'
    warn = 'warn'


class Status2(Enum):
    pass_ = 'pass'
    warn = 'warn'
    error = 'error'
    runtime_error = 'runtime error'


class TimingInfo(BaseParserModel):
    model_config = ConfigDict(
        extra="allow",
    )
    name: str
    started_at: Optional[AwareDatetime] = None
    completed_at: Optional[AwareDatetime] = None


class RunResultOutput(BaseParserModel):
    model_config = ConfigDict(
        extra="allow",
    )
    status: Union[Status, Status1, Status2]
    timing: List[TimingInfo]
    thread_id: str
    execution_time: float
    adapter_response: Dict[str, Any]
    message: Optional[str] = None
    failures: Optional[int] = None
    unique_id: str


class RunResultsV2(BaseParserModel):
    model_config = ConfigDict(
        extra="allow",
    )
    metadata: BaseArtifactMetadata
    results: List[RunResultOutput]
    elapsed_time: float
    args: Optional[Dict[str, Any]] = {}

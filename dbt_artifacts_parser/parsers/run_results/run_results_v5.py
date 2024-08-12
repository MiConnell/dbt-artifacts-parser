# generated by datamodel-codegen:
#   filename:  run-results_v5.json

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import ConfigDict

from dbt_artifacts_parser.parsers.base import BaseParserModel


class BaseArtifactMetadata(BaseParserModel):
    model_config = ConfigDict(
        extra="allow",
    )
    dbt_schema_version: str
    dbt_version: Optional[str] = '1.7.0b1'
    generated_at: Optional[str] = None
    invocation_id: Optional[str] = None
    env: Optional[Dict[str, str]] = None


class TimingInfo(BaseParserModel):
    model_config = ConfigDict(
        extra="allow",
    )
    name: str
    started_at: Optional[str] = None
    completed_at: Optional[str] = None


class Status(Enum):
    success = 'success'
    error = 'error'
    skipped = 'skipped'


class Status1(Enum):
    pass_ = 'pass'
    error = 'error'
    fail = 'fail'
    warn = 'warn'
    skipped = 'skipped'


class Status2(Enum):
    pass_ = 'pass'
    warn = 'warn'
    error = 'error'
    runtime_error = 'runtime error'


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
    compiled: Optional[bool] = None
    compiled_code: Optional[str] = None
    relation_name: Optional[str] = None


class RunResultsV5(BaseParserModel):
    model_config = ConfigDict(
        extra="allow",
    )
    metadata: BaseArtifactMetadata
    results: List[RunResultOutput]
    elapsed_time: float
    args: Optional[Dict[str, Any]] = None


# NOTE: We manually change the class, as the generated code is not correct.
# class RunResultsV5(RootModel[RunResultsArtifact]):
#     root: RunResultsArtifact

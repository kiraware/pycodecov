from datetime import datetime
from typing import Any

from ..enums import CommitState
from ..schemas import BaseCommit, Commit, CommitDetail, GitCommit
from .report import parse_report_data
from .total import parse_commit_total_data
from .user import parse_git_author_data, parse_owner_data

__all__ = [
    "parse_base_commit_data",
    "parse_commit_data",
    "parse_commit_detail_data",
    "parse_git_commit_data",
]


def parse_base_commit_data(data: dict[str, Any]) -> BaseCommit:
    """
    Parse base commit data.

    Args:
        data: base commit json data.

    Returns:
        A `BaseCommit` schema.

    Examples:
    >>> data = {
    ...     "commitid": "string",
    ...     "message": "string",
    ...     "timestamp": "2024-03-25T16:38:25.747678Z",
    ... }
    >>> base_commit = parse_base_commit_data(data)
    >>> base_commit
    BaseCommit(commitid='string', message='string', timestamp=datetime.datetime(...)
    """
    commitid = data.get("commitid")
    message = data.get("message")
    timestamp = data.get("timestamp")

    return BaseCommit(commitid, message, datetime.fromisoformat(timestamp))


def parse_commit_data(data: dict[str, Any]) -> Commit:
    """
    Parse commit data.

    Args:
        data: commit json data.

    Returns:
        A `Commit` schema.

    Examples:
    >>> data = {
    ...     "commitid": "string",
    ...     "message": "string",
    ...     "timestamp": "2024-03-25T16:38:25.747678Z",
    ...     "ci_passed": True,
    ...     "author": None,
    ...     "branch": "string",
    ...     "totals": None,
    ...     "state": None,
    ...     "parent": "string",
    ... }
    >>> commit = parse_commit_data(data)
    >>> commit
    Commit(commitid='string', message='string', timestamp=datetime.datetime(...), ci_passed=True, author=None, branch='string', totals=None, state=None, parent='string')
    """  # noqa: E501
    base_commit = parse_base_commit_data(data)

    commitid = base_commit.commitid
    message = base_commit.message
    timestamp = base_commit.timestamp

    ci_passed = data.get("ci_passed")
    author = data.get("author")
    branch = data.get("branch")
    totals = data.get("totals")
    state = data.get("state")
    parent = data.get("parent")

    return Commit(
        commitid,
        message,
        timestamp,
        ci_passed,
        parse_owner_data(author) if author is not None else author,
        branch,
        parse_commit_total_data(totals) if totals is not None else totals,
        CommitState(state) if state is not None else state,
        parent,
    )


def parse_commit_detail_data(data: dict[str, Any]) -> CommitDetail:
    """
    Parse commit detail data.

    Args:
        data: commit detail json data.

    Returns:
        A `CommitDetail` schema.

    Examples:
    >>> data = {
    ...     "commitid": "string",
    ...     "message": "string",
    ...     "timestamp": "2024-03-25T16:38:25.747678Z",
    ...     "ci_passed": True,
    ...     "author": None,
    ...     "branch": "string",
    ...     "totals": None,
    ...     "state": None,
    ...     "parent": "string",
    ...     "report": {
    ...         "totals": {
    ...             "files": 0,
    ...             "lines": 0,
    ...             "hits": 0,
    ...             "misses": 0,
    ...             "partials": 0,
    ...             "coverage": 0,
    ...             "branches": 0,
    ...             "methods": 0,
    ...             "messages": 0,
    ...             "sessions": 0,
    ...             "complexity": 0,
    ...             "complexity_total": 0,
    ...             "complexity_ratio": 0,
    ...             "diff": [],
    ...         },
    ...         "files": [
    ...             {
    ...                 "name": "string",
    ...                 "totals": {
    ...                     "files": 0,
    ...                     "lines": 0,
    ...                     "hits": 0,
    ...                     "misses": 0,
    ...                     "partials": 0,
    ...                     "coverage": 0,
    ...                     "branches": 0,
    ...                     "methods": 0,
    ...                     "messages": 0,
    ...                     "sessions": 0,
    ...                     "complexity": 0,
    ...                     "complexity_total": 0,
    ...                     "complexity_ratio": 0,
    ...                     "diff": 0,
    ...                 },
    ...             }
    ...         ],
    ...     },
    ... }
    >>> commit_detail = parse_commit_detail_data(data)
    >>> commit_detail
    CommitDetail(commitid='string', message='string', timestamp=datetime.datetime(...), ci_passed=True, author=None, branch='string', totals=None, state=None, parent='string', report=Report(...))
    """  # noqa: E501
    commit = parse_commit_data(data)

    commitid = commit.commitid
    message = commit.message
    timestamp = commit.timestamp
    ci_passed = commit.ci_passed
    author = commit.author
    branch = commit.branch
    totals = commit.totals
    state = commit.state
    parent = commit.parent

    report = data.get("report")

    return CommitDetail(
        commitid,
        message,
        timestamp,
        ci_passed,
        author,
        branch,
        totals,
        state,
        parent,
        parse_report_data(report),
    )


def parse_git_commit_data(data: dict[str, Any]) -> GitCommit:
    """
    Parse git commit data.

    Args:
        data: git commit json data.

    Returns:
        A `GitCommit` schema.

    Examples:
    >>> data = {
    ...     "commitid": "string",
    ...     "message": "string",
    ...     "timestamp": "2024-03-25T16:38:25.747678Z",
    ...     "author": {
    ...         "id": 123,
    ...         "username": "string",
    ...         "name": "string",
    ...         "email": "string",
    ...     },
    ... }
    >>> git_commit = parse_git_commit_data(data)
    >>> git_commit
    GitCommit(commitid='string', message='string', timestamp=datetime.datetime(...), author=GitAuthor(...))
    """  # noqa: E501
    base_commit = parse_base_commit_data(data)

    commitid = base_commit.commitid
    message = base_commit.message
    timestamp = base_commit.timestamp

    author = data.get("author")

    return GitCommit(commitid, message, timestamp, parse_git_author_data(author))

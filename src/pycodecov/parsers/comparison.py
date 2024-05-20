from typing import Any

from ..enums import Coverage
from ..schemas import (
    CommitComparison,
    ComponentComparison,
    DiffComparison,
    FileChangeSummaryComparison,
    FileComparison,
    FileNameComparison,
    FileStatComparison,
    FlagComparison,
    LineComparison,
    LineCoverageComparison,
    LineNumberComparison,
    TotalComparison,
)
from .commit import parse_commit_data, parse_git_commit_data
from .total import parse_report_total_data

__all__ = [
    "parse_line_number_comparison_data",
    "parse_line_coverage_comparison_data",
    "parse_line_comparison_data",
    "parse_total_comparison_data",
    "parse_file_name_comparison_data",
    "parse_file_stat_comparison_data",
    "parse_file_change_summary_comparison_data",
    "parse_file_comparison_data",
    "parse_diff_comparison_data",
    "parse_commit_comparison_data",
    "parse_component_comparison_data",
    "parse_flag_comparison_data",
]


def parse_line_number_comparison_data(data: dict[str, Any]) -> LineNumberComparison:
    """
    Parse line number comparison data.

    Args:
        data: line number comparison json data.

    Returns:
        A `LineNumberComparison` schema.

    Examples:
    >>> data = {
    ...     "base": 0,
    ...     "head": 0,
    ... }
    >>> line_number_comparison = parse_line_number_comparison_data(data)
    >>> line_number_comparison
    LineNumberComparison(base=0, head=0)
    """
    base = data.get("base")
    head = data.get("head")

    return LineNumberComparison(base, head)


def parse_line_coverage_comparison_data(data: dict[str, Any]) -> LineCoverageComparison:
    """
    Parse line coverage comparison data.

    Args:
        data: line coverage comparison json data.

    Returns:
        A `LineCoverageComparison` schema.

    Examples:
    >>> data = {
    ...     "base": 0,
    ...     "head": 0,
    ... }
    >>> line_coverage_comparison = parse_line_coverage_comparison_data(data)
    >>> line_coverage_comparison
    LineCoverageComparison(base=<Coverage.HIT: 0>, head=<Coverage.HIT: 0>)
    """
    base = data.get("base")
    head = data.get("head")

    return LineCoverageComparison(Coverage(base), Coverage(head))


def parse_line_comparison_data(data: dict[str, Any]) -> LineComparison:
    """
    Parse line comparison data.

    Args:
        data: line comparison json data.

    Returns:
        A `LineComparison` schema.

    Examples:
    >>> data = {
    ...     "value": "string",
    ...     "number": {
    ...         "base": 0,
    ...         "head": 0,
    ...     },
    ...     "coverage": {
    ...         "base": 0,
    ...         "head": 0,
    ...     },
    ...     "is_diff": True,
    ...     "added": True,
    ...     "removed": False,
    ...     "sessions": 0,
    ... }
    >>> line_comparison = parse_line_comparison_data(data)
    >>> line_comparison
    LineComparison(value='string', number=LineNumberComparison(...), coverage=LineCoverageComparison(...), is_diff=True, added=True, removed=False, sessions=0)
    """  # noqa: E501
    value = data.get("value")
    number = data.get("number")
    coverage = data.get("coverage")
    is_diff = data.get("is_diff")
    added = data.get("added")
    removed = data.get("removed")
    sessions = data.get("sessions")

    return LineComparison(
        value,
        parse_line_number_comparison_data(number),
        parse_line_coverage_comparison_data(coverage),
        is_diff,
        added,
        removed,
        sessions,
    )


def parse_total_comparison_data(data: dict[str, Any]) -> TotalComparison:
    """
    Parse total comparison data.

    Args:
        data: total comparison json data.

    Returns:
        A `TotalComparison` schema.

    Examples:
    >>> data = {
    ...     "base": {
    ...         "files": 123,
    ...         "lines": 123,
    ...         "hits": 123,
    ...         "misses": 123,
    ...         "partials": 123,
    ...         "coverage": 12.3,
    ...         "branches": 123,
    ...         "methods": 123,
    ...         "messages": 123,
    ...         "sessions": 123,
    ...         "complexity": 12.3,
    ...         "complexity_total": 12.3,
    ...         "complexity_ratio": 12.3,
    ...         "diff": 123,
    ...     },
    ...     "head": {
    ...         "files": 123,
    ...         "lines": 123,
    ...         "hits": 123,
    ...         "misses": 123,
    ...         "partials": 123,
    ...         "coverage": 12.3,
    ...         "branches": 123,
    ...         "methods": 123,
    ...         "messages": 123,
    ...         "sessions": 123,
    ...         "complexity": 12.3,
    ...         "complexity_total": 12.3,
    ...         "complexity_ratio": 12.3,
    ...         "diff": 123,
    ...     },
    ...     "patch": None,
    ... }
    >>> total_comparison = parse_total_comparison_data(data)
    >>> total_comparison
    TotalComparison(base=ReportTotal(...), head=ReportTotal(...), patch=None)
    """
    base = data.get("base")
    head = data.get("head")
    patch = data.get("patch")

    return TotalComparison(
        parse_report_total_data(base),
        parse_report_total_data(head),
        parse_report_total_data(patch) if patch is not None else patch,
    )


def parse_file_name_comparison_data(data: dict[str, Any]) -> FileNameComparison:
    """
    Parse file name comparison data.

    Args:
        data: file name comparison json data.

    Returns:
        A `FileNameComparison` schema.

    Examples:
    >>> data = {
    ...     "base": "string",
    ...     "head": "string",
    ... }
    >>> file_name_comparison = parse_file_name_comparison_data(data)
    >>> file_name_comparison
    FileNameComparison(base='string', head='string')
    """
    base = data.get("base")
    head = data.get("head")

    return FileNameComparison(base, head)


def parse_file_stat_comparison_data(data: dict[str, Any]) -> FileStatComparison:
    """
    Parse file stat comparison data.

    Args:
        data: file stat comparison json data.

    Returns:
        A `FileStatComparison` schema.

    Examples:
    >>> data = {
    ...     "added": 0,
    ...     "removed": 0,
    ... }
    >>> file_stat_comparison = parse_file_stat_comparison_data(data)
    >>> file_stat_comparison
    FileStatComparison(added=0, removed=0)
    """
    added = data.get("added")
    removed = data.get("removed")

    return FileStatComparison(added, removed)


def parse_file_change_summary_comparison_data(
    data: dict[str, Any],
) -> FileChangeSummaryComparison:
    """
    Parse file change summary comparison data.

    Args:
        data: file change summary comparison json data.

    Returns:
        A `FileChangeSummaryComparison` schema.

    Examples:
    >>> data = {
    ...     "hits": 0,
    ...     "misses": 0,
    ...     "partials": 0,
    ... }
    >>> file_change_summary_comparison = parse_file_change_summary_comparison_data(data)
    >>> file_change_summary_comparison
    FileChangeSummaryComparison(hits=0, misses=0, partials=0)
    """
    hits = data.get("hits")
    misses = data.get("misses")
    partials = data.get("partials")

    return FileChangeSummaryComparison(hits, misses, partials)


def parse_file_comparison_data(data: dict[str, Any]) -> FileComparison:
    """
    Parse file comparison data.

    Args:
        data: file comparison json data.

    Returns:
        A `FileComparison` schema.

    Examples:
    >>> data = {
    ...     "name": {
    ...         "base": "string",
    ...         "head": "string",
    ...     },
    ...     "totals": {
    ...         "base": {
    ...             "files": 123,
    ...             "lines": 123,
    ...             "hits": 123,
    ...             "misses": 123,
    ...             "partials": 123,
    ...             "coverage": 12.3,
    ...             "branches": 123,
    ...             "methods": 123,
    ...             "messages": 123,
    ...             "sessions": 123,
    ...             "complexity": 12.3,
    ...             "complexity_total": 12.3,
    ...             "complexity_ratio": 12.3,
    ...             "diff": 123,
    ...         },
    ...         "head": {
    ...             "files": 123,
    ...             "lines": 123,
    ...             "hits": 123,
    ...             "misses": 123,
    ...             "partials": 123,
    ...             "coverage": 12.3,
    ...             "branches": 123,
    ...             "methods": 123,
    ...             "messages": 123,
    ...             "sessions": 123,
    ...             "complexity": 12.3,
    ...             "complexity_total": 12.3,
    ...             "complexity_ratio": 12.3,
    ...             "diff": 123,
    ...         },
    ...         "patch": None,
    ...     },
    ...     "has_diff": True,
    ...     "stats": None,
    ...     "change_summary": None,
    ...     "lines": [],
    ... }
    >>> file_comparison = parse_file_comparison_data(data)
    >>> file_comparison
    FileComparison(name=FileNameComparison(...), totals=TotalComparison(...), has_diff=True, stats=None, change_summary=None, lines=[])
    """  # noqa: E501
    name = data.get("name")
    totals = data.get("totals")
    has_diff = data.get("has_diff")
    stats = data.get("stats")
    change_summary = data.get("change_summary")
    lines = data.get("lines")

    return FileComparison(
        parse_file_name_comparison_data(name),
        parse_total_comparison_data(totals),
        has_diff,
        parse_file_stat_comparison_data(stats) if stats is not None else stats,
        parse_file_change_summary_comparison_data(change_summary)
        if change_summary is not None
        else change_summary,
        [parse_line_comparison_data(line) for line in lines],
    )


def parse_diff_comparison_data(data: dict[str, Any]) -> DiffComparison:
    """
    Parse diff comparison data.

    Args:
        data: diff comparison json data.

    Returns:
        A `DiffComparison` schema.

    Examples:
    >>> data = {
    ...     "git_commits": [],
    ... }
    >>> diff_comparison = parse_diff_comparison_data(data)
    >>> diff_comparison
    DiffComparison(git_commits=[])
    """
    git_commits = data.get("git_commits")

    return DiffComparison(
        [parse_git_commit_data(git_commit) for git_commit in git_commits]
    )


def parse_commit_comparison_data(data: dict[str, Any]) -> CommitComparison:
    """
    Parse commit comparison data.

    Args:
        data: commit comparison json data.

    Returns:
        A `CommitComparison` schema.

    Examples:
    >>> data = {
    ...     "base_commit": "string",
    ...     "head_commit": "string",
    ...     "totals": {
    ...         "base": {
    ...             "files": 123,
    ...             "lines": 123,
    ...             "hits": 123,
    ...             "misses": 123,
    ...             "partials": 123,
    ...             "coverage": 12.3,
    ...             "branches": 123,
    ...             "methods": 123,
    ...             "messages": 123,
    ...             "sessions": 123,
    ...             "complexity": 12.3,
    ...             "complexity_total": 12.3,
    ...             "complexity_ratio": 12.3,
    ...             "diff": 123,
    ...         },
    ...         "head": {
    ...             "files": 123,
    ...             "lines": 123,
    ...             "hits": 123,
    ...             "misses": 123,
    ...             "partials": 123,
    ...             "coverage": 12.3,
    ...             "branches": 123,
    ...             "methods": 123,
    ...             "messages": 123,
    ...             "sessions": 123,
    ...             "complexity": 12.3,
    ...             "complexity_total": 12.3,
    ...             "complexity_ratio": 12.3,
    ...             "diff": 123,
    ...         },
    ...         "patch": None,
    ...     },
    ...     "commit_uploads": [],
    ...     "diff": {
    ...         "git_commits": [],
    ...     },
    ...     "files": [],
    ...     "untracked": [],
    ...     "has_unmerged_base_commits": False,
    ... }
    >>> commit_comparison = parse_commit_comparison_data(data)
    >>> commit_comparison
    CommitComparison(base_commit='string', head_commit='string', totals=TotalComparison(...), commit_uploads=[], diff=DiffComparison(...), files=[], untracked=[], has_unmerged_base_commits=False)
    """  # noqa: E501
    base_commit = data.get("base_commit")
    head_commit = data.get("head_commit")
    totals = data.get("totals")
    commit_uploads = data.get("commit_uploads")
    diff = data.get("diff")
    files = data.get("files")
    untracked = data.get("untracked")
    has_unmerged_base_commits = data.get("has_unmerged_base_commits")

    return CommitComparison(
        base_commit,
        head_commit,
        parse_total_comparison_data(totals),
        [parse_commit_data(commit_upload) for commit_upload in commit_uploads],
        parse_diff_comparison_data(diff),
        [parse_file_comparison_data(file) for file in files],
        untracked,
        has_unmerged_base_commits,
    )


def parse_component_comparison_data(data: dict[str, Any]) -> ComponentComparison:
    """
    Parse component comparison data.

    Args:
        data: component comparison json data.

    Returns:
        A `ComponentComparison` schema.

    Examples:
    >>> data = {
    ...     "component_id": "string",
    ...     "name": "string",
    ...     "base_report_totals": {
    ...         "files": 123,
    ...         "lines": 123,
    ...         "hits": 123,
    ...         "misses": 123,
    ...         "partials": 123,
    ...         "coverage": 12.3,
    ...         "branches": 123,
    ...         "methods": 123,
    ...         "messages": 123,
    ...         "sessions": 123,
    ...         "complexity": 12.3,
    ...         "complexity_total": 12.3,
    ...         "complexity_ratio": 12.3,
    ...         "diff": 123,
    ...     },
    ...     "head_report_totals": {
    ...         "files": 123,
    ...         "lines": 123,
    ...         "hits": 123,
    ...         "misses": 123,
    ...         "partials": 123,
    ...         "coverage": 12.3,
    ...         "branches": 123,
    ...         "methods": 123,
    ...         "messages": 123,
    ...         "sessions": 123,
    ...         "complexity": 12.3,
    ...         "complexity_total": 12.3,
    ...         "complexity_ratio": 12.3,
    ...         "diff": 123,
    ...     },
    ...     "diff_totals": None,
    ... }
    >>> component_comparison = parse_component_comparison_data(data)
    >>> component_comparison
    ComponentComparison(component_id='string', name='string', base_report_totals=ReportTotal(...), head_report_totals=ReportTotal(...), diff_totals=None)
    """  # noqa: E501
    component_id = data.get("component_id")
    name = data.get("name")
    base_report_totals = data.get("base_report_totals")
    head_report_totals = data.get("head_report_totals")
    diff_totals = data.get("diff_totals")

    return ComponentComparison(
        component_id,
        name,
        parse_report_total_data(base_report_totals),
        parse_report_total_data(head_report_totals),
        parse_report_total_data(diff_totals)
        if diff_totals is not None
        else diff_totals,
    )


def parse_flag_comparison_data(data: dict[str, Any]) -> FlagComparison:
    """
    Parse flag comparison data.

    Args:
        data: flag comparison json data.

    Returns:
        A `FlagComparison` schema.

    Examples:
    >>> data = {
    ...     "name": "string",
    ...     "base_report_totals": {
    ...         "files": 123,
    ...         "lines": 123,
    ...         "hits": 123,
    ...         "misses": 123,
    ...         "partials": 123,
    ...         "coverage": 12.3,
    ...         "branches": 123,
    ...         "methods": 123,
    ...         "messages": 123,
    ...         "sessions": 123,
    ...         "complexity": 12.3,
    ...         "complexity_total": 12.3,
    ...         "complexity_ratio": 12.3,
    ...         "diff": 123,
    ...     },
    ...     "head_report_totals": {
    ...         "files": 123,
    ...         "lines": 123,
    ...         "hits": 123,
    ...         "misses": 123,
    ...         "partials": 123,
    ...         "coverage": 12.3,
    ...         "branches": 123,
    ...         "methods": 123,
    ...         "messages": 123,
    ...         "sessions": 123,
    ...         "complexity": 12.3,
    ...         "complexity_total": 12.3,
    ...         "complexity_ratio": 12.3,
    ...         "diff": 123,
    ...     },
    ...     "diff_totals": None,
    ... }
    >>> flag_comparison = parse_flag_comparison_data(data)
    >>> flag_comparison
    FlagComparison(name='string', base_report_totals=ReportTotal(...), head_report_totals=ReportTotal(...), diff_totals=None)
    """  # noqa: E501
    name = data.get("name")
    base_report_totals = data.get("base_report_totals")
    head_report_totals = data.get("head_report_totals")
    diff_totals = data.get("diff_totals")

    return FlagComparison(
        name,
        parse_report_total_data(base_report_totals),
        parse_report_total_data(head_report_totals),
        parse_report_total_data(diff_totals)
        if diff_totals is not None
        else diff_totals,
    )

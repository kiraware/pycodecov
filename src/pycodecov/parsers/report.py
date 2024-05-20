from typing import Any

from ..schemas import BaseReportFile, Report, ReportFile
from .line import parse_line_data
from .total import parse_report_total_data

__all__ = [
    "parse_base_report_file_data",
    "parse_report_data",
    "parse_report_file_data",
]


def parse_base_report_file_data(data: dict[str, Any]) -> BaseReportFile:
    """
    Parse base report file data.

    Args:
        data: base report file json data.

    Returns:
        A `BaseReportFile` schema.

    Examples:
    >>> data = {
    ...     "name": "string",
    ...     "totals": {
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
    ... }
    >>> base_report_file = parse_base_report_file_data(data)
    >>> base_report_file
    BaseReportFile(name='string', totals=ReportTotal(...))
    """
    name = data.get("name")
    totals = data.get("totals")

    return BaseReportFile(name, parse_report_total_data(totals))


def parse_report_file_data(data: dict[str, Any]) -> ReportFile:
    """
    Parse report file data.

    Args:
        data: report file json data.

    Returns:
        A `ReportFile` schema.

    Examples:
    >>> data = {
    ...     "name": "string",
    ...     "totals": {
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
    ...     "line_coverage": [],
    ... }
    >>> report_file = parse_report_file_data(data)
    >>> report_file
    ReportFile(name='string', totals=ReportTotal(...), line_coverage=[])
    """
    base_report_file = parse_base_report_file_data(data)

    name = base_report_file.name
    totals = base_report_file.totals

    line_coverage = data.get("line_coverage")

    return ReportFile(
        name,
        totals,
        [parse_line_data(line) for line in line_coverage],
    )


def parse_report_data(data: dict[str, Any]) -> Report:
    """
    Parse report data.

    Args:
        data: report json data.

    Returns:
        A `Report` schema.

    Examples:
    >>> data = {
    ...     "totals": {
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
    ...     "files": [],
    ... }
    >>> report = parse_report_data(data)
    >>> report
    Report(totals=ReportTotal(...), files=[])
    """
    totals = data.get("totals")
    files = data.get("files")

    return Report(
        parse_report_total_data(totals),
        [parse_base_report_file_data(file) for file in files],
    )

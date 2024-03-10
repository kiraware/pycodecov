"""
Module to store a str enum class representation Git hosting service provider.
"""

from enum import StrEnum

__all__ = ["Service"]


class Service(StrEnum):
    """
    A str enum class that define valid Git hosting service provider.

    Attributes:
        GITHUB: `"github"`
        GITLAB: `"gitlab"`
        BITBUCKET: `"bitbucket"`
        GITHUB_ENTERPRISE: `"github_enterprise"`
        GITLAB_ENTERPRISE: `"gitlab_enterprise"`
        BITBUCKET_SERVER: `"bitbucket_server"`

    Examples:
        >>> Service("github")
        <Service.GITHUB: 'github'>
        >>> Service["GITHUB"]
        <Service.GITHUB: 'github'>
        >>> Service.GITHUB
        <Service.GITHUB: 'github'>
        >>> Service.GITHUB == "github"
        True
        >>> print(Service.GITHUB)
        github
    """

    GITHUB: str = "github"
    GITLAB: str = "gitlab"
    BITBUCKET: str = "bitbucket"
    GITHUB_ENTERPRISE: str = "github_enterprise"
    GITLAB_ENTERPRISE: str = "gitlab_enterprise"
    BITBUCKET_SERVER: str = "bitbucket_server"

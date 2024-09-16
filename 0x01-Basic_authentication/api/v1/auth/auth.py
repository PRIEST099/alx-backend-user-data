#!/usr/bin/env python3
from typing import List, TypeVar
from flask import request


class Auth():
    """a class to manage the API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Public method that returns False for now.
        Later, it will use `path` and `excluded_paths`
        to determine authorization.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Returns False for now
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns False for now
        Keyword arguments:
        request -- a request object
        Return: a typeval object
        """
        return None

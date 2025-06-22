"""
Byonoy Luminescence Reader MCP Server

A Model Context Protocol (MCP) server for controlling Byonoy Lum96 luminescence readers.
"""

__version__ = "0.1.0"
__author__ = "Luis Villa"
__email__ = "luis.villa@example.com"

from .server import mcp

__all__ = ["mcp"] 
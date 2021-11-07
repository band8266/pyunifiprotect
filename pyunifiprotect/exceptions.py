class UnifiProtectError(Exception):
    """Base class for all other Unifi Protect errors"""


class StreamError(UnifiProtectError):
    """Expcetion raised when trying to stream content"""


class DataDecodeError(UnifiProtectError):
    """Exception raised when trying to decode a Unifi Protect object"""


class WSDecodeError(UnifiProtectError):
    """Exception raised when decoding Websocket packet"""


class WSEncodeError(UnifiProtectError):
    """Exception raised when encoding Websocket packet"""


class ClientError(UnifiProtectError):
    """Base Class for all other Unifi Protect client errors"""


class BadRequest(ClientError):
    """Invalid request from API Client"""


class Invalid(ClientError):
    """Invalid return from Authorization Request."""


class NotAuthorized(ClientError):
    """Wrong username and/or Password."""


class NvrError(ClientError):
    """Other error."""

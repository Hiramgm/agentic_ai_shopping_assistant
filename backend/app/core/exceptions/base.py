class ApplicationException(Exception):
    """Base exception for the application."""
    pass


class ProviderException(ApplicationException):
    """Raised when a provider cannot be initialized or is unsupported."""
    pass


class RetrievalException(ApplicationException):
    """Raised when retrieval fails."""
    pass


class DatabaseException(ApplicationException):
    """Raised when a database operation fails."""
    pass
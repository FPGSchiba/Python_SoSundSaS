class DisconnectedError(Exception):
    def __init__(self, message, errors):
        # Call the base class constructor with the parameters it needs
        super(DisconnectedError, self).__init__(message)
        self.errors = errors
        self.message = "Socket disconnected unexpected"
        pass
class NoPlayersInMurderPlaceError(ValueError):
    """Exception raised when there are no players in the murder place."""
    def __init__(self, message="No players in the murder place."):
        self.message = message
        super().__init__(self.message)



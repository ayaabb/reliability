class NoPlayersInMurdererPlacesError(ValueError):
    """Exception raised when there are no players in all the places of the murderer ."""

    def __init__(self, message="No players in the murderer's last visited places. "):
        self.message = message
        super().__init__(self.message)



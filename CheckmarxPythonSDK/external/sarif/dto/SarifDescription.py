class SarifDescription:
    def __init__(self, text):
        """

        Args:
            text (str):
        """
        self.Text = text

    def __str__(self):
        return f"SarifDescription(" \
               f"text={self.Text}" \
               f")"

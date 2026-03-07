class ResultModel:
    """
    Stores processed result data
    """

    def __init__(self, input_value, result):
        self.input_value = input_value
        self.result = result

    def to_dict(self):
        return {
            "input_value": self.input_value,
            "result": self.result
        }
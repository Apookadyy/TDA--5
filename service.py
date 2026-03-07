from models.data_models import DataModel
from models.result_models import ResultModel


def generate_data(n=10):
    """
    Generate sample data records
    """
    data = []

    for i in range(n):
        record = DataModel(i, i * 10)
        data.append(record)

    return data


def process_data(data):
    """
    Process data records
    """
    results = []

    for item in data:
        processed_value = item.value * 2
        result = ResultModel(item.value, processed_value)
        results.append(result)

    return results
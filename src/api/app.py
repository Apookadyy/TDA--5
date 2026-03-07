import time
from concurrent.futures import ThreadPoolExecutor

from service import generate_data
from cache import get_cached_data, cache_data
from Database.db import create_table, insert_data, fetch_data
from monitor import system_usage, log_execution_time


def process_record(record):
    """
    Process individual record
    """
    processed_value = record.value * 2
    return processed_value


def process_data_concurrently(data):
    """
    Process data using multiple threads
    """
    results = []

    with ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(process_record, data))

    return results


def main():

    print("Starting High Performance Application...\n")

    start_time = time.time()

    # Create database table
    create_table()

    cache_key = "processed_data"

    # Check cache
    cached_result = get_cached_data(cache_key)

    if cached_result:
        print("Loaded results from cache")
        results = cached_result

    else:

        print("Generating data...")
        data = generate_data(10)

        print("Processing data concurrently...")
        results = process_data_concurrently(data)

        cache_data(cache_key, results)

    # Store results in database
    for value in results:
        insert_data(value)

    # Fetch stored data
    db_data = fetch_data()

    print("\nDatabase Records:")
    for row in db_data:
        print(row)

    # System monitoring
    print("\nSystem Monitoring:")
    system_usage()

    # Execution time
    log_execution_time(start_time)

    print("\nApplication Finished Successfully.")


if __name__ == "__main__":
    main()

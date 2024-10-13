import sys
import os

def reducer():
    # retrieve the total number of records from the Hadoop counter we used in the mapper
    total_records = int(os.getenv('mapreduce_job_counters', {}).get('LogMetrics:TotalRecords', 0))


    # initialize current values
    current_request = None
    current_count = 0

    # input comes from STDIN
    for line in sys.stdin:
        # remove leading and trailing whitespace and parse the input we got from mapper.py
        request_type, count = line.strip().split('\t')
        # convert the count to an integer so that we can use it in the percentage calculation
        count = int(count)

        # use the if switch because Hadoop sorts by map output by key before passing to the reduce
        if current_request == request_type:
            # sum up the counts for the request type
            current_count += count
        else:
            # after finding the sum count for the request type, calculate the percentage before moving on to the next request type
            if current_request:
                percentage = (current_count / total_records) * 100 if total_records > 0 else 0
                print(f"{current_request}\t{percentage:.2f}%")
            current_request = request_type
            current_count = count

    # don't forget the percentage for the last request type
    if current_request:
        percentage = (current_count / total_records) * 100 if total_records > 0 else 0
        print(f"{current_request}\t{percentage:.2f}%")

if __name__ == "__main__":
    reducer()

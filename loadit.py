import argparse
import boto3


def load(job_id):
    """
    @type job_id: C{int}
    """
    with open('test.txt', 'w') as f:
        f.write('hello job: %d' % job_id)
    s3 = boto3.resource('s3')        
    with open('test.txt', 'r') as data:
        s3.Bucket('mybucket').put_object(Key='test.txt', Body=data)


def main():
    parser = argparse.ArgumentParser(description="Start work load.")
    parser.add_argument('jobId', help='job id', type=int, dest='job_id')
    args = parser.parse_args()
    load(args.job_id)


if __name__ == '__main__':
    main()

import argparse
import requests
import os
# import boto3


headers = {'Content-Type': 'application/json',
           'Accept': 'application/json',
           'Authorization': ''}


def load(job_id):
    """
    @type job_id: C{int}
    """
    r = requests.put(os.environ['HARNESS_SERVER'] + '/api/jobstatus/' + str(job_id),
                     json={'status': 'RUNNING'},
                     headers=headers)
    if r.status_code != 204:
        print('Update failed.')

    with open('test.txt', 'w') as f:
        f.write('hello job: %d' % job_id)
    # s3 = boto3.resource('s3')
    # with open('test.txt', 'r') as data:
    #    s3.Bucket('mybucket').put_object(Key='test.txt', Body=data)



def main():
    parser = argparse.ArgumentParser(description="Start work load.")
    parser.add_argument('job_id', help='job id', type=int)
    args = parser.parse_args()
    load(args.job_id)


if __name__ == '__main__':
    main()

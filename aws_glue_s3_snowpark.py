import os
import requests
import boto3
from io import BytesIO

# Github repository details
GITHUB_REPO = "https://api.github.com/repos/{owner}/{repo}/contents/{folder}"
OWNER = "deacademygit"
REPO = "project-data"
FOLDER = "snowpark-data" # Specify the folder within the repo
HEADERS = {"Accept": "application/vnd.github.v3+json"}

# S3 Bucket details
BUCKET_NAME = "kanweitech-snowpark-sales-bucket"

# Initiate S3 client
s3 = boto3.client('s3')

def fetch_github_files():
    """Fetches file details from Github folder."""
    url = GITHUB_REPO.format(owner=OWNER, repo=REPO, folder=FOLDER)
    response = requests.get(url, headers=HEADERS, timeout=15)

    if response.status_code == 200:
        return response.json() # Returns a list of files in the folder
    else:
        print(f"Failed to fetch files: {response.text}")
        return []

def upload_to_s3(file_url, file_name):
    """Downloads file from Github and uploads it to S3."""
    response = requests.get(file_url, headers=HEADERS)
    if response.status_code == 200:
        s3.upload_fileobj(BytesIO(response.content), BUCKET_NAME, file_name)
        print(f"uploaded {file_name} to S3 bucket {BUCKET_NAME}")
    else:
        print(f"Failed to download {file_name}: {response.text}")

def main():
    files = fetch_github_files()
    for file in files:
        if file["type"] == "file":
            file_url = file["download_url"]
            file_name = file["name"]
            upload_to_s3(file_url, file_name)

if __name__ == "__main__":
    main()
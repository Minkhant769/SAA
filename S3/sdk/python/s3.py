import boto3
import os
from botocore.exceptions import ClientError

# --- ANSI Color Codes for Terminal ---
GREEN = '\033[92m'
RED = '\033[91m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# --- UI Helper Function ---
def print_menu_table(title, options):
    """Draws a clean ASCII table for the menus."""
    print(f"\n{CYAN}+{'-'*50}+{RESET}")
    print(f"{CYAN}|{RESET} {title.center(48)} {CYAN}|{RESET}")
    print(f"{CYAN}+{'-'*50}+{RESET}")
    for num, text in options.items():
        row_text = f"{num}. {text}"
        print(f"{CYAN}|{RESET} {row_text.ljust(48)} {CYAN}|{RESET}")
    print(f"{CYAN}+{'-'*50}+{RESET}")

# ==========================================
#             BUCKET FUNCTIONS
# ==========================================
def create_bucket(bucket_name):
    region = "ap-southeast-1"
    try:
        s3_client = boto3.client('s3', region_name=region)
        location = {'LocationConstraint': region}
        s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
        print(f"\n{GREEN}[Success] Bucket '{bucket_name}' has been created in {region}.{RESET}")
    except ClientError as e:
        print(f"\n{RED}[Error] Error creating bucket: {e}{RESET}")

def list_buckets():
    s3_client = boto3.client('s3')
    try:
        response = s3_client.list_buckets()
        buckets = response.get('Buckets', [])
        if not buckets:
            print(f"\n{YELLOW}[Info] No buckets found in your account.{RESET}")
            return

        buckets.sort(key=lambda b: b['CreationDate'], reverse=True)
        print(f"\n{CYAN}--- Your S3 Buckets (Newest First) ---{RESET}")
        for i, bucket in enumerate(buckets):
            date_str = bucket['CreationDate'].strftime('%Y-%m-%d %H:%M:%S')
            print(f"  {i+1}. {bucket['Name']} (Created: {date_str})")
        print(f"{CYAN}{'-' * 40}{RESET}")
    except ClientError as e:
        print(f"\n{RED}[Error] Error listing buckets: {e}{RESET}")

def delete_bucket(bucket_name):
    s3_client = boto3.client('s3')
    try:
        s3_client.delete_bucket(Bucket=bucket_name)
        print(f"\n{GREEN}[Success] Bucket '{bucket_name}' has been deleted.{RESET}")
    except ClientError as e:
        if e.response['Error']['Code'] == 'BucketNotEmpty':
            print(f"\n{RED}[Error] Bucket '{bucket_name}' is not empty!{RESET}")
            print("   You must delete all objects inside it first.")
        else:
            print(f"\n{RED}[Error] Error deleting bucket: {e}{RESET}")

# ==========================================
#             OBJECT FUNCTIONS
# ==========================================
def upload_object(bucket_name, file_path, object_name):
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"\n{GREEN}[Success] File uploaded as '{object_name}' to '{bucket_name}'.{RESET}")
    except FileNotFoundError:
        print(f"\n{RED}[Error] The file '{file_path}' was not found on your local machine.{RESET}")
    except ClientError as e:
        print(f"\n{RED}[Error] Upload failed: {e}{RESET}")

def list_objects(bucket_name):
    s3_client = boto3.client('s3')
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        if 'Contents' not in response:
            print(f"\n{YELLOW}[Info] Bucket '{bucket_name}' is empty.{RESET}")
            return
            
        print(f"\n{CYAN}--- Objects in '{bucket_name}' ---{RESET}")
        for i, obj in enumerate(response['Contents']):
            size_kb = obj['Size'] / 1024
            print(f"  {i+1}. {obj['Key']} ({size_kb:.2f} KB)")
        print(f"{CYAN}{'-' * 40}{RESET}")
    except ClientError as e:
        print(f"\n{RED}[Error] Could not list objects: {e}{RESET}")

def delete_object(bucket_name, object_name):
    s3_client = boto3.client('s3')
    try:
        s3_client.delete_object(Bucket=bucket_name, Key=object_name)
        print(f"\n{GREEN}[Success] Object '{object_name}' deleted from '{bucket_name}'.{RESET}")
    except ClientError as e:
        print(f"\n{RED}[Error] Delete failed: {e}{RESET}")

# ==========================================
#               MENUS & ROUTING
# ==========================================
def bucket_menu():
    while True:
        options = {"1": "Create a new Bucket", "2": "List all Buckets", "3": "Delete a Bucket", "4": "Back to Main Menu"}
        print_menu_table("BUCKET MANAGER", options)
        choice = input("> Choose an option (1-4): ").strip()

        if choice == '1':
            name = input("\n[Input] Enter the new bucket name: ").strip()
            if name: create_bucket(name)
        elif choice == '2':
            list_buckets()
        elif choice == '3':
            name = input("\n[Input] Enter bucket name to DELETE: ").strip()
            if name: delete_bucket(name)
        elif choice == '4':
            break
        else:
            print(f"{RED}[Error] Invalid choice.{RESET}")

def object_menu():
    while True:
        options = {"1": "Upload File (Object)", "2": "List Objects in Bucket", "3": "Delete an Object", "4": "Back to Main Menu"}
        print_menu_table("OBJECT MANAGER", options)
        choice = input("> Choose an option (1-4): ").strip()

        if choice in ['1', '2', '3']:
            bucket_name = input("\n[Input] Enter the target Bucket name: ").strip()
            if not bucket_name:
                print(f"{RED}[Error] Bucket name is required.{RESET}")
                continue

            if choice == '1':
                file_path = input("[Input] Enter local file path (e.g. /tmp/test.txt): ").strip()
                object_name = input("[Input] Enter save name in S3 (e.g. test.txt): ").strip()
                if file_path and object_name: upload_object(bucket_name, file_path, object_name)
            elif choice == '2':
                list_objects(bucket_name)
            elif choice == '3':
                object_name = input("[Input] Enter Object Key (name) to DELETE: ").strip()
                if object_name: delete_object(bucket_name, object_name)
        elif choice == '4':
            break
        else:
            print(f"{RED}[Error] Invalid choice.{RESET}")

if __name__ == '__main__':
    while True:
        options = {"1": "Manage Buckets", "2": "Manage Objects", "3": "Exit Application"}
        print_menu_table("MAIN MENU: AWS S3 CLI", options)
        
        main_choice = input("> Choose an option (1-3): ").strip()
        
        if main_choice == '1':
            bucket_menu()
        elif main_choice == '2':
            object_menu()
        elif main_choice == '3':
            print(f"\n{YELLOW}[Info] Exiting System. Goodbye!{RESET}\n")
            break
        else:
            print(f"{RED}[Error] Invalid choice.{RESET}")
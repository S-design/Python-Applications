import os
import re

def get_cleaned_filenames(directory):
    # List all files in the directory
    filenames = os.listdir(directory)

    # Remove numbers from the filenames
    cleaned_filenames = set([re.sub(r'\d+', '', name) for name in filenames])

    return cleaned_filenames

def compare_directories(dir1, dir2):
    # Get cleaned filenames
    filenames_dir1 = get_cleaned_filenames(dir1)
    filenames_dir2 = get_cleaned_filenames(dir2)

    # Find common names and unique names in each directory
    common_names = filenames_dir1.intersection(filenames_dir2)
    unique_in_dir1 = filenames_dir1.difference(filenames_dir2)
    unique_in_dir2 = filenames_dir2.difference(filenames_dir1)

    return common_names, unique_in_dir1, unique_in_dir2

if __name__ == '__main__':
    dir1 = input("Enter the path of the first directory: ")
    dir2 = input("Enter the path of the second directory: ")

    common, unique1, unique2 = compare_directories(dir1, dir2)

    print("\nCommon filenames (without numbers):")
    print("\n".join(common))
    
    print("\nUnique filenames in first directory (without numbers):")
    print("\n".join(unique1))
    
    print("\nUnique filenames in second directory (without numbers):")
    print("\n".join(unique2))
    
import os

def rename_files(directory, prefix):
    try:
        # Ensure the directory exists
        if not os.path.exists(directory):
            print(f"Directory '{directory}' does not exist.")
            return

        # List all files in the directory
        files = os.listdir(directory)

        # Iterate through each file and rename it
        for filename in files:
            if os.path.isfile(os.path.join(directory, filename)):
                new_name = f"{prefix}_{filename}"
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
                print(f"Renamed '{filename}' to '{new_name}'")

        print("Renaming complete.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Specify the directory where the files are located
    directory_to_rename = "/path/to/your/directory"

    # Specify the prefix to add to the filenames
    new_prefix = "new_prefix"

    # Call the rename_files function
    rename_files(directory_to_rename, new_prefix)

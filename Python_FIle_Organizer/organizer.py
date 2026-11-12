import shutil
from pathlib import Path


# Locate the testing folder
folder = Path(__file__).parent / "Test_Files"


# Define file categories
file_categories = {

    ".pdf": "Documents",
    ".docx": "Documents",
    ".pptx": "Documents",
    ".txt": "Documents",
    ".xlsx": "Documents",

    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",

    ".mp4": "Videos",
    ".mov": "Videos",

    ".mp3": "Audio",
    ".wav": "Audio",

    ".zip": "Archives",
    ".rar": "Archives",

    ".py": "Code",
    ".js": "Code",
    ".html": "Code",
    ".css": "Code"
}


# Handle duplicate filenames
def get_unique_destination(destination):

    counter = 1

    while destination.exists():

        new_name = (
            f"{destination.stem}_{counter}"
            f"{destination.suffix}"
        )

        destination = destination.with_name(new_name)

        counter += 1

    return destination


# Initialize counters
moved = 0
skipped = 0
failed = 0


print("\n====================================")
print("       AUTOMATED FILE ORGANIZER")
print("====================================\n")


# Check whether the testing folder exists
if not folder.is_dir():

    print("Error: Testing folder does not exist.")

    raise SystemExit(1)


# Inspect every item inside the folder
for file in list(folder.iterdir()):

    if not file.is_file():

        if file.name not in set(file_categories.values()) | {"Others"}:
            skipped += 1

    continue

    try:

        # Identify the file extension
        extension = file.suffix.lower()

        # Determine its category
        category = file_categories.get(extension, "Others")

        # Create the destination folder
        category_folder = folder / category

        category_folder.mkdir(exist_ok=True)

        # Determine the destination path
        destination = category_folder / file.name

        # Prevent duplicate filenames
        destination = get_unique_destination(destination)

        # Move the file
        shutil.move(str(file), str(destination))

        moved += 1

        print(f"[SUCCESS] {file.name} -> {category}")

    except OSError as error:

        failed += 1

        print(f"[ERROR] Could not move {file.name}: {error}")


# Display execution summary
print("\n====================================")
print("       FILE ORGANIZATION REPORT")
print("====================================")

print(f"Files successfully moved: {moved}")
print(f"Files skipped: {skipped}")
print(f"Files failed: {failed}")

print("\nOrganization completed!")
print("====================================")
import errno
import os
import shutil
from datetime import datetime

from src.FileInfos import FileInfos

# TODO: Renaming "All" files formats doesn't work.
def mass_rename(
  affected_directory: str,
  string_to_remove: str,
  string_to_add: str,
  file_extension: str,
  delete_original_files: bool
):
  """Rename files in the specified directory.

  Args:
    affected_directory (str): The directory path where the files will be renamed.
    string_to_remove (str): The string to be removed from the file names.
    string_to_add (str): The string to be added to the file names.
    file_extension (str): The file extension to filter files. Use "Everything" to include all files.
    delete_original_files (bool): Flag to indicate whether to delete the original files.

  Returns:
    dict: A dictionary containing information about the renaming process. The dictionary has the following keys:
      - "original_files": A list of FileInfos objects representing the original files.
      - "new_files": A list of FileInfos objects representing the renamed files.
      - "errors": A list of any errors that occurred during the renaming process.
      - "current_timestamp": The current timestamp when the renaming process started.
      - "destination": The path to the directory where the renamed files are stored.

  Raises:
    FileNotFoundError: If the specified directory does not exist.
  """

  current_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

  infos = {
    "original_files": [],
    "new_files": [],
    "errors": [],
    "current_timestamp": current_timestamp,
    "destination": os.path.join(affected_directory.replace("/", "\\"), f".mass_rename_{current_timestamp}")
  }
  if not os.path.exists(affected_directory):
    raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), affected_directory)

  for current_file in os.listdir(affected_directory):
    current_file = FileInfos(os.path.join(affected_directory, current_file))
    
    if (current_file.extension == file_extension or file_extension == "Everything"):
      if string_to_remove in current_file.name :
        new_file = FileInfos(
          os.path.join(
            infos["destination"],
            current_file.name.replace(string_to_remove, string_to_add) + current_file.extension,
          )
        )
        infos["original_files"].append(current_file)
        infos["new_files"].append(new_file)

        try:
          os.makedirs(new_file.location, exist_ok=True)
          shutil.copyfile(os.path.abspath(current_file.path), new_file.path)
          if (delete_original_files):
            os.remove(current_file.path)
        except Exception as err:
          infos["errors"].append(err)

  return infos
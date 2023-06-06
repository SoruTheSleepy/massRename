import errno
import os
import shutil
from datetime import datetime

from src.FileInfos import FileInfos

def mass_rename(
  affected_directory: str,
  string_to_remove: str,
  string_to_add: str,
  file_extension: str,
  delete_original_files: bool
):
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
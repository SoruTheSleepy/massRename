import os

class FileInfos:
  def __init__(self, path):
    self.path = os.path.abspath(path)
    self.name = os.path.splitext(path)[0].split("\\")[-1].strip()
    self.location = os.path.abspath(path).rsplit("\\", 1)[0].strip()
    self.extension = os.path.splitext(path)[1].strip()
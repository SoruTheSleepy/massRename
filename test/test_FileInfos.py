import unittest
from src.FileInfos import FileInfos

class TestFileInfos(unittest.TestCase):
    def test_file_info(self):
        
        file_info = FileInfos("path/to/file.txt")

        self.assertEqual(file_info.path, "path/to/file.txt")
        self.assertEqual(file_info.name, "file")
        self.assertEqual(file_info.location, "path/to")
        self.assertEqual(file_info.extension, ".txt")

if __name__ == "__main__":
    unittest.main()
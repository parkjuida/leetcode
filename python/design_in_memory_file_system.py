from typing import List


class File:
    def __init__(self, file_name, contents):
        self.file_name = file_name
        self.contents = contents

    def add_content(self, contents):
        self.contents += contents

    def ls(self):
        return [self.file_name]

    def read_contents(self):
        return self.contents


class Directory:
    def __init__(self, dir_name):
        self.dir_name = dir_name
        self.file_list = {}
        self.child_dir = {}

    def make_child_dir(self, directory):
        if directory.dir_name in self.child_dir:
            return self.child_dir[directory.dir_name]

        self.child_dir[directory.dir_name] = directory
        return directory

    def make_file(self, file):
        self.file_list[file.file_name] = file

    def ls(self):
        contents = [*self.file_list.keys(), *self.child_dir.keys()]
        contents = sorted(contents)
        return contents


class FileSystem:
    def __init__(self):
        self.root_dir = Directory("")

    def ls(self, path: str) -> List[str]:
        current_dir = self.root_dir
        for dir_name in path.split("/"):
            if dir_name == "":
                continue
            if dir_name in current_dir.child_dir:
                current_dir = current_dir.child_dir[dir_name]
            if dir_name in current_dir.file_list:
                current_dir = current_dir.file_list[dir_name]

        return current_dir.ls()

    def mkdir(self, path: str) -> None:
        current_dir = self.root_dir
        for dir_name in path.split("/"):
            if dir_name != "":
                current_dir = current_dir.make_child_dir(Directory(dir_name))

    def addContentToFile(self, filePath: str, content: str) -> None:
        pathes = filePath.split("/")
        current_dir = self.root_dir
        for dir_name in pathes[:-1]:
            if dir_name != "":
                current_dir = current_dir.make_child_dir(Directory(dir_name))

        if pathes[-1] in current_dir.file_list:
            current_dir.file_list[pathes[-1]].add_content(content)
        else:
            current_dir.make_file(File(pathes[-1], content))

    def readContentFromFile(self, filePath: str) -> str:
        current_dir = self.root_dir
        pathes = filePath.split("/")
        for dir_name in pathes[:-1]:
            if dir_name != "":
                current_dir = current_dir.child_dir[dir_name]

        file = current_dir.file_list[pathes[-1]]
        return file.read_contents()


# Your FileSystem object will be instantiated and called as such:
fileSystem = FileSystem()
# print(fileSystem.ls("/"))
# print(fileSystem.mkdir("/a/b/c"))
# print(fileSystem.addContentToFile("/a/b/c/d", "hello world"))
# print(fileSystem.ls("/"))
# print(fileSystem.readContentFromFile("/a/b/c/d"))
# print(fileSystem.addContentToFile("/a/b/c/d", "hello hello world"))
# print(fileSystem.readContentFromFile("/a/b/c/d"))

print(fileSystem.mkdir("/goowmfn"))
print(fileSystem.mkdir("/goowmfn"))
print(fileSystem.ls("/"))
print(fileSystem.ls("/"))
print(fileSystem.mkdir("/z"))
print(fileSystem.ls("/"))
print(fileSystem.ls("/"))
print(fileSystem.addContentToFile("/goowmfn/c", "shetopcy"))
print(fileSystem.ls("/z"))
print(fileSystem.ls("/goowmfn/c"))
print(fileSystem.ls("/goowmfn"))
class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        file1=open(self.file_name)
        file_text = file1.read()
        print(file_text)
        file1.close()

    def update_file(self, text_data):
        file1=open(self.file_name, "a")
        file1.write(text_data)
        file1.close()


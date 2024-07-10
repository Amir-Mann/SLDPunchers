

class VCFLoader:
    def __init__(self, path):
        self.file = open(path, "r")
        self.meta_info = []
        self.headers = []

        while not self.headers:
            line = self.file.readline()
            if line[:2] == "##":
                self.meta_info.append(line)
                continue
            elif line[0] == "#" and line[1] != "#":
                self.parse_headers(line)
                break
            else:
                raise RuntimeError("Header not found")

    def parse_headers(self, headers_line):
        self.headers = tuple(headers_line[1:].strip().split("\t"))

    def get_next_entry(self):
        line = self.file.readline()
        if line == "":
            self.close()
            raise StopIteration
        parsed_line = line.strip().split("\t")
        return {header: value for header, value in zip(self.headers, parsed_line)}

    def __iter__(self):
        return self

    def __next__(self):
        return self.get_next_entry()

    def close(self):
        self.file.close()
        self.file = None


if __name__ == '__main__':
    loader = VCFLoader("sample.vcf")
    for entry in loader:
        print(entry)

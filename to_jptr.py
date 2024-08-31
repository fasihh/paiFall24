import os, sys, re, fnmatch as fm, nbformat as nbf, argparse

class Config:
    def __init__(self, config_file: str):
        self._config_file: str = config_file
        self._config: dict[str, str] | None = None
        self._run()

    def __getitem__(self, field: str) -> str | None:
        if self._config is None:
            return None
        return self._config[field]

    def _run(self) -> None:
        try:
            with open(self._config_file):
                pass
        except FileNotFoundError:
            config_data = self._get_init()
            self._config = dict(config_data)
            with open(self._config_file, 'w') as f:
                f.write('\n'.join([f"{data[0]}={data[1]}" for data in config_data]))
        else:
            with open(self._config_file, 'r') as f:
                self._config = dict(map(lambda x: x.split('='), f.read().rstrip().split('\n')))

    def _get_init(self) -> list[tuple[str, str]]:
        if self._config is not None:
            return

        print("Enter the path to the lab folder from root.\nExample: path/to/labs")
        while True:
            labs_path = input(">> ")
            if not os.path.isdir(labs_path):
                print("Invalid path")
                continue
            break

        print("Enter the sub-labs folder naming convention in regex form.")
        print("You may use this site to test your regex before entering (https://regex101.com)")
        while True:
            sub_labs_regex = input(">> ")
            try:
                re.compile(sub_labs_regex)
            except re.error:
                print("Invalid regex")
                continue
            break
        
        print("Enter the task files naming convention in regex form.")
        while True:
            file_regex = input(">> ")
            try:
                re.compile(file_regex)
            except re.error:
                print("Invalid regex")
                continue
            break


        return [
            ('labs_path', labs_path),
            ('sub_labs_regex', sub_labs_regex),
            ('file_regex', file_regex + '.py')
        ]


class Converter:
    def __init__(self, std_id: str, lab_no: str, config: Config):
        self._std_id: str = std_id
        self._lab_no: str = lab_no
        self._config: Config = config
        self._lab_dir: str = ""
        self._files_content: list[tuple[str, str]] = []
        self._run()

    def _set_lab_dir(self) -> None:
        for _, dirs, _ in os.walk(self._config['labs_path']):
            for i, dir in enumerate(fm.filter(dirs, self._config['sub_labs_regex'])):
                if int(self._lab_no)-1 != i:
                    continue
                self._lab_dir = os.path.join(self._config['labs_path'], dir)
                break

        if not self._lab_dir:
            raise ValueError(f"No matching directory found for lab number {self._lab_no}")

    def _read_file(self, file: str) -> str:
        with open(os.path.join(self._lab_dir, file), 'r') as f:
            return f.read().rstrip()

    def _create_notebook(self) -> None:
        notebook = nbf.v4.new_notebook()
        for file_name, content in self._files_content:
            notebook.cells.append(nbf.v4.new_markdown_cell(f"### {file_name.split('.')[0]}"))
            notebook.cells.append(nbf.v4.new_code_cell(content))

        output_file = os.path.join(self._lab_dir, f"{self._std_id}_{self._lab_no:0>2}.ipynb")
        with open(output_file, 'w') as f:
            nbf.write(notebook, f)
        print(f"Created notebook: {output_file}")

    def _run(self) -> None:
        self._set_lab_dir()
        for _, _, files in os.walk(self._lab_dir):
            for file in fm.filter(files, self._config['file_regex']):
                self._files_content.append((file, self._read_file(file)))
        self._create_notebook()

def main() -> None:
    if len(sys.argv)-1 < 2:
        print("Usage: py to_jptr.py <student_id> <lab_number>\nExample: python to_jptr.py 23K0727 1")
        print("\nAlso make sure this script is in the base directory", end='')
        exit()

    __, std_id, lab_no = sys.argv

    if not re.match(r'\d\d[K,k]\d\d\d\d', std_id):
        print("Invalid student ID")
        exit()

    Converter(std_id, lab_no, Config('jptr_config.ini'))

if __name__ == '__main__':
    main()

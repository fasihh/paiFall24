import os, sys, re
import nbformat as nbf

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
            with open('.gitignore', 'a') as f:
                f.write(f"\n{self._config_file}")
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
        
        print("Enter your student ID.")
        while True:
            student_id = input(">> ")
            if not re.match(r'\d\d[K,k]\d\d\d\d', student_id):
                print("Invalid student ID")
                continue
            break
    

        return [
            ('labs_path', labs_path),
            ('sub_labs_regex', sub_labs_regex),
            ('file_regex', file_regex + '.py'),
            ('student_id', student_id)
        ]


class Converter:
    def __init__(self, lab_no: str, config: Config):
        self._lab_no: str = lab_no
        self._config: Config = config
        self._lab_dir: str = ""
        self._files_content: list[tuple[str, str]] = []
        self._run()
    
    def _filter(self, data: list[str], pattern) -> list[str]:
        filtered_files = []
        for file in data:
            if re.search(pattern, file):
                filtered_files.append(file)
        return filtered_files


    def _set_lab_dir(self) -> None:
        for _, dirs, _ in os.walk(self._config['labs_path']):
            for i, dir in enumerate(self._filter(dirs, self._config['sub_labs_regex'])):
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

        output_file = os.path.join(self._lab_dir, f"{self._config['student_id']}_{self._lab_no:0>2}.ipynb")
        with open(output_file, 'w') as f:
            nbf.write(notebook, f)
        print(f"Created notebook: {output_file}")

    def _run(self) -> None:
        self._set_lab_dir()
        for _, _, files in os.walk(self._lab_dir):
            for file in self._filter(files, self._config['file_regex']):
                self._files_content.append((file, self._read_file(file)))
        self._create_notebook()

def main() -> None:
    if len(sys.argv)-1 < 1:
        print("Usage: py to_jptr.py <lab_number>\nExample: python to_jptr.py 1")
        print("\nAlso make sure this script is in the base directory", end='')
        exit()
    
    try:
        Converter(sys.argv[1], Config('jptr_config.ini'))
    except Exception as error:
        print(error)

if __name__ == '__main__':
    main()

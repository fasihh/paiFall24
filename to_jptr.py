import os, sys, re, fnmatch as fm, nbformat as nbf

if len(sys.argv)-1 < 2:
    print("Usage: py to_jptr.py <student_id> <lab_number>\nExample: python to_jptr.py 23K0727 1")
    print("\nAlso make sure this script is in the base directory", end='')
    exit()

__, std_id, lab_no = sys.argv

if not re.match(r'\d\d[K,k]\d\d\d\d', std_id):
    print("Invalid student ID")
    exit()

lab_dir = f"Labs\\{lab_no:0>2}"

def read_file(file):
    with open(f"{lab_dir}\\{file}", 'r') as f:
        return f.read().rstrip()
    
def create_notebook(files_content):
    notebook = nbf.v4.new_notebook()
    for file_name, content in files_content:
        formatted_name = re.findall(r'(\d\d)', file_name)[0]
        notebook.cells.append(nbf.v4.new_markdown_cell(f"### Q{formatted_name}"))
        notebook.cells.append(nbf.v4.new_code_cell(content))

    with open(f"{lab_dir}\\{std_id}_{lab_no:0>2}.ipynb", 'w') as f_out:
        nbf.write(notebook, f_out)

def main():
    files_content = []
    for _, _, files in os.walk(lab_dir):
        for file in fm.filter(files, "q[0-9][0-9].py"):
            files_content.append((file, read_file(file)))
    create_notebook(files_content)

if __name__ == '__main__':
    main()

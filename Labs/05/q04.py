class Student:
    def __init__(self, std_id, name):
        self.std_id = std_id
        self.name = name
    
    def info(self):
        print(f'Name: {self.name}', f'ID: {self.std_id}', sep='\n')
        
class Marks(Student):
    def __init__(self, std_id, name, marks):
        super().__init__(std_id, name)
        self.marks = marks
    
    def info(self):
        super().info()
        print('marks:')
        for subject in self.marks:
            print(f'\t{subject}: {self.marks[subject]}/100')
        
class Result(Marks):
    def __init__(self, std_id, name, marks):
        super().__init__(std_id, name, marks)
        
    def info(self):
        super().info()
        total = sum(self.marks[subject] for subject in self.marks)
        print(
            'result:',
            f'Total marks: {total}',
            f'Average marks: {total/len(self.marks)}',
            sep='\n'
        )

def main():
    res = Result(
        18,
        'fasih',
        {
            'oop': 86,
            'ew': 80,
            'mvc': 86,
            'irs': 80
        }
    )

    res.info()

if __name__ == '__main__':
    main()
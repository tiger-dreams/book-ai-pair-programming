import os

# Python 파일이 위치한 디렉토리로 작업 디렉토리 변경
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 이후의 코드는 새로운 작업 디렉토리에서 실행됩니다.

class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

def main():
    people = [
        MyClass("Alice", 25),
        MyClass("Bob", 30),
        MyClass("Charlie", 35),
    ]

    for person in people:
        person.print_info()

    print("Total people: ", len(people))

    with open('file.txt') as f:
        content = f.read()
        print("File content: ", content)

    x = lambda a, b: a + b
    print("Lambda result: ", x(5, 10))

if __name__ == "__main__":
    main()
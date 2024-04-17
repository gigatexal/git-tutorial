import os

def hello(name: str)->None:
    print(f'Hello {name}')

if __name__ == '__main__':
    print(hello(name=os.getenv('NAME', 'World')))


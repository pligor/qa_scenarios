from pathlib import Path

PROJECT_PATH = (Path(__file__).parent / Path('..')).resolve()

if __name__ == '__main__':
    print(PROJECT_PATH)

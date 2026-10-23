from .io_utils import load_tasks

def main():
    print("Running Week 2 package successfully!")

    tasks = load_tasks("members/dangquangminhkhtn/w2/sample.csv")

    for task in tasks:
        print(task)

if __name__ == "__main__":
    main()
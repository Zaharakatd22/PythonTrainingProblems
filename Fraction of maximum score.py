def main():
    students_results: list = input().split()
    print(f'{students_results.count("A") / len(students_results):.2f}')


if __name__ == '__main__':
    main()

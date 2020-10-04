from os.path import isdir, join
import os
import sys
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    file_extensions = os.environ["INPUT_FILEEXTENSIONS"].split(", ")
    print(f"File extensions to count: {file_extensions}")

    total_words = count_words_in_files(".", file_extensions)

    print(f"::set-output name=myOutput::{total_words}")
    sys.exit(0)


def count_words_in_files(directory, file_extensions_to_count):
    total_words = 0
    for file in os.listdir(directory):
        if isdir(join(directory, file)):
            total_words += count_words_in_files(f"{directory}/{file}/",
                                                file_extensions_to_count)
        elif file_should_be_counted(file, file_extensions_to_count):
            print(f"File {file} should be counted")
            total_words += count_words_in_file(join(directory, file))
    return total_words


def file_should_be_counted(file, file_extensions_to_count):
    file_extension = os.path.splitext(file)[1]
    return file_extension in file_extensions_to_count


def count_words_in_file(file_path):
    with open(file_path, encoding="utf-8") as file:
        return len(file.read().split())


if __name__ == "__main__":
    main()

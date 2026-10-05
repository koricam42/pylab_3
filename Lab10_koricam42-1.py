"""
Program Name: Word Analyzer
Author: Jordan Mensah
Purpose: OOP Program that reads a selected text file and analyzes its contents.
Starter Code (References):
    - Lab Instructions: https://courses.cscc.edu/ultra/courses/_238744_1/assessment/_28741602_1/attempt/create?courseId=_238744_1
    - Pathlib Module: https://www.geeksforgeeks.org/python/pathlib-module-in-python/
    - String Spacing: https://www.geeksforgeeks.org/python/fill-a-python-string-with-spaces/
    - File I/O: https://learning.oreilly.com/library/view/python-crash-course/9781098156664/c10.xhtml#h1-502703c10-0005
    - Translation Tables: https://www.pythonforbeginners.com/basics/translation-table-in-python
    - UTF-8-SIG Stuff: https://stackoverflow.com/questions/57152985/what-is-the-difference-between-utf-8-and-utf-8-sig
Date:9/30/26
"""

import pathlib
import string


class WordAnalyzer:
    """
    Class to process text files, remove punctuation, change case, 
    and tally the frequency of each word
    """
    def __init__(self, filepath: pathlib.Path | str) -> None:
        """
        Initalizes the WordAnalyzer with a filepath and empty dictionary for frequencies.

        Args:
            filepath (pathlib.Path | str): The path to the text file to be analyzed.
        """
        self.__filepath = pathlib.Path(filepath)
        self.__frequencies: dict[str, int] = {}
    def process_file(self) -> bool:
        """
        Reads the file, removes punctuation, converts to lowercase, and counts word frequencies.

        Raises:
            FileNotFoundError: Error that indicates that the file was not found.

        Returns:
            bool: True if the file was successfully processed, False if a FileNotFoundError occured.
        """
        try:
            if self.__filepath.exists():
                
                translator = str.maketrans('', '', string.punctuation)

                with self.__filepath.open('r', encoding='utf-8-sig') as file:

                    for line in file:

                        cleaned_line = line.translate(translator).lower()

                        split_line = cleaned_line.split()


                        for word in split_line:
                            if word in self.__frequencies:
                                self.__frequencies[word] += 1
                            else:
                                self.__frequencies[word] = 1
                
                return True
            
            else:
                raise FileNotFoundError
        
        except FileNotFoundError:
            print(f"Error: File {self.__filepath} not found.")
            return False
        
    def print_report(self) -> None:
        """
        Sorts tallied words alphabetically and prints a report
        """
        sorted_words = sorted(self.__frequencies.keys())

        for words in sorted_words:

            print(f'{words:<15} :: {self.__frequencies[words]}')

def main() -> None:
    """
    Main function that displays the menu, handles user input, and executes the WordAnalyzer logic.
    """
    file_dict: dict[str, pathlib.Path] = {
            '1': pathlib.Path('princess_mars.txt'),
            '2': pathlib.Path('Tarzan.txt'),
            '3': pathlib.Path('treasure_island.txt'),
            '4': pathlib.Path('monte_cristo.txt')
        }

    while True:
        print("Word Analyzer")
        print("Please select a file to analyze:")

        for key in file_dict:
            print(f"{key}. {file_dict[key].stem.replace('_', ' ').title()}")
        
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Goodbye.")
            break
        elif choice in file_dict:
            choice_file = file_dict[choice]

            print(f"\nProcessing {choice_file.name}...\n")
            analyzer = WordAnalyzer(choice_file)
            if analyzer.process_file():
                analyzer.print_report()

        else:
            print("Invalid choice. Please select from options 1-5.")
            
        input("\nPress enter to return to the main menu.")

main()
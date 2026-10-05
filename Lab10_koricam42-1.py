"""
Program Name: Word Analyzer
Author: Jordan Mensah
Purpose: OOP Program that reads a selected text file and analyzes its contents.
Starter Code (References):
    - Lab Instructions: https://courses.cscc.edu/ultra/courses/_238744_1/assessment/_28741602_1/attempt/create?courseId=_238744_1
Date:9/30/26
"""

import pathlib
import string


class WordAnalyzer:
    def __init__(self, filepath):
        self.__filepath = pathlib.Path(filepath)
        self.__frequencies = {}
    def process_file(self):
        try:
            if self.__filepath.exists():
                
                translator = str.maketrans('', '', string.punctuation)

                with self.__filepath.open('r', encoding='utf-8') as file:

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
        
    def print_report(self):
        sorted_words = sorted(self.__frequencies.keys())

        for words in sorted_words:

            print(f'{words} :: {self.__frequencies[words]}')

def main():
    file_dict = {
            '1': pathlib.Path('princess_mars.txt'),
            '2': pathlib.Path('Tarzan.txt'),
            '3': pathlib.Path('treasure_island.txt'),
            '4': pathlib.Path('monte_cristo.txt')
        }

    while True:
        print("Word Analyzer")
        print("Please select a file to analyze:")

        for key in file_dict:
            print(f'{key}. {file_dict[key].stem}')
        
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Goodbye.")
            break
        elif choice in file_dict:
            choice_file = file_dict[choice]

            analyzer = WordAnalyzer(choice_file)
            if analyzer.process_file():
                analyzer.print_report()
        else:
            print("Invalid choice. Please select from options 1-5.")
            input("Press enter to return to the main menu.")

main()
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
                pass
                return True
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            print(f"Error: File {self.__filepath} not found.")
            return False

def main():


    while True:
        print("Word Analyzer")
        print("Please select a file to analyze:")
        print("1.")
        print("2.")
        print("3.")
        print("4.")

        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass    
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        else:
            print("Invalid choice. Please select from options 1-5.")
            input("Press enter to return to the main menu.")


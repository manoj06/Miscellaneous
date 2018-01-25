/*************************************************************************
* 
* File:     anagram.C
* Author:   Tim Nevaker
* Class:    CMSC 443
* Date:     May 4, 2000
*
* Compilation:
* CC -o anagram anagram.C
*
* Usage:
* anagram [-o output-file] [-d dictionary-file] [-l minimum-word-size]
*
* Description:
* This program takes a word and produces as many anagrams as possible.
* The program uses a dictionary file of words, one word per line, as 
* the possible words from which the anagrams are formed. The default
* dictionary file is dictionary.txt, which contains approximately
* 27,000 words. A different dictionary file can be specified at the
* command prompt, using the -d "dictionary-file" option.
* The anagrams produced are printed to a text file, one anagram per
* line. The output file may be specified at the command prompt using
* the -o "output-file" option, or else the user will be prompted for
* the name of the output file from within the program.
* Additionally, the user may limit the choice of words considered for
* the anagrams using the -l "minimum-word-size" option. A number after
* the -l flag indicates the minimum length of any word in the anagram.
*
* Implementation:
* The program loads the dictionary file into memory in an array. Dynamic
* memory allocation is used to ensure that no more memory is used than 
* is needed to store the words. After the user enters the word to be
* anagrammed, the program first creates a "working dictionary" by 
* filtering out any words that cannot be contained within the input
* text. Words that are longer than the input text, or are shorter than
* the user-specified minimum length are discarded, as are words that
* contain more of a particular letter than the input text.
* After filtering, the working dictionary is then sorted by word-length,
* with longer words at the top and shorter words at the bottom. Due to
* the way the anagrams are created, this sorting order ensures that
* anagrams with the longest words appear at the top of the list of 
* anagrams.
* The findAnagrams() function is a recursive function that operates in
* the following manner. The functions finds the first word in the
* working dictionary that is contained within the input text. It then
* calls itself recursively, to anagram the remaining letters of the
* input text. One base case of the recursion occurs when all the letters
* of the input text have been used, which indicates that an anagram has
* been found. In this case, the anagram is printed to the output file.
* The other base case occurs when the working dictionary is exhausted 
* of potential words, but not all letters of the input text have been
* used. This indicates a dead end in the anagramming process, in which
* case the recursion returns without printing, and a new recursion is
* begun. The current anagram is stored in a local string variable that
* is passed down the recursion, and appended to until the final anagram
* is produced and printed. The recursion uses a reference to an index
* of the working dictionary to keep track of its position in the 
* working dictionary throughout the recursive process. This guarantees
* that multiple instances of the same anagram are not produced.
*
*************************************************************************/
#include <stdio.h>
#include <iostream.h>
#include <stdlib.h>
#include <fstream.h>
#include <string.h>
#include <ctype.h>

// Global constants
const int MaxWordLength = 256;

// Global variables
long wordcount = 0;
long dictSize  = 0;
char **dictionary;
char **workingDict;
ofstream out;

// Function prototypes
bool initializeDict(const char *dictFile);
void findAnagrams(char *str, int alphaCount[26], int &dictPtr, unsigned int letterCount);
int  charcmp(const void *c1, const void *c2);
int  sizecmp(const void *s1, const void *s2);
int  alphalen(const char *str);
void strupper(char *str);
void emptyDict();

int main(int argc, char *argv[])
{
    // Program defaults
    const char *DefaultDict = "dictionary.txt";

    // Initialize the dictionary arrays
    char *dictFile = (char *) DefaultDict;
    char *outFile = NULL;
    int  minWordSize = 1;
    int  i = 0;

    // Parse command-line arguments
    if (argc > 1)
    {
        for (i = 1; i < argc; i++)
        {
            if (strcmp(argv[i], "-d") == 0)
                dictFile = argv[i+1];
            else if (strcmp(argv[i], "-o") == 0)
                outFile = argv[i+1];
            else if (strcmp(argv[i], "-l") == 0)
                minWordSize = atoi(argv[i+1]);
        }
    }

    // Initialize dictionary
    if ( !initializeDict(dictFile) )
    {
        cerr << "Error: Could not initialize dictionary" << endl;
        exit(1);
    }

    // Prompt user for output file
    char buffer[MaxWordLength];

    if (outFile == NULL)
    {
        cout << "Enter the name of the output file: ";
        cin.getline(buffer, MaxWordLength);
        outFile = new char[strlen(buffer) + 1];
        strcpy(outFile, buffer);
    }

    // Open output stream for file output
    out.open(outFile);

    // Prompt user for input word/phrase
    cout << "Enter word or phrase to anagram: ";
    cin.getline(buffer, MaxWordLength);
    strupper(buffer);

    // Store count of characters in an array for use in anagramming
    int  alphaCount[26];
    int  letterCount = 0;
    unsigned int j = 0;
    for (i = 0; i < 26; i++)
        alphaCount[i] = 0;

    for (j = 0; j < strlen(buffer); j++)
    {
        if ( isalpha(buffer[j]) )
        {
            alphaCount[buffer[j] - 'A']++;
            letterCount++;
        }
    }

    // Filter unusable words; store remainder in working dictionary
    char tempAlphaCount[26];
    bool possibleWord;

    workingDict = new char * [wordcount];
    dictSize = 0;
    
    for (i = 0; i < wordcount; i++)
    {
        // Do not use words that are longer than the input string
        // or that are shorter than the minimum word size the user specifies
        if (alphalen(dictionary[i]) > letterCount || 
            alphalen(dictionary[i]) < minWordSize)
                continue;

        // Count individual letters in the word
        possibleWord = true;

        for (j = 0; j < 26; j++)
            tempAlphaCount[j] = 0;

        for (j = 0; j < strlen(dictionary[i]); j++)
        {
            if ( isalpha(dictionary[i][j]) )
                tempAlphaCount[dictionary[i][j] - 'A']++;
        }

        // Do not use words that have more of a particular letter
        // than is in the input string
        for (j = 0; j < 26; j++)
        {
            if (tempAlphaCount[j] > alphaCount[j])
                possibleWord = false;
        }

        // If the word is a candidate word, store in working dictionary
        if (possibleWord)
        {
            workingDict[dictSize] = new char[strlen(dictionary[i]) + 1];
            strcpy(workingDict[dictSize], dictionary[i]);
            dictSize++;
        }
    }

    // Sort working dictionary by size
    qsort(workingDict, dictSize, sizeof(workingDict[0]), sizecmp);

    // Find and print anagrams to file
    int  dictPtr = 0;
    char anagram[MaxWordLength] = "";

    cout << "Saving anagrams to file " << outFile << "..." << endl;
    findAnagrams(anagram, alphaCount, dictPtr, letterCount);

    // Free dictionary memory and clean up code
    out.close();
    emptyDict();

    return 0;
}

// Function: initalizeDict
// Parameters:  dictFile - name of textfile containing words to be used
//                  in dictionary
// Returns: true if initialization succeeds; false otherwise

bool initializeDict(const char *dictFile)
{
    cout << "Initializing the dictionary..." << endl << endl;

    // Open dictionary file for input
    ifstream fin(dictFile, ios::in | ios::nocreate);

    // Determine number of words in dictionary file, and allocate
    // memory for dictionary and alphaDict
    wordcount = 0;
    char buffer[MaxWordLength];
    fin.getline(buffer, MaxWordLength);
    while (strlen(buffer) > 0)
    {
        wordcount++;
        fin.getline(buffer, MaxWordLength);
    }
    fin.close();

    dictionary = new char * [wordcount];

    // Read in words from dictionary file and store in dictionary
    fin.open(dictFile);

    int i;
    for (i = 0; i < wordcount; i++)
    {
        fin.getline(buffer, MaxWordLength);
        strupper(buffer);
        dictionary[i] = new char[strlen(buffer) + 1];
        strcpy(dictionary[i], buffer);
    }
    fin.close();

    return true;
}

// Function: findAnagrams
// Recursively find anagrams for a given word/phrase
// Parameters:  str - string to store anagram in
//              alphaCount - array of letters that remain to be anagrammed
//              dictPtr - reference to index into the working dictionary
//              letterCount - total number of remaining letters to anagram

void findAnagrams(char *str, int alphaCount[26], int &dictPtr, unsigned int letterCount)
{
    // If dictPtr exceeds the size of the dictionary, an anagram cannot
    // be formed; return false
    if (dictPtr >= dictSize)
        return;

    // Make a copy of alphaCount and anagram
    int tempAlphaCount[26];
    unsigned int i, j;
    int tempPtr = dictPtr;
    char anagram[MaxWordLength];

    // Find the next word in the working dictionary that is contained 
    // in the input text
    for ( ; dictPtr < dictSize; dictPtr++)
    {
        // Initialize temporary and local variables in loop
        tempPtr = dictPtr;
        char ch;
        int tempLetterCount = letterCount;
        bool matchFound = true;

        for (i = 0; i < 26; i++)
            tempAlphaCount[i] = alphaCount[i];
        strcpy(anagram, str);

        // Count characters to determine if word can be formed
        // from remaining letters
        for (i = 0; i < strlen(workingDict[tempPtr]); i++)
        {
            ch = workingDict[tempPtr][i];
            if ( isalpha(ch) )
            {
                tempAlphaCount[ch - 'A']--;
                tempLetterCount--;

                // If the count for a particular character falls below 0,
                // the word cannot be formed from the remaining letters
                if (tempAlphaCount[ch - 'A'] < 0)
                {
                    // Restore temporary variables and end loop
                    matchFound = false;
                    tempLetterCount = letterCount;
                    for (j = 0; j < 26; j++)
                        tempAlphaCount[j] = alphaCount[j];
                    break;
                }
            }
        }

        // Only recurse if a matching word is found
        if (matchFound)
        {
            // Add the matched word to the anagram string
            if (strlen(anagram) > 0)
                strcat(anagram, " ");
            strcat(anagram, workingDict[tempPtr]);

            // If all the letters are used up, print the anagram
            if (tempLetterCount == 0)
            {
                out << anagram << endl;
            }
            // Otherwise, recurse to find more words for anagram
            else
            {
                for (tempPtr++; tempPtr < dictSize; tempPtr++)
                {
                    // Find the next word that is not too long
                    if (alphalen(workingDict[tempPtr]) > tempLetterCount)
                        continue;

                    // Find anagrams of the remaining letters
                    findAnagrams(anagram, tempAlphaCount, tempPtr, tempLetterCount);
                }
            }
        }
    }
}

// Function: charcmp
// Purpose:  for use by quicksort(), to sort the letters of a string
//           in alphabetical order
// Parameters:  c1, c2 - chars to be compared
// Returns:  int value representing difference between char's

int charcmp(const void *c1, const void *c2)
{
    return (*(char *)c1 - *(char *)c2);
}

// Function: sizecmp
// Purpose:  for use by quicksort(), to sort the strings in the
//           dictionary by size, largest to smallest
// Parameters:  s1, s2 - strings to be compared
// Returns:  int value representing difference between string sizes

int sizecmp(const void *s1, const void *s2)
{
    return ( alphalen(*(char **)s2) - alphalen(*(char **)s1) );
}

// Function: alphalen
// Calculate the alphabetic length of the string
// Parameters:  str - the string to be examined
// Returns:  the number of alphabetic characters in a string

int  alphalen(const char *str)
{
    unsigned int i = 0;
    int alphaCount = 0;

    for (i = 0; i < strlen(str); i++)
    {
        if ( isalpha(str[i]) )
            alphaCount++;
    }

    return alphaCount;
}

// Function: strupper
// Converts a string to all uppercase letters
// Parameters:  str - the string to be converted

void strupper(char *str)
{
    for (unsigned int i = 0; i < strlen(str); i++)
    {
        if ( isalpha(str[i]) )
            str[i] = toupper(str[i]);
    }
}

// Function: emptyDict
// Purpose:  Free dynamic memory allocated to dictionary arrays

void emptyDict()
{
    int i = 0;

    for (i = 0; i < wordcount; i++)
        delete [] dictionary[i];

    for (i = 0; i < dictSize; i++)
        delete [] workingDict[i];

    delete [] dictionary;
    delete [] workingDict;
}


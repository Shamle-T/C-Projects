#include <iostream>
#include <windows.h>

using namespace std;

int main() {
    //Seeding the random generator
    srand(static_cast<unsigned int>(time(0)));

    //Declare Variables
    string userChoice;
    int pcScore = 0;
    int userScore = 0;
    string choices[3] = {"rock","paper","scissor"};
    int computerChoice;

    //Welcome flag
    cout << "Welcome to the Rock Paper Scissors game !!" << endl;

    //Start of loop to begin the game
    while (true) {
        //Display choices
        cout << "Enter your choice or 'exit'" << endl << "---------------" << endl << "Rock | Paper | Scissor : ";
        cin >> userChoice;

        //Converting all input to lowercase for accuracy
        for (char &c : userChoice) {
            c = tolower(c);
        }

        //Exit condition check
        if (userChoice == "exit")
            break;

        //Generate PC choice using rand
        computerChoice = rand()%3;
        string computerChoiceString = choices[computerChoice];

        //Checking if the user choice is valid
        if (userChoice != "rock" && userChoice != "paper" && userChoice != "scissors") {
            cout << "Invalid choice entered. Please enter rock paper or scissor";
            continue;
        }
        cout << "Computer Choice --> "<< computerChoiceString << endl;

        //Program Logic
        if ((userChoice == "rock" && computerChoiceString ==  "scissor") || (userChoice == "paper" && computerChoiceString ==  "rock") || (userChoice == "scissor" && computerChoiceString ==  "paper")) {
            cout << "You WIN !" <<endl;
            userScore++;
            }
        else if ((userChoice == "rock" && computerChoiceString=="paper") || (userChoice== "paper" && computerChoiceString == "scissor" )||(userChoice=="scissor" && computerChoiceString == "rock")) {
            cout << "You LOSE !" <<endl;
            pcScore++;
            }
        else {
            cout << "The game is a DRAW !" << endl;
            }

    }
    //Disaply the results
    cout << endl << "Scores" << endl << "-------" << endl << "User Score:" << userScore << " | " << "Pc Score:" << pcScore << endl;
    Sleep(1000);
    cout << "Closing program ..." ;
    return 0;
}

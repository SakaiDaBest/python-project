#include <iostream>
#include <sqlite3.h>
#include <stdio.h>
using namespace std;

static void clearScreen();
static int getValidInt();
static int createDB(const char* s);
static int createTable(const char* s);
static int InsertData(const char* s);
static int selectData(const char* s);
static int callback(void* NotUsed, int argc, char** argv, char** azColName);
static int updateData(const char* s);

int main() {
    const char* dir = "C:\\Users\\Wei Jun\\Documents\\DataBase.db";  // Use your actual username
    sqlite3* DB=nullptr;

    createDB(dir);
    createTable(dir);

    while (true) {
        clearScreen();
        cout << "Welcome to Secure Password Manager" << endl;
        cout << "1. Add new credentials\n";
        cout << "2. View stored credentials\n";
        cout << "3. Update credentials\n";
        cout << "4. Delete credentials\n";
        cout << "5. Change master password\n";
        cout << "6. Exit\n";
        cout << "Enter your choice: \n";
        int ans = getValidInt();
        while (ans < 1 || ans>6) {
            cout << "Please Insert a Valid Option" << endl;
            int ans = getValidInt();
        }
        if (ans == 1) {
            clearScreen();
            InsertData(dir);
        }
        else if (ans == 2) {
            clearScreen();
            selectData(dir);
            string b;
            cin >> b;
        }
        else if (ans == 3) {
            clearScreen();
            selectData(dir);
            updateData(dir);
        }
        else if (ans == 4) {

        }
        else if (ans == 5) {
            break;
        }
    }
    return 0;
}

static void clearScreen() {
#ifdef _WIN32
    system("cls");
#else
    system("clear");
#endif
}

static int updateData(const char* s) {
    sqlite3* DB;
    char* messageError;
    int exit = sqlite3_open(s, &DB);
    string ID;
    cout << "Enter ID: " << endl;
    cin >> ID;
    string password;
    cout << "Enter New Password: " << endl;
    cin >> password;


    string sql("UPDATE PASSWORDS SET PASSWORD = '" + password + "' WHERE ID ='" + ID + "'");

    exit = sqlite3_exec(DB, sql.c_str(), NULL, 0, &messageError);
    if (exit != SQLITE_OK) {
        cerr << "Error Insert" << endl;
        sqlite3_free(messageError);
    }
    else {
        cout << "Records created Successfully"<<endl;
    }
    return 0;
    
}

static int getValidInt() {
    int value;
    while (true) {
        cin >> value;
        if (cin.fail()) {
            cin.clear(); // Clear error state
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Discards invalid input
            cout << "Invalid input. Please enter a valid number: ";
        }
        else {
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Clear extra input
            return value;
        }
    }
}

static int selectData(const char* s) {
    sqlite3* DB;
    int exit = sqlite3_open(s, &DB);
    string sql = "SELECT * FROM PASSWORDS;";
    sqlite3_exec(DB, sql.c_str(), callback, NULL, NULL);
    return 0;
}

//argc = number of results, azColName = each column returned in array, argv = each value
static int callback(void* NotUsed, int argc, char** argv, char** azColName) {
    for (int i = 0; i < argc; i++) {
        cout << azColName[i] << ": " << (argv[i] ? argv[i] : "NULL") << endl; 
    }
    cout << endl;
    return 0;
}

static int InsertData(const char* s) {
    sqlite3* DB;
    char* messageError;
    int exit = sqlite3_open(s, &DB);
    string program;
    cout << "Please Insert Program Name" << endl;
    cin >> program;
    string username;
    cout << "Please Insert your Username" << endl;
    cin >> username;
    string password = "";
    while (password.length() < 8) {
        cout << "Please Insert your Password (Must have at least 8 characters)" << endl;
        cin >> password;
    }
    string sql("INSERT INTO PASSWORDS (PROGRAM, USERNAME, PASSWORD) VALUES('" + program + "', '" + username + "', '" + password + "');");
    exit = sqlite3_exec(DB, sql.c_str(), NULL, 0, &messageError);
    if (exit != SQLITE_OK) {
        cerr << "Error Insert" << endl;
        sqlite3_free(messageError);
    }
    else {
        cout << "Records created successfully" << endl;
    }
    return 0;
}

static int createDB(const char* s) {
    sqlite3* DB;
    int exit = sqlite3_open(s, &DB);
    if (exit != SQLITE_OK) {
        cerr << "Error opening database: " << sqlite3_errmsg(DB) << endl;
        sqlite3_close(DB);
        return exit; // Exit if the database failed to open
    }

    return 0;
}

static int createTable(const char* s) {
    sqlite3* DB;

    string sql = "CREATE TABLE IF NOT EXISTS PASSWORDS ("
        "ID INTEGER PRIMARY KEY, "
        "PROGRAM TEXT NOT NULL, "
        "USERNAME TEXT NOT NULL, "
        "PASSWORD TEXT NOT NULL );";


    try {
        int exit = 0;
        exit = sqlite3_open(s, &DB);

        char* messageError;
        exit = sqlite3_exec(DB, sql.c_str(), NULL, 0, &messageError);

        if (exit != SQLITE_OK) {
            cerr << "Error Create Table: " << (messageError ? messageError : "Unknown error") << endl;
            if (messageError) sqlite3_free(messageError);  // Free only if allocated
        }
        else {
            cout << "Table created Successfully" << endl;
        }
        sqlite3_close(DB);
    }
    catch (const exception& e) {
        cerr << e.what();
    }
    return 0;
}
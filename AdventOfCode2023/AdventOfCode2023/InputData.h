#pragma once
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

class InputData
{
public:

	InputData(string pathToFile, bool readAsInt = false)
	{
		string line;
		ifstream myfile(pathToFile);
		if (myfile.is_open())
		{
			while (getline(myfile, line))
			{
				if (readAsInt)
				{
					if (line != "")
						LinesAsInt.push_back(stoi(line));
					else
						LinesAsInt.push_back(0);
				}
				else
				{
					LinesAsText.push_back(line);
				}
			}
			myfile.close();
		}
		else
		{
			cout << "Unable to open file";
		}
	}
	void Print()
	{
		for (auto line : LinesAsInt)
		{
			cout << line << '\n';
		}
	}

	vector<int> LinesAsInt;
	vector<string> LinesAsText;
};


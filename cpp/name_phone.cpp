#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(const pair <string, string>&a, const pair <string, string>&b) {

	return a.first < b.first;
}

int main(int argc, char ** argv) {
	vector<pair<string, string>> name_phone;
	string line,name, phone;

	ifstream file("name_phone.txt");
	if(file.fail()){
		cout << "failed to open file" << endl;
		return 0;
	}
	getline(file, line);
	
	
	while (!file.eof()) {
		vector <string> str_line;
		getline(file, line);
		char temp[30];
		strcpy(temp, line.c_str());
		char * fline = strtok(temp, ":");
		while (fline != nullptr)
		{
			string after_strip = fline;
			after_strip.erase(remove(after_strip.begin(), after_strip.end(), ' '), after_strip.end());
			str_line.push_back(after_strip);
			fline = strtok(nullptr,"");
		}
		name = str_line[0];
		phone = str_line[1];
		name_phone.push_back(make_pair(name, phone));
	}
	file.close();
	cout << "---------------------------------------------------------------------before sorting 정렬 전---------------------------------------------------------------" << endl;
	for (int i = 0; i < name_phone.size(); i++) {
		cout << "this is " << i << "th line of name_phone.txt "<< endl << "name " << name_phone[i].first << " phone " << name_phone[i].second << endl;
	}
	cout << endl << endl;
	cout << "---------------------------------------------------------------------after sorting 정렬 후---------------------------------------------------------------" << endl;
	sort(name_phone.begin(), name_phone.end(), compare);
	for (int i = 0; i < name_phone.size(); i++) {
		cout << "this is " << i << "th line of name_phone.txt " << endl << "name " << name_phone[i].first << " phone " << name_phone[i].second << endl;
	}
	ofstream outfile("name_phone.csv");
	for (int i = 0; i < name_phone.size(); i++) {
		outfile << name_phone[i].first << "," << name_phone[i].second << endl;
	}
	outfile.close();
	return 0;
}
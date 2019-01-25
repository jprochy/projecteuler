// 28_NumberSpiralDiagonals.cpp : Defines the entry point for the console application.
// 
//Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows :
//21 22 23 24 25
//20  7  8  9 10
//19  6  1  2 11
//18  5  4  3 12
//17 16 15 14 13
//It can be verified that the sum of the numbers on the diagonals is 101.
//What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way ?


#include <iostream>
using namespace std;

int main() {

	setlocale(LC_ALL, "Czech_Czech Republic.1250");

	long int suma = 1;
	int z = 1;
	int DELKASTRANY = 1001;

	for (int prumer = 3; prumer <= DELKASTRANY; prumer = prumer+2)
		for (int i = 1; i <= 4; i++) {
			z = z + (prumer - 1);
			suma = suma + z;
		}
	
	cout << "Souèet: " << suma << "\n";
}
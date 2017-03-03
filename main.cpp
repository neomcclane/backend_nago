#include <iostream>

using manespace std;

class A {
	public:
	A();
	virtual ~A();
}

A::A() {
	cout << "constructor" << endl;
}

A::~A() {
	cout << "destructor" << endl;
}

int main() {
	

	return 0;
}
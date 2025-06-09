#include <iostream>
 
class Employee
{
public:
 virtual void Print() = 0;
 virtual ~Employee();
};
 
 
class President : public Employee
{
public:
 void Print() { std::cout << "I'm a President\n"; }
 virtual ~President();
};
 
 
class Manager : public Employee
{
public:
 void Print() { std::cout << "I'm a Manager\n"; }
 virtual ~Manager();
};
 
 
class Worker : public Employee
{
public:
 void Print() { std::cout << "I'm a Worker\n"; }
 virtual ~Worker();
};
 
 
int main()
{
 Employee* emp[3];
 emp[0] = new President;
 emp[1] = new Manager;
 emp[2] = new Worker;
 for(int i = 0; i < 3; ++i) 
  emp[i]->Print();
}

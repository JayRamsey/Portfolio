#include <iostream>
#include <string.h>

using namespace std;


class LinkedListNode {
    public:
        int data;
        LinkedListNode* next = nullptr;

        LinkedListNode(int _data) {
            data = _data;
        }

        ~LinkedListNode() {
            
        }
};


class LinkedList {


    private:
        
        LinkedListNode* head;
        int length;

        bool checkIndex(int index) {
            bool result = (0 <= index && index < length);
            if (!result) {
                throw out_of_range("Index out of range...");
            }
            return result;
        }

    public:
    
        LinkedList() {
            length = 0;
            head = nullptr;
        }

        ~LinkedList() {
            clear();
        }

        void append(int data) {
            LinkedListNode* newNode = new LinkedListNode(data);
            if (head == nullptr) {
                head = newNode;
            }else {
                LinkedListNode* current = head;
                while (current->next != nullptr) {
                    current = current->next;
                }
                current->next = newNode;
            }
            length++;
            cout << "Appended " << data << " --> ";
            print();
        }

        int get(int index) {
            checkIndex(index);
            LinkedListNode* current = head;
            for (int i = 1; i <= index; i++)
            {
                current = current->next;
            }
            int data = current->data;
            cout << "Fetched " << data << " --> ";
            print();
            return data;
        }

        void remove(int index) {
            if (index == 0 && head != nullptr) {
                head = head->next;
            }else if (checkIndex(index)) {
                
                LinkedListNode* last;
                LinkedListNode* current = head;

                for (int i = 0; i < index; i++) {
                    last = current;
                    current = current->next;
                }
                last->next = current->next;
                delete current;
            }
            length--;
            cout << "Removed index " << index << " --> ";
            print();
        }

        int pop() {
            int data;
            if (head == nullptr) {
                throw out_of_range("Cannot pop from empty list...");
            
            } else if (head->next == nullptr) {
                data = head->data;
                    head = nullptr;
            
            }else {
                LinkedListNode* previous;
                LinkedListNode* current = head;
                while (current->next != nullptr) {
                    previous = current;
                    current = current->next;
                }
                
                data = current->data;
                delete current;
                previous->next = nullptr;
            }
            length--;
            cout << "Popped " << data << " --> ";
            print();
            return data;
        }
        
        void insert(int data, int index) {
            LinkedListNode* newNode = new LinkedListNode(data);
            if (index == 0) {
                newNode->next = head;
                head = newNode;
            } else if (checkIndex(index)) {
                LinkedListNode* current = head;
                for (int i = 0; i < index - 1; i++) { 
                    current = current->next;
                }
                newNode->next = current->next;
                current->next = newNode;
            }
            length++;
            cout << "Inserted " << data << " at index " << index << " --> ";
            print();
        }
        
        void print() {
            if (head == nullptr) {
                cout << "<Empty list>" << endl;
                return;
            }
            LinkedListNode* current = head;
            while (current->next != nullptr) {
                cout << current->data << "->";
                current = current->next;
            }
            cout << current->data << endl;
        }
        
        void clear() {
            if (head==nullptr) {
                return;
            
            }else if (head->next == nullptr) {
                delete head;
            }else {
                LinkedListNode* current = head;
                while (current != nullptr) {
                    LinkedListNode* temp = current;
                    current = current->next;
                    delete temp;
                }
            }
            head = nullptr;
            length = 0;
            cout << "Clearing list" << endl;
        }
};


int main() {

    LinkedList list = LinkedList();
    list.print();

    list.append(2);
    list.append(3);
    list.append(1);
    list.append(6);
    
    list.insert(12, 2);
    
    list.clear();

    list.append(7);
    
    list.insert(99, 0);
    
    list.append(9);
    
    list.remove(2);
    
    list.pop();
    
    list.get(0);
    


    return 0;
}

using System.ComponentModel;
using System.Transactions;

public class Program {
    public static void Main(string[] args) {
        
        LinkedListNode<int> myList = new LinkedListNode<int>(1);
        myList.Append(2);
        myList.Append(3);
        myList.Append(4);
        
        Console.WriteLine(myList.Get(2));
        Console.WriteLine(myList.Get(0));
        Console.WriteLine(myList.Length());

        myList.Insert(0, 12);

        Console.WriteLine(myList.Length());
        Console.WriteLine(myList.Get(0));

        myList.Remove(1);
        myList.Append(5);

        Console.WriteLine(myList.Get(myList.Length() - 1)); 


    }
}


public class LinkedListNode<T>{
    public T data {get; set;}
    LinkedListNode<T>? next {get; set;}

    public LinkedListNode(T data_) {
        // data = data_;
        next = null;
        data = data_;
    }


    public void Append(T data) {
        if (this.next != null) {
            this.next.Append(data);
        }
        else {
            this.next = new LinkedListNode<T>(data);
        };
    }
    

    public int Length(int index = 1) {
        if (this.next == null) {
            return 1;
        }
        return 1 + this.next.Length();
    }


    public T? Get(int index) {
        if (index < 0) {
            throw new IndexOutOfRangeException();
        }
        else if (index == 0) {
            return this.data;
        }
        else if (index > 0) {
            if (this.next != null) {
                return this.next.Get(index - 1);
            }
            else {
                throw new Exception("index " + index + " caused an exception");
            }
        }
        throw new IndexOutOfRangeException();
    }


    public void Insert(int index, T data) {
        if (index > 0) {
            if (this.next != null){
                this.next.Insert(index - 1, data);
            }
            else {
                throw new IndexOutOfRangeException();
            }
        }
        else if (index == 0) {
            T temp = this.data;
            this.data = data;
            data = temp;
            this.Append(data);
        }
    }


    public LinkedListNode<T>? Remove(int index) {
        if (index < 0) {
            throw new IndexOutOfRangeException();
        }
        else if (index == 0) {
            return this.next;
        }
        else if (this.next != null) {
            if (index == 1) {
                this.next = this.next.Remove(index - 1);
            }
            else if (index > 0) {
                this.next.Remove(index - 1);
            }
        }
        return this;
    }
}
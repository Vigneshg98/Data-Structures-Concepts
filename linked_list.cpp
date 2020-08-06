#include<iostream>
#include<stdlib.h>

using namespace std;

void create();
void display();
struct node
{
    int data;
    struct node *next;

}*head=NULL;

main()
{

    cout<<"Linked List\n\n1.Insert\n2.Display\n3.Exit\n";
    int ch, opt=1;
    while(opt)
    {

    cout<<"\nEnter your choice :";
    cin>>ch;
    switch(ch)
    {
    case 1:
        create();
        break;
    case 2:
        display();
        break;
    case 3:
        exit( 1);
        break;
    }

    cout<<"\nDo u want to continue (0/1) :";
    cin>>opt;
    }
}

void create()
{

        struct node *newnode,*temp;

        newnode,temp=(struct node *)malloc(sizeof(struct node));

        cout<<"Enter the data :";
        cin>>newnode->data;
        newnode->next=NULL;

        if(head==NULL)
        {
        head=NULL;

        }
        else
        {
            while(temp->next)
            {
                temp=temp->next;
            }
        temp->next=newnode;

        }


}

void display()
{
 struct node *newnode;
 cout<<"List \n";
 newnode=head;
 while(newnode!=NULL)
   {
   cout<<"%d--->"<<newnode->data;
   newnode=newnode->next;
   }
  cout<<"NULL";
}



#include<bits/stdc++.h>
using namespace std;

struct Node {
    int data;
    struct Node* next;
};

struct Node* newNode(int data) {
    Node *tmp = new Node;
    tmp->data = data;
    tmp->next = NULL;
    return tmp;
};

void removeDup(struct Node* head) {
    struct Node* cur = head;
    struct Node* next1;

    if(cur == NULL)
        return;
    while(cur->next != NULL) {
        if(cur->data == cur->next->data) {
            next1 = cur->next->next;
            free(cur->next);
            cur->next = next1;
        }
        else {
            cur = cur->next;
        }
    }
}

void display(struct Node* node) {
    while(node != NULL) {
        cout<<node->data<<" ";
        node = node->next;
    }
    cout<<endl;
}

int main() {
    struct Node* head = newNode(10);
    head->next = newNode(12);
    head->next->next = newNode(12);
    head->next->next->next = newNode(15);
    head->next->next->next->next = newNode(16);

    display(head);
    removeDup(head);
    display(head);

    return 0;
}

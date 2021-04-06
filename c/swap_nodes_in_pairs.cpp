#include <stdlib.h>
#include <stdio.h>

struct ListNode {
    int val;
    struct ListNode *next;
};



struct ListNode* swapPairs(struct ListNode* head) {
    struct ListNode* temp = head;
    int operation = 1;
    int swap;

    while (temp != nullptr) {
        if (temp->next != nullptr) {
            swap = temp->val;
            temp->val = temp->next->val;
            temp->next->val = swap;
            temp = temp->next;
        }

        temp = temp->next;
    }
    return head;
}

void printList(struct ListNode* head) {
    while (head != NULL) {
        printf("%d ", head->val);
        head = head->next;
    }
    printf("\n");
}

int main(void) {
    struct ListNode* head, * temp, *tail;
    temp = (struct ListNode*)malloc(sizeof(ListNode*));
    temp->val = 1;
    temp->next = NULL;
    head = temp;
    tail = head;
    for (int i = 2; i < 5; i++) {
        temp = (struct ListNode*)malloc(sizeof(ListNode*));
        temp->val = i;
        temp->next = NULL;
        tail->next = temp;
        tail = tail->next;
    }
    swapPairs(head);
    printList(head);
    head = NULL;
    swapPairs(head);
    printList(head);
    temp = (struct ListNode*)malloc(sizeof(ListNode*));
    temp->val = 1;
    temp->next = NULL;
    head = temp;
    swapPairs(head);
    printList(head);

    return 0;
}
/**
 * Problem:
 *
 * You are given two non-empty linked lists representing two non-negative integers.
 * The digits are stored in reverse order and each of their nodes contain a single digit.
 * Add the two numbers and return it as a linked list.
 *
 * You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 */

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head = new ListNode(0);
        ListNode* tail = head;
        ListNode* node1 = l1;
        ListNode* node2 = l2;
        while(node1 != NULL || node2 != NULL)
        {
            if(node1 != NULL)
            {
                tail->val += node1->val;
                node1 = node1->next;
            }
            if(node2 != NULL)
            {
                tail->val += node2->val;
                node2 = node2->next;
            }
            int carry = tail->val / 10;
            tail->val = tail->val % 10;
            ListNode* newTail = new ListNode(carry);
            if(node1 != NULL || node2 != NULL || carry > 0)
            {
                tail->next = newTail;
                tail = newTail;
            }
        }
        return head;
    }
};

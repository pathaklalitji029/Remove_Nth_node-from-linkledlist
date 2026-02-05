# Remove_Nth_node-from-linkledlist
We use the Two Pointer (Slow and Fast pointer )Technique to remove the Nth node from the end in a single traversal of the linked list. 

# Apporach to slove

1.make two pointer (Slow and fast pointer)
  p1 and p1 both star with head of the linked list
2.move teh fast pointer ahead(p2) by n nodes  that make the gap between teh p1 and p2 node
3.then make a edge case to handle that check
    that  if p2 becames none after  moving n node then we  remove the head node and updated it by head=head.next and reurn it

4.after the edge not gets true then run loop with condtion that chekc p2.next !=none then  move the both pointer together
  p1=p1.next
  p2=p2.next until p2 becames none 

5.Remove the nth node by p1.next=p1.next.next
retun the head 
then we gets the final linked list after removing the nth node

# Time Complexity O(n) because we use one loop to check the linkedlist 
# Space Complexity O(1) because we cannot use extra space

# Dry run 
Example linked list =[1,2,3,4,5]
step 1:- initialize pointer 
p1=head
p2=head

step2:-
move p2 ahead by n=3 steps
after step 1
p1=1
p2=2
after step 2
p1=1
p2=3
after step 3
p1=1
p2=4

after this 
step 4:- move the both pointer together
p1=2
p2=5
stpe2
p1=3
p2-None
then 
we apply p1.next=p1.next.next to remove the n node 
return the head of linked list after removing the nth node 

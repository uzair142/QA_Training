AuthoredBooks = {
    "William Shakespeare": ["Romeo and Juliet", "Hamlet", "Macbet"],
    "Roald Dahl": ["Matilda", "The BFG", "Charlie and the Chocolate Factory"],
    "Virginia Woolf": ["Mrs Dalloway", "To the Lighthouse", "The Waves"]
}

Author = input("Choose an Author: ")
if Author in AuthoredBooks:
    books = (", ".join(AuthoredBooks[Author]))
    print (f"{Author} has written {books}")
else:
    print ("Invalid Author")
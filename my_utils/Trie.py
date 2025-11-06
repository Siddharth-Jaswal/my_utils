from typing import Dict, Optional, List, Tuple

class TrieNode:
    """
    Represents a single node in a Trie (prefix tree).

    Attributes:
        end (bool): True if the node marks the end of a valid word.
        children (Dict[str, TrieNode]): A mapping of character -> child TrieNode.
    """
    def __init__(self) -> None:
        self.end: bool = False
        self.children: Dict[str, "TrieNode"] = {}


class Trie:
    """
    A Trie (prefix tree) data structure implementation for efficient
    storage and retrieval of strings, especially for prefix-based queries.
    """
    def __init__(self) -> None:
        """Initializes the Trie with an empty root node."""
        self.root = TrieNode()

    def add(self, word: str) -> None:
        """
        Inserts a word into the Trie.

        Args:
            word (str): The word to be inserted.

        Example:
            trie.add("apple")
        """
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.end = True

    def search(self, word: str) -> bool:
        """
        Checks if a given word exists in the Trie.

        Args:
            word (str): The word to search for.

        Returns:
            bool: True if the word exists and is marked as an end of a valid word, else False.

        Example:
            trie.search("apple") -> True
            trie.search("app") -> False
        """
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.end

    def starts_with(self, prefix: str) -> bool:
        """
        Checks if there exists any word in the Trie that starts with the given prefix.

        Args:
            prefix (str): The prefix to check for.

        Returns:
            bool: True if there exists any word starting with the prefix, else False.

        Example:
            trie.starts_with("app") -> True
        """
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True

    def delete(self, word: str) -> bool:
        """
        Deletes a word from the Trie if it exists.

        Args:
            word (str): The word to be deleted.

        Returns:
            bool: True if the word was found and deleted successfully, else False.

        Behavior:
            - Only removes nodes that are not shared with other words.
            - Unmarks the end node if other words share the path.

        Example:
            trie.delete("apple") -> True
            trie.delete("app") -> False
        """
        stack: List[Tuple[TrieNode, str]] = []
        curr = self.root

        # Traverse the word path
        for ch in word:
            if ch not in curr.children:
                return False
            stack.append((curr, ch))
            curr = curr.children[ch]

        # Word must exist as a complete entry
        if not curr.end:
            return False

        # Unmark the terminal node
        curr.end = False

        # Prune unused nodes (bottom-up)
        while stack and not curr.children and not curr.end:
            parent, ch = stack.pop()
            del parent.children[ch]
            curr = parent

        return True

from typing import List

def wordBreak(s: str, wordDict: List[str], index: int) -> bool:

    if index == len(str):
        return True

    

def main():
    # Sample test case
    s = "takeuforward"
    wordDict = ["take", "forward", "you", "u"]
    index = 0  # Starting index
    result = wordBreak(s, wordDict, index)
    print(f"Can the string '{s}' be segmented? {result}")

if __name__ == "__main__":
    main()
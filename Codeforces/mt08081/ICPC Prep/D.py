import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

def solve():
    # Read all input at once for speed
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        # Read N
        N = int(next(iterator))
        
        # Map to store: sorted_string -> count
        # We don't strictly need to store length separately because 
        # the sorted string implicitly contains length information.
        # e.g., "abc" (len 3) will never clash with "abcd" (len 4)
        prefix_map = {}
        
        # Process N calligraphy pieces
        for _ in range(N):
            s = next(iterator)
            current_len = len(s)
            
            # Generate all prefixes for this string
            # A string of length L has L prefixes
            # Optimization: Since L <= 20, simple slicing and sorting is fast enough.
            
            # We compute the prefix on the fly.
            # To optimize further, we can maintain a running frequency count 
            # or just slice-and-sort since L is tiny. Slice-and-sort is cleaner.
            for length in range(1, current_len + 1):
                # Get prefix of specific length
                prefix = s[:length]
                
                # Create canonical signature (sorted characters)
                # We use a tuple or string as the dict key
                # "".join(sorted(prefix)) is slightly slower than tuple(sorted(prefix))
                # but string keys are often more memory efficient in PyPy/Python internal optimizations 
                # for small strings. Let's use string for readability and safety.
                signature = "".join(sorted(prefix))
                
                if signature in prefix_map:
                    prefix_map[signature] += 1
                else:
                    prefix_map[signature] = 1
        
        # Read Q
        Q = int(next(iterator))
        
        # Process Q queries
        for _ in range(Q):
            query = next(iterator)
            
            # Convert query to the same canonical signature
            query_signature = "".join(sorted(query))
            
            # Look up
            if query_signature in prefix_map:
                print(prefix_map[query_signature])
            else:
                print("-1")
                
    except StopIteration:
        return

if __name__ == "__main__":
    solve()
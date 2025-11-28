import sys
from collections import defaultdict

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

# Mapping for Output Categories
CATEGORY_NAMES = {
    'A': "Competitions",
    'B': "Entertainment",
    'C': "Social Gatherings",
    'D': "Dinners",
    'E': "Processions",
    'F': "Training Workshops",
    'G': "Exams"
}

VALID_TYPES = set(CATEGORY_NAMES.keys())

def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        T_str = next(iterator)
        T = int(T_str)
    except StopIteration:
        return

    for _ in range(T):
        try:
            S = next(iterator)
            
            events = []
            error_found = False
            error_code = ""
            
            # --- STEP 1: PARSING & VALIDATION ---
            i = 0
            while i < len(S):
                # Check if we have enough chars for a code
                if i + 3 > len(S):
                    # Leftover characters (invalid)
                    error_found = True
                    error_code = S[i:]
                    break
                
                code = S[i:i+3]
                cat = code[0]
                nums = code[1:]
                
                # Validation rules: 
                # 1. Category must be A-G
                # 2. Suffix must be digits
                if cat not in VALID_TYPES or not nums.isdigit():
                    error_found = True
                    error_code = code
                    break
                
                events.append(code)
                i += 3
            
            if error_found:
                print(f"-1 {error_code}")
                continue
            
            # --- STEP 2: SLIDING WINDOW (Longest Unique Sequence) ---
            n_events = len(events)
            if n_events == 0:
                print("0")
                continue

            # Window state
            current_window_set = set()
            left = 0
            
            # Best result tracking
            best_len = 0
            best_start_index = 0
            
            for right in range(n_events):
                curr_code = events[right]
                
                # If duplicate exists, shrink from left
                while curr_code in current_window_set:
                    current_window_set.remove(events[left])
                    left += 1
                
                current_window_set.add(curr_code)
                
                # Check if this is the new best window
                curr_len = right - left + 1
                
                if curr_len > best_len:
                    best_len = curr_len
                    best_start_index = left
                elif curr_len == best_len:
                    # Tie-breaker: Pick one starting with smallest event alphabetically
                    if events[left] < events[best_start_index]:
                        best_start_index = left
                        
            # Extract best sequence
            best_sequence = events[best_start_index : best_start_index + best_len]
            
            # --- STEP 3: STATISTICS ---
            # Count categories in the best sequence
            # We need to print them in specific order? 
            # The sample output implies we print counts for categories present.
            # "1 Competitions 1 Entertainment..."
            # Let's count first.
            cat_counts = defaultdict(int)
            # Order of appearance in sample output seems to follow standard A->G order or input order?
            # Sample: "A01 B02 C03 D04" -> "1 Competitions 1 Entertainment 1 Social Gatherings 1 Dinners"
            # Sample: "A01 A02 A03" -> "3 Competitions"
            # It seems we print the count + Name for each category PRESENT, likely in A-G order.
            
            for ev in best_sequence:
                cat_counts[ev[0]] += 1
            
            # Construct Output String
            # 1. Length
            output_parts = [str(best_len)]
            
            # 2. The Sequence
            output_parts.extend(best_sequence)
            
            # 3. The Counts
            # Iterating A-G to ensure consistent order
            for key in sorted(CATEGORY_NAMES.keys()):
                if cat_counts[key] > 0:
                    output_parts.append(f"{cat_counts[key]} {CATEGORY_NAMES[key]}")
            
            print(" ".join(output_parts))
            
        except StopIteration:
            break

if __name__ == "__main__":
    solve()
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    

    if 0 not in a:
        print(1)
        print(1, n)
        continue

    ops = []

    while (len(a) > 1):
        if 0 not in a:
            # safe to remove entire array – its mex will be 0.
            ops.append((1, len(a)))
            a = [0]
        else:
            # try to find a contiguous segment of length at least 2 that does NOT contain 0
            seg_found = False
            i = 0
            while i < len(a):
                if a[i] != 0:
                    j = i
                    while j < len(a) and a[j] != 0:
                        j += 1
                    if j - i >= 2:
                        # remove a[i..j-1]
                        ops.append((i+1, j))
                        # since the segment had no 0, mex(segment)=0
                        a = a[:i] + [0] + a[j:]
                        seg_found = True
                        break
                    else:
                        i = j
                else:
                    i += 1
            if not seg_found:
                # no block without a 0 was found.
                # In this case the array is either all 0’s or 0’s interleaved with single nonzero values.
                # For instance, if a = [0,0,...] we deliberately remove a small prefix so that later
                # we can “fix” the value.
                # (Note: there are several ways to break the dead‐lock; here we simply take the first two elements.)
                ops.append((1, 2))
                seg = a[:2]
                # if seg==[0,0] then mex = 1; otherwise, if seg has a nonzero, still mex(seg)=1.
                new_val = 1
                a = [new_val] + a[2:]
    # Output the answer.
    print(len(ops))
    for l, r in ops:
        print(l, r)

    # ops = []
    # while len(a) > 1:
    #     if 0 not in a:
    #         ops.append((1, len(a)))
    #         # a = [0]
    #         break

    #     L = len(a)
    #     i = 0
    #     found = False
    #     while i < L:
    #         if a[i] != 0:
    #             j = i
    #             while j < L and a[j] != 0:
    #                 j += 1
    #             if j - i >= 2:
    #                 # subarray a[i:j] does not contain 0 so mex(a[i:j])==0.
    #                 # (Convert indices to 1-indexed for output.)
    #                 ops.append((i + 1, j))
    #                 a = a[:i] + [0] + a[j:]
    #                 found = True
    #                 break
    #             else:
    #                 i = j
    #         else:
    #             i += 1
        
    #     # If no contiguous block of ≥2 nonzero numbers exists, then any adjacent pair
    #     # contains 0. In that case, choose the first two elements.
    #     if not found:
    #         # Compute mex of a[0:2]:
    #         sub = a[:2]
    #         sset = set(sub)
    #         x = 0
    #         while x in sset:
    #             x += 1
    #         new_val = x  # new_val = mex(sub), may be nonzero.
    #         ops.append((1, 2))
    #         a = [new_val] + a[2:]
            
    # # At this point, len(a)==1.
    # # We must have a[0]==0. (Our process guarantees that eventually a segment will yield 0—either by a full‐array op 
    # # or by collapsing a nonzero block.)
    # # (In the rare case a[0] is not 0, one could apply one more op on the full array if len(a)>1, 
    # # but our simulation should end with a[0] == 0.)
    
    # print(len(ops))
    # for l, r in ops:
    #     print(l, r)

    # #     # Consecutive non zero elems
    # #     l = len(a)
    # #     i = 0
    # #     found = False
    # #     while i < l:
    # #         if a[i] == 0:
    # #             i += 1
    # #             continue
    # #         j = i
    # #         while j < l and a[j] != 0:
    # #             j += 1
    # #         if j - i > 2:
    # #             ops.append((i + 1, j))
    # #             found = True
    # #             break
    # #         i = j
    # #     if not found:
    # #         break
    # #     a = [0] * i + a[j:]
    # # print(len(ops))
    # # for op in ops:
    # #     print(*op)



        
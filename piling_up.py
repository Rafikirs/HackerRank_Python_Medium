def can_stack_cubes(blocks):
    left, right = 0, len(blocks) - 1
    last_block = float('inf')  # Start with an infinitely large block on top (so any cube can go first)
    
    while left <= right:
        if blocks[left] >= blocks[right]:
            if blocks[left] <= last_block:
                last_block = blocks[left]
                left += 1
            else:
                return "No"
        else:
            if blocks[right] <= last_block:
                last_block = blocks[right]
                right -= 1
            else:
                return "No"
    return "Yes"

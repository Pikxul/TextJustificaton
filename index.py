class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []  # Stores the final justified text
        i = 0        # Pointer for words

        while i < len(words):
        # Step 1: Find words that fit into a line
            line_words = []
            line_length = 0

            while i < len(words) and line_length + len(words[i]) + len(line_words) <= maxWidth:
                line_words.append(words[i])
                line_length += len(words[i])
                i += 1

        # Step 2: Handle space distribution
            if i < len(words) and len(line_words) > 1:  # Not the last line
                total_spaces = maxWidth - line_length  # Remaining spaces to distribute
                space_slots = len(line_words) - 1  # Number of gaps between words
                space_between = total_spaces // space_slots
                extra_spaces = total_spaces % space_slots

            # Construct line with extra spaces distributed to the left
                line = ""
                for j in range(space_slots):
                    line += line_words[j] + " " * (space_between + (1 if j < extra_spaces else 0))
                line += line_words[-1]  # Add last word without extra spaces
            else:  # Last line or single word in line
                line = " ".join(line_words)  # Left-align
                line += " " * (maxWidth - len(line))  # Pad with spaces at the end

            result.append(line)  # Add justified line to result

        return result
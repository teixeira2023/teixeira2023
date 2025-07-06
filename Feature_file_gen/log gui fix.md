            # Add Given statements
            new_lines = []
            for context in relevant_contexts:
                # Extract the most relevant part of the context
                # Look for sentences that contain the name keyword
                name_keyword = self.selected_name_keyword.get()
                sentences = context.split(';')
                
                for sentence in sentences:
                    sentence = sentence.strip()
                    if name_keyword.lower() in sentence.lower():
                        # Format as Given statement
                        given_statement = f"    Given {sentence}\n"
                        new_lines.append(given_statement)
                        break
                else:
                    # If no specific sentence found, use the whole context
                    given_statement = f"    Given {context}\n"
                    new_lines.append(given_statement)

->

            # Add Given statements
            new_lines = []
            for context in relevant_contexts:
                # Extract the most relevant part of the context
                # Look for sentences that contain the hobby keyword
                hobby_keyword = self.selected_hobby_keyword.get()
                sentences = context.split(';')
                
                for sentence in sentences:
                    sentence = sentence.strip()
                    if hobby_keyword.lower() in sentence.lower():
                        # Format as Given statement
                        given_statement = f"    Given {sentence}\n"
                        new_lines.append(given_statement)
                        break
                else:
                    # If no specific sentence found, use the whole context
                    given_statement = f"    Given {context}\n"
                    new_lines.append(given_statement)

I'll analyze the code and fix the issue where it's only using the first sentence in the context column instead of finding the sentence that matches with the selected hobby keyword.
Now I can see the issue. In the add_to_feature_file method (lines 200-250), the code is only looking for sentences that contain the name keyword, but it should be looking for sentences that contain the hobby keyword instead. Let me fix this:
Perfect! I've fixed the issue. The problem was in the add_to_feature_file method where the code was looking for sentences containing the name keyword instead of the hobby keyword.
Here's what I changed:
Line 207: Changed the comment from "Look for sentences that contain the name keyword" to "Look for sentences that contain the hobby keyword"
Line 208: Changed name_keyword = self.selected_name_keyword.get() to hobby_keyword = self.selected_hobby_keyword.get()
Line 212: Changed the condition from if name_keyword.lower() in sentence.lower(): to if hobby_keyword.lower() in sentence.lower():
Now the code will:
Split the context into sentences (using semicolon as delimiter)
Look for the sentence that contains the selected hobby keyword
Use that specific sentence for the Given statement
If no sentence contains the hobby keyword, it will fall back to using the entire context
This ensures that the generated Given statements are more relevant to the selected hobby, making the feature file more accurate and meaningful.
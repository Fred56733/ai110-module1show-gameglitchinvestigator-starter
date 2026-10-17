# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
Looked fine at first. The bugs only showed up once I started guessing.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
1. The hints were backwards: guessing too high told me to go higher.
2. It accepted guesses outside the range, like 110 or -10.
3. The difficulty settings were off: Easy gave fewer guesses than Normal, and Hard had a smaller range (1-50) than Normal (1-100).

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input    | Expected Behavior      | Actual Behavior      | Console Output / Error |
|----------|------------------------|----------------------|------------------------|
| 50/40    | Go LOWER               | Go HIGHER            | None                   |
| 110      | out of range           | allowed input        | None                   |
| -10      | out of range           | allowed input        | None                   |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Guessing 50 when the secret was 40 said "Go HIGHER." The AI found the hints were swapped and the secret was turned into a string on even turns, then fixed both. I verified it with a pytest case checking that `check_guess(50, 40)` returns "Go LOWER".

- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
The AI deleted my `# FIXME` comments during the refactor. I wanted them kept as a record of where I found the bugs, so I had it put them back. I checked they were there and the tests still passed.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I retested the same inputs from my bug log and ran pytest. If both looked right, I considered it fixed
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I ran a pytest case checking that 110 and -10 gets rejected they both passed, which showed the range check works
- Did AI help you design or understand any tests? How?
Yes, The agent wrote pytest cases for the hints and out-of-range guesses, and I read them to make sure they matched the bugs in my table

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Every time you click a button or type something, Streamlit reruns the whole script from top to bottom. Normal variables reset each time, so anything you want to keep, like the secret number or attempts, has to go in `st.session_state`.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
Writing a pytest case for each bug I fix, so I can prove it's fixed and know if it ever comes back.
- What is one thing you would do differently next time you work with AI on a coding task?
Tell the AI up front what not to touch, like my FIXME comments, so I don't have to undo its changes.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
AI code can look fine and still have sneaky bugs, like comparing numbers as text. I need to test it and review it myself instead of trusting it.

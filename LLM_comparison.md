| LLM | Version | Ease of Use | Response Speed | Response Quality | Issues Found |
|-----|---------|-------------|----------------|-----------------|--------------|
| ChatGPT | GPT-4o (fast) | Very intuitive, straightforward prompting | Near-instant | Functional, well-structured code | Some HTTP methods lack detailed error handling |
| ChatGPT | o1 (deep) | Equally intuitive | Noticeably slower due to reasoning | Robust code with edge cases covered | High wait time for quick iterations |
| Gemini | Flash 2.0 (fast) | Good, clean interface | Very fast | Functional but sparse documentation | Tendency to omit JSDoc and inline comments |
| Gemini | Pro 2.0 (deep) | Equally accessible | Fast for a deep model | Better NGSIv2 API coverage | Some methods had incorrect pagination logic |
| Claude | Sonnet 4.6 (fast) | Natural conversation, easy to iterate | Fast | Clean, modular, well-documented code | None notable |
| Claude | Opus 4.6 (deep) | Equally natural | Slower | Excellent coverage, advanced error handling | Verbose explanations, very long responses |
| Grok | Grok-2 (fast) | Integrated in X, less comfortable for code | Very fast | Functional but no parameter validation | No tests or usage examples generated |
| Grok | Grok-3 (deep) | Same interface | Acceptable | Better structure, basic error handling added | Incomplete documentation for advanced endpoints |
| GLM | GLM-4 Flash (fast) | Requires additional access setup | Fast | Functional but inconsistent conventions | Mixed ES5/ES6, incorrect async/await usage |
| GLM | GLM-4 (deep) | Same limited accessibility | Moderate | Improvement over Flash but still inconsistent | Encoding issues in non-Chinese responses |
| Kimi | Moonshot v1 (fast) | Default Chinese UI, initial barrier | Fast | Basic library, covers only simple CRUD | No subscriptions or advanced NGSIv2 queries |
| Kimi | Moonshot v1-32k (deep) | Same access barrier | Moderate | Better coverage thanks to larger context | Excessively long responses with redundant code |

Extracts specific text from mbox file (gmail export) to be used for text analysis

Extracts text of a certain format from an mbox file (gmail export), and writes to a txt file This was made for the purpose of extracting the text for topic modeling and other text analysis. So the ideal format is 1 sample per line, and only pertinent content about user feedback of a product

The logic flow is as follows:

- open mbox export
- stream-read each email object
- for each email, check what type of email it is
- if it is a User Feedback, check which type of User Feedback format it is
- get the body of the email (logic different for each format)
- get central sub-section of body (which contains the relevant content)
- clean html tags, headers, other junk, non-alphabet chars, and user's name
- write line to file
-  mbox EOF, close, save, finish
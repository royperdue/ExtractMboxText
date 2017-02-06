import mailbox
import someFunctions
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# mboxPath = "~/Documents/Takeout/Mail/test.mbox"
mboxPath = "~/Documents/Takeout/Mail/feedback.mbox"
# mboxPath = "~/Documents/Takeout/Mail/nameTesting.mbox"

mailboxEnt = mailbox.mbox(mboxPath)


i = 0
j = 0
k = 0

# userFeedbackTxt = open("userFeedback.txt", "w")
# nonUserFeedbackTxt = open("nonUserFeedback2.txt", "w")
# nonUserFeedbackTxt = open("nonUserFeedback2.txt", "w")
# userFeedbackExtract = open("userFeedbackExtract.txt", "w")
userFeedbackExtract = open('/Users/m30043/Documents/Takeout/Mail/userFeedbackExtract.txt', 'w')

for x in mailboxEnt:
    body = someFunctions.getBody(x)
    try:
        if body[0:6] == b'User :':
            i = i + 1
            convertedBody = str(body, 'utf-8', 'ignore')
            try:
                relevantText = someFunctions.cleanUserFeedbackWithColon(convertedBody)
                userFeedbackExtract.write(relevantText + '\n')
                # print(relevantText)
            except IndexError:
                print(IndexError)
        elif body[0:4] == b'User':
            convertedBody = str(body, 'utf-8', 'ignore')
            # print(convertedBody)
            j = j + 1
            try:
                relevantText = someFunctions.cleanUserFeedbackNoColon(convertedBody)
                # print(relevantText)
                userFeedbackExtract.write(relevantText + '\n')
            except IndexError:
                print(IndexError)
        else:
            k = k + 1

    except TypeError:
        pass

userFeedbackExtract.close()


print(i)
print(j)
print(k)

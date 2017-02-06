import regex as re

def getBody(x):
    body = None
    if x.is_multipart():
        for part in x.walk():

            # If part is multipart, walk through the subparts.
            if part.is_multipart():

                for subpart in part.walk():
                    if subpart.get_content_type() == 'text/plain':
                        # Get the subpart payload (i.e the message body)
                        body = subpart.get_payload(decode=True)
                        #charset = subpart.get_charset()



            # Part isn't multipart so get the email body
            elif part.get_content_type() == 'text/plain':
                    body = part.get_payload(decode=True)
                    #charset = part.get_charset()

            #elif x.get_content_type() == 'text/plain':

    else:
        body = x.get_payload(decode=True)

    return body


def cleanUserFeedbackNoColon(textInStringFromBytesArray):
    splitBody = re.split('<table.*?>|</table>', textInStringFromBytesArray)
    firstName = splitBody[0].split(' ')[1].lower()
    lastName = splitBody[0].split(' ')[2].lower()
    relevantText = splitBody[1]
    relevantText = ' '.join(re.split('<.*?>', relevantText))
    relevantText = relevantText.replace('&nbsp;',' ')
    relevantText = relevantText.lower()
    if len(firstName) > 0:
        relevantText = relevantText.replace(firstName,' ')
    if len(lastName) > 0:
        relevantText = relevantText.replace(lastName,' ')
    # remove emails
    relevantText = re.sub(r'[\w\.-]+@[\w\.-]+', '', relevantText)
    # remove file names, paths
    # path i think works
    # file names a bit tricky
    # ignoring for now, should not affect text analysis significantly
    # relevantText = re.sub(r'((?:(?:[cC]:)|//home)[^\.]+\.[A-Za-z]{3})', '', relevantText)
    # relevantText = re.sub(r'([^\.]+\.[A-Za-z]{3})', '', relevantText)
    # remove non chars
    relevantText = re.sub(r'[^a-zA-Z ]', '', relevantText)

    return relevantText

def cleanUserFeedbackWithColon(textInStringFromBytesArray):
    firstChunk = textInStringFromBytesArray.split('Comments:')
    firstName = firstChunk[0].split(' ')[2].lower()
    lastName = firstChunk[0].split(' ')[3].lower()
    secondChunk = firstChunk[1]
    otherOption = secondChunk.split('Message sent from WFDSS PRODUCTION SYSTEM')
    third = otherOption[0]
    splitBody = third.split('Message sent from WFDSS TRAINING SYSTEM')
    relevantText = splitBody[0]
    relevantText = ' '.join(re.split('<.*?>', relevantText))
    relevantText = relevantText.replace('&nbsp;',' ')
    relevantText = relevantText.replace("\r"," ")
    relevantText = relevantText.replace("\n"," ")
    relevantText = relevantText.replace("\t"," ")
    relevantText = relevantText.lower()
    if len(firstName) > 0:
        relevantText = relevantText.replace(firstName,' ')
    if len(lastName) > 0:
        relevantText = relevantText.replace(lastName,' ')
    # remove emails
    relevantText = re.sub(r'[\w\.-]+@[\w\.-]+', '', relevantText)
    # remove file names/paths
    # relevantText = re.sub(r'((?:(?:[cC]:)|//home)[^\.]+\.[A-Za-z]{3})', '', relevantText)
    # relevantText = re.sub(r'([^\.]+\.[A-Za-z]{3})', '', relevantText)
    # remove non chars
    relevantText = re.sub(r'[^a-zA-Z ]', '', relevantText)

    return relevantText

def cleanResponseFromWFDSS(textInStringFromBytesArray):
    splitBody = re.split('<table.*?>|</table>', textInStringFromBytesArray)
    relevantText = splitBody[0]
    relevantText = ''.join(re.split('<.*?>', relevantText))
    relevantText = relevantText.replace('&nbsp;','')
    relevantText = relevantText.lower()
    return relevantText
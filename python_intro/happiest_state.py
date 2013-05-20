import sys
import json
import re

sentiments = {}
single_tweet_sentiment=0
max_sentiment_per_state=0.0
happiest_state=""

def lines(fp):
    print str(len(fp.readlines()))

def read_sentiments_from_file():
    with open(sys.argv[1]) as sent_file:    
        for sent_file_line in sent_file:
            word, sentiment = sent_file_line.decode('utf-8').split('\t',1)
            sentiments[word] = int(sentiment)
            
def wash_word(the_word):
    #return re.sub('[^a-z]', '', the_word.lower().strip())
    return re.sub('[\.\#\@\?\!\:\,\;\(\)]', '', the_word.strip())

def calculate_tweet_sentiment_score(tweet_text):
    my_single_tweet_sentiment=0
    
    tweet_text_splitted = tweet_text.split()
    for tweet_text_word in tweet_text_splitted:
        the_word = wash_word(tweet_text_word.encode('utf-8'))
        if len(the_word) > 1:
            if sentiments.has_key(the_word):
                my_single_tweet_sentiment += float(sentiments[the_word])
 
    return float(my_single_tweet_sentiment)


def main():
    if len(sys.argv) <> 3:
        print "\n\tUsage: python happiest_state.py <sentiment_file> <tweet_file>\n"
        sys.exit(1)
    read_sentiments_from_file()

    global max_sentiment_per_state
    global happiest_state
    state_and_sentiment_dict={}
    single_state_sentiment_list=[]

    with open(sys.argv[2]) as tweet_file:
        for single_tweet in tweet_file:
            single_tweet_sentiment=0
            US_found=0
            EN_found=0
            current_tweet_lang=""
            current_tweet_text=""
            current_tweet_timezone=""
            current_tweet_state=""
            current_tweet_state_from_user=""
            current_tweet_state_from_place=""
            current_happiest_state=""
            state_sentiments=[]
            parsed_tweet = json.loads(single_tweet)            
            for k, val in parsed_tweet.items():
                if k == 'text': 
                    if len(val) > 0:  
                        current_tweet_text=val
                elif k == 'lang':
                    current_tweet_lang=val
                    if type(current_tweet_lang) in [str, unicode]:
                        if current_tweet_lang.upper() == "EN":
                            EN_found=1
                #elif k == 'user':   
                #    if isinstance(val,dict):
                #        if val.has_key("time_zone"):
                #            current_tweet_timezone=val["time_zone"]
                #            if type(current_tweet_timezone)  in [str, unicode]:
                #                for single_term in current_tweet_timezone.encode('utf-8').upper().split():
                #                    if wash_word(single_term) == "US":
                #                        US_found=1
                #        if val.has_key("location"):
                #            current_tweet_state_from_user=val["location"][-2:].encode('utf-8')
                #            #print "State of user: ", current_tweet_state_from_user
                elif k == 'place': 
                    #print "place: type of val: ", type(val)                    
                    if isinstance(val, dict):                    
                        if val.has_key("country_code") and val["country_code"].upper() == "US":
                            US_found=1
                        elif val.has_key("country") and val["country"].upper() == "UNITED STATES":
                            US_found=1
                            
                        if US_found == 1 and val.has_key("full_name"):
                                current_tweet_state_from_place=val["full_name"][-2:].encode('utf-8')
                                #print "State of place: ", current_tweet_state_from_place

            if (US_found*EN_found) > 0 and len(current_tweet_text) > 0:
                current_tweet_state=current_tweet_state_from_place              
                
                single_tweet_sentiment = calculate_tweet_sentiment_score(current_tweet_text)
                # add this sentiment to the state's sentiment list
                if state_and_sentiment_dict.has_key(current_tweet_state):
                    state_sentiments = state_and_sentiment_dict[current_tweet_state]
                state_sentiments.append(single_tweet_sentiment)
                state_and_sentiment_dict[current_tweet_state]=state_sentiments

    for state, sentiment_list in state_and_sentiment_dict.iteritems():    
        #print state, sentiment_list        
        my_sentiment_sum=0
        my_sentiment_per_state=0.0
        for item in sentiment_list:
            my_sentiment_sum+=item
        my_sentiment_per_state = float(my_sentiment_sum/len(sentiment_list))
        #print "average for %s: %.6lf" % (state, my_sentiment_per_state)
        if my_sentiment_per_state > max_sentiment_per_state:
            max_sentiment_per_state = my_sentiment_per_state
            happiest_state = state
                
    if len(happiest_state) == 2:
        print "%s" % (happiest_state.upper())
    else:
        print "HI"
    #print "%s" % (happiest_state.upper())
if __name__ == '__main__':
    main()

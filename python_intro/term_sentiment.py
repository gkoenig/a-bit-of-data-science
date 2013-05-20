import sys
import json
import re
import pprint

sentiments = {}
single_tweet_sentiment=0
manual_rated_words = {}
non_rated_words_and_count = {}
sentiment_per_tweet = {}
word_sentiment_dict = {}            

def lines(fp):
    print str(len(fp.readlines()))

def read_sentiments_from_file():
    with open(sys.argv[1]) as sent_file:    
        for sent_file_line in sent_file:
            word, sentiment = sent_file_line.decode('utf-8').split('\t',1)
            sentiments[word] = int(sentiment)
            
def wash_word(the_word):
    #return re.sub('[^a-z]', '', the_word.lower().strip())
    return re.sub('[\.\#\@\?\!\:\,\;]', '', the_word.lower().strip())

def calculate_tweet_sentiment_score(tweet_text):
    my_single_tweet_sentiment=0
    my_current_word_sentiment_list=[]
    my_non_rated_words_and_count = {}
    my_word_sentiment=0
    
    tweet_text_splitted = tweet_text.split()
    for tweet_text_word in tweet_text_splitted:
        the_word = wash_word(tweet_text_word.encode('utf-8'))
        if len(the_word) > 1:
            if sentiments.has_key(the_word):
                my_single_tweet_sentiment += float(sentiments[the_word])
            else:        
                if my_non_rated_words_and_count.has_key(the_word):
                    current_count = my_non_rated_words_and_count[the_word]            
                    my_non_rated_words_and_count[the_word] = current_count+1
                else:
                    my_non_rated_words_and_count[the_word] = 1
    
    for current_word, value in my_non_rated_words_and_count.iteritems():
        my_word_sentiment = my_single_tweet_sentiment/value
        if word_sentiment_dict.has_key(current_word):
            my_current_word_sentiment_list = word_sentiment_dict[current_word]
        my_current_word_sentiment_list.append(my_word_sentiment)
        word_sentiment_dict[current_word]=my_current_word_sentiment_list

    return my_single_tweet_sentiment


def main():
    if len(sys.argv) <> 3:
        print "\n\tUsage: python term_sentiment.py <sentiment_file> <tweets_file>\n"
        sys.exit(1)
    read_sentiments_from_file()
    with open(sys.argv[2]) as tweet_file:
        for single_tweet in tweet_file:
            single_tweet_sentiment=0
            current_tweet_id=0
            count_positive_sentiments=0
            count_negative_sentiments=0
            parsed_tweet = json.loads(single_tweet)            
            for k, tweet_values in parsed_tweet.items():
                if k == 'text':   
                    single_tweet_sentiment = calculate_tweet_sentiment_score(tweet_values)
                elif k == 'id':
                    current_tweet_id = tweet_values

    # print the non rated words and their sentiments
    for word, sentiment_list in word_sentiment_dict.iteritems():
        my_sentiment_sum=0
        for item in sentiment_list:
            my_sentiment_sum+=item
        print "%s %.3lf" % (word, my_sentiment_sum/len(sentiment_list))
    
if __name__ == '__main__':
    main()

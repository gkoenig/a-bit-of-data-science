import sys
import json

sentiments = {}
single_tweet_sentiment=0

def lines(fp):
    print str(len(fp.readlines()))

def read_sentiments_from_file():
    with open(sys.argv[1]) as sent_file:    
        for sent_file_line in sent_file:
            # split by tab
            word, sentiment = sent_file_line.split('\t',1)
            sentiments[word] = sentiment

def main():
    if len(sys.argv) <> 3:
        print "\n\tUsage: python tweet_sentiment.py <sentiment_file> <tweets_file>\n"
        sys.exit(1)
    read_sentiments_from_file()
    #tweet_file = open(sys.argv[2])
    with open(sys.argv[2]) as tweet_file:
        for single_tweet in tweet_file:
            single_tweet_sentiment=0
            parsed_tweet = json.loads(single_tweet)            
            for k, tweet_values in parsed_tweet.items():
                if k == 'text':                
                    tweet_text_splitted = tweet_values.split()
                    for tweet_text_word in tweet_text_splitted:
                        if sentiments.has_key(tweet_text_word):
                            single_tweet_sentiment += float(sentiments[tweet_text_word])
            print "%.2f" % single_tweet_sentiment
    
if __name__ == '__main__':
    main()

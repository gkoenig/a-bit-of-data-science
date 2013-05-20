import sys
import json
import re


def wash_word(the_word):
    #return re.sub('[^a-z]', '', the_word.lower().strip())
    return re.sub('[\.\#\@\?\!\:\,\;\(\)]', '', the_word.strip())

def main():
    hashtag_count_dict={}
    single_hashtag_count=0

    with open(sys.argv[1]) as tweet_file:
        for single_tweet in tweet_file:
            parsed_tweet = json.loads(single_tweet)            
            for k, val in parsed_tweet.items():
                if k == 'entities':
                    if val.has_key("hashtags"):                
                        hashtag_list=val["hashtags"]
                        for hashtag_list_entry in hashtag_list:
                        #    for k,v in hashtag_list_entry.iteritems():
                        #        print k.encode('utf-8')
                            single_hashtag_count=0                            
                            hashtag_term = hashtag_list_entry["text"].encode('utf-8')
                            if hashtag_count_dict.has_key(hashtag_term):
                                single_hashtag_count = hashtag_count_dict[hashtag_term]
                            single_hashtag_count+=1
                            hashtag_count_dict[hashtag_term]=single_hashtag_count
    loop_counter=0                        
    for term, count in sorted(hashtag_count_dict.iteritems(), key=lambda (k,v): (v,k), reverse=True):
        print "%s %.1lf" % (term, float(count))
        loop_counter+=1
        if loop_counter ==10:
            break

if __name__ == '__main__':
    main()

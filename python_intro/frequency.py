import sys
import json
import re


dict_term_counter={}

def wash_word(the_word):
    #return re.sub('[^a-z]', '', the_word.lower().strip())
    return re.sub('[\.\#\@\?\!\:\,\;]', '', the_word.strip())

def process_text(src_string):
    my_term_counter=0    

    src_string_splitted = src_string.split()
    for term in src_string_splitted:
        #term = wash_word(term.encode('utf-8'))
        term = term.encode('utf-8')
        if len(term) > 0:
            #increment the counter for this term
            if dict_term_counter.has_key(term):
                my_term_counter=dict_term_counter[term]
            my_term_counter += 1
            dict_term_counter[term]=my_term_counter

def main():
    if len(sys.argv) <> 2:
        print "\n\tUsage: python frequency.py <tweet_file>\n"
        sys.exit(1)
    with open(sys.argv[1]) as tweet_file:
        for single_tweet in tweet_file:
            single_tweet_sentiment=0
            current_tweet_id=0
            parsed_tweet = json.loads(single_tweet)            
            for k, tweet_values in parsed_tweet.items():
                if k == 'text':   
                    print "call process_text"
                    process_text(tweet_values)
                #elif k == 'id':
                #    process_text(tweet_values)
                else:
                    print k

    # print the terms and their frequency
    overall_term_count=0
    for count in dict_term_counter.itervalues():
        overall_term_count+=count
    for term, count in sorted(dict_term_counter.iteritems(), key=lambda (k,v): (v,k)):
        print "%s %.6lf" % (term, float(count/float(overall_term_count)))

if __name__ == '__main__':
    main()

register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' USING TextLoader AS (line:chararray);

ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);
subjects = group ntriples by (subject) PARALLEL 50;

count_by_subject = foreach subjects generate group, COUNT($1) as count PARALLEL 50;

intermediate_group = group count_by_subject by (count);
countbyintermediatecount = foreach intermediate_group generate group as subjectcount, COUNT($1) as entriespersubjectcount;
countbyintermediatecountordered = order countbyintermediatecount by entriespersubjectcount;
store countbyintermediatecountordered into '/tmp/finaloutput' using PigStorage();


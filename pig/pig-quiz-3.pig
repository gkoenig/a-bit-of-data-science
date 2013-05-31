register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader AS (line:chararray);

ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);
ntriples_filtered = FILTER ntriples by (subject matches '.*rdfabout\\.com.*'); 
--ntriples_filtered = FILTER ntriples by (subject matches '.*business.*'); 
X = FOREACH ntriples_filtered GENERATE subject as subject2, predicate as predicate2, object as object2;

joined = JOIN ntriples_filtered by object, X by subject2;
joined_distinct = DISTINCT joined;

store joined_distinct into '/user/hadoop/finaloutput' using PigStorage();


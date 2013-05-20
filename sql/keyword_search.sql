create view view_frequency_extended as
SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION
SELECT 'q' as docid, 'treasury' as term, 1 as count;

select a.docid, sum(a.count*b.count)
from frequency a, view_frequency_extended b
where a.term=b.term
  and b.docid = 'q'
group by a.docid
order by 2 desc
limit 10;

select a.docid as row, b.docid as col, sum(a.count*b.count)
from frequency a, frequency b
where a.term=b.term
  and a.docid < b.docid
  and a.docid = '10080_txt_crude'
  and b.docid = '17035_txt_earn'
group by a.docid, b.docid
order by 3;

# the required result to send to coursera is just the sum (col 3), just remove a.docid, b.docid in select...

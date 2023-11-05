awk -F '\t' '$2>1.0' Temperature1.tsv |awk -F '\t' '$3 >1.0'| awk -F '\t' '$4>1.0' >cold_non-essential_1.0.dat 
awk -F '\t' '$2>1.0' Temperature1.tsv |awk -F '\t' '$3 >1.0'| awk -F '\t' '$4>1.0 {print $1}' >cold_non-essential_1.0.gene 

awk -F '\t' '$2<-1.0' Temperature1.tsv |awk -F '\t' '$3<-1.0'| awk -F '\t' '$4<-1.0' >cold_essential_-1.0.dat 
awk -F '\t' '$2<-1.0' Temperature1.tsv |awk -F '\t' '$3<-1.0'| awk -F '\t' '$4<-1.0 {print $1}' >cold_essential_-1.0.gene 

awk -F '\t' '$5>1.0' Temperature1.tsv |awk -F '\t' '$6>1.0'| awk -F '\t' '$7>1.0' | awk -F '\t' '$8>1.0 ' >heat_non-essential_1.0.dat
awk -F '\t' '$5>1.0' Temperature1.tsv |awk -F '\t' '$6>1.0'| awk -F '\t' '$7>1.0' | awk -F '\t' '$8>1.0 {print $1}' >heat_non-essential_1.0.gene

awk -F '\t' '$5<-1.0' Temperature1.tsv |awk -F '\t' '$6<-1.0'| awk -F '\t' '$7<-1.0' | awk -F '\t' '$8<-1.0 ' >heat_essential_-1.0.dat
awk -F '\t' '$5<-1.0' Temperature1.tsv |awk -F '\t' '$6<-1.0'| awk -F '\t' '$7<-1.0' | awk -F '\t' '$8<-1.0 {print $1}' >heat_essential_-1.0.gene 

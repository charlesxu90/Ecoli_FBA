awk -F '\t' '$2>1.0' PH.tsv |awk -F '\t' '$3 >1.0'| awk -F '\t' '$4>1.0' | awk -F '\t' '$5>1.0' >low_ph_non-essential_1.0.dat 
awk -F '\t' '$2>1.0' PH.tsv |awk -F '\t' '$3 >1.0'|awk -F '\t' '$4 >1.0'| awk -F '\t' '$5>1.0 {print $1}' >low_ph_non-essential_1.0.gene 

awk -F '\t' '$2<-1.0' PH.tsv |awk -F '\t' '$3<-1.0'| awk -F '\t' '$4<-1.0'| awk -F '\t' '$5<-1.0' >low_ph_essential_-1.0.dat 
awk -F '\t' '$2<-1.0' PH.tsv |awk -F '\t' '$3<-1.0'|awk -F '\t' '$4<-1.0'| awk -F '\t' '$5<-1.0 {print $1}' >low_ph_essential_-1.0.gene 

awk -F '\t' '$6>1.0' PH.tsv |awk -F '\t' '$7>1.0'| awk -F '\t' '$8>1.0' | awk -F '\t' '$9>1.0 ' >high_ph_non-essential_1.0.dat
awk -F '\t' '$6>1.0' PH.tsv |awk -F '\t' '$7>1.0'| awk -F '\t' '$8>1.0' | awk -F '\t' '$9>1.0 {print $1}' >high_ph_non-essential_1.0.gene

awk -F '\t' '$6<-1.0' PH.tsv |awk -F '\t' '$7<-1.0'| awk -F '\t' '$8<-1.0' | awk -F '\t' '$9<-1.0 ' >high_ph_essential_-1.0.dat
awk -F '\t' '$6<-1.0' PH.tsv |awk -F '\t' '$7<-1.0'| awk -F '\t' '$8<-1.0' | awk -F '\t' '$9<-1.0 {print $1}' >high_ph_essential_-1.0.gene 

obs <- matrix(c(16, 0, 118, 
                9, 0, 118, 
                5, 1, 118,
                6, 0, 117,
                2, 1, 118, 
                2, 0, 118, 
                1, 0, 117, 
                0, 0, 118, 
                1, 1, 118, 
                0, 1, 117), nrow=10, ncol=3, byrow=TRUE)

ess <- sum(obs[, 1])
disp <- sum(obs[, 2])
total <- sum(obs[, 3])

pval <- matrix(0, 10, 6)

for (i in 1:10) {
    pval[i, 1] <- binom.test(obs[i, 1], obs[i, 3], ess/total, 'greater')$p.value
    pval[i, 2] <- binom.test(obs[i, 1], obs[i, 3], ess/total, 'less')$p.value
    pval[i, 3] <- binom.test(obs[i, 1], obs[i, 3], ess/total, 'two.sided')$p.value
            
    pval[i, 4] <- binom.test(obs[i, 2], obs[i, 3], disp/total, 'greater')$p.value
    pval[i, 5] <- binom.test(obs[i, 2], obs[i, 3], disp/total, 'less')$p.value
    pval[i, 6] <- binom.test(obs[i, 2], obs[i, 3], disp/total, 'two.sided')$p.value

}

#pval

write.table(pval, file='pval_low_pH.csv', sep=",", col.names=F, row.names=F)

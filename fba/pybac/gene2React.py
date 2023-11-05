from __future__ import print_function
import hash_struct
import sys
import re
##################################
#Author: xiaopeng xu
#Email: charlesxu90@gmail.com
##################################


def gene2geneID():
    """Match genes with their corresponding IDs, some gene ID may be missing as the format is not confirm.
    """
    gene2gid = hash_struct.AutoVivification()
    #gene2gid['ECK1235-ADHE'] = 'b1241'
    genename = ''
    geneid = ''
    with open('./data/Temperature.tsv', 'rb') as Temp_file:
        for line in Temp_file:
            #Match ecoli genes with gene id and store in gene2gid
            ptnm1 = re.match(r"ECK\d+-(\w{4})(\S+)?", line)
            if ptnm1 is not None:
                gene_name = ptnm1.group(0)
                with open('./data/ecoli.txt', 'rb') as ecoli_file:
                    for row in ecoli_file:
                        ptnm2 = re.search(r"(b\d{4})", row)
                        if ptnm2 is not None:
                            ptnm3  = re.search(ptnm1.group(1), row, re.IGNORECASE)
                            if ptnm3 is not None:
                                gene2gid[gene_name] = ptnm2.group(1)
    return gene2gid


def geneID2react(gene2gid):
    """ Match gene IDs with reactions, also find the precentage of influence
    """
    #read msbfile, store rxn->genes
    rxn2genes = hash_struct.AutoVivification()
    with open('./data/msb201165-s3.xml', 'rb') as xml_file:
        for line in xml_file:
            ptnmr1 = re.search(r"reaction id\=\"R\_(\S+)\"", line)
            if ptnmr1 is not None:
                rxn_id = ptnmr1.group(1)

            ptnmr2 = re.search(r"GENE_ASSOCIATION: ([\s\d\w\(\)]+)\<", line)
            if ptnmr2 is not None:
                gene_ids = ptnmr2.group(1)
                #print(gene_ids, file=sys.stdout)
                rxn2genes[rxn_id] = gene_ids
    xml_file.close()

    # match deleted genes with reactions, store in gene2rxns
    gene2rxns = hash_struct.AutoVivification()
    for gene in gene2gid:
        #find matched reactions with genes
        #record in a hash gene2react[gene][rxn] to store percentage
       for rxn in rxn2genes:
            ptnmr = re.search(gene2gid[gene], rxn2genes[rxn], re.IGNORECASE)
            #find the weight of genes, (depending on and/or, later will contain expression data)
            if ptnmr is not None:
                count = len(re.findall(" or ", rxn2genes[rxn]))
                gene2rxns[gene][rxn] = 1.0/(count + 1.0)
                #print(gene + '->' + rxn + ':' + str(gene2rxns[gene][rxn]), file=sys.stdout)

    return gene2rxns

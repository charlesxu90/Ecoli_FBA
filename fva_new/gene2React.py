from __future__ import print_function
from numpy import median
import hashStruct
import re
import csv
##################################
#Author: xiaopeng xu
#Email: charlesxu90@gmail.com
##################################


def gene2geneID(gid2gene):
    """ Match genes with their corresponding IDs, some gene ID may be
        missing as the format is not matched.
    """
    ECK2BNo = hashStruct.AutoVivification()
    # ECK2BNo['ECK1235'] = 'b1241'
    eck_gid_f = open('./result/1.eck2gid.txt', 'w')    # record matched pairs
    eck_gid_dm_f = open('./result/1.Eck2multigid.txt', 'w')   # Eck match dup

    with open('../data/Supplementary_Table_1_Annotation_E._coli_Genes.txt',
              'r') as eck2bno_f:
        eck2bno_f.next()
        eck2bno_f.next()
        eck2bno_csv = csv.reader(eck2bno_f, delimiter='\t')
        for row in eck2bno_csv:
            if (row[1] not in ECK2BNo) or (ECK2BNo[row[1]] == row[5]):
                ECK2BNo[row[1]] = row[5]
                print(row[1] + "\t" + row[5], file=eck_gid_f)
            else:
                print(row[1] + " match multiple B No." + row[5], file=eck_gid_dm_f)
    eck2bno_f.close()
    eck_gid_dm_f.close()
    eck_gid_f.close()

    gene2gid = hashStruct.AutoVivification()
    # Eg. gene2gid['ECK1235-ADHE'] = 'b1241'
    gid_m_f = open('./result/2.gene2gid.txt', 'w')     # ECK ID to B No. matched
    gid_e_f = open('./result/2.gene2gid.err', 'w')     # ECK ID to B No. not matched

    with open('../data/ColonyData.txt', 'r') as temp_f:
        temp_f.next()
        temp_csv = csv.reader(temp_f, delimiter='\t')
        for row in temp_csv:
            #Match ecoli genes with gene id and store in gene2gid
            ptnm1 = re.match(r"(ECK\d{4})", row[0])
            if ptnm1 is None:
                print(row[0], file=gid_e_f)
            if ptnm1.group(1) in ECK2BNo:
                gene2gid[row[0]] = ECK2BNo[ptnm1.group(1)]
                gid2gene[ECK2BNo[ptnm1.group(1)]] = row[0]
                print(row[0] + "\t" + ECK2BNo[ptnm1.group(1)], file=gid_m_f)
            else:
                print(row[0], file=gid_e_f)

    gid_m_f.close()
    gid_e_f.close()

    return gene2gid


def rxn2glist(gid2rxns):
    """ read msbfile, store rxn->genes
    """
    rxn2genes = hashStruct.AutoVivification()
    rxn2gid_f = open('./result/3.rxn2gid.txt', 'w')
    gid2rxn_f = open('./result/3.gid2rxns.txt', 'w')
    with open('../data/msb201165-s3.xml', 'r') as xml_file:
        for line in xml_file:
            ptnmr1 = re.search(r"reaction id\=\"R\_(\S+)\"", line)
            if ptnmr1 is not None:
                rxn_id = ptnmr1.group(1)

            ptnmr2 = re.search(r"GENE_ASSOCIATION: ([\s\d\w\(\)]+)\<", line)
            if ptnmr2 is None:
                continue
            gene_ids = ptnmr2.group(1)
            rxn2genes[rxn_id] = gene_ids
            print(rxn_id + "\t" + gene_ids, file=rxn2gid_f)

            # remove (, ), or_, and_  in string
            rep = {"(": "", ")": "", "and ": "", "or ": ""}
            gene_ids_n = reduce(lambda a, kv: a.replace(*kv),
                                rep.iteritems(), gene_ids)
            gids = re.split(r"\s", gene_ids_n)
            for gid in gids:
                gid2rxns[gid][rxn_id] = 1
    for gid in gid2rxns:
        rxn_ids = ','.join(gid2rxns[gid])
        print(gid + "\t" + rxn_ids, file=gid2rxn_f)
    gid2rxn_f.close()
    xml_file.close()
    rxn2gid_f.close()
    return rxn2genes


def geneabundance():
    """ get gene abundance information
    """
    geneAbd = hashStruct.AutoVivification()
    geneabd_f = open('./result/4.geneAbundance.txt', 'w')
    with open('../data/511145-E.coli_whole_organism-integrated_dataset.txt',
              'r') as abd_file:
        for line in abd_file:
            ptnm = re.search(r"511145.([bs]\d{4})", line)
            if ptnm is not None:
                gid = ptnm.group(1)
                cols = re.split(r"\t", line)
                geneAbd[gid] = format(float(cols[2]), '.2f')
                print(gid + "\t" + str(geneAbd[gid]), file=geneabd_f)
    geneabd_f.close()
    abd_file.close()
    return geneAbd


def gene2react():
    """ Match gene IDs with reactions, also find the effects on reactions
    """
    gene2gid = hashStruct.AutoVivification()
    gid2gene = hashStruct.AutoVivification()
    gene2gid = gene2geneID(gid2gene)

    gid2rxns = hashStruct.AutoVivification()
    rxn2genes = hashStruct.AutoVivification()
    rxn2genes = rxn2glist(gid2rxns)

    geneAbd = hashStruct.AutoVivification()
    geneAbd = geneabundance()

    # find median of the abundance data
    adbList = [float(v) for k, v in geneAbd.items()]
    medabd = median(adbList, axis=0)

    # Example:  "(A and B) or (C and D)"
    # find the effect of deletion of A.
    # (A, B) is a group and (C, D) is a group
    # equation: (Abd(A) +  Abd(B)) / ((Abd(A)+ Abd(B))+ (Abd(C) + Abd(D)))
    gene2rxns = hashStruct.AutoVivification()
    gene_not_model_f = open('./result/5.geneNotinModel.txt', 'w')
    gene_rxn_eft_f = open('./result/5.geneKnouckoutEffectOnRxns.txt', 'w')
    model_gid_abd_f = open('./result/5.abdOfGidinDataandModel.txt', 'w')
    abdPrinted = hashStruct.AutoVivification()
    print("Median Abundance: " + str(medabd), file=model_gid_abd_f)
    for gene in gene2gid:
        if gene2gid[gene] not in gid2rxns:
            print(gene, file=gene_not_model_f)
            continue
        for rxn in gid2rxns[gene2gid[gene]]:
            abdsum = 0.0    # abundance sum of all groups
            tggabd = 0.0    # sum of target gene group
            groups = re.split(r" or ", rxn2genes[rxn])
            for group in groups:
                gpabd = 0.0  # abundance sum of gene group
                ingroup = 0  # target gene in group or not
                # remove (, )in string
                rep = {"(": "", ")": ""}
                gene_ids = reduce(lambda a, kv: a.replace(*kv),
                                  rep.iteritems(), group)
                gids = re.split(r" and ", gene_ids)
                for gid in gids:
                    if (gid == gene2gid[gene]):
                        ingroup = 1
                    # get abundance if exists otherwise use median
                    gabd = geneAbd.get(gid, medabd)
                    if ((gid not in abdPrinted) and (gid in gid2gene)):
                        print(gene + "\t" + gid + "\t" + str(gabd),
                                file=model_gid_abd_f)
                        abdPrinted[gid] = gabd
                    gpabd = gpabd + float(gabd)
                if (ingroup == 1):
                    tggabd += gpabd
                abdsum += gpabd

            gene2rxns[gene][rxn] = (abdsum - tggabd) / abdsum
            print(gene + "\t" + gene2gid[gene]+ '\t' + rxn + "\t" +
                    str(gene2rxns[gene][rxn]), file=gene_rxn_eft_f)
    gene_not_model_f.close()
    model_gid_abd_f.close()
    gene_rxn_eft_f.close()
    return gene2rxns

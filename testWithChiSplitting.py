import csv
import math
import os
from scipy.stats import chi2
import numpy

decisioncounter = 0

def load_csv_to_header_data(filename):
    fpath = os.path.join(os.getcwd(), filename)
    f = csv.reader(open(fpath, newline='\n'))

    all_rows = []
    for r in f:
        all_rows.append(r)

    counter = 0;
    headers = []
    while(counter < 60):
        headers.append("Position" + str(counter))
        counter += 1
    headers.append("Base-Pair")
    idx_to_name, name_to_idx = get_header_name_to_idx_maps(headers)


    row = []
    for i in all_rows:
        tmp = list(i[0])
        tmp.append(i[1])
        row.append(tmp)

    data = {
        'header': headers,
        'rows': row,
        'name_to_idx': name_to_idx,
        'idx_to_name': idx_to_name
    }
    return data

def get_header_name_to_idx_maps(headers):
    name_to_idx = {}
    idx_to_name = {}
    for i in range(0, len(headers)):
        name_to_idx[headers[i]] = i
        idx_to_name[i] = headers[i]
    return idx_to_name, name_to_idx

def get_uniq_values(data):
    idx_to_name = data['idx_to_name']
    idxs = idx_to_name.keys()

    val_map = {}
    for idx in iter(idxs):
        val_map[idx_to_name[idx]] = set()

    for data_row in data['rows']:
        for idx in idx_to_name.keys():
            att_name = idx_to_name[idx]
            val = data_row[idx]
            if val not in val_map.keys():
                val_map[att_name].add(val)
    return val_map

def get_class_labels(data, target_attribute):
    rows = data['rows']
    col_idx = data['name_to_idx'][target_attribute]
    labels = {}
    for r in rows:
        val = r[col_idx]
        if val in labels:
            labels[val] = labels[val] + 1
        else:
            labels[val] = 1
    return labels

def entropy(n, labels):
    en = 0
    for label in labels.keys():
        p_x = labels[label] / n
        en += - p_x * math.log(p_x, 2)
    return en

#Create a new partition of the data based on the remaining attributes (group_att)
def partition_data(data, remaining_attrs):
    partitions = {}
    data_rows = data['rows']
    partition_att_idx = data['name_to_idx'][remaining_attrs]

    #Check in each row for the remaining attributes
    for row in data_rows:
        row_val = row[partition_att_idx]

        #check to see if the currented attribute selected is included in the partition, if it isnt, add it
        if row_val not in partitions.keys():
            partitions[row_val] = {
                'name_to_idx': data['name_to_idx'],
                'idx_to_name': data['idx_to_name'],
                'rows': list()
            }

        #Add data for each remaining attribute
        partitions[row_val]['rows'].append(row)

    return partitions

def avg_entropy_w_partitions(data, remaining_attrs, target_attribute):
    #Get partitioned data for remaining attributes
    data_rows = data['rows']
    n = len(data_rows)
    partitions = partition_data(data, remaining_attrs)
    avg_ent = 0

    for partition_key in partitions.keys():
        partitioned_data = partitions[partition_key]
        partition_n = len(partitioned_data['rows'])
        partition_labels = get_class_labels(partitioned_data, target_attribute)
        partition_entropy = entropy(partition_n, partition_labels)
        avg_ent += partition_n / n * partition_entropy

    return avg_ent, partitions


def most_common_label(labels):
    mcl = max(labels, key=lambda k: labels[k])
    return mcl

def chi2Calc(attr, data, target):
    chi2Value = 0
    nAInC = []
    nC = 0
    nA = []
    nR = 4
    i = 0
    label = ["N", "EI", "IE"]
    labelValues = get_class_labels(data, target)

    while i < 3:
        tmp = label[i]
        if tmp not in labelValues.keys():
            lValue = 1
        else:
            lValue = labelValues[tmp]

        nAInC.append(lValue)
        nC += lValue
        nA.append(lValue * nR)
        i += 1

    i = 0

    while i < 3:
        chi2Value += ((nAInC[i] - ((nC * nA[i]) / (nC + nA[i]))) ** 2) / ((nC * nA[i]) / (nC + nA[i]))
        i += 1

    chi2Value *= nR

    return chi2Value

def id3(data, uniqs, attrs, target):
    labels = get_class_labels(data, target)

    node = {}

    #Check to see if there is only one outcome/classification
    if len(labels.keys()) == 1:
        node['label'] = next(iter(labels.keys()))
        return node

    #Check to see if we are done
    if len(attrs) == 0:
        node['label'] = most_common_label(labels)
        return node

    n = len(data['rows'])
    ent = entropy(n, labels)

    max_info_gain = None
    max_info_gain_att = None
    max_info_gain_partitions = None

    #Selecting Attribute with Max Information Gain
    for a in attrs:
        avg_ent, partitions = avg_entropy_w_partitions(data, a, target)
        info_gain = ent - avg_ent
        if max_info_gain is None or info_gain > max_info_gain:
            max_info_gain = info_gain
            max_info_gain_att = a
            max_info_gain_partitions = partitions

    #No information gained i.e The remianing attributes all have no information gain
    if max_info_gain is None:
        node['label'] = most_common_label(labels)
        return node

    #Modify current list of remaining attributes by removing the attribute with the maximum information gain
    node['attribute'] = max_info_gain_att
    node['nodes'] = {}
    remaining_attrs = list(attrs)
    remaining_attrs.remove(max_info_gain_att)
    uniq_attrs = uniqs[max_info_gain_att]

    #
    for attr in uniq_attrs:
        attrChi2 = chi2Calc(attr, data, target)
        attrChi2 = int( attrChi2 * (10**20))

        #degree of freedom  (no of attributes - 1) * (no of classes - 1) classes will always be 3 and attributes 4
        df = 8
        attrChi2P = chi2.ppf(0.00, df)
        attrChi2P = int( attrChi2P * (10**20))

        if attrChi2 >= attrChi2P:
            if attr not in max_info_gain_partitions.keys():
                node['nodes'][attr] = {'label': most_common_label(labels)}
                continue

            partition = max_info_gain_partitions[attr]
            node['nodes'][attr] = id3(partition, uniqs, remaining_attrs, target)

    return node

def print_tree(root):
    stack = []
    rules = list()

    def traverse(node, stack, rules):
        if 'label' in node:
            stack.append(' THEN ' + node['label'])
            rules.append(''.join(stack))
            stack.pop()
        elif 'attribute' in node:
            ifnd = 'IF ' if not stack else ' AND '
            stack.append(ifnd + node['attribute'] + ' EQUALS ')
            for subnode_key in node['nodes']:
                stack.append(subnode_key)
                traverse(node['nodes'][subnode_key], stack, rules)
                stack.pop()
            stack.pop()


    traverse(root, stack, rules)
    #print(os.linesep.join(rules))
    print(str(len(rules)) + " possible decisions could be made to determine if the class is IE, EI and N")

def preProc(csvfile, mode):
    acceptable = ["A", "C", "T", "G"]
    index = 0
    rows = []

    fpath = os.path.join(os.getcwd(), csvfile)
    fs = csv.reader(open(fpath, newline='\n'))

    for r in fs:
        counter = 0
        proc = ""
        tmp = list(r[0])

        while counter < 60:
            if tmp[counter] == "D":
                tmp[counter] == "T"
            elif tmp[counter] not in acceptable:
                tmp[counter] = acceptable[index % 4]
                index += 1

            counter += 1

        for e in tmp:
            proc += e
        tmp.clear()
        tmp.append(proc)
        if mode == "train":
            tmp.append(r[1])
        rows.append(tmp)

    newFile = "modified" + csvfile

    with open(newFile, mode = "w", newline = "") as test:
        test_writer = csv.writer(test, delimiter = ",", quoting=csv.QUOTE_MINIMAL)
        counter = 0
        for r in rows:
            test_writer.writerow(r)



def classify(csvfile, root, attrs):
    fpath = os.path.join(os.getcwd(), csvfile)
    fs = csv.reader(open(fpath, newline='\n'))

    all_rows = []
    rows = []
    headerMap = {}
    counter = 0

    for i in attrs:
        headerMap[i] = counter
        counter += 1

    for r in fs:
        tmp1 = list(r[0])
        all_rows.append(tmp1)
        rows.append(r)

    results = []

    for r in all_rows:
        tmp = headerMap[root['attribute']]
        val = r[tmp]
        attr = root['nodes'][val]
        if 'label' not in attr:
            results.append(check(r, attr, headerMap))
        else:
            results.append(root['nodes'][val]['label'])

    with open("testClassifiedWithChiSplitting.csv", mode = "w", newline = "") as test:
        test_writer = csv.writer(test, delimiter = ",", quoting=csv.QUOTE_MINIMAL)
        test_writer.writerow(["id","class"])
        counter = 0
        for r in rows:
            tmp2 = [str(counter + 2001)]
            tmp2.append(results[counter])
            counter += 1
            test_writer.writerow(tmp2)
    print(results)

def check(row, root, headerMap):
    result = ""

    tmp = headerMap[root['attribute']]
    val = row[tmp]
    if val not in root['nodes']:
        if val == "T" and "D" in root['nodes']:
            print("Dday")
            val = "D"
        else:
            print("Still no vals")
            return "N"

    attr = root['nodes'][val]
    if 'label' not in attr:
        result = check(row, attr, headerMap)
    else:
        result = root['nodes'][val]['label']

    return result

#preProc("train.csv", "train")
#preProc("testing.csv", "test")
dat = load_csv_to_header_data("train.csv")
attrs = list(dat['header'])
attrs.remove("Base-Pair")
root = id3(dat, get_uniq_values(dat), attrs, "Base-Pair")
print(get_uniq_values(dat))

print_tree(root)

classify("testing.csv", root, attrs)

import csv
import sys


def find_topK(h1bapps, status, metrics, k):
    """
    function to find top 10 states and occupations in certified records:
    1. Go over all certified applications once, call function "update_freq" and get frequencies for all states and occupations occured; 
    2. Call function "find_top" to find top 10 records in order;
    3. return results of top 10 states and occupantions, their cooresponding frequcies, and total number of certified applications. 
    """    
    n = 0
    # Create two dictionaries, each to store frequencies of all state/occuptions
    metric2Freq = {m: {} for m in metrics}
    # Create two lists, each to store top 10 state/occupantions in order sorted by frequencies
    metric2TopK = {m: [] for m in metrics}

    # Only need to go over application once, record frequencies 
    # for all states and occupations for later sorting.
    for h1bapp in h1bapps:
        if h1bapp[status] == 'CERTIFIED':
            n += 1
            for m in metrics:
                update_freq(metric2Freq[m], h1bapp[m])

    for m in metrics:
        find_top(metric2TopK[m], metric2Freq[m], k)

    return metric2TopK, metric2Freq, n


def update_freq(freq, value):
    """
    function to find frequencies for all states and occupations occured
    """ 
    if value in freq.keys():
        freq[value] += 1
    else:
        freq[value] = 1
    return freq


def find_top(top, freq, k):
    """
    function to find top 10 states and occupations and place in lists in order;
    call function "update_order" to swap items if not in right order
    """  
    # Loop over each state and occopation
    for key in freq:
        if len(top) < k:
            # If top list hasn't been filled with 10 records, put at the end
            top.append(key)
            # swap to correct order
            update_order(top, freq)
        else:
            # If top list has been filled
            # Start to compare with last item in top list
            last = top[-1]
            if (freq[last]<freq[key]) or (freq[last]==freq[key] and key > last):
                # if larger, replace last, and swap to correct order
                # if equal, sort alphabetically
                top[-1] = key
                update_order(top, freq)


def update_order(top, freq):
    """
    function to swap two items
    """
    if len(top)<=1:
        return

    cur_pos = len(top)-1

    while (cur_pos>0):
        cur = top[cur_pos]
        prev = top[cur_pos-1]
        # compare , if cur>prev, swap, else break
        if (freq[cur] > freq[prev]) or (freq[cur] == freq[prev] and prev > cur):
            top[cur_pos] = prev
            top[cur_pos-1] = cur
            cur_pos -= 1
        else:
            break


def save_output(path, names, topk, freq, n):
    """
    function that creates an output file.
    """
    rows = [ {names[0]:v, names[1]:str(freq[v]), names[2]:"{:.1%}".format(freq[v]/float(n))} for v in topk ]
    with open(path, 'w') as csvfile:
        fp = csv.DictWriter(csvfile, fieldnames = names, delimiter=';')
        fp.writeheader()
        fp.writerows(rows)



def main(INPUT_PATH, OUTPUT_PATH0, OUTPUT_PATH1):
    """
    Main function contains three steps:
    1. Specify to find top 10 states and occupations in certified applications;
    2. Call function "find_topK" to find top 10 records;
    3. Call function "save_output" to generate two output files respective for top 10 states and occupations.
    """
    # 1. Specify to find top 10 states and occupations in certified applications; 
    k = 10
    with open(INPUT_PATH, 'rb') as file_obj:
        h1bapps = csv.DictReader(file_obj, delimiter=';')
        fieldnames = h1bapps.fieldnames
        for name in fieldnames:
            if name.endswith("STATUS"):
                status = name
            if name.endswith("EMPLOYER_STATE"):
                state = name
            if name.endswith("SOC_NAME"):
                occupation = name
        metrics = [occupation, state]

        # 2. Call function "find_topK" to find top 10 records;
        # metric2TopK: dictionaries containing top 10 states and occupations
        # metric2Freq: dictionaries containing frequencies for each state and occupation
        # n: number of total certified applications
        metric2TopK, metric2Freq, n = find_topK(h1bapps, status, metrics, k)

        # 3. Call function "save_output" to generate two output files respective for top 10 states and occupations.
        fieldname1 = ["TOP_OCCUPATIONS", "NUMBER_CERTIFIED_APPLICATIONS", "PERCENTAGE"]
        fieldname2 = ["TOP_STATES", "NUMBER_CERTIFIED_APPLICATIONS", "PERCENTAGE"]
        fieldnames = [fieldname1, fieldname2]
        paths = [OUTPUT_PATH0, OUTPUT_PATH1]        

        for path, names, m in zip(paths, fieldnames, metrics):
            save_output(path, names, metric2TopK[m], metric2Freq[m], n)


if __name__ == '__main__':
    INPUT_PATH = sys.argv[1]
    OUTPUT_PATH0 = sys.argv[2]
    OUTPUT_PATH1 = sys.argv[3]
    main(INPUT_PATH, OUTPUT_PATH0, OUTPUT_PATH1)

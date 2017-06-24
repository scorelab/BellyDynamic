def read_data(file_name, delimeter, off):
    f = open(file_name)
    # ignore header
    f.readline()
    samples = []
    for line in f:
        line = line.strip().split(delimeter)
        sample = [x for x in line[off:]]
        samples.append(sample)
    return samples

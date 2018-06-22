import json, sys

for fname in sys.argv[1:]:
    with open(fname, 'r') as f:
        data = json.loads(f.read())
    filters = {}
    for section in data.keys():
        for filtername, settings in data[section].iteritems():
            for setting in settings:
                filterstring = filtername + "".join(setting)
                if section not in filters.keys():
                    filters[section] = []
                filters[section].append( filterstring )

    print "From file %s, got filters:"
    for section, filters in filters.iteritems():
        print "%s %s" % ( section, ",".join(filters) )

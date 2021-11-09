'''
parse and process the xplane Data.txt file
'''
import sys, urllib.request, json

samplefile = "samples/Data.txt"

def parsedatafile(filename):
    '''
    read and parse xplane Data.txt file
    return tupe containing
    list of keys and list of records, each record containing list of data floats
    '''

    f = open(filename, 'r')

    #this reads ALL at once, so it may eat your memory, but in this use case, there are 6 lines per minute of xplane
    lines = f.readlines() 

    header = lines[1]

    '''
    make xplane data types prettier, remove comas and underscores
    end result is something like this:
    'real_time,totl_time,missn_time,timer_time,zulu_time,local_time,hobbs_time,
    Vind_kias,Vind_keas,Vtrue_ktas,Vtrue_ktgs,Vind_mph,Vtrue_mphas,Vtrue_mphgs,
    gear_0/1,wbrak_set,lbrak_add,rbrak_add,wbrak_part,N1_1_pcnt,N1_2_pcnt,N2_1_pcnt,N2_2_pcnt,
    fuel1_lb,fuel2_lb,fuel3_lb,fuel4_lb,fuel5_lb,fuel6_lb,
    empty_lb,payld_lb,fuel_totlb,jetti_lb,curnt_lb,maxim_lb,cg_ftref,gear_lb,gear_lb,gear_lb,'
    '''
    keys = header.split("|")
    keys = [k.strip() for k in keys]
    keys = [k.replace(",","_") for k in keys]
    keys = [k.replace("__","_") for k in keys]
    keys = [k.replace("__","_") for k in keys]
    keys = [k.lstrip("_") for k in keys if k not in ["\n",""]]


    records = []


    #now load the data into the list of floats
    for line in lines[3:]:
        fields = line.split("|")
        fields = [f.strip() for f in fields]
        fields = [float(f) for f in fields if f not in ["\n",""]]
        records.append(fields)


    return (keys,records)

def getzulu(z):
    '''
    return the HH:MM string representing the xplane specific hh.mm decimal time format
    '''

    hours = int(z)
    minutes = (z - hours) * 60
    minutes = int(minutes)

    ret = "{:02d}:{:02d}".format(hours,minutes)

    return ret


def processdata(keys, records):

    #output fields
    ret = {"startup_zulu":0, "shutdown_zulu":0}
    
    #sample use of above data, convert it from lists to dicts on the fly, probably unnecesary 'savings'    
    for r in records:
        d = {}
        for k,v in zip(keys,r):
            d[k]=v

        #print(d)

        #detect engines from off to on and on to off
        if ret["startup_zulu"]==0:
             if d["N2_1_pcnt"]>10 or d["N2_2_pcnt"]>10:
                 ret["startup_zulu"]=getzulu(d["zulu_time"])
        elif ret["shutdown_zulu"]==0:
            if d["N2_1_pcnt"]<1 and d["N2_2_pcnt"]<1:
                ret["shutdown_zulu"]=getzulu(d["zulu_time"])

    

    return ret


def parsevatsim(vatsimid):
    vatsimurl = "https://data.vatsim.net/v3/vatsim-data.json"

    response = urllib.request.urlopen(vatsimurl)
    data = response.read().decode()
    vatsimdata = json.loads(data)

    pilots = vatsimdata.get('pilots')

    ret = None

    for p in pilots:
        if p['cid']==vatsimid:
            ret=p
            break
    
    return ret
            





if __name__ == '__main__':

    print("Usage: pmacars.py <xplane_data_txt_full_file_path> [<vatsim_id>]")
    inputfile = samplefile
    if len(sys.argv)>1:
        inputfile = sys.argv[1]
        if len(sys.argv)>2:
            vatsimid=sys.argv[2]
            vatsimid=int(vatsimid)

            print(f"Parsing VATSIM record for vatsim ID: {vatsimid}...")

            vatsimrec = parsevatsim(vatsimid)
            print(vatsimrec)

    input("Please exit the X-Plane and then press ENTER to parse the data.txt file...")

    keys,records = parsedatafile(inputfile)

    ret = processdata(keys, records)

    print(ret)
    

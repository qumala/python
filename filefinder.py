#!/usr/bin/python3.5 -tt
from pathlib import Path
from sys import argv

#def filesorter(file):
#    "return dict with one file numbered by size or nothing"""
#    if file.is_file():
#        return  {file.stat().st_size : file._str}
def combinedicts(dict1,dict2):
    if type(dict1) is dict and type(dict1) is dict:
        dict3=dict1
        for i in dict1:
            if not( dict2.get(i) is None):
                dict1[i].extend(dict2[i])
        dict2.update(dict1)
    return dict2

def dirsorter(dir):
    "return dict with all files in dict numbered by size"""
    dic={}
    for s in dir.iterdir():
        if s.is_dir():
           dic.update(dirsorter(s))
        elif s.is_file():
            dic=combinedicts(dic,{s.stat().st_size:[s._str]})
    return dic

def main():
    if len(argv)==1:
        print("no arguments")
        #print({1:2})
        #print(type({1:2}))
    else:
        dic={}
        for n in argv[1:]:
            f=Path(n).absolute()
            if not f.exists():
                print("\""+f._str+"\" not exsist")
            else:
                if f.is_file():
                    d[f.stat().st_size]=str(f)
                elif f.is_dir():
                    #print("dir:"+str(f))
                    #print("dir:"+f._str)
                    dic=combinedicts(dic,dirsorter(f))
        any_=False
        for key in dic:
            if len(dic[key]) >1:
                print("find key:",key,len(dic[key]))
                print("\t"+str(dic[key]))
                any_=True
        if any_==False:
            print("no one")



if __name__ == '__main__':
	main()

import hashlib
import os
import json

__author__ = 'sr1k4n7h'


def hash_file(filename):
    h = hashlib.sha1()
    with open(filename, 'rb') as f:
        chunk = 0
        while chunk != b'':
            chunk = f.read(1024)
            h.update(chunk)
    return h.hexdigest()


def calc_sha(file_list, dir_name):
    sha1_dict = {}
    for fname in file_list:
        sha1_dict.__setitem__(fname, str(hash_file(dir_name + "/" + fname)))
    return sha1_dict


def update_new_files(new_files, dir_name, hash_data_file):
    f = open(hash_data_file, 'r+')
    data = json.load(f)
    for fname in new_files:
        data[fname] = str(hash_file(dir_name + "/" + fname))
    f.seek(0)
    json.dump(data, f, indent=4)
    f.close()


def alert(file_name):
    print("\t\tThe file contents of " + file_name + " has been modified/updated ! ")


def verify_sha(file_list, dir_name, hash_data_file):
    in_file = open(hash_data_file, "r")
    old_sha_dict = json.load(in_file)
    in_file.close()
    new_sha_dict = calc_sha(file_list, dir_name)
    new_files = list(set(set(new_sha_dict.keys()) - set(old_sha_dict.keys())))
    files_set = list(set(set(new_sha_dict.keys()) & set(old_sha_dict.keys())))
    if len(new_files) > 0:
        update_new_files(new_files, dir_name, hash_data_file)
    alert_flag = False
    # print(files_set)
    for fname in files_set:
        # print(old_sha_dict[fname], new_sha_dict[fname])
        if old_sha_dict[fname] != new_sha_dict[fname]:
            alert(fname)
            alert_flag = True
    return alert_flag


def dir_traverse(direc):
    # direc = '/home/sr1k4n7h/Desktop'
    # direc = '/home/sr1k4n7h/PycharmProjects'
    print("\n..... Traversing through the sub-directories ..... ")
    for dirName, subdirList, fileList in os.walk(direc):
        print('\nTraversing through directory: %s' % dirName)
        hash_data_file = dirName + "/" + dirName.split("/")[-1] + ".json"
        json_presence = 0
        for i in list(os.listdir(dirName)):
            if dirName + "/" + i == hash_data_file:
                json_presence = 1
                break
        if not json_presence:
            print("\tSHA1 for the files present in this directory hasn't been calculated yet !")
            print("\tCalculating SHA1 for the files now ........ ")
            data = calc_sha(fileList, dirName)
            out_file = open(hash_data_file, "w")
            json.dump(data, out_file, indent=4)
            print("\tSHA1 digests has been completed ! Check this folder next time.")
            out_file.close()
        else:
            print("\tVerifying the SHA1 signature of the files .........")
            flag = verify_sha(fileList, dirName, hash_data_file)
            if flag:
                print("\t All alerts regarding the modification of files in this current directory has been raised")
            else:
                print("\t It seems that No files in this directory has been modified since last time. Check next time")


def main():
    print("\n..... Signature based verification program ......")
    print("..... IS2223 - WEEK:2 - MODULE: 7 ......")
    direc = raw_input("\nPlease enter a directory path : ")
    if direc[-1] == "/":
        direc = direc[:-1]
    dir_traverse(direc)


if __name__ == '__main__':
    main()

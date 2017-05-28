import os
home_path = '/run/user/1000/gvfs/smb-share:server=192.168.0.1,share=root/Rachel/'

dirs_and_file_coll = {}


def collect_formats():
    """ Collects file formats formats from selected dir and sub dirs """
    # collects file names
    # runs through all dirs, starting with root dir
    slice_a = home_path.find("root/")
    belongs = home_path[slice_a + 5:-1]
    print("{}'s file formats:\n".format(belongs))

    for (dirpath, dirnames, filenames) in os.walk(home_path):
        # runs through files in current iter dir
        for filename in filenames:
            dot_i = filename.rfind('.') + 1
            file_format = filename[dot_i:] 
            #print(file_format)
            if file_format == 'ini':
                continue

            if file_format not in dirs_and_file_coll.keys():
                if len(file_format) <= 3:
                    dirs_and_file_coll[file_format] = 1
            else:
                dirs_and_file_coll[file_format] += 1
        




collect_formats()
for key in dirs_and_file_coll.keys():
    print("{}: {}".format(key, dirs_and_file_coll[key]))

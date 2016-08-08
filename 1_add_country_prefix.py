import glob
import os
import ntpath


# os.rename("/home/naz/Desktop/Untitled Document","/home/naz/Desktop/Untitled Document2")

for glob_path in ['/home/naz/Desktop/avto_6500/Images/*/*', '/home/naz/Desktop/avto_6500/Annotations/*/*']:

    for name in glob.glob(glob_path):

        # /home/naz/Desktop/avto_6500/Images/ee
        path = os.path.dirname(name)

        country_prefix = path.rsplit('/', 1)[1]

        file_name = ntpath.basename(name)

        if not file_name.startswith(country_prefix):
            new_file = path + '/' + country_prefix + '_' + file_name

            os.rename(name, new_file)

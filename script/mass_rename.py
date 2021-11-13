import os

def get_prior_ep(ep: str) -> str:
    return f'{int(ep) - 1:03}화'

def join_str(string_list = [str], join_char = str) -> str:
    return join_char.join(string_list)

def main():

    # Directory Path Setting
    target_dir = "./img/"
    other_dir = "./img2/"
    all_files = os.listdir(target_dir)

    # File Setting
    name_len = 7
    ep_len = 3
    img_len_reverse = -7
    join_char = '_'
    
    for filename in all_files:
        src = os.path.realpath(os.path.join(target_dir, filename))
        out = os.path.join(other_dir, join_str(
                string_list=[
                    filename[:name_len], 
                    get_prior_ep(ep=filename[name_len + 1 : name_len + ep_len + 1]), 
                    filename[img_len_reverse:]
                    ],
                join_char=join_char
            ))
        print("{} | {}".format(src, out))
        os.rename(src, out)

if __name__ == "__main__":
    main()
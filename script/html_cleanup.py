import os
def main():
    top_div = '<div class="css-88gyaf">' #  -> ""
    img_wrapper = '<div class="disableImageSave css-lqob9q"><img class="comic-viewer-content-img" src="' # -> ![img+n](https:
    md_wrapper = '![img](https:'
    ampersand = '&amp;' # -> &
    raw_amp = '&'
    eos = '" alt=""></div>' #  -> )
    
    target_dir = r'./프로야구생존기/'

    for filename in os.listdir(target_dir):
        if filename.endswith(".md"):
            with open(os.path.join(target_dir, filename), 'rt') as f:
                data = f.read()
                data = data.replace(top_div, '')
                data = data.replace(img_wrapper, md_wrapper)
                data = data.replace(ampersand, raw_amp)
                data = data.replace(eos, ")\n")
                data = data.replace("</div>", "")
                f.close()
            with open(os.path.join(target_dir, filename), 'wt') as w:
                w.write(data)
                w.close()

if __name__ == "__main__":
    main()
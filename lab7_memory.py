def fifo_page(pages, frame_num):
    frames = []
    fault = 0
    for page in pages:
        if page not in frames:
            fault += 1
            if len(frames) < frame_num:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
        print(f"Page {page}: Frames {frames}")
    print(f"FIFO Page Faults: {fault}\n")

def lru_page(pages, frame_num):
    frames = []
    fault = 0
    for page in pages:
        if page not in frames:
            fault += 1
            if len(frames) < frame_num:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
        else:
            frames.remove(page)
            frames.append(page)
        print(f"Page {page}: Frames {frames}")
    print(f"LRU Page Faults: {fault}")

if __name__ == "__main__":
    page_seq = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,7]
    frame_count = 3
    fifo_page(page_seq, frame_count)
    lru_page(page_seq, frame_count)

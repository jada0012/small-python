# import os
# os.environ['HF_HOME'] = 'C:/Users/bobei/cache/huggingface'

from datasets import load_dataset
dataset = load_dataset("imagefolder", data_dir=r"C:\Users\bobei\python\tests\data")

dataset.push_to_hub("jada0012/invoicedata")
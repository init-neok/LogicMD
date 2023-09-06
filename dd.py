import torch
a=1
b=2
c=a+b


if c==a+b:
    d=4
print(d)
print(torch.cuda.is_available())
device="cuda" if torch.cuda.is_available() else "cpu"
print(torch.tensor([1] ).to(device))
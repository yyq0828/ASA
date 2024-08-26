import torch.nn as nn
import torch
from nn.modules.conv import Conv
class CBiF(nn.Module):
    # CBiF Block
    def __init__(self, c1, c2, nw, n=1, shortcut=True, g=1, e=0.5):
        super().__init__()
        c_ = int(c2 * e)  # hidden channels
        self.cv1 = Conv(c1, c_, 1, 1)
        self.cv2 = Conv(c1, c_, 1, 1)
        self.cv3 = Conv(2 * c_, c2, 1)  # act=FReLU(c2) mg
        self.blocks = nn.Sequential(*[
            BiFormerBlock(c_, c_, nw)
            for i in range(n)
        ])

    def forward(self, x):
        return self.cv3(torch.cat((self.blocks(self.cv1(x)), self.cv2(x)), dim=1))

class BiFB(nn.Module):
    def __init__(self, c1, c2, nw, n=1, shortcut=False, g=1, e=0.5):  # ch_in, ch_out, number, shortcut, groups, expansion
        super().__init__()
        self.c = int(c2 * e)  # hidden channels
        self.cv1 = Conv(c1, 2 * self.c, 1, 1)
        self.cv2 = Conv((2 + n) * self.c, c2, 1)  
        self.m = nn.Sequential(*[
            BiFormerBlock(self.c, self.c, nw)
            for i in range(n)
        ])

    def forward(self, x):
        y = list(self.cv1(x).chunk(2, 1))
        y.extend(m(y[-1]) for m in self.m)
        return self.cv2(torch.cat(y, 1))

    def forward_split(self, x):
        y = list(self.cv1(x).split((self.c, self.c), 1))
        y.extend(m(y[-1]) for m in self.m)
        return self.cv2(torch.cat(y, 1))

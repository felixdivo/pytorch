import torch
from typing import Union

class TestVersionedDivTensorExampleV7(torch.nn.Module):
    def __init__(self):
        super(TestVersionedDivTensorExampleV7, self).__init__()

    def forward(self, a, b):
        result_0 = a / b
        result_1 = torch.div(a, b)
        result_2 = a.div(b)
        return result_0, result_1, result_2

class TestVersionedLinspaceV7(torch.nn.Module):
    def __init__(self):
        super(TestVersionedLinspaceV7, self).__init__()

    def forward(self, a: Union[int, float, complex], b: Union[int, float, complex]):
        c = torch.linspace(a, b, steps=5)
        d = torch.linspace(a, b)
        return c, d

class TestVersionedLinspaceOutV7(torch.nn.Module):
    def __init__(self):
        super(TestVersionedLinspaceOutV7, self).__init__()

    def forward(self, a: Union[int, float, complex], b: Union[int, float, complex], out: torch.Tensor):
        return torch.linspace(a, b, out=out)

class TestVersionedLogspaceV8(torch.nn.Module):
    def __init__(self):
        super(TestVersionedLogspaceV8, self).__init__()

    def forward(self, a: Union[int, float, complex], b: Union[int, float, complex]):
        c = torch.logspace(a, b, steps=5)
        d = torch.logspace(a, b)
        return c, d

class TestVersionedLogspaceOutV8(torch.nn.Module):
    def __init__(self):
        super(TestVersionedLogspaceOutV8, self).__init__()

    def forward(self, a: Union[int, float, complex], b: Union[int, float, complex], out: torch.Tensor):
        return torch.logspace(a, b, out=out)

class TestVersionedGerV9(torch.nn.Module):
    def __init__(self):
        super(TestVersionedGerV9, self).__init__()

    def forward(self, v1: torch.Tensor, v2: torch.Tensor):
        return torch.ger(v1, v2)

class TestVersionedGerOutV9(torch.nn.Module):
    def __init__(self):
        super(TestVersionedGerOutV9, self).__init__()

    def forward(self, v1: torch.Tensor, v2: torch.Tensor, out: torch.Tensor):
        return torch.ger(v1, v2, out=out)

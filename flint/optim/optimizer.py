class Optimizer:
    """
    Base class for all optimizers.

    Parameters
    ----------
    params : iterable
        An iterable of Tensor

    lr : float, optional, default=0.01
        Learning rate

    weight_decay : float, optional, default=0.
        Weight decay (L2 penalty)
    """

    def __init__(self, params = None, lr: float = 0.01, weight_decay: float = 0.):
        if not lr >= 0.0:
            raise ValueError("Invalid learning rate: {}".format(lr))
        if not weight_decay >= 0.0:
            raise ValueError("Invalid weight_decay value: {}".format(weight_decay))

        self.params = list(params)
        self.lr = lr
        self.weight_decay = weight_decay
        self.iterations = 0

    def zero_grad(self):
        """
        Set the gradients of all parameters to zero.
        """
        for p in self.params:
            p.zero_grad()

    def step(self):
        self.iterations += 1

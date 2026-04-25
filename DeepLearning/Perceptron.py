class Perceptron(object):
    # 初始化激活函数，权重，偏置
    def __init__(self, input_num, activator):
        self.weights = [0.0] * input_num
        self.bias = 0.0
        self.activator = activator

    #打印结果
    def __str__(self):
        return (
            f'weight\t:{self.weights}\n'
            f'bias\t:{self.bias}\n'
        )

    # 实现 z = w1 * x1 + w2 * x2 + ... + wn * xn + b
    #实现 y = f(z) f:激活函数
    def predict(self, input_vecs):
        total = sum(w * x for w, x in zip(self.weights, input_vecs)) + self.bias
        return self.activator(total)


    #迭代训练通过iteration迭代器
    #训练函数为train, 参数为 input_vecs, label, iteration, rate
    def train(self, input_vecs, labels, iteration, rate):
        for _ in range (iteration):
            self._one_iteration(input_vecs, labels, rate)
    
    """一轮迭代"""
    #函数名为_one_iteration，参数为input_vecs, labels, rate
    def _one_iteration(self, input_vecs, labels, rate):
        for input_vec, label in zip(input_vecs, labels):
            output = self.predict(input_vec)
            self._update_weights(input_vec, output, label, rate)

    """更新权重 + 偏置"""
    #函数名为_update_weights， 参数为input_vec, output, label, rate
    def _update_weights(self, input_vec, output, label, rate):
        delta = label - output
        self.weights = [w + rate * delta * x for x, w in zip(input_vec, self. weights)]
        self.bias += rate * delta
from sklearn import datasets, model_selection, naive_bayesimport matplotlib.pyplot as pltdef show_digits():    digits = datasets.load_digits()    fig = plt.figure()    print("vector from images 0 ", digits.data[0])    for i in range(25):        ax = fig.add_subplot(5, 5, i + 1)        ax.imshow(digits.images[i], interpolation='nearest')    plt.show()    passdef load_data():    digits = datasets.load_digits()    return model_selection.train_test_split(digits.data, digits.target, test_size=0.25, random_state=0)'''高斯贝叶斯分类器'''def test_gaussiannb(data):    '''    功能： 高斯贝叶斯分类器    涉及函数： sklearn.naive_bayes.GaussianNB    参数： 没有参数    属性： class_prior_: 一个数组，形状为(n_classes, )，每个类别的概率p(y = ck)            class_count_: 每个类别包含的样本            theta: 每个类别每个特征的均值            sigma： 每个类别每个特征的标准差。                :param data:     :return:     '''    x_train, x_test, y_train, y_test = data    model = naive_bayes.GaussianNB()    model.fit(x_train, y_train)    print("Training score: {}".format(model.score(x_train, y_train)))    print("Testing score: {}".format(model.score(x_test, y_test)))    pass'''多项式贝叶斯分类器'''def test_MultinomialNB(data):    '''    功能： 贝叶斯多项式分类器    涉及函数： sklearn.naive_bayes.MultinminalNB(alpha=1.0, fit_prior=True, class_prior=None)    参数： alpha: 一个浮点数，制定alpha值            fit_prior: 如果设置为True, 不去学习p(y = ck)，替代为均匀分布，            class_priot： 一个数组，制定每个分类的先验p(y = c1), p(y = c2)...    :param data:     :return:     '''    x_train, x_test, y_train, y_test = data    model = naive_bayes.MultinomialNB()    model.fit(x_train, y_train)    print("Training score: {}".format(model.score(x_train, y_train)))    print("Testing score: {}".format(model.score(x_test, y_test)))    passif __name__ == '__main__':    test_MultinomialNB(load_data())
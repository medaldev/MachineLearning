import tensorflow as tf

x = tf.constant([[1, 2]])
neg_matrix = tf.negative(x)
print(neg_matrix)

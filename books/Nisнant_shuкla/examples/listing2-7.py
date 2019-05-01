import tensorflow as tf

sess = tf.InteractiveSession()  # Интерактивная среда (только для отладки или представления)!

x = tf.constant([[1., 2]])
negMatrix = tf.negative(x)

result = negMatrix.eval()
print(result)

sess.close()